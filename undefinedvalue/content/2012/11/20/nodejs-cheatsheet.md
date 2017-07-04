Title: Node.js Cheatsheet
Date: 2012-11-20 15:54:01
Category: Blog
Slug: nodejs-cheatsheet
Alias: 2012/11/20/nodejs-cheatsheet/
Tags: node, javascript, cheatsheet


I am learning about [node.js](http://nodejs.org). This is my cheatsheet. It may not be useful to you at all.

Also see [My JavaScript Cheatsheet](http://undefinedvalue.com/2011/06/16/my-javascript-cheatsheet).
<!--break-->
## Documentation

- API Docs: <http://nodejs.org/api/>
   - Debugger: <http://nodejs.org/api/debugger.html>
   - Cluster: <http://nodejs.org/docs/latest/api/cluster.html>
- _Up and Running with Node.js_: <http://ofps.oreilly.com/titles/9781449398583/>
- _Async JavaScript: Build More Responsive Apps with Less Code_ by Trevor Burnham: <http://pragprog.com/book/tbajs/async-javascript>
- [A short guide to Connect Middleware](http://stephensugden.com/middleware_guide/)

## Installation

- Downloadable installers: http://nodejs.org/download/
- Installing via various package managers: https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager
- Source code: https://github.com/joyent/node

## Debugging

- <http://nodejs.org/api/debugger.html>
- <https://github.com/dannycoates/node-inspector>

## Utilities

- [npm](https://npmjs.org) - package manager for Node
- [supervisor](https://github.com/isaacs/node-supervisor) - automatically restarts Node-based server when files change
- [nodemon](https://github.com/remy/nodemon) - automatically restarts Node-based server when files change
- [forever](https://github.com/nodejitsu/forever) - ensures that a script runs continuously
- [Winser](http://jfromaniello.github.com/winser/) - runs Node as a Windows service, using [nssm](http://nssm.cc)
- [docco](http://jashkenas.github.com/docco/) and [docco-husky](https://github.com/mbrevoort/docco-husky) - documentation generator
- [node-inspector](https://github.com/dannycoates/node-inspector) - browser-based debugging interface

## Modules

These libraries are especially useful (to me, for what I have done):

   * [Express](http://expressjs.com) - web application framework
   * [Connect](http://www.senchalabs.org/connect/) - middleware framework
   * [Jade](http://jade-lang.com) - template engine
   * [Socket.IO](http://socket.io) - support for WebSockets and other connection mechanisms
   * [Request](https://github.com/mikeal/request) - simplified HTTP requests
   * [xml2js](https://github.com/Leonidas-from-XIV/node-xml2js) - simple XML-to-JavaScript converter
   * [nconf](https://github.com/flatiron/nconf) - configuration files
   * [PDFKit](http://pdfkit.org) - PDF generation
   * [Backbone](http://backbonejs.org) - client-side data models, views, UI binding
   * [Underscore](http://underscorejs.org/) - functional programming helper library
   * [Async.js](https://github.com/caolan/async) - asynchronous JavaScript
   * [Q.js](https://github.com/kriskowal/q) - asynchronous promises
   * [Mocha](http://visionmedia.github.com/mocha/) - testing framework
   * [should.js](http://github.com/visionmedia/should.js) - BDD-style assertion library
   * [Chai](http://chaijs.com/) - BDD- and TDD-style assertion library

See https://npmjs.org for a complete list of all available modules.

## Creating a New Web App with the Express Framework

If you don't already have the Express framework installed, do this:

    npm install -g express

To create a new app, do this:

    express --sessions MyNewApp
    cd MyNewApp
    npm install

To run the app:

    cd MyNewApp
    node app

By default, the app will listen for requests on port 3000, so you can browse to http://locahost:3000/ to view the app. Modify `app.js` or set the `PORT` environment variable to use a different port.


## Snippets

<script src="https://gist.github.com/4118742.js?file=nodejs_snippets.js"></script>
