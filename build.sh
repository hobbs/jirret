#!/bin/bash
pip wheel --wheel-dir=wheelhouse -r requirements.txt
tar -cvf dist/gerrit-jira-hook.tar ./ --exclude=dist --exclude=.git
