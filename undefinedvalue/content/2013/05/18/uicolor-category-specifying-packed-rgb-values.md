Title: UIColor Category for Specifying Packed RGB Values
Date: 2013-05-19 00:36:53
Category: Blog
Slug: uicolor-category-specifying-packed-rgb-values
Alias: 2013/05/18/uicolor-category-specifying-packed-rgb-values/
Tags: uicolor, iosdev, category


iOS's [UIColor](https://developer.apple.com/library/ios/#documentation/uikit/reference/UIColor_Class/Reference/Reference.html) class makes it pretty easy to specify a color using red, green, blue (RGB) and alpha components:

	 // set pale yellow color
	 label.textColor = [UIColor colorWithRed:1.0
	                                   green:1.0
	                                    blue:0.5
	                                   alpha:1.0];

However, as with many Cocoa API's, it's pretty verbose. Web developers would specify that color using the hexcode shorthand `#ffff80`, and many graphics editing tools would generate a hexcode value like that rather than values in the range 0.0&ndash;1.0.

So I made a simple category on UIColor that lets one write stuff like this:

    #include "UIColor+KDJPackedRGB.h"

    // ...

    // set pale yellow color
    label.textColor = [UIColor colorWithRGB24:0xffff80];

See <https://gist.github.com/kristopherjohnson/5606209>
