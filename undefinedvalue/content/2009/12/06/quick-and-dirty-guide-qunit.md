Title: Quick-and-Dirty Guide to QUnit
Date: 2009-12-06 22:07:52
Category: Blog
Slug: quick-and-dirty-guide-qunit
Alias: 2009/12/06/quick-and-dirty-guide-qunit/
Tags: tutorial, qunit, jquery, javascript, unittesting


I'm playing around with [JavaScript](http://en.wikipedia.org/wiki/Javascript) in my spare time, and have started creating a web app. As I usually do, particularly when learning something new, I am using a [test-driven development](http://en.wikipedia.org/wiki/Test-driven_development) approach. I looked at a few JavaScript unit-testing frameworks, and decided to go with [QUnit](http://docs.jquery.com/QUnit), the testing framework used by the jQuery project.

QUnit isn't too hard to set up or use, but my unfamiliarity with JavaScript, jQuery, and related things meant it took a little more work than it should have. A few out-of-date QUnit tutorials on the web made things worse. So, here is a quick-and-dirty QUnit tutorial that might be helpful for others who are the same boat that I was in.
<!--break-->
### Download Library Files

First, we need to download jQuery and the two files that make up QUnit. Here are the links:

- [jquery.js](http://jquery.com/) (Click the big **Download** button on the right side of that page.)
- [qunit.js](http://github.com/jquery/qunit/raw/master/qunit/qunit.js)
- [qunit.css](http://github.com/jquery/qunit/raw/master/qunit/qunit.css)

**Note:** When you download jQuery, you'll end up with a file called `jquery-1.3.2.min.js`, or something like that. I rename it to `jquery.js` to keep things simple.

We'll put all three files into the directory where the JavaScript code is going to be. Of course, in real life you can put them wherever you want.

### Production Code to be Tested

Next, we will need some JavaScript code to test. Some poor confused souls put their JavaScript code and tests in their HTML files, but we're going to do things The Right Way and put the production code and the test code into their own files.

Here is our production module, `calculator.js`, which provides sophisticated mathematical functionality:

    // calculator.js
    
    var Calculator = function () {
        this.add      = function (a, b) { return a + b; };
        this.subtract = function (a, b) { return a - b; };
        this.multiply = function (a, b) { return a * b; };
        this.divide   = function (a, b) { return a / b; };
    };

### Test Cases

Here are our tests, in `calculator_tests.js`:

    // calculator_tests.js
    
    Calculator.runTests = function () {
    
        test("add", function () {
            var c = new Calculator();
            equals(c.add(1, 1), 2, "1 + 1");
            equals(c.add(2, 2), 4, "2 + 2");
        });
    
        test("subtract", function () {
            var c = new Calculator();
            equals(c.subtract(1, 1), 0, "1 - 1");
            equals(c.subtract(100, 1), 99, "100 - 1");
        });
    
        test("multiply", function () {
            var c = new Calculator();
            equals(c.multiply(1, 1), 1, "1 * 1");
            equals(c.multiply(2, 2), 4, "2 * 2");
            equals(c.multiply(17, 23), 391, "17 * 23");
        });
    
        test("divide", function () {
            var c = new Calculator();
            equals(c.divide(1, 1), 1, "1 / 1");
            equals(c.divide(8, 2), 4, "8 / 2");
            equals(c.divide(1, 0), Infinity, "1 / 0");
        });
    };

Here, I've made my test function a member of the module I'm testing, but you can define it however you want.

See the [QUnit API documentation](http://docs.jquery.com/QUnit#API_documentation) for info about the test functions. All you need to know to understand the above is that `test(name, function)` creates a test case, and `equals(actual, expected, message)` checks equivalence of results.

### HTML Test Runner

Finally, we need an HTML file, `calculator_tests.html`, which loads all the modules, runs the tests, and displays the results in a web browser:

    <html>
    <head>
    
    <!-- Load jQuery and QUnit -->
    <script src="jquery.js"></script>
    <script src="qunit.js"></script>
    <link rel="stylesheet" href="qunit.css" type="text/css" media="screen" />
    
    <!-- Load modules to be tested -->
    <script src="calculator.js"></script>
    <script src="calculator_tests.js"></script>
    
    <!-- This jQuery fragment calls Calculator.runTests() after the document loads -->
    <script>
    $(document).ready(function(){
        Calculator.runTests();    
    });
    </script>
    
    </head>

    <body>
    <!-- QUnit will put the results in the elements here -->
    <h1 id="qunit-header">Calculator Tests</h1>
    <h2 id="qunit-banner"></h2>
    <h2 id="qunit-userAgent"></h2>
    <ol id="qunit-tests"></ol>
    </body>
    </html>

With all those files in place, just open `calculator_tests.html` in a web browser, and it will show the results. Successful tests will be green, and failed tests will be red. You can click the individual tests to get detailed lists of the assertions.

So, that's it. Read the QUnit docs, and start writing some tests.
