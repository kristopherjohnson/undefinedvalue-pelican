Title: Branching and Merging
Date: 2004-02-28 16:45
Author: Kristopher Johnson
Tags: versioncontrol, programming, sourcesafe
Slug: branching-and-merging

A few months ago, we started developing a new product that was a major
extension of an existing product. While we may have been able to keep
one codeline that supported both the old product and the new product,
many factors led us to decide to branch the codeline. I have continued
to maintain the old codeline for existing deployments, while I and a
group of others have worked on the new codeline.

In the new codeline, we have tried to correct many of our past sins. The
original product was developed under a tight deadline with vague
requirements and insufficient testing, and the codeline reflects that.
The new codeline has some significant architectural changes in addition
to having the new features.

I have been trying to keep things in sync between old and new. When we
find and fix a bug in one codeline, or when a feature change is made
that is desirable for both codelines, I merge that change into the
other. This was easy at first, but as the underlying architectures
diverge, it has become more difficult.

One problem is that we are using SourceSafe, and I can't find any good
features for assisting in analyzing the differences between branches to
intelligently decide what needs to be merged and what does not. At the
level of individual files, branches can be merged, but I can't find an
easy way to get a report of all changed for all files in both codelines
and to merge individual sets of changes. (Maybe SS has better features,
but I can't find them.) So we have had an informal manual process, which
relies on other people telling me about things that have to be merged,
and on my having time to do the merge.

This situation sucks, so what I decided to do about it was to write some
Python scripts to help me. The first script I've written just compares
the files in two directories, and writes diff files to a third
directory. My hope was that this would give me a list of a dozen or so
non-matching files, and I could spend the weekend getting everything
back in shape. I'd then just run the script every few days to find new
changes.

Unfortunately, when I ran the script, I found that the number of
non-matching files was 135. Each codeline also has a few dozen files
that are unique (that is, not corresponding to a file in the other
project). Clearly, this is going to take more than a weekend.

I'm not sure exactly what I should have done to prevent things from
getting so bad. Obviously, having one person (myself) be the only person
working on synchronization between the codelines was a problem. Not
having automated unit tests is another factor, because without such
tests, it is dangerous to have changes merged back and forth without a
lot of analysis. A better version-control tool would have helped,
particularly one that supports merging an identifiable set of related
changes to multiple files rather than forcing an all-or-nothing merge of
all changes on a file-by-file basis.

Ultimately the core problem is that our original codeline had to be
thrown together hastily, leading to code that is difficult to adapt to
our new requirements while still meeting the old requirements. So I can
blame management for not giving us sufficient time. Unfortunately,
management isn't going to fix my problem for me, so I'll be working this
weekend.

(For another story about branching/merging issues, I recommend the story
of [Mac Word 6.0](http://weblogs.asp.net/Rick_Schaut/archive/2004/02/26/80193.aspx).)

