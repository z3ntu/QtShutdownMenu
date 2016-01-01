# QtShutdownMenu

This is a shutdown & lock script designed for use with the i3 WM.

## Screenshots
__Shutdown menu__

![Shutdown-Menu](http://i.imgur.com/4yS5Dxb.png)

__Lockscreen__

![Lockscreen](http://i.imgur.com/oLIPYWE.png)

## Dependencies
### ShutdownMenu
- Python 3
- PyQt5

### Lock script
- ImageMagick
- i3lock
- scrot


## How to use
```
# Install dependencies
pacman -S ttf-liberation python-pyqt5 imagemagick scrot i3lock

# Install
./install.sh
```
Then you can create bindings in your i3 config (possibly in `~/.config/i3/config`) or just call `qtshutdownmenu` or `lock`.

## Credits
- The file `icon.png` is 'CC By 3.0'. The lock icon itself was made by [João Miranda](https://thenounproject.com/term/lock/7657/), modified by [/u/Beaverman](https://www.reddit.com/user/Beaverman).
- Idea for the shutdown script is based on a script in [CrunchBang Linux](https://gist.github.com/jonyamo/5675359) which is written with PyGTK. New service commands by [@commonquail](https://gist.github.com/commonquail).
- [Original Lock script](http://pastebin.com/ViRWBH90) is by [/u/Badel2](https://www.reddit.com/user/Badel2).
