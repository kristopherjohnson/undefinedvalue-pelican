Title: Setting Up Drupal 6 on Ubuntu 10.10 on EC2
Date: 2010-11-12 22:14:23
Category: Blog
Slug: setting-drupal-6-ubuntu-1010-ec2
Alias: 2010/11/12/setting-drupal-ubuntu-1010-ec2/
Tags: ubuntu, ec2, drupal, admin


For several years, I've been using pretty-cheap web hosting services for my blog, my [corporate website](http://capablehands.net), and other webby things. However, I'm pretty sure that it would be even cheaper to use [Amazon EC2](http://aws.amazon.com/ec2/), especially as they now offer [free usage](http://aws.amazon.com/free/) for a year. I also like the ease with which one can scale EC2 servers up or down, and run temporary instances for a few cents per hour.

Of course, this means I have to figure out how to move everything from where it is to a new EC2 instance. Most of the stuff I care about is managed in [Drupal](http://drupal.org/), so step one is figuring out how to set up Drupal on an EC2 host.

I decided to go with [Ubuntu](http://www.ubuntu.com) as my OS, because I'm a long-time Debian user and my brushes with Ubuntu have been positive. A little research showed that they had an easy-to-install `drupal6` package and a few other packages that I plan to use in my plans for world conquest.

But no matter how easy/straightforward things look, they are always a little bit complicated. Here are my notes for setting things up, which may be helpful to others, and will probably be helpful to me whenever I end up redoing this.

I assume the reader has basic knowledge of how to connect to servers via SSH, knows a little bit about setting up Apache and Drupal, and is comfortable using a text editor to modify configuration files.
<!--break-->
### Launch Ubuntu 10.10 Instance on EC2

(For more details and help, check out the [EC2StartersGuide](https://help.ubuntu.com/community/EC2StartersGuide) in Ubuntu Community Documentation.)

0. If you don't already have an Amazon Web Services account, go to http://aws.amazon.com/ and click the Sign Up Now button. After you give them all your info (including credit card info), you may need to wait for authorization to use the services. (I had to wait about 12 hours.) Then create and download your private keys and certificates. (Note: in the rest of this document, I'll use the symbol `$EC2_PKEY` to mean the full path and name of your stored private key file.)
0. Sign in to the [AWS Management Console](https://console.aws.amazon.com/s3/home) (which, unfortunately, requires Adobe Flash Player, so you can't do this on an iPad).
0. Click the *Amazon EC2* tab, and click the *Launch Instance* button
0. Choose a suitable AMI. I went with ami-508c7839, which is a 32-bit EBS-based Ubuntu 10.10 instance that runs in the US-East availability zone. For lists of other available Ubuntu AMIs, see the [EC2StartersGuide](https://help.ubuntu.com/community/EC2StartersGuide) and the [Alestic](http://alestic.com/) site.
0. On the *Instance Details* page of the wizard, set these details:
  * Number of instances: 1
  * Instance type: Micro (required for Free Tier)
  * Availability Zone: No preference
  * Launch Instances
0. For *Advanced Instance Options*, accept the defaults.
0. Fill in something for the Name tag. You will eventually have a list of instances, so make this descriptive.
0. Choose a new key pair or create a new one.
0. Choose an existing security group or create a new security group. It is **very important** that you set up a security group that allows access via the SSH port, and you probably want the HTTP port open also.
0. Assuming everything looks good, click the *Launch Instance* button.
0. Return to the *Amazon EC2* tab in the AWS Management Console. You should see your new instance with a status of "Pending". Wait for it to become "Running".
0. Select your new instance in the top pane. In the bottom pane, you will see a bunch of info. Select the contents of the *Public DNS* field. It will look something like this: `ec2-XX-XX-XX-XXX.compute-1.amazonaws.com`. This is the hostname you will use to connect. In the rest of this guide, I'll denote this address as `$EC2_HOST`in the rest of this article.
0. Verify that you can connect to the new instance. If you have Mac OS X, Linux, or another UNIXy box, you can run SSH like this: `ssh -i $EC2_PKEY ubuntu@$EC2_HOST`. If you are on Windows, then figure out how to use [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/).  If all is well, you will be greeted with a prompt like this: `ubuntu@ip-XX-XX-XXX-XXX:~$ `.

### Set Up DNS

You *could* use that Public DNS to connect to your server forever, but you will probably want a real domain name. So, head on over to your favorite registrar and register a new domain, or change an existing domain to point to your new server.

Amazon recommends using a CNAME (alias) record that points to your EC2 instance's public DNS. However, I've found that the public DNS can change for no apparent reason, so if you expect people to connect to your site, you should use Amazon's Elastic IP service to assign a static IP address to your server. (Note that after assigning the static IP, the public DNS for your server will change to match the static IP, so be sure to refresh your EC2 dashboard instance display after setting up the Elastic IP to get the final DNS or IP address.)

I'll use the symbol $MY_HOSTNAME in the remainder of this document to denote the domain name that you want to use. (In my case, $MY_HOSTNAME is "happyspacelab.com".)

### Install Drupal and Related Packages

0. Go back to your SSH command prompt on the EC2 box (reconnecting if necessary).
0. Update the package index with this command: `sudo apt-get update`
0. Upgrade existing packages with this command: `sudo apt-get upgrade` (Answer "Yes" when asked whether to continue.)
0. Install Drupal and all dependencies (Apache, MySQL, PHP, etc.) with this command: `sudo apt-get install drupal6`
   * You will be prompted for various passwords and names. Write down whatever you enter.
   * Mail Configuration: No configuration (unless you really want to do this now)
   * Database type: mysql
   * Default choices for everything else
0. Restart Apache with this command: `sudo /etc/init.d/apache2 restart`
0. Verify that Apache is working and all the firewalls have port 80 open by visiting your site with a web browser. You can use `http://$EC2_HOST` or `http://$MY_HOSTNAME` (assuming enough time has passed for DNS propagation). You should see a web page that says "It Works!".
0. Visit the Drupal installation page: `http://$EC2_HOST/drupal6/install.php` (and then follow normal Drupal installation procedures)
   * Click the link to set up in English
   * Fill in the fields and click *Send and continue*
      * Note: You will not be able to enable Clean URLs at this time. Don't worry; we'll get to that.
   * If you have not set up email on the server, you'll get a warning that mail could not be sent. Ignore.
At this point, you should have a usable Drupal installation, accessible at `http://$EC2_HOST/drupal6/` or at `http://$MY_HOSTNAME/drupal6`. Go into the Administration screens and configure the site as desired, or wait until you have finished subsequent steps.

### Set Up Virtual Host

The `/drupal6/` part of the URL is ugly, so we'll set up virtual hosting so that the Drupal content is available at `http://$MY_HOSTNAME/`.

0. Go back to your SSH command prompt on the EC2 box (reconnecting if necessary).
0. `cd /etc/apache2/sites-available`
0. Create a new file named $MY_HOSTNAME (substituting your actual hostname), with these contents (and remember to start your editor with `sudo`):
    &lt;VirtualHost *:80&gt;
        ServerAdmin webmaster@$MY_HOSTNAME.com
        ServerName $MY_HOSTNAME
        ServerAlias $MY_HOSTNAME *.$MY_HOSTNAME.com
        DocumentRoot /usr/share/drupal6
        RewriteEngine On
        RewriteOptions inherit
    &lt;/VirtualHost&gt;
0. `sudo a2ensite $MY_HOSTNAME`
0. `sudo a2enmod rewrite`
0. Open the file `/usr/share/drupal6/.htaccess` with a text editor (remember `sudo`), and uncomment the line that says
    RewriteBase /
0. `sudo /etc/init.d/apache2 restart`
0. Visit `http://$MY_HOSTNAME/` with a web browser. You should see the Drupal front page, rather than the "It Works!" page.

### Enable Clean URLs

With the virtual hosting stuff set up, you can now enable Clean URLs in Drupal. Log in to the Drupal page as administrator, go to Administrator > Site Configuration > Clean URLs, select *Enable* and click *Save configuration*.

### Set Up Memcached

Amazon will be charging us for EBS I/O requests (we only get one million free I/O requests per month with the Free Tier), so let's set up Drupal to use [memcached](http://memcached.org/) to reduce the amount of I/O and improve performance.

This is a simple setup, using a single memcached instance running on the local machine. For more complicated situations, refer to the [Drupal memcache module documentation](http://drupal.org/project/memcache).

0. `sudo apt-get install memcached php5-memcached`
0. In the file `/etc/php5/apache2/conf.d/memcached.ini`, add this line: `memcache.hash_strategy="consistent"`
0. Download and unarchive the [Memcache API and Integration](http://drupal.org/project/memcache) module in `/usr/share/drupal6/sites/all/modules`
0. In your site's `settings.php`, add the snippet provided below to set `cache_inc` and `memcache_key_prefix`.
0. `sudo /etc/init.d/apache2 reload`
0. Go to Administer > Site building > Modules and enable the Memcache Admin module
0. Go to Administer > Site configuration > Memcache and enable "Show memcache statistics at the bottom of each page". After this is enabled, you can scroll down to the bottom of the page to verify that memcache is working and that things are in the cache. (You can then disable this if you find the display annoying.)

Here is the snippet to be added/modified in `settings.php`. In place of `some_unique_prefix`, substitute your site's name or some other value that is unique for your site.

    $conf = array(
        'cache_inc' => '/usr/share/drupal6/sites/all/modules/memcache/memcache.inc',
        'memcache_key_prefix' => 'some_unique_prefix',
    );


### Set up Alternative PHP Cache

As a further measure to reduce the number of I/O requests and improve performance, we'll install the [Alternative PHP Cache](http://www.php.net/manual/en/intro.apc.php) (APC).

0. `sudo apt-get install php-apc`
0. Add the following line to `/etc/php5/conf.d/apc.ini`

<pre>
apc.stat = 0
</pre>

You can monitor the performance of APC by installing the `apc.php` script:

0. `sudo gunzip /usr/share/doc/php-apc/apc.php.gz`
0. `sudo ln -s /usr/share/doc/php-apc/apc.php /usr/share/drupal6/apc.php`
0. In a web browser, go to `http://$MY_HOSTNAME/apc.php`. You should see stats for APC.

### Performance Adjustments

0. Go to Administer > Site configuration > Performance
0. Set _Caching Mode_ to "Normal"
0. Set _Page compression_ to "Disabled" (Apache is already configured to compress stuff, so there is no need to have Drupal do it.)
0. Set _Block cache_, _Optimize CSS files_, and _Optimize JavaScript files_ to "Enabled"
0. Click the _Save configuration_ button

### Set Up Drupal Multisite

If you are cheap enough to go with free hosting, you'll probably want to go ahead and put multiple Drupal sites, each with their own doman name, on this same host. This is fairly easy to do. Here are a bunch of documents describing how to do it: http://drupal.org/node/43816

However, here are quick-and-dirty instructions:

0. For each site, create a file in `/etc/apache2/sites-available` like you did in the **Set Up Virtual Host** section, above.  Substitute the appropriate host name in each new file.
0. `cd /usr/share/drupal6/sites`
0. Copy the `default` site to a directory named $MY_HOSTNAME: `sudo cp -a default $MY_HOSTNAME`
0. For each site, you need to create another database. Here's the easy way to do that:
   0. Run this command: `sudo dpkg-reconfigure drupal6`
   0. Answer the prompts as follows:
      0. Reinstall database: Yes
      0. Database type: mysql
      0. Connection method: Unix socket
      0. Name of the database's administrative user: root
      0. Password: [root's MySQL password, as you specified when MySQL was installed]
      0. Username for drupal6: [enter a site-specific user name to own the new database, e.g., "myhostname2"]
      0. Database name: [enter a site-specific database name, e.g., "myhostname2"] 
   0. The new configuration is in the `/usr/share/drupal6/sites/default` directory. Copy that to host-specific directory: `sudo cp -a default myhostname2`
   0. The `sites\default` directory that you just copied has a `files` directory which is a symlink to `/var/lib/drupal6/files`. If you don't want all your Drupal instances to put their files in the same place, then do the following:
      0. `sudo rm myhostname2/files`
      0. `sudo mkdir myhostname2/files`
      0. `sudo chown myhostname2/files`
      0. `sudo chgrp www-data myhostname2/files`
      0. `sudo chmod 750 myhostname2/files`
   0. `sudo /etc/init.d/apache2 restart`
   0. Visit `http://myhostname/install.php` to complete the installation process for this new Drupal instance.
   0. Repeat the site-specific steps for setting up memcached (update settings.php, enable the module, etc.), and repeat the Performance Adjustments steps

For more details on this method of setting up multisite on Ubuntu, see http://drupal.org/node/138889

After setting up a few sites this way, I found that the daily Drupal cron job would run for some of my sites, but not for others. The cron job is triggered by the file `/etc/cron.d/drupal6`, which calls `/usr/share/drupal6/scripts.cron.sh`, but I never figured out exactly why it was working for some sites and other others.

I was able to get the cron job running for all sites by adding a `baseurl.php` file to each of the `/usr/share/drupal6/sites` subdirectories. `/usr/share/drupal6/scripts.cron.sh` looks at this file, and at `settings.php`, to determine the appropriate URL for invoking the script that site. The contents of each file should look like this:

    $base_url = 'http://example.com';

Substitute the appropriate host name for `example.com`. Note that the URL should _not_ have a slash at the end.

### Cleaning Up

So, you've followed all the instructions above, and you've got a working Drupal server. Congratulations!

Remember that Amazon is going to be charging you for this instance that you've set up. Even if you stop the instance, Amazon still charges you by the hour. So, if you aren't really ready to use this instance, you'll want to terminate it via the AWS Management Console.

Note that "terminating" really means "deleting". After terminating the instance, you won't be able to restart it. It's gone forever, unless you take steps to save the image in S3.

### Odds and Ends

   * The Drupal [Backup and Migrate](http://drupal.org/project/backup_migrate) module makes it easy to move Drupal data from your old site to your new site.
   * If you don't want to set up your system as a mail server, but do want SMTP to work so that Drupal can send you mail, look at the [SMTP Authentication](http://drupal.org/project/smtp) module.
   * [Duplicity](http://duplicity.nongnu.org/) is a nifty tool for making incremental backups to Amazon S3 (or other destinations). See http://www.problogdesign.com/how-to/automatic-amazon-s3-backups-on-ubuntu-debian/.

### To-Do

There are a few little things I want to figure out when I have time. If anyone already knows the answers, I'd appreciate learning about them.

   * The Ubuntu AMI is a 15 GB boot image, but I am using less than 2 GB of it. The Amazon Free Tier only allows 10 GB of EBS storage, so I've thought about shrinking the boot image. (On the other hand, 5 GB of excess storage only costs fifty cents per month, so why worry?)
   * I want to automatically back up my volume and my MySQL database to S3 periodically.

### References

Here are some links I traversed while figuring this stuff out:

   * https://help.ubuntu.com/community/EC2StartersGuide
   * http://drupal.org/node/138889
   * http://groups.drupal.org/node/8004
   * http://awebfactory.com.ar/node/275
   * http://www.sunsetlakesoftware.com/2010/09/15/how-run-drupal-amazon-ec2-using-new-micro-instance
   * http://www.control-escape.com/web/configuring-apache2-debian.html
   * http://drupal.org/project/memcache
   * http://fplanque.com/dev/linux/install-apc-php-cache-debian-lenny
   * http://www.imminentweb.com/technologies/tune-apc-improve-php-performance
   * http://2bits.com/articles/high-php-execution-times-drupal-and-tuning-apc-includeonce-performance.html
