Title: What's Good on TCM This Week?
Date: 2016-11-04 22:34:41
Category: Blog
Slug: whats-good-tcm-week
Alias: 2016/11/04/whats-good-tcm-week/
Tags: tcm, node, movies


I like old movies. In the old days, we had TV stations known as "UHF channels" that showed lots of old movies all night long. But UHF channels are gone, and today all we have is the Turner Classic Movies (TCM) channel and website.

I like film noir, sci-fi, horror, and westerns. TCM has a lot of these movies, but it also shows a lot of stuff I'm not interested in. I don't like browsing the upcoming schedule via the TCM website or via my cable provider's interface, so I wanted a way to generate a schedule just for me so that I can record good stuff on my DVR, or watch available movies on [Watch TCM](http://www.tcm.com/watchtcm/) or my cable provider's on-demand service.

It turns out that TCM offers a [web services APIs](http://www.tcm.com/tcmws/v1/docs/welcome.html) that allow one to retrieve schedule information. So I've whipped up a script that that grabs the schedule for the next week and identifies the movies that match my preferences.

The result is a web page: [What's Good on TCM?](http://secretspacelab.com/tcm.html).

The page displays the movies coming up during the next week that might be "good" according to my taste. You can click the name of a movie or name of a director, actor, or screenwriter to search the TCM database for more information.

Your preferences may not match mine. That's OK; if you are a computer person, you might be able to customize my script to find your musicals or romances or screwball comedies or whatever it is you want. It's available on GitHub: <https://github.com/kristopherjohnson/kjtcmws>.
