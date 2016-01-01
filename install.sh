#!/bin/bash

shutdownloc="/usr/local/bin/qtshutdownmenu"
lockloc="/usr/local/bin/lock"
iconloc="/usr/share/icons/lock.png"

cat << EOF
Copying:
'shutdownmenu.py' to '$shutdownloc'
'lock.sh' to '$lockloc'
'icon.png' to '$iconloc'
EOF

# Copy files
sudo cp shutdownmenu.py $shutdownloc
sudo cp icon.png $iconloc
sudo cp lock.sh $lockloc

# Set permissions
sudo chmod +x $shutdownloc
sudo chmod +x $lockloc

