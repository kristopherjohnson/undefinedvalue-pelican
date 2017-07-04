Title: My JavaScript Cheatsheet
Date: 2011-06-16 18:49:43
Category: Blog
Slug: my-javascript-cheatsheet
Alias: 2011/06/16/my-javascript-cheatsheet/
Tags: jquery, javascript, cheatsheet


A couple of times per year, I have to work on something that requires me to write some [JavaScript](http://en.wikipedia.org/wiki/JavaScript). When I do, I have to reacquaint myself with the language by skimming through [_JavaScript: The Good Parts_]( http://undefinedvalue.com/2009/11/29/javascript-good-parts) and finding some good online reference documentation.

In an effort to reduce the time needed to do this next time, I'm recording the little things that I ran across that I didn't remember or wished I could have found faster. So this is my own personal refresher for JavaScript. It may not help you at all.

Also see my [Node.js Cheatsheet](http://undefinedvalue.com/2012/11/20/nodejs-cheatsheet).

## Reference Links

* [ECMAScript Language Specification, 3rd edition (PDF)](http://www.ecma-international.org/publications/files/ECMA-ST-ARCH/ECMA-262,%203rd%20edition,%20December%201999.pdf)
* [webplatform.org: JavaScript](http://docs.webplatform.org/wiki/javascript)
* Mozilla Developer Network
   * [JavaScript Reference](https://developer.mozilla.org/en/JavaScript/Reference)
   * [JavaScript Guide](https://developer.mozilla.org/en/JavaScript/Guide)
   * [Array](https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/Array), [Boolean](https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/Boolean), [Date](https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/Date), [Error](https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/Error), [Function](https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/Function), [Math](https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/Math), [Number](https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/Number), [Object](https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/Object), [RegExp](https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/RegExp), [String](https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/String)
* Douglas Crockford: [Code Conventions](http://javascript.crockford.com/code.html), [Private Members](http://javascript.crockford.com/private.html)
* [Essential JavaScript Patterns for Beginners](http://addyosmani.com/resources/essentialjsdesignpatterns/book/)
* [jQuery Docs](http://docs.jquery.com/Main_Page), [Getting Started with jQuery](http://docs.jquery.com/Tutorials:Getting_Started_with_jQuery), [Quick and Dirty Guide to QUnit](http://undefinedvalue.com/2009/12/06/quick-and-dirty-guide-qunit)
* [Microsoft Ajax Library Client Reference](http://msdn.microsoft.com/en-us/library/bb397536.aspx)
* [DOM Level 1](http://www.w3.org/TR/2000/WD-DOM-Level-1-20000929/)
* [DOM Level 2 Core](http://www.w3.org/TR/2000/REC-DOM-Level-2-Core-20001113/core.html), [DOM Level 2 Events]( http://www.w3.org/TR/2000/REC-DOM-Level-2-Events-20001113/events.html), [DOM Level 2 HTML](http://www.w3.org/TR/2003/REC-DOM-Level-2-HTML-20030109/html.html)
* [DOM Level 3 Core](http://www.w3.org/TR/2004/REC-DOM-Level-3-Core-20040407/core.html), [DOM Level 3 XPath](http://www.w3.org/TR/DOM-Level-3-XPath/xpath.html)
* [WebKit DOM Reference](http://developer.apple.com/library/safari/#documentation/AppleApplications/Reference/WebKitDOMRef/index.html#//apple_ref/doc/uid/TP40006089), [WebKit DOM Programming Topics](http://developer.apple.com/library/safari/#documentation/AppleApplications/Conceptual/SafariJSProgTopics/WebKitJavaScript.html#//apple_ref/doc/uid/TP40001483), [Apple JavaScript Coding Guidelines](http://developer.apple.com/library/safari/#documentation/ScriptingAutomation/Conceptual/JSCodingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40006088)
* [Gecko DOM Reference](https://developer.mozilla.org/en/Gecko_DOM_Reference)
* [XMLHttpRequest](http://www.w3.org/TR/XMLHttpRequest/)
* [Geolocation API Specification](http://dev.w3.org/geo/api/spec-source.html)
<!--break-->
## Gotchas

Generally, use <tt>===</tt> and <tt>!==</tt> rather than <tt>==</tt> and <tt>!=</tt> (which coerce arguments before comparison).

Numeric values are really IEEE floating-point, even when they look like integers.

<tt>NaN</tt> is not equal to itself. Use <tt>isNaN()</tt>

Semicolons are often optional, but interpreter may insert semicolons in unexpected places, so it is best to use semicolons and to put opening braces on the same line as the keyword.

If `var` declaration is missing, then a variable is global.  The scope of a `var` is the entire function in which it is declared (blocks do not create a new scope)

Note difference between `substr(startIndex, charCount)` and `substring(startIndex, endIndex)`.

Avoid using <tt>/* */</tt> style comments, as regular expressions can contain similar character sequences.

## Special Values and Constants

<pre>
null, undefined, false, true, NaN, Infinity
</pre>

Values that are considered to be "false" in conditionals: <tt>undefined, null, false, '', 0, NaN</tt>

<tt>typeof obj</tt> returns one of these values: <tt>'undefined', 'object', 'boolean', 'number', 'string', 'function'</tt>. If the operand is an array or <tt>null</tt>, then the result is <tt>'object'</tt>. If the operand is a regexp, the result may be either <tt>'object'</tt> or <tt>'function'</tt>.

## Standard Methods

- array.**concat**(item...)
- array.**join**(separator)
- array.**pop**()
- array.**push**(item...)
- array.**reverse**()
- array.**shift**()
- array.**slice**(start, end)
- array.**sort**(comparefn)
- array.**splice**(start, deleteCount, item...)
- array.**unshift**(item...)
- function.**apply**(thisArg, argArray)
- number.**toExponential**(fractionDigits)
- number.**toFixed**(fractionDigits)
- number.**toPrecision**(precision)
- number.**toString**(radix)
- object.**hasOwnProperty**(name)
- regexp.**exec**(string)
- regexp.**test**(string)
- string.**charAt**(pos)
- string.**charCodeAt**(pos)
- string.**concat**(string...)
- string.**indexOf**(searchString, position)
- string.**lastIndexOf**(searchString, position)
- string.**localeCompare**(that)
- string.**match**(regexp)
- string.**replace**(searchValue, replaceValue)
- string.**search**(regexp)
- string.**slice**(start, end)
- string.**split**(separator, limit)
- string.**substring**(start, end)
- string.**toLocaleLowerCase**()
- string.**toLocaleUpperCase**()
- string.**toLowerCase**()
- string.**toUpperCase**()
- String.**fromCharCode**(char...)

## Syntax Examples and Snippets

<script src="https://gist.github.com/4046616.js?file=cheatsheet.js"></script>
