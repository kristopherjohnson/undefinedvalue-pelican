Title: KJGridLayout
Date: 2012-03-15 10:40:19
Category: Blog
Slug: kjgridlayout
Alias: 2012/03/15/kjgridlayout/
Tags: samplecode, iosdev


Xcode's Interface Builder is a pretty good user-interface layout tool, especially for simple situations. However, it is not the best tool for every job. Sometimes you have to write code to dynamically create user interface elements or to move them around as the view is resized.

When you do this, you find that iOS doesn't help you much beyond some rudimentary autoresizing options. While iOS 5 does provide some autolayout features, they are limited, and they don't help at all if you need to support earlier versions of iOS.

I had a need to do a [grid-based layout](http://en.wikipedia.org/wiki/Grid_(page_layout)) in an iOS app. I hoped to find a grid-layout component like one would find in [Android](http://developer.android.com/reference/android/widget/GridLayout.html) or [WPF](http://msdn.microsoft.com/en-us/library/system.windows.controls.grid.aspx), but there is no such thing built into iOS.

I also couldn't find any third-party implementations. I found a few posts and samples for making a grid-like `UITableView`, but I wanted a way to lay out things in a grid in a plain-old `UIView`.

So I decided to write my own grid-layout thingees for iOS.

The results are the `KJGridLayout` class and the `KJGridLayoutView` class, which you can find on [GitHub](http://github.com/kristopherjohnson/KJGridLayout). Check out the [README](http://github.com/kristopherjohnson/KJGridLayout/blob/master/README.markdown) and feel free to use them yourself. I hope someone finds this stuff useful.
