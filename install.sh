#! /bin/sh

apt-get update
apt-get install mplayer -y
apt-get install python -y
mkdir /var/log/file-check

chmod +x ./checkfile.py
chmod +x ./check


echo "done!"
