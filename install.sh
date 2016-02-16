#!/bin/bash
if [ "x$GERRIT_PATH" == "x" ];
    then echo "Usage: GERRIT_PATH=<gerrit install path> ./install.sh"
        exit 1;
fi
# install virtualenv
pip install --use-wheel --no-index --find-links=wheelhouse virtualenv
pip install --use-wheel --no-index --find-links=wheelhouse -r requirements.txt
# copy hooks to gerrit install path
cp src/hooks $GERRIT_PATH/hooks
