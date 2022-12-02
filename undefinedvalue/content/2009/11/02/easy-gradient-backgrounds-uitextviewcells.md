Title: Easy Gradient Backgrounds for UITextViewCells
Date: 2009-11-03 00:28:23
Category: Blog
Slug: easy-gradient-backgrounds-uitextviewcells
Alias: 2009/11/02/easy-gradient-backgrounds-uitextviewcells/
Tags: samplecode, iphone, ipad, iosdev


When you create a table-view-based iPhone app, by default you get tables with plain white rows.  But all the cool kids are making apps with 3D-ish gradient backgrounds.  You want to make those kinds of apps too, right?  This article explains how.
<!--break-->
## Overview

Making table cells with custom backgrounds is a common thing for iPhone developers to want to do, and there is a lot of information around the net about how to do it.  Why should you read this tutorial?  Well, this tutorial is designed to make it as easy as possible: just copy some files to your project, make a couple of source code changes, and *bang!* instant gradient backgrounds.  With easy stuff like this out of the way, you can concentrate on doing whatever is unique for your application.

Also, unlike some older tutorials, this one lets you use the built-in `UITableViewCell` `textLabel` and `detailTextLabel` properties, rather than creating your own custom cell from scratch.  So it's easy to retrofit existing code.

To give credit where it's due, I got a lot of this information from the article [How To Make Ultra-Slick Gradient UITableView Cells](http://maniacdev.com/2009/10/how-to-make-ultra-slick-gradient-uitableview-cells/) at manicadev.com, so go check that site out.

What we'll do is create a simple example project, and then show how to add the gradients.


## Creating the Example Project

We'll start by creating a run-of-the-mill iPhone app that displays a table.  These are the steps:

0. In Xcode, choose the **File -> New Project…** menu item.
0. Choose **iPhone OS -> Application** in the left pane of the **New Project** dialog.
0. Select **Navigation-based Application**, leave **Use Core Data for storage** uncheck, and click **Choose…**
0. Save the project as "GradientTableViewCellExample"

Open the `RootViewController.m` source file, and replace the `tableView:numberOfRowsInSection:` and `tableView:cellForRowAtIndexPath:` methods with these bodies:

    - (NSInteger)tableView:(UITableView *)tableView
     numberOfRowsInSection:(NSInteger)section {

        return 1000;
    }

    - (UITableViewCell *)tableView:(UITableView *)tableView
             cellForRowAtIndexPath:(NSIndexPath *)indexPath {

        static NSString *CellIdentifier = @"Cell";

        UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:CellIdentifier];
        if (cell == nil) {
            cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleSubtitle
                                          reuseIdentifier:CellIdentifier];
            [cell autorelease];
        }

        int rowIndex = indexPath.row;
        cell.textLabel.text = [NSString stringWithFormat:@"Row %d",
                               rowIndex];
        cell.detailTextLabel.text = [NSString stringWithFormat:@"This is the detail text for row %d",
                                     rowIndex];

        return cell;
    }

Build and run the project, and you'll see this:

<img src="https://undefinedvalue.com/sites/undefinedvalue.com/files/NoGradient.png" alt="App with no gradient">

Not bad, but it would look more interesting if, instead of the flat white table cells, we had three-dimensional-looking gradient backgrounds on those cells.


## Adding the Gradient Background Image

First, we'll need a background image.  You can look at the [How To Make Ultra-Slick Gradient UITableView Cells](http://maniacdev.com/2009/10/how-to-make-ultra-slick-gradient-uitableview-cells/) article to see how to make one of these from scratch, using Adobe Photoshop Elements, but here's an image you can steal directly from this page:

<a href="https://undefinedvalue.com/sites/undefinedvalue.com/files/CellGradientBackground.png"><img src="https://undefinedvalue.com/sites/undefinedvalue.com/files/CellGradientBackground.png" alt="CellGradientBackground.png"></a>

Add this image to your project, or create your own background image if you're so-inclined.


## Adding the GradientTableViewCell class

Grab the source files [GradientTableViewCell.h](https://undefinedvalue.com/sites/undefinedvalue.com/files/GradientTableViewCell.h) and [GradientTableViewCell.m](https://undefinedvalue.com/sites/undefinedvalue.com/files/GradientTableViewCell.m), and add them to your project.

`GradientTableViewCell` overrides two methods of `UITableViewCell`.  First, we override the `initWithStyle:reuseIdentifier:` method so that it adds the gradient background image, stretching it to fill the cell.


    - (id)initWithStyle:(UITableViewCellStyle)style reuseIdentifier:(NSString *)reuseIdentifier {
        if (self = [super initWithStyle:style reuseIdentifier:reuseIdentifier]) {
            UIImage *image = [UIImage imageNamed:@"CellGradientBackground.png"];
            UIImageView *imageView = [[UIImageView alloc] initWithImage:image];
            imageView.contentMode = UIViewContentModeScaleToFill;
            self.backgroundView = imageView;
            [imageView release];
        }
        return self;
    }

Then, we have to override the `setSelected:animated:` method.  The inherited method sets the cell's subviews' background colors, but we want the subviews to have transparent backgrounds so that the gradient background shows through:

    - (void)setSelected:(BOOL)selected animated:(BOOL)animated {

        [super setSelected:selected animated:animated];

        for (UIView *view in self.contentView.subviews) {
            view.backgroundColor = [UIColor clearColor];
        }
    }



## Using the GradientTableViewCell class

Now, we just have to change our `RootViewController.m` file so that it will use `GradientTableViewCell` instead of a plain old `UITableViewCell`.

Add an `#import` at the top:

    #import "GradientTableViewCell.h"

Then, change this line in `tableView:cellForRowAtIndexPath:`

    cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleSubtitle
                                  reuseIdentifier:CellIdentifier];

to this:

    cell = [[GradientTableViewCell alloc] initWithStyle:UITableViewCellStyleSubtitle
                                        reuseIdentifier:CellIdentifier];

Build and run the project, and you should get this:

<img src="https://undefinedvalue.com/sites/undefinedvalue.com/files/WithGradient.png" alt="With gradient">

See, easy!

Note that the gradient image I provide is pretty subtle, so the effect may not show up well in your web browser.  Look at in on an actual iPhone, and experiment with different background images to get the effect you want.
