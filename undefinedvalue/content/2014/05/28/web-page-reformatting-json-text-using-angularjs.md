Title: A Web Page for Reformatting JSON Text, using AngularJS
Date: 2014-05-29 03:49:54
Category: Blog
Slug: web-page-reformatting-json-text-using-angularjs
Alias: 2014/05/28/web-page-reformatting-json-text-using-angularjs/
Tags: json, angularjs


A little over a year ago, I published [A Web Page for Reformatting JSON Text](https://undefinedvalue.com/2013/03/02/web-page-reformatting-json-text), which is a simple web page for pretty-printing JSON data. I'm now learning [AngularJS](https://angularjs.org), so as an exercise I reimplemented the page using Angular rather than the original's [jQuery](http://jquery.com).

This version is a little nicer than the original in the following ways:

- You can type or paste text into the top box and the formatted JSON immediately appears in the lower box. There is no longer a need to press a **Format** button because Angular's data-binding mechanism takes care of automatically updating the output whenever the input changes. (This is possible with jQuery too, but takes more work.)
- You can control the indentation width of the formatted JSON.
- When the input is not valid JSON, the output panel changes its background color to red when displaying the error message.

Here it is: [JSON Formatter with AngularJS](https://s3.amazonaws.com/undefinedvalue/ng-formatjson.html)

Short link: <http://bit.ly/formatjson>

You can look at the full source here: [Gist](https://gist.github.com/kristopherjohnson/176dc5cc09dfc77cd4a6)

or as a fiddle: <http://jsfiddle.net/oldmankris/qK9LK/>

If don't know anything about AngularJS, but are curious about it, look at the source and note the following:

- The magic of Angular comes from the `ng-` attributes attached to HTML elements. There is no need for a separate template language or explicit DOM manipulation.
- The [ng-app](https://docs.angularjs.org/api/ng/directive/ngApp) attribute attached to the `html` element sets up the [module](https://docs.angularjs.org/guide/module) that contains our app's code.
- The [ng-controller](https://docs.angularjs.org/api/ng/directive/ngController) attribute attached to the `div` element defines which controller function to use.
- The [ng-model](https://docs.angularjs.org/api/ng/directive/ngModel) attribute attached to the first `textarea` element binds its content to the `inputText` variable
- The [ng-bind](https://docs.angularjs.org/api/ng/directive/ngBind) attribute attached to the second `textarea` element binds its content to the value of the `outputText` variable, and the [ng-class](https://docs.angularjs.org/api/ng/directive/ngClass) attribute binds its CSS class to the value of the `outputClass` variable.
- The  [ng-options](https://docs.angularjs.org/api/ng/directive/select) and [ng-model](https://docs.angularjs.org/api/ng/directive/ngModel) directives on the `select` element bind it to the `indentOptions` and `selectedIndentOption` variable.
- In the controller code, we set initial values for the `inputText`, `indentOptions`, and `selectedInputOption` variables, and then use [$scope.$watch()](https://docs.angularjs.org/api/ng/type/$rootScope.Scope) to update the values of `outputText` and `outputClass` whenever any of the inputs change.

