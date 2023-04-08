Title: Simpler Résumé Updates
Slug: simpler-résumé-updates
Date: 2023-04-08 13:12:37.538605
Category: Blog
Tags: automation, jobsearch

I decided to update my résumé this week. No, I haven't lost my job, and I'm not
actively looking for a new one, but a little while ago I asked people on
Mastodon how to acquire practical experience with "cloud stuff" if your job
doesn't provide it, and someone suggested
[The Cloud Resume Challenge](https://cloudresumechallenge.dev).  (Unfortunately
I can't find the post that suggested it, and can't remember who made it, but
thank you anonymous helpful Mastodon person.)

The challenge is to create a website that displays your résumé, but uses various
features of AWS, Azure, Google Cloud Platform, or whatever cloud provider you
want to explore.  So, when you go looking for a cloud-related job, you have your
résumé online and you can talk to an interviewer about all the interesting stuff
you learned about deploying a website to the cloud with load balancing and
serverless code and whatever else you want to brag about.

I've started the learning process (and I've passed the AWS Certified Cloud
Practioner exam), but before I go further I decided I should probably have an
up-to-date résumé.  For the past couple of decades I've had a résumé in multiple
formats (Word, PDF, RTF, etc.) and when I've needed to update it, I've had to
make edits to all of those files and then deploy them to all the places where it
is available for download.

Making similar small edits to a few files every few years isn't a lot of work,
but it does seem like the kind of thing I should automate for my fancy new
cloud-native résumé website deployment.

This turned out to be pretty easy.  I started with the plain-text ("ASCII")
format of my résumé and converted it into
[Markdown](https://daringfireball.net/projects/markdown/syntax) format by adding
a few formatting tags.  The result of that process is visible here:
<https://github.com/kristopherjohnson/resume/blob/main/src/kjresume.md>.

Then I set up a
[Makefile](https://github.com/kristopherjohnson/resume/blob/main/Makefile) with
rules for using [Pandoc](https://pandoc.org) to generate all the other formats
from that source file.  So, whenever I need to update my résumé, I just edit
`kjresume.md` and then I can execute `make all` to generate all the other
formats, and then push that back up to my
<https://github.com/kristopherjohnson/resume> repository.

Finally, I just have to update all the pages that have links to my résumé (for
example, the [My Résumé](https://undefinedvalue.com/pages/kjresume.html) page on
this website) so that they point to the auto-updated files in my GitHub repo.

The best thing is now I don't have to install Microsoft Word again whenever I
want to update my résumé.
