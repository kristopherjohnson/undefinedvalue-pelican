Title: OS X Server Local Websites for Web Developers
Date: 2014-05-25 12:10:59
Category: Blog
Slug: os-x-server-local-websites-web-developers
Alias: 2014/05/25/os-x-server-local-websites-web-developers/


[OS X Server](https://itunes.apple.com/us/app/os-x-server/id714547929) is now available free of charge for members of Apple's iOS Developer Program, so I have it installed on most of my machines. Unfortunately, having OS X Server installed complicates the use of the built-in local Apache web server which I use for web development. I've figured out how to make things work the way I like, and I have written this article so that I can find the information again when I need it. Maybe it will help somebody else too.
<!--break-->
## Enabling Local Websites

First, to enable the web server, open the OS X Server app, select **Websites** in the sidebar,  and flip the switch to **On**. You should be able to visit <http://localhost/> in a web browser and see a page titled "Welcome to OS X Server".

While you are on the Websites configuration screen, you may want to enable PHP and Python web applications.

If you have the Xcode service enabled, then instead of "Welcome to OS X Server" you may see the Xcode Bots page. This may be OK with you, but if you would rather not see the Xcode stuff in place of the default website, then in the Server app, go to the **Websites** screen, double-click **Server Website** to edit it, click the **Edit...** button next to **Index Files**, and remove the `/xcode` entry. Now, visiting <http://localhost/> should take you to the "Welcome to OS X Server" screen, and you can visit <http://localhost/xcode> to see Xcode Bots.

## Website Directories

Next, you need to know where you can put your website files so that they will be served by the server. By default, the server will look for files in `/Library/Server/Web/Data/Sites/Default`. You could put your files in that directory, but I prefer to use symlinks so that I can keep all my files in my home directory. So, for example, if your main website file is `/Users/kdj/work/mywebapp/index.html`, you can symlink it like this:

    ln -s /Users/kdj/work/mywebapp /Library/Server/Web/Data/Sites/Default/mywebapp

Then if you visit `http://localhost/mywebapp`, you should see your website.

## Per-user Website Directories

Alternatively, instead of making modifications to the `/Library/Server/Web/Data/Sites` directory, you might want to set up per-user websites as are available on OS X when Server is not installed and "Web Sharing" is enabled. To do this, you have to edit the `https_server_app.conf` configuration file. This file is only writable by root by default, so you will need to use `sudo`. So, for example, if you use `vi`, then do this to edit the file:

    sudo vi /Library/Server/Web/Config/apache2/httpd_server_app.conf

You need to uncomment two lines. First, uncomment the line for `apple_userdir_module` to enable it:

    #Server-specific modules
    # SERVER_INSTALL_PATH_PREFIX should be set as Environment variable in launchd.plist
    LoadModule apple_userdir_module ${SERVER_INSTALL_PATH_PREFIX}/usr/libexec/apache2/mod_userdir_apple.so

Then uncomment the line that includes the user configurations:

    # User home directories
    Include /private/etc/apache2/extra/httpd-userdir.conf

Then, after stopping and restarting the Websites service, you should be able to access directories under your `~/Sites` directory. For example, if your user account name is `kdj`, and you have a website at `/Users/kdj/Sites/mywebapp/index.html`, then you should be able to visit <http://localhost/~kdj/mywebapp>.

## MAMP

If you want to quickly set up an Apache/MySQL/PHP/Perl/Python stack, then check out [MAMP](http://www.mamp.info/en/) as an alternative to using the built-in Apache server.

## Credits

Thanks to Pascal Qyy for providing [an Ask Different answer](http://apple.stackexchange.com/a/59836/1017) that was helpful.
