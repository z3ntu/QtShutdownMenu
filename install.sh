#!/bin/bash
if [ "$1" == "--prefix" ]; then
  if [ "$2" != "" ]; then
    PREFIX=$2
  else
    echo "Please specify a prefix."
    echo "Use --help for more information."
    exit
  fi
elif [ "$1" == "--help" ]; then
  echo "This script supports:"
  echo "./install.sh --prefix <prefix>"
  echo "You may need to run this script as root."
  echo "This will copy shutdownmenu.py & lock.sh to \$PREFIX/bin/ and icon.png to /usr/share/icons/"
  exit
else
  PREFIX=/usr/local
fi

#install -Dm644 "$srcdir/shutdownmenu.py" "$pkgdir/$PREFIX/bin/qtshutdownmenu"
#install -Dm644 "$srcdir/lock.sh" "$pkgdir/$PREFIX/bin/lock"
#install -Dm644 "$srcdir/icon.png" "$pkgdir/usr/share/icons/lock.png"
install -Dm755 "shutdownmenu.py" "$PREFIX/bin/qtshutdownmenu"
install -Dm755 "lock.sh" "$PREFIX/bin/lock"
install -Dm755 "icon.png" "/usr/share/icons/lock.png"
