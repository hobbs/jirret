#!/bin/bash
pip wheel --wheel-dir=wheelhouse -r requirements.txt
tar -cvzf dist/gerrit-jira-hook.tar.gz ./ --exclude=dist --exclude=.git --exclude=src/hooks/jira-hook.config
