Title: Configuring WebDAV and Digest Authentication for Ubuntu
Date: 2011-12-08 22:42:40
Category: Blog
Slug: configuring-webdav-and-digest-authentication-ubuntu
Alias: 2011/12/08/configuring-webdav-and-digest-authentication-ubuntu/
Tags: webdav, ubuntu
AdSense: yes


I'm looking at using [WPKG](http://wpkg.org/) as a mechanism for distributing software updates to client workstations.  WPKG appears to be a pretty nice system, but it has one big downside: one has to set up a WebDAV-enabled server if the updates are to be pulled from the Internet instead of from a local shared directory.  So I've spent a few hours learning the intricacies of  setting up WebDAV on [my Ubuntu-based Internet server](https://undefinedvalue.com/2010/11/12/setting-drupal-ubuntu-1010-ec2) and accessing it from Windows machines.  Here's what I learned.
<!--break-->
I started by following the steps here: [How To Set Up WebDAV With Apache2 On Ubuntu 9.04](http://www.howtoforge.com/how-to-set-up-webdav-with-apache2-on-ubuntu-9.04).

That seemed to get me working: I could access the `webdav` directory without any problem using web browsers, Mac OS X, or Linux.  However, it didn't work when I tried to connect from Windows, which is unfortunate, because Windows is the one platform where I need it to work.

After a couple of hours of Googling and hair-pulling, I discovered that the problem is that Windows Vista and Windows 7 don't support Basic HTTP authentication for WebDAV.  One needs to either use Digest authentication, or [make registry changes](http://support.microsoft.com/kb/841215) to enable Basic authentication.

I didn't want to force registry changes on all the client machines, and Digest authentication is The Right Thing anyway, so I changed my Apache configuration to do it.

Here are the new lines that ended up in my `/etc/apache2/sites-available/default` file:

        <Directory /var/www/webdav/>
                Options Indexes MultiViews
                AllowOverride None
                Order allow,deny
                allow from all
        </Directory>

        Alias /webdav /var/www/webdav

        <Location /webdav/>
                DAV On
                AuthType Digest
                AuthName "webdav"
                AuthDigestDomain /webdav/
                AuthDigestProvider file
                AuthUserFile /var/www/webdav/.digest_passwd.dav
                Require valid-user
        </Location>

I had to enable the `auth_digest` module:

    sudo a2enmod auth_digest

Then I had to create the digest authentication file, adding the user `test`:

    sudo htdigest -c /var/www/webdav/.digest_passwd.dav webdav test
    sudo chown root:www-data /var/www/webdav/.digest_passwd.dav
    sudo chmod 640 /var/www/webdav/.digest_passwd.dav

With all those changes made, I did this

    sudo /etc/init.d/apache2 restart

And then I verified that I could do the following from my Windows box:

    net use \\example.com\webdav MYPASSWORD /user:test
    dir \\example.com\webdav

With that done, I then set up WPKG and everything was easy and smooth!

(Not really, but the problems weren't due to WebDAV.)
