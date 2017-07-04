Title: iOS and Android Icon Sizes
Date: 2013-04-05 20:39:24
Category: Blog
Slug: ios-and-android-icon-sizes
Alias: 2013/04/05/ios-and-android-icon-sizes/
Tags: iosdev, androiddev


Every once in a while, I have to tell a graphic designer all the sizes needed for iOS and Android icons. So I'm putting together a summary here for easy reference.

## iOS

For more details on requirements and guidelines for iOS app icons, see [iOS Human Interface Guidelines: Icons and Image Sizes](https://developer.apple.com/library/ios/documentation/UserExperience/Conceptual/MobileHIG/IconMatrix.html#//apple_ref/doc/uid/TP40006556-CH27-SW1) and [Technical Q&A QA1686: App Icons on iPad and iPhone](https://developer.apple.com/library/ios/qa/qa1686/_index.html).

All icons must be in PNG format with 24-bit color.

### App Icons

For an app for iOS 7 and later, we need icon image files in these sizes:

- 1024 x 1024
- 512 x 512
- 228 x 228
- 180 x 180
- 152 x 152
- 120 x 120
- 87 x 87
- 80 x 80
- 76 x 76
- 58 x 58
- 40 x 40
- 29 x 29
- 144 x 144 (if supporting iOS 6.1 or earlier)
- 114 x 114 (if supporting iOS 6.1 or earlier)
- 100 x 100 (if supporting iOS 6.1 or earlier)
- 72 x 72 (if supporting iOS 6.1 or earlier)
- 57 x 57 (if supporting iOS 6.1 or earlier)
- 50 x 50 (if supporting iOS 6.1 or earlier)

iOS icons are opaque. Note that iOS will automatically round the corners and add the glossy shine effect when it displays the icon. You may want to pre-render the shine effect if you want more control over how it looks.

### Toolbar, Navigation Bar, and Tab Bar Icons

- Use pure white and transparent regions
- Do not include a drop shadow
- Use anti-aliasing

For toolbar and navigation bar icons, create images with these sizes:

- 22 x 22
- 44 x 44 (high resolution)

For tab bar icons, create images with these sizes:

- 25 x 25
- 50 x 50 (high-resolution)

For each toolbar, navigation bar, or tab bar icon, you may provide a single image, which iOS will treat as a template to generate unselected and selected appearances, or you may provide two images: one for the unselected appearance and another for the selected appearance. 

Note that the sizes given for toolbar, navigation bar, and tab bar icons here are approximate. Images may be slightly larger or slightly smaller than these sizes. Give all icons in a bar a similar visual weight.

### Apple Watch Icons

If the iOS app includes an Apple Watch app, the following icons are needed:

### Notification Center Icons

- 29 x 29 (38mm watch)
- 36 x 36 (42mm watch)

### Long Look Notification Icons

- 80 x 80 (38mm watch)
- 88 x 88 (42mm watch)

### Home Screen Icon and Short Look Icon

- 172 x 172 (38mm watch)
- 196 x 196 (42mm watch)

### Menu Icons

- 70 x 70, with content size 46 x 46 (38mm watch)
- 80 x 80, with content size 54 x 54 (42mm watch)

### Watch Companion Icons

- 58 x 58
- 87 x 87

## Android

### App Icons

For an Android app launcher icon, we need PNG image files in these sizes:

- 512 x 512 (Google Play)
- 144 x 144 (xxhdpi)
- 96 x 96 (xhdpi)
- 72 x 72 (hdpi)
- 48 x 48 (mdpi)

Note that Android app icons don't have to be square: the alpha channel can be used to create transparent areas, so an icon should have a distinct silhouette.

If the app generates notifications, then we need a 24 x 24 icon image. Notification icons must be entirely white except for transparent regions.

For more details on requirements and guidelines for Android app icons, see [Launcher Icons](http://developer.android.com/guide/practices/ui_guidelines/icon_design_launcher.html) and [Iconography](http://developer.android.com/design/style/iconography.html)

### Action Bar Icons

- 96 x 96 (xxhdpi)
- 64 x 64 (xhdpi)
- 48 x 48 (hdpi)
- 32 x 32 (mdpi)

### Small/Contextual Icons

- 48 x 48 (xxhdpi)
- 32 x 32 (xhdpi)
- 24 x 24 (hdpi)
- 16 x 16 (mdpi)

### Notification Icons

- 72 x 72 (xxhdpi)
- 48 x 48 (xhdpi)
- 36 x 36 (hdpi)
- 24 x 24 (mdpi)
