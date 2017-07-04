Title: A Gforth Interface to the wiringPi Library
Date: 2016-01-24 13:50:16
Category: Blog
Slug: gforth-interface-wiringpi-library
Alias: 2016/01/24/gforth-interface-wiringpi-library/
Tags: wiringPi, raspberrypi, gforth


I recently obtained a [Raspberry Pi](https://www.raspberrypi.org), an [Arduino](https://www.arduino.cc), and a model train set. This should keep me busy and out of trouble for a while.

My plan is to use the Arduino to read sensors and control the turnout switches on the track, but I think it is easier to use the RPi to do some initial experimentation with driving relays and other electronic components. I did the typical [make-an-LED-blink](https://gist.github.com/kristopherjohnson/1f3c0e70899766447dd0) exercise using the [wiringPi](http://wiringpi.com) library. It wasn't difficult, but I wished there was an interactive way to play with the [GPIO](https://www.raspberrypi.org/documentation/usage/gpio/README.md) pins, rather than going through a cycle of editing, compiling, and executing a C program whenever I wanted to try something.

Then I remembered [Forth](https://en.wikipedia.org/wiki/Forth_%28programming_language%29). Forth was designed as an interactive language for controlling hardware, and seemed like the perfect solution for me.

After looking at a few possibilities for Forth-based solutions, I decided to use [Gforth](https://www.gnu.org/software/gforth/), as it provides a straightforward way to call functions in the wiringPi library without the need to build my own Forth.

Here is my Gforth interface to the wiringPi library: <https://github.com/kristopherjohnson/wiringPi_gforth>

Now, back to the train set...
