Title: 20 Years Ago
Date: 2012-06-05 00:22:21
Category: Blog
Slug: 20-years-ago
Alias: 2012/06/04/20-years-ago/
Tags: selfindulgence


It was 20 years ago this month that I graduated from college and got my first professional programming job. It has me reminiscing about what the computer programming profession was like before the Internet.
<!--break-->
I had used the Internet in college. However, back then we didn't have web browsers. We had [FTP](http://en.wikipedia.org/wiki/File_Transfer_Protocol), [Gopher](http://en.wikipedia.org/wiki/Gopher_(protocol)), and [Usenet newsgroups](http://en.wikipedia.org/wiki/Usenet). So all that I really did with the Internet was download some software and engage in stupid arguments.

Back then the only way to be on the Internet was to be at a university or working for a company that did work for the Department of Defense. So when I graduated, that was the end of the Internet for me, until a few years later when [GEnie](http://en.wikipedia.org/wiki/GEnie), [CompuServe](http://en.wikipedia.org/wiki/CompuServe),) and [America Online](http://en.wikipedia.org/wiki/AOL) started provding Internet access to the masses.

Here's what a programmer's life was like back then:

My job search consisted of looking at classified ads in newspapers. I'd send a printed resum&eacute; and cover letter to each local company that was hiring programmers.  The interviewing process was very similar to what it is today, except that there was no way to tell someone to look at your Stack Overflow or Github acttivity to get a feel for how well you could write code.

I got a couple of job offers, and took the one that seemed more interesting. Of course, back then it was hard to get a feel for how good an employer any company could be, due to lack of message boards or other ways to chat with current and former employees of that company.

When I started work, I had a [DEC VT340](http://terminals.classiccmp.org/wiki/index.php/DEC_VT340) display in my cubicle. This was connected via a local area network ([10BASE2](http://en.wikipedia.org/wiki/10BASE2), I believe) to the terminal server connected to a [VAXcluster](http://en.wikipedia.org/wiki/VMScluster).  The DEC VT340 was a character-based terminal, supporting 80x24 and 132x24 resolutions. It could even display multiple colors!

We wrote software for the following platforms:

- [SunOS](http://en.wikipedia.org/wiki/SunOS) (later to be renamed "SOLARIS")
- [AT&T System V](http://en.wikipedia.org/wiki/UNIX_System_V) UNIX
- [VMS](http://en.wikipedia.org/wiki/OpenVMS)
- [OS/2](http://en.wikipedia.org/wiki/OS/2) 1.3

Notice the lack of a notable operating system in that list?  We didn't touch Windows until NT 4.0 was released.  Our users had to use VT100-style terminals for most of our apps. A few "graphical" apps ran on OS/2 with a Matrox graphics card that displayed 1280x1024 images (and cost a few thousand dollars).

I had a [Macintosh SE](http://en.wikipedia.org/wiki/Macintosh_SE) at home, but _nobody_ in the professional world used Macs, and Apple was expected to go out of business any day.

Everything we wrote had to be portable between all those operating systems. Everything was written in C. Some of the compilers supported the new [ANSI C](http://en.wikipedia.org/wiki/ANSI_C) standard, but some did not, so most of the code was old K&R-style C. I learned a lot about writing portable code back then, and today I still feel a shudder whenever I have to use a proprietary API.

I settled on [Emacs](http://en.wikipedia.org/wiki/Emacs) as my editor back then. It was awesome because on a 80x24 display you could _display two files side by side_, and you could show _a terminal window and debugger window at the same time_. (I would never recommend that anyone learn Emacs today, but back then, it was the best way to work.)

A full build of our application from scratch took almost 24 hours. Obviously, you can't get much done with a 24-hour build-and-run cycle, so we would coordinate among ourselves to make whatever changes were needed, then schedule a recompilation of the minimum set of source files, and if they all compiled then we would relink the application. Even this minimal effort often took almost an hour, so everyone was very careful about making changes.

I had done a little C++ in college, and was hoping to use that again, but the company had done a big project in C++, and had so many problems with the compilers that they swore never to use C++ again.  (We would eventually use C++ a few years later when the time came to develop Presentation Manager applications for OS/2.)

Before the Internet, "online documentation" meant [man pages](http://en.wikipedia.org/wiki/Man_page).  Try reading a few man pages on an 80x24 display, and imagine that being your only online source of operating system information.

Thankfully, we also had complete sets of the hardcopy documentation. One entire wall of the office contained the then-current VMS documentation. Another wall contained the previous-version VMS documentation. A third wall had the UNIX documentation. 

Back then, the O'Reilly books about UNIX utilities were the most valuable things you had in your cube. You could also rely on your memory, because as complex as these operating systems were for the time, their APIs only consisted of a few dozen functions.  It was actually possible to memorize the entire platform API (try that with Java or .NET).

Delivering a software release to a client meant sending them a [DECtape](http://en.wikipedia.org/wiki/DECtape), either through the mail, or when a fix was urgently needed, by overnight courier. Because remote access to the sites was often impossible, or impractical due to slow modem speeds, we'd often need to physically visit sites to install new software or upgrade existing software.

We didn't have email. We wrote memos, and had a lot more meetings that people do these days. An administrative assistant took the mail cart around each day to deliver the memos and mail. We generated many, many binders full of technical documentation. Some of that documentation was created by technical writers using [WordPerfect](http://en.wikipedia.org/wiki/WordPerfect), but a most of it was plain ASCII text and simple [ASCII art](http://en.wikipedia.org/wiki/ASCII_art).

Back then, I knew everything, and I was going to change the world. It was a wonderful feeling. I consider myself fortunate to have learned programming before Windows and Java ruined everything. But now I have a computer in my pocket that is more powerful and more useful than the million-dollar mainframe I wrote code for back then, so I wouldn't want to go back.
