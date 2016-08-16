sentry-release
==============

Simple Python script to create a release in Sentry and then upload a single sourcemap file to it

## Use

    pip install -r requirements.txt
    python sentry-release.py sentry_org_id sentry_project_id release_id "path/to/file.js.map" "http://www.example.com/assets/file.js.map" sentry_auth_token
