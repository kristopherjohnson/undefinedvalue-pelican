Title: Saving a View as a Photo in an iPhone App
Date: 2009-01-16 06:52:00
Category: Blog
Slug: saving-view-photo-iphone-app
Alias: 2009/01/16/saving-view-photo-iphone-app/
Tags: iphone, samplecode, code


<p>
For an iPhone app that I'm working on, I want to be able to save the screen image to the Photos album.  My first attempt at this was complicated: I created a color space, a bitmap context, a <tt>CGImage</tt>, and finally a <tt>UIImage</tt>, copying and pasting most of the code from the <em>Quartz 2D Programming Guide</em>.  Unfortunately, it didn't work; I kept getting BAD_ACCESS signals when I called <tt>UIImageWriteToSavedPhotosAlbum()</tt>, even though it looked to me like everything was correct.
</p>
<p>
After Googling for a bit for known issues with UIImageWriteToSavedPhotosAlbum, I ran across a far easier solution to the problem.  Here are the methods I ended up with:
</p>
<div style="overflow: scroll; border: 1px solid #666"><pre>
// Create an image for the view and save it to the Photos library
- (void)savePhotoOfView:(UIView *)view
{
    UIGraphicsBeginImageContext(view.bounds.size);
    [view drawRect:view.bounds];
    UIImage *image = UIGraphicsGetImageFromCurrentImageContext();
    UIGraphicsEndImageContext();

    UIImageWriteToSavedPhotosAlbum(image,
                                   self,
                                   @selector(savedPhotoImage:didFinishSavingWithError:contextInfo:),
                                   NULL);
}

// Called by UIImageWriteToSavedPhotosAlbum() when it completes
- (void)   savedPhotoImage:(UIImage *)image
  didFinishSavingWithError:(NSError *)error
               contextInfo:(void *)contextInfo
{    
    NSString *message = @"This image has been saved to your Photos album";
    if (error) {
        message = [error localizedDescription];
    }
    UIAlertView *alert = [[UIAlertView alloc] initWithTitle:nil
                                                    message:message
                                                   delegate:nil
                                          cancelButtonTitle:@"OK"
                                          otherButtonTitles:nil];
    [alert show];
    [alert release];
}
</pre></div>
<p>
These just call the view's <tt>drawRect</tt> method to create an image, save the image to the Photos library, and then pop up an alert box to let the user know what happened.
</p>
