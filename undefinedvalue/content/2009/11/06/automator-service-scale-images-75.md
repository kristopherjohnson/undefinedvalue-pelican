Title: Automator Service: Scale Images by 75%
Date: 2009-11-06 17:17:14
Category: Blog
Slug: automator-service-scale-images-75
Alias: 2009/11/06/automator-service-scale-images-75/
Tags: automator


Here is yet another Snow Leopard Automator service: This one takes an image file and scales it down to 75% of its original size. This is great for screenshots, as all the text is still readable at that size, but you can put it in a web page or document without filling the screen.
<!--break-->
## How to Use It

0. Select one or more image files in the Finder.
0. From the Services menu, choose **Scale Images by 75%**
0. Look for the scaled images on the desktop.

For example, to create the Automator screenshot you see at the bottom of this article, I used Shift-Command-4 to select an area of the screen. The screenshot image file was put on my desktop. Then I right-clicked the image file and chose **Scale Images by 75%**, which created a new image file next to the original.


## How to Create It

In Automator, create a new Service that receives selected **image files** in **Finder**.

Add these actions:

0. **Copy Finder Items** (Note: you can skip this if you would rather replace the original image file.)
0. **Scale Images** with **By Percentage** set to 75.

Save the service as "Scale Images by 75%".

<img src="http://undefinedvalue.com/sites/undefinedvalue.com/files/Scale_Images_by_75_percent.png" alt="Picture">
