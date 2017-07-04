Title: Core Animation Performance Tips
Date: 2010-05-18 10:36:44
Category: Blog
Slug: core-animation-performance-tips
Alias: 2010/05/18/core-animation-performance-tips/
Tags: performance, optimization, gamedevelopment, coreanimation


In my copious free time, I've been working on a videogame for the iPad. Friends and family may interject here that it seems like I'm *always* working on a videogame in my free time, but I've never actually finished one. This time is different. Really.

All of my personal projects are intended primarily to be interesting and fun for me. I gave myself a couple of technical constraints to keep things challenging:

- All the code is well-factored idiomatic Objective-C. Unlike a lot of iPhone/iPad game programmers, I'm not writing all the guts in low-level C or C++ and then sprinkling a minimal amount of Cocoa on top to interface with the OS.
- I'm using Core&nbsp;Animation as my "engine", rather than the OpenGL ES API or an off-the-shelf gaming engine. (Note: My game only needs a couple dozen sprites.)

So far, things have worked out well. I was worried that using Objective-C and Core&nbsp;Animation might lead to performance issues on the iPad, but that hasn't been the case. I have run into a couple of issues with Core&nbsp;Animation that were pretty easy to fix.
<!--break-->
### Layer Creation Is Expensive

My game's "sprites" are just Core&nbsp;Animation layers. When I initially implemented the game, I was creating layers and adding them to the view as needed, and then deleting them when they were no longer needed. This turned out to cause problems; a few frames would get dropped whenever a layer was created.

The fix for this was to create a pool of layers and add them all to the view at startup, and reuse those layers as needed. Unused layers get their `hidden` property set false.


### Watch Out for Misaligned Images

If you run an app with Instruments with the Core Animation tool, it has an option to highlight "misaligned images." I couldn't find a lot of information on this, but apparently if you give layers positions that are not perfectly aligned to pixels, Core Animation does some anti-aliasing when rendering those layers, which degrades performance.

The easy fix is to just round all positions to whole pixels, via something like this:

    - (void) setSpritePosition:(CGPoint)position {
        CGPoint alignedPosition;
        alignedPosition.x = floorf(0.5f + position.x);
        alignedPosition.y = floorf(0.5f + position.y);
        sprite.position = alignedPosition;
    }

This got rid of most of my misaligned images, but I do still have some sprites that get rotated or scaled via a transform, and such images are always misaligned, unless they are rotated by some multiple of 90 degrees. Thankfully, I only have a few such sprites.
