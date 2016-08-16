import sys

import requests

URL_BASE = 'https://app.getsentry.com/api/0/'


def print_status(response, success_message, error_message):
    padding = 4

    def out(text):
        print ' ' * padding + text

    if response.status_code < 400:
        out(success_message)
    else:
        out(error_message + ': ' + response.text)


def create_release():
    url = URL_BASE + 'projects/{}/{}/releases/'.format(organization, project)
    data = {'version': release_id}
    r = requests.post(url, data=data, headers=headers)
    print_status(r, 'Created release {}'.format(release_id), 'Error creating release {}'.format(release_id))


def upload_sourcemap():
    url = URL_BASE + 'projects/{}/{}/releases/{}/files/'.format(organization, project, release_id)
    files = {'file': open(map_file_local_path, 'rb')}
    data = {'name': map_file_web_path}
    r = requests.post(url, data=data, files=files, headers=headers)
    print_status(r, 'Uploaded {}'.format(map_file_local_path), 'Error uploading {}'.format(map_file_local_path))


def main():
    print "Publishing to Sentry as release {}...".format(release_id)
    create_release()
    upload_sourcemap()
    print "Done publishing to Sentry"


if __name__ == "__main__":
    organization = sys.argv[1]
    project = sys.argv[2]
    release_id = sys.argv[3]
    map_file_local_path = sys.argv[4]
    map_file_web_path = sys.argv[5]
    token = sys.argv[6]
    headers = {'Authorization': 'Bearer ' + token}
    main()
