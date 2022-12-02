Title: iPhone Sample Code: Tiles
Date: 2010-02-06 04:28:21
Category: Blog
Slug: iphone-sample-code-tiles
Alias: 2010/02/05/iphone-sample-code-tiles/
Tags: samplecode, iphone, iosdev, coreanimation


As an exercise in using the [Core Animation](http://en.wikipedia.org/wiki/Core_Animation) API, I've implemented a little iPhone app that reproduces the behavior of the iPhone home screen's icon reorganization interface. (You know, dragging the wiggly icons around.) You can download my sample code to see how it works. Some descriptions of the highlights follow below.
<!--break-->
<img src="https://undefinedvalue.com/sites/undefinedvalue.com/files/Tiles_Screenshot.png" alt="Screenshot" style="float: right;">

The source code and Xcode project can be downloaded here: [tilessample](https://github.com/kristopherjohnson/tilessample/zipball/master).

Source is also available on [GitHub](https://github.com/kristopherjohnson/tilessample).

The primary classes to look at are [`TilesViewController`](http://github.com/kristopherjohnson/tilessample/blob/master/Classes/TilesViewController.m) and [`Tile`](http://github.com/kristopherjohnson/tilessample/blob/master/Classes/Tile.m). The view controller implements all of the "logic" of the application, while the `Tile` class has the animations.

An instance of `Tile` represents one of the icons, and is derived from `CAGradientLayer`.  The gradient layer properties get set to provide a gloss effect for the tiles.  `Tile` also provides a few animations, initiated by calling these methods:

- `appearDraggable`: Changes the tile to be partially transparent, and makes it slightly bigger. This is invoked when the user touches a tile.
- `appearNormal`: Reverses the effects of `appearDraggable`. This is invoked when the tile is released.
- `startWiggling`: Starts a tile "wiggling", as in the iPhone home screen while in reorganization mode.
- `stopWiggling`: Stops the wiggling effect

The `TilesViewController` class is pretty straightforward. When the user touches a the screen, the `touchesBegan` method determines which tile was touched, calls its `appearDraggable` method, and calls other tiles' `startWiggling` methods.

As the user drags the tile around the screen, the `touchesMoved` method moves the dragged tile, and moves the other tiles as needed to provide an open space for it. Core Animation takes care of all the zooming around of the icons.

When the user lets go of the tile, the `touchesEnded` method drops it in place and removes all the animations.

Things I learned from this project:

- Turning on the `masksToBounds` property for layers slows things down quite noticeably.
- When hit-testing layers, you have to use a layer's presentation layer, not a model layer itself.
- `CAGradientLayer` is easy to use.

Here are some things I don't understand. (Maybe some smart person can explain.)

- When hit-testing to see which layer was touched, I had to do both `[touch locationInView:view]` and `[view convertPoint:location toView:nil]`. However, when handling touch-moves, I only have to use `[touch locationInView:view]`. I don't understand why the coordinate systems are (apparently) different.

----

**Update: 2012-04-16:** Changed the layer-initialization code so that it draws in high resolution on a Retina display. Updated the links above to point to GitHub. The tilessample repository on BitBucket is officially abandoned.
