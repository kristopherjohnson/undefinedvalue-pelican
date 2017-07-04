Title: Customizing Android Action Bar for Edit Mode
Date: 2013-07-25 13:06:38
Category: Blog
Slug: customizing-android-action-bar-edit-mode
Alias: 2013/07/25/customizing-android-action-bar-edit-mode/
Tags: androiddev, android, actionbar


I spent a *long* time trying to get a [contextual action bar (CAB)](http://developer.android.com/design/patterns/actionbar.html) working for an editing mode in an Android app I'm developing. My goal was to have a CAB appear whenever the user started changing field values on a screen, and the user would tap the *Done* button when complete. The CAB would also show a "Revert Changes" button allowing the user to undo whatever they did.

This initially seemed like the easiest way to indicate to the user that they had made changes and needed to explicitly save them, but Android's default implementation of CAB has some drawbacks:

- The standard button is titled "Done". I would prefer it to be "Save", but there is no easy-to-use `setTitle()` method available.
- If user hits the *BACK* button, the CAB disappears, and there is no straightforward way for the app to determine whether the CAB disappeared because the user hit Done or because they hit *BACK*, or any way to intercept the processing of the *BACK* button while a CAB is displayed.
- I have to write code to restore the CAB state on a [configuration change](http://developer.android.com/guide/topics/resources/runtime-changes.html)

While browsing around the web trying to find examples of workarounds for these issues, I ran across a blog post explaining why using a CAB for this scenario won't work, even if I did fix the aforementioned problems:

[Edit Mode and why using a Contextual ActionBar is a bad idea](http://dazcorp.blogspot.com/2013/04/edit-mode-and-why-using-contextual.html)

(Short version: If user double-taps or long-presses an edit field, it will pop up its own text-selection CAB which would blow away my CAB and eventually lead to a `NullPointerException`.)

So, I'm not using a CAB, but will instead customize the look of the non-contextual action bar as suggested in that blog post.
