Title: Git GUI Clients for OS X
Date: 2013-02-28 13:55:54
Category: Blog
Slug: git-gui-clients-os-x
Alias: 2013/02/28/git-gui-clients-os-x/
Tags: github, git


I have recently evaluated a few [Git](http://git-scm.com) GUI apps for OS X. Here are my impressions.
<!--break-->
## SourceTree

<http://www.sourcetreeapp.com>

Pros:

- Free
- Supports Mercurial repositories
- Supports Subversion repositories (via git-svn)
- Supports [git-flow](https://github.com/nvie/gitflow)
- Information-rich display layout (but some say it is too complicated)
- Also available for Windows

Cons:

- Least attractive

I have been using SourceTree for the past year, and while I do remember some confusion when I first used it, it feels very easy to use now. I like its support of Subversion and of git-flow, and I think it has the most useful screen layout. However, it is ugly.


## Tower

<http://www.git-tower.com>

Pros:

- Visually attractive

Cons:

- Not free, most expensive ($59)
- Not available from Mac App Store (If I have to pay for a Mac app, that's where I want to buy it.)
- Inefficient UI (too much empty space, too many clicks required to perform common operations)
- Only shows one repository at a time

Tower is the prettiest of the bunch, but feels inefficient, and is a lot more expensive than the other options. When the 30-day trial expires, I will delete it.


## Gitbox

<http://gitboxapp.com>

Pros:

- Minimalistic (in a good way)

Cons:

- Not free (but only $15)
- Minimalistic (in a bad way)
- No integrated diff-viewer. Viewing differences requires launching an external tool.

Gitbox is focused on making it easy to commit changes with a few keystrokes. It is not very good for browsing through changes, due to the need to use an external app to view changes. This app isn't appealing to me. I don't need a GUI to quickly make commits: I use the command line for that. I like having a GUI to make it easy for me to review changes before I commit or push, and Gitbox doesn't help me with that.


## GitX-dev

<https://github.com/rowanj/gitx>

Pros:

- Free
- Open-source

Cons:

- Clumsy staging workflow

This feels a lot like SourceTree, but is not as polished. It is nice that it's open-source/free-as-in-speech, but if all one cares about is free-as-in-beer, SourceTree is the better free option.


## GitHub for Mac

<http://mac.github.com>

Pros:

- Free
- Nice integration with GitHub.com website
- Attractive easy-to-use UI

Cons:

- Feels dumbed-down

I would recommend this to someone who only uses Git in association with GitHub. It is easy to use and is a great match for the workflow promoted by GitHub. But as a general-purpose Git client, it seems to be missing some features (or maybe I just didn't try hard enough to find them).


## Closing Thoughts

I typically work alone. Sometimes I work with one other developer. I don't have to worry much about merging or keeping track of lots of commits by other developers. So, what I want from a Git client may be different from what others need.

I use the command line for anything "complicated". I don't trust the GUIs to do what I expect. All Git GUIs should provide some sort of log that indicates exactly what git operations they have performed.

It looks like I will stick with SourceTree, but I will force myself to use the others once in a while. SourceTree feels right to me, but I wonder whether that is due more to familiarity than to actual goodness.

I will probably recommend GitHub for Mac to any newbies who ask.
