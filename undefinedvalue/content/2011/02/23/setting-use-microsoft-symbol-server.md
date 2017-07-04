Title: Setting Up for Use of Microsoft Symbol Server
Date: 2011-02-23 22:13:30
Category: Blog
Slug: setting-use-microsoft-symbol-server
Alias: 2011/02/23/setting-use-microsoft-symbol-server/
Tags: visualstudio, debugging


When debugging native Win32 code, it is useful to have the debug symbols for all of Microsoft's DLLs.  The easiest way to set this up is to just set an environment variable before starting Visual Studio (or other Microsoft debugging tools):

    set _NT_SYMBOL_PATH=srv*c:\symbols*http://msdl.microsoft.com/download/symbols

The first time you run the debugger after setting this, it will take some time to start as it downloads symbol files from the Internet into your local symbol cache, but it will be faster after that.  Whenever you update your system with patches or service packs, the new symbols will automatically be downloaded the next time you debug.

For more information, see these pages:

* http://support.microsoft.com/kb/311503
* [http://msdn.microsoft.com/en-us/library/ee416588(VS.85).aspx](http://msdn.microsoft.com/en-us/library/ee416588(VS.85).aspx)

(This post is really for my own benefit. I have trouble finding this information whenever I set up a new development workstation, so I'm putting it somewhere I'll know to look.)
