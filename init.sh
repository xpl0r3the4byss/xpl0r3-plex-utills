#!/bin/bash
#FILE=/config/config.ini
#if test -f "$FILE"
#then
#    echo "$FILE exists, if you are having issues, please make sure you are running the latest version of the config file."
#else
#    cp -r /app/config/config.ini /config/config.ini
#    echo "copied files"
#fi
#
exec gunicorn -w 4 --bind 0.0.0.0:5000 plex-utills:app
#config_check.py