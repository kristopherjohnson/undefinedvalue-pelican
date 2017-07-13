Title: Sprinting to the Finish
Date: 2004-10-20 05:05
Author: Kristopher Johnson (noreply@blogger.com)
Tags: managing
Slug: sprinting-to-the-finish

I haven't written much in my blog about what I'm doing at work. This is
because I've wanted to avoid writing anything that could get me into
trouble with my managers, coworkers, or customers. However, I do want to
write a little about what's going on at work, because that is what I'm
spending most of my time thinking about. So I'll write, but I'll have to
leave a lot of the details out.

We're approaching the deadline (Nov. 15) for getting our system
installed and operational at the customer site. This is a hard deadline;
it absolutely cannot slip beyond that date. Software-wise, I think we're
OK. The problem is that we don't have many of the the custom hardware
components that will make up the production system. The software works
great with mock objects taking the place of the hardware, but until we
test the system with the actual hardware, we won't really know if
everything works.

Integration testing is starting tomorrow, so I'll be in the office this
evening putting the final touches on the test environment. Hardware
components will be showing up during the week, so I expect many long
hours of hooking new things up and figuring out why they aren't working.

It is too early to really know what we did right and what we should do
differently next time, but I've already started my lists:

What we did right:

-   developed simulators for the non-existent hardware and host server
-   designed an architecture that made it easy to enable/disable various
    features and to use simulators just like they are the real things
-   refactored and redesigned as we went along
-   as the deadline approaches, the managers have been willing to reduce
    the scope
-   we haven't had to work overtime very much (although that may change
    in the coming weeks)

What we didn't do right:

-   few automated tests
-   didn't find time for code reviews
-   haven't had any non-developers use the system
-   I couldn't figure out how to spend less time managing and more time
    working with the code

The code that we have developed for this project is supposed to become a
new framework to be used for developing similar systems. I already
expect a lot of resistance. We have a lot of decoupling between
different subsystems, which leads to more flexibility but also makes
things look very complicated in comparison to the older codebase. There
are some things that could be made simpler, so I hope to have some time
to clean those things up before presenting the new framework to others
in the software development group. I know they are going to hate it, but
I'm not going to worry about that.

There were a few weeks in the middle of the project when I got a little
depressed and burned out. We weren't getting the information we needed
on hardware, our project manager was re-assigned to another project, and
I felt that it was up to me to fix every problem myself. Thankfully, I
got past that by allowing myself to focus just on what I could do and to
stop worrying about what I couldn't do. Now, we've got a month to go,
and I am pretty optimistic about how things will turn out.

When it's over, I'll allow myself to finally take a vacation. I haven't
had any time off since I joined the company 15 months ago. Not taking
any vacation has probably been my biggest mistake.

After some time off, I'll have to do some heavy thinking about what I
want to do with my career. This recent project experience has given me
more insight into how the company works and how its management does
things. I have more data to consider as I decide whether this is where I
want to stay for a while, or whether it is time to move on to something
else. At the moment, "something else" is very attractive, but I don't
know how I'll feel after the project is behind me.

