Title: Electronics and PIC Microcontrollers
Date: 2004-10-10 21:22
Author: Kristopher Johnson
Tags: electronics, pic, microcontroller
Slug: electronics-and-pic-microcontrollers

Over the past few months, I've been trying to learn more about
electronics. My job involves a lot of devices and embedded software,
which piqued my interest. As with everything else I do, I want to
understand how it all works.

I had a couple of digital electronics courses in college, so I know how
to design circuits with NAND gates, inverters, flip-flops, and so on.
But I've never known much about capacitors, coils, transistors,
amplifiers, oscillators, or other "analog" stuff, other than the
formulas needed to pass physics tests.

So I bought a couple of books on electronics, and bought one of those
Radio Shack "Electronics Learning Lab" thingees. I read the electronics
books, but they didn't do much for me. The first few chapters were just
refreshers of things I remembered from physics classes (V=IR and all
that stuff), and the later chapters were a little incomprehensible (too
many formulas, not much explanation of what the circuits actually do).

The Learning Lab has sat on the shelf. Going through its experiments
would have helped, but I never had time when I had interest, and never
had interest when I had time.

A couple of weeks ago I got into PIC microcontroller programming. My
current project involves some PIC firmware development, and while I
won't be directly involved in that, I wanted to learn enough about the
process that I could make some intelligent decisions about it. (I'm
supposedly directing this effort.)

I bought the "PICkit 1 Flash Starter Kit" from
[Microchip](http://www.microchip.com/). It includes a programmer/testing
board, a couple of PIC microcontrollers (a PIC12f675 and a PIC16F684),
and some tutorials and documentation. I also bought *Programming and
Customizing PICmicro Microcontollers* by Myke Predko. Using these and a
few little tidbits from the web, I've written the traditional "flashing
LED" program, and also a 7-segment LED controller program.

So far, I've written PIC code in assembly language. The PIC's
instruction set is very small, with only 35 instructions, so I picked it
up pretty quick. There are some differences between programming for PICs
and for other microprocessors, mostly related to lack of RAM, register
bank switching, and the separate code/data spaces, but it's not too hard
once you learn the techniques. It's nice to get back into this kind of
low-level programming.

When my programs get too complex for assembly, I'll probably give
[PicForth](http://www.rfc1149.net/devel/picforth) a try. There are C
compilers and other languages for the PIC, but I'd prefer to stay as
low-level as I can. I notice that PicForth doesn't support the
controllers that I have, so I may have to play around with its code
generator a bit.

Wiring the PIC into circuits on the Learning Lab breadboard is helping
me get back into the electronics study. It's easier for me to write code
than to figure out how to wire together a bunch of resistors,
capacitors, and transistors, but once I've got the circuit working I can
play with replacing some of the PIC functions with electronic
components, and vice versa.

So now I have something to do while my helicopter batteries are
recharging.

