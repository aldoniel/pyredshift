# pyredshift
A minimalist GUI for redshift on Raspberry py OS to change screen temperature, written in python.\
It just a shell script quickly written for my own usage, but someone might find it useful.\
It works on my raspberry zero 2, but it should work on zero 1, 2 and 3.\
It won't work on raspberry 4 and 5 because gamma and brighness is not implemented in the driver (see [issue](https://github.com/raspberrypi/firmware/issues/1274))

# Install
  * you need the redshift package from the repository, if it's not already installed.
  * install easygui (pip install easygui) : easy tkinter "dialog in one function" module for a few kB.
  * copy redshift.py where you want, make executable (chmod +x), make a shortcut and run.

![GUI img](gui.png)

(It will look like more gnome style on raspberry.)

# See also
The same in nim (faster) : https://github.com/aldoniel/nimredshift/
