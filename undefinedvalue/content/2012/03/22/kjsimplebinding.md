Title: KJSimpleBinding
Date: 2012-03-22 10:15:47
Category: Blog
Slug: kjsimplebinding
Alias: 2012/03/22/kjsimplebinding/
Tags: opensource, iosdev


Mac OS X provides a pretty nice [data-binding](http://en.wikipedia.org/wiki/UI_data_binding) technology for developers, called [Cocoa bindings](http://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/CocoaBindings/CocoaBindings.html). Unfortunately, the Cocoa bindings mechanism is not available to iOS developers, so iOS developers have to spend a lot of time writing code to keep user-interface elements and data in sync.

However, while Cocoa Bindings is not available on iOS, the underlying [key-value coding](http://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/KeyValueCoding/Articles/KeyValueCoding.html) (KVC) and [key-value observing](https://developer.apple.com/library/mac/#documentation/cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html) (KVO) mechanisms are, so it is straightforward to implement your own poor man's data-binding mechanism and eliminate some of the drudgery.

I have done just that. My [`KJSimpleBinding`](http://github.com/kristopherjohnson/KJSimpleBinding/blob/master/README.markdown) library is available on [GitHub](http://github.com/kristopherjohnson/KJSimpleBinding). I hope it is useful to someone, and I hope I have time to make it less simple.

I'm not the only one to try this. Here are a few similar projects I found on GitHub:

- http://github.com/dewind/KeyPathBindings
- http://github.com/jonsterling/Observe
- http://github.com/mruegenberg/objc-simple-bindings
- http://github.com/zeasy/EasyBinding

