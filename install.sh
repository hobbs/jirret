#!/bin/bash
os='linux'
case "$(uname -s)" in
   Linux)
     ;;

   CYGWIN*|MINGW32*|MSYS*)
     os='windows'
     ;;

   *)
     echo 'other OS'
     exit 1
     ;;
esac

if [ "x$GERRIT_PATH" == "x" ];
    then echo "Usage: GERRIT_PATH=<gerrit install path> sh install.sh"
        exit 1;
fi

# install virtualenv
pip install --use-wheel --no-index --find-links=wheelhouse virtualenv

# create vritual environment
if [ ! -d ".venv" ]; then
    virtualenv .venv
fi

# active it
if [ $os == "windows" ]; then 
    source .venv/Scripts/activate
else
    source .venv/bin/activate
fi

# install requirements
pip install --use-wheel --no-index --find-links=wheelhouse -r requirements.txt
# copy hooks to gerrit install path
cp src/hooks/* $GERRIT_PATH/hooks
