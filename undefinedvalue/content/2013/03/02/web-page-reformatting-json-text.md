Title: A Web Page for Reformatting JSON Text
Date: 2013-03-02 22:57:23
Category: Blog
Slug: web-page-reformatting-json-text
Alias: 2013/03/02/web-page-reformatting-json-text/
Tags: json


After I published my [OS X Automator Service for Reformatting JSON Text](http://undefinedvalue.com/2013/03/01/os-x-automator-service-reformatting-json-text), one commenter said that he always uses <http://jsonformat.com/>. I have used that, but I hate the output it produces. Its output is more readable than JSON with all the whitespace stripped out, but not by much.

It also seemed a little silly for such a web page to require a back-end service to do the work. I figured I could whip up a simple web page that wouldn't require any server round-trips to do its work, and that produced reformatted output that wouldn't make me cry. 

Here it is: [JSON Reformatter](http://s3.amazonaws.com/undefinedvalue/formatjson.html)

You can look at the source here: <https://gist.github.com/kristopherjohnson/5073681>

Enjoy!

----

**Update 2014-05-29:** New version, implemented using AngularJS: <http://undefinedvalue.com/2014/05/28/web-page-reformatting-json-text-using-angularjs>
