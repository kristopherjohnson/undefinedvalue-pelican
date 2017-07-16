Title: Workflow for Remote CVS, Local Git
Date: 2010-07-02 13:31:32
Category: Blog
Slug: workflow-remote-cvs-local-git
Alias: 2010/07/02/workflow-remote-cvs-local-git/
Tags: git, cvs
AdSense: yes


One of my clients uses a [CVS](http://ximbiot.com/cvs/) repository for all its source code. People recognize that there are better options available than CVS, but it's been cranking along fine for 15 years, and they see no compelling reason to change.

However, I really like being able to commit incremental changes often in my own personal branches, and while not connected to the company network (I work from home). So I've been checking out files from the CVS repository, using [Git](http://git-scm.com/) locally to manage modifications, and then periodically committing those changes back to the remote CVS repository.

I figured I'd write up what I'm doing, in case others want to try the same thing, or others can tell me a better way to do what I'm doing. I'm still a bit of a Git newbie, so if I'm doing something stupid, please let me know.
<!--break-->
I'm assuming the reader has a basic understanding of CVS and Git. If not, see the [CVS manual](http://ximbiot.com/cvs/manual/) and/or the [Git tutorial](http://www.kernel.org/pub/software/scm/git/docs/gittutorial.html). I predominantly work on Windows, but I use [PowerShell](http://en.wikipedia.org/wiki/Windows_PowerShell), so there is no difference between the commands I use on Windows and those I use on Mac OS X or Linux.

In the examples, I'll use a few variables:

    USER=myusername
    CVSROOT=:pserver:$USER@cvsserver:2401/cvsrepository
    PROJECT=myprojectname
    DROPBOX=mydropboxfolder

($DROPBOX refers to my [Dropbox](https://www.dropbox.com/referrals/NTE0Mzc3MDY5?src=global0) directory, where I keep all sorts of little files that I want synched to all my computers.  If you haven't looked at Dropbox, do.)

First, we need to get the CVS repository.  Git does have a [git-cvsimport](http://www.kernel.org/pub/software/scm/git/docs/git-cvsimport.html) command that I could use to suck all the CVS stuff into a local Git repository, but the CVS repository is huge, so that would be very slow, and frankly, I don't really trust `git-cvsimport`. So I just do what I would normally do to get stuff from CVS:

    cvs login
    cd ~/work
    cvs checkout $PROJECT

Next, I set up the local Git repository:

    cd ~/work/$PROJECT
    git init

The working directory contains a lot of files that I don't want or need to track with Git, so I've got a standard `.gitignore` file that looks like this:

    CVS
    .#*
    
    .hg
    .hgignore
    
    bin
    obj
    Debug
    Release
    TestResults
    *.obj
    *.suo
    *.ncb
    *.user
    *.tli
    *.tlh
    *.idb
    *.pdb
    
    build
    *.pbxuser
    *.perspectivev3
    .DS_Store
    xcuserdata
    
    *.old
    *.log
    *.out
    *.cache
    
I just copy it from my Dropbox:

    cp $DROPBOX/.gitignore .

Now, I'm ready to import everything into the Git repository:

    git add .
    git commit -m "Initial commit"

I keep a local tag `cvssync` that indicates the last time that the Git and CVS repositories matched.

    git tag cvssync

Now I'm ready to do some work.  I always want the `master` Git branch to match CVS, so I create a topic branch where I do my work:

    git checkout -b develop

After very efficiently and productively adding all the error-free code needed to implement whatever I'm implementing, I'm ready to commit on my `develop` branch.

    git commit -am "Implemented the whosey-whatsit"

I tend to commit changes frequently. If I go more than an hour or so without a commit, I get worried.  The great thing about frequent commits is that it is easy to undo things.  The bad thing about frequent commits is that your commit history has lots and lots of entries, but as nobody is going to see that history but me, I don't worry about that.

Now my boss calls and asks when the thing is going to be ready, and I tell him I'll check it into CVS right away.  

First, I quit Visual Studio or whatever editor(s) I'm using, because the next few operations will cause the contents of files to change, and IDE's often don't handle that gracefully. This step also ensures that I don't forget to save all my changed files.

I have to merge the `develop` branch back into the `master` branch:

    git checkout master
    git merge develop

Then, I pull in whatever changes others have added to CVS

    cvs update -d
    git commit -am "Sync with CVS"

(I skip the `git commit` here if there were no changes from CVS.)

I check what I've changed since the `cvssync` tag, to remind myself and to verify it is right:

    git log cvssync..
    cvs diff

Finally, I can push my changes to CVS:

    cvs commit -m "Implemented the whosey-whatsit"

My employer likes to put the `$Id$` tag into source files, so after a `cvs commit`, any committed files are going to have new identifiers, so I need to commit those changes to my `master` branch

    git commit -am "Sync with CVS"

I update my `cvssync` tag:

    git tag -f cvssync

If, while I'm doing my work, others check things into CVS, and I need those changes, here is what I generally do (after quitting Visual Studio):

    git commit -am "Check in work branch"
    git checkout master
    cvs update -d
    git commit -am "Pull from CVS"
    git checkout develop
    git rebase master

It may seem like a lot of work, but it's saved me a couple of times already. I have some aliases and scripts that automate some of the steps, so my actual workflow is not as verbose as what I've written here.
