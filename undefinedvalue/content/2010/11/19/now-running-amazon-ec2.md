Title: Now Running on Amazon EC2
Date: 2010-11-19 23:13:19
Category: Blog
Slug: now-running-amazon-ec2
Alias: 2010/11/19/now-running-amazon-ec2/
Tags: blog, ubuntu, ec2, drupal, admin


This blog is now running in the [Amazon Elastic Compute Cloud (EC2)](http://aws.amazon.com/ec2/). I hope that nobody notices any difference.
<!--break-->
Migrating the blog over to the new server was relatively straightforward, using Drupal's [Backup and Migrate](http://drupal.org/project/backup_migrate) module. After [getting Drupal set up on the new server](/2010/11/12/setting-drupal-ubuntu-1010-ec2), I just copied all my themes, modules, and files from the old server to the new and then did a restore of the database.

I am using a [t1.micro](http://aws.amazon.com/ec2/instance-types/) EC2 instance, which is the cheapest and least-powerful EC2 instance. So far, it seems to be handling the load fine, but I'll need to see how it works over the next few weeks. If all goes well, I'm going to try moving all my other web sites to the same server. None of my sites gets more than a few hundred hits per day, so if I can handle them all with one cheap easy-to-manage server, I'll be very happy. But if I have to upgrade to a beefier instance, all it takes is a couple of minutes and a few dollars.

Time will tell how bad being dependent on Amazon is in comparison to being dependent on the web hosting services I've used. I suspect it will be better.

I'm switching to [Google Apps](http://www.google.com/apps/intl/en/group/index.html) for my e-mail and other such services. Configuring and managing your own e-mail servers these days is a colossal waste of time unless you have some very special requirements.

## A Few Weeks Later...

Amazon AWS charges for November: $2.88.  $2.40 of that was for having an unattached elastic IP address for 240 hours, and $0.17 was for running a Small (rather than Micro) instance for a couple of hours, so I expect my costs going forward to be lower.

AWS charges for December: $0.52.

AWS charges for January: $0.52.

(In contrast, my previous hosting plans cost me a total of $20 per month.) 

Google's webmaster tools indicate that my blog pages are now downloading in about 150 ms, as opposed to around 400 ms with my old provider. So performance seems to have improved quite a bit.
