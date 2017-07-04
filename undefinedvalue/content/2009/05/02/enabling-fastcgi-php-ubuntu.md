Title: Enabling FastCGI for PHP on Ubuntu
Date: 2009-05-02 08:44:35
Category: Blog
Slug: enabling-fastcgi-php-ubuntu
Alias: 2009/05/02/enabling-fastcgi-php-ubuntu/
Tags: ubuntu, sysadmin, php, fastcgi, debian, apache, drupal


I'm setting up a [virtual private server](http://en.wikipedia.org/wiki/Virtual_private_server). If all goes well, I'll be moving all my websites from their current shared-hosting arrangements to this VPS.

I started with a minimal Ubuntu 8.10 image and installed all the LAMP stuff. Things went smoothly until I decided to try to enable FastCGI for Drupal. Googling for things like "ubuntu apache php fastcgi" results in zillions of links to suggested methods, all of which were very complicated and required digging through docs.  I figured there had to be a simple way to do it.

After a few hours of research, I finally did stumble upon what I wanted.  My problem was that I was googling for "ubuntu", when I should have been googling for "debian".

The info I needed was here: http://michiel.vanbaak.info/docsphp5fcgi.htm.  Thank you, Michiel&nbsp;van&nbsp;Baak!

(To those of you saying "But you should really be using [nginx](http://en.wikipedia.org/wiki/Nginx) instead of Apache," my response is "Yes, I know. Leave me alone.")
