Title: Improving SCons Performance for MSVC8
Date: 2007-07-14 05:47:00
Category: Blog
Slug: improving-scons-performance-msvc8
Alias: 2007/07/14/improving-scons-performance-msvc8/
Tags: scons


<p>
The developers of <a href="http://www.scons.org">SCons</a> don't seem to be very interested in this, but I've found a way to dramatically speed up SCons builds for MSVC8 (Visual Studio 2005's C++ compiler).
</p>
<pp>
We've got a fairly big codebase with a few levels.  It was taking over a minute to read all the SConstruct/SConscript files, even when there was nothing to do.
</p>
<p>
I ran the profiler, and found that the bulk of the time was in minidom.py and expatbuilder.py.  This was surprising, because I didn't think SCons used XML.
<p>
Searching further, it turns out that for MSVC8, to determine library and include paths SCons opens a registry key which contains XML, and parses it.  For our codebase, it was doing this about 300 times per build.
</p>
<p>
So, I hacked up my personal copy of SCons/Tool/msvc.py, and now instead of over a minute, it only takes 20 seconds.  I don't consider this a "patch", because I don't really know much about SCons internals, and so this could be totally wrong, but maybe someone can figure out the right way to do what I have done and get it into CVS.
</p>
<p>
The idea is to cache the results of _get_msvc8_path, so that the XML parsing doesn't happen every time.  I added a global variable to msvc.py, containing an empty dictionary:
</p>
<pre>
# START NEW CODE
# KDJ: cache results of _get_msvc8_path in a dictionary
cached_msvc8_path = {}
# END NEW CODE
</pre>
<p>
Then, I changed a few lines in get_msvc_path as follows:
</p>
<pre>
    if version_num >= 8.0:
        # ORIGINAL: return _get_msvc8_path(path, str(version_num), platform, suite)
        # START NEW CODE
        global cached_msvc8_path
        if not cached_msvc8_path.has_key(path):
            cached_msvc8_path[path] = _get_msvc8_path(path, str(version_num), platform, suite)
        return cached_msvc8_path[path]
        # END NEW CODE
    elif version_num >= 7.0:
        return _get_msvc7_path(path, str(version_num), platform)
</pre>
