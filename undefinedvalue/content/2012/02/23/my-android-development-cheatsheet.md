Title: My Android Development Cheatsheet
Date: 2012-02-24 00:10:44
Category: Blog
Slug: my-android-development-cheatsheet
Alias: 2012/02/23/my-android-development-cheatsheet/
Tags: cheatsheet, android


If I had my druthers, I'd spend all my time developing mobile apps. I've always been fascinated with pocket-sized computers, and have owned many through the years. Unfortunately, for most of my life such devices have been little more than toys, and so I've had to focus my expertise on writing code for "real computers".

This is true even now, during the explosion of smartphone and tablet usage. I'm one of those dinosaurs who knows how to use C, C++, MFC, ATL, CORBA, UNIX, and other ancient magic, so there are sometimes a few months of old-school development between mobile-development gigs. I write iOS stuff for fun, so I keep those skills sharp, but Android is something I touch only when I'm being paid to do so. Thus, I have to find a way to quickly get back up to speed when the Android work does come.

This is my little refresher for when I arrive back in Android-land. It may not help you at all.

**WARNING:** The below was written back when I wrote apps that targeted Android 2.x. A lot of it is obsolete with the 4.x API. Someday maybe I'll update this.
<!--break-->
## References

- [Android Development Home](http://developer.android.com/index.html)
- [Android Dev Guide](http://developer.android.com/guide/index.html)
- [Android Design](http://developer.android.com/design/index.html)
- [Android API Reference](http://developer.android.com/reference/packages.html)
- [Google Play (formerly Android Market)](http://support.google.com/googleplay/android-developer/)

## Eclipse

- [Downloading Eclipse](http://eclipse.org/downloads/) (get the package for Java developers)
   - Note: A new Mac won't have Java the runtime installed. You will be prompted to download and install it when you try to run Eclipse the first time.
- [Downloading and Installing the SDK](http://developer.android.com/sdk/index.html)
- Use Ctrl+Space for "Content Assist" (autocomplete)
- Search -> File... is the only decent multi-file search command. And that's where the multi-file Replace button is hidden.
- Code templates, key bindings, and other settings are saved per-workspace. They can be exported and imported into other workspaces.

## Android SDK

- Do `android update project --path .` to prepare a directory for command-line builds. This will create `local.properties`. To make a release build, do `ant all clean release`. 
- [App Signing](http://developer.android.com/guide/publishing/app-signing.html). To share a `debug.keystore` between developers, create it like this: `keytool -genkey -keypass android -keystore debug.keystore -alias androiddebugkey -storepass android -validity 1000 -dname "CN=Android Debug,O=Android,C=US"`

## Compatibility Library

A [compatibility library](http://developer.android.com/sdk/compatibility-library.html) is available to provide newer API features to older API levels.

## Application Resources

See http://developer.android.com/guide/topics/resources/index.html

## Styles and Themes

Application-specific styles are defined in XML files in the `res/values` folder of the project. Syntax for style definitions is described here: http://developer.android.com/guide/topics/resources/style-resource.html

The standard Android style and theme definitions can be found in the `platforms/android-N/data/res/values` folder in the Android SDK (where _N_ is the platform version).

All available style properties are listed here: http://developer.android.com/reference/android/R.attr.html

All available styles are listed here: http://developer.android.com/reference/android/R.style.html

For more on Styles and Themes: http://developer.android.com/guide/topics/ui/themes.html

## Assets

These tools help generate assets for Android apps:

- Android Asset Studio: <http://android-ui-utils.googlecode.com/hg/asset-studio/dist/index.html>
- ActoinBar Style Generator: <http://actionbarstylegenerator.com/>
- Android Holo Colors: <http://android-holo-colors.com>

## Activity Lifecycle

Activities exist in one of three states:

- Resumed (or Running): activity is in foreground and has user focus
- Paused: another activity is in the foreground and has focus, but this activity is still visible
- Stopped: activity is completely obscured, but still maintains state

Lifecycle callbacks:

- `onCreate()` - followed by `onStart()`
  - `onRestart()` - followed by `onStart()`
  - `onStart()`
    - `onResume()` - followed by `onPause()`
    - `onPause()` - followed by `onResume()` or `onStop()`
  - `onStop()` - followed by `onDestroy()` or `onRestart()`
- `onDestroy()` - final call

Activity is killable after `onPause()`, `onStop()`, or `onDestroy()`. (Only `onPause()` is "guaranteed" to be called.)

When Activity A starts Activity B:

0. A's `onPause()` method executes
0. B's `onCreate()`, `onStart()`, and `onResume()` methods execute.
0. If A is no longer visible, its `onStop()` method executes

`onSaveInstanceState(Bundle)` will be called if an activity may be killed. If called, it will be called before `onStop()`, but there are no guarantees about whether it will occur before or after `onPause()`. Bundle will be passed to `onCreate(Bundle)` and `onRestoreInstanceState(Bundle)` if activity is recreated. By default, this mechanism saves/restores states of all views in the hierarchy, as long as each widget has an ID.

## Fragments and Loaders

See [Fragments](http://developer.android.com/guide/topics/fundamentals/fragments.html) and [Loaders](http://developer.android.com/guide/topics/fundamentals/loaders.html). Also see http://android-developers.blogspot.com/2011/02/android-30-fragments-api.html.

The compatibility library has support for fragments and loaders. Need to derive class from [FragmentActivity](http://developer.android.com/reference/android/support/v4/app/FragmentActivity.html) and use `getSupportFragmentManager()` and `getSupportLoaderManager()`.

## Menus

For basic implementation of menu triggered by MENU button or action bar, override `onCreateOptionsMenu()` and `onOptionsItemSelected()`.

To change options menu after creation, override `onPrepareOptionsMenu()`. On Android 3.0+, need to call `invalidateOptionsMenu()` to force system to call `onPrepareOptionsMenu()`.

To create context menu for a view, call `registerForContextMenu()`, then implement `onCreateContextMenu()` and `onContextItemSelected()`.

More about menus here: http://developer.android.com/guide/topics/ui/menus.html

## Dialogs

Override `onCreateDialog(int)` and maybe `onPrepareDialog(int, Dialog)`. Use the `AlertDialog`, `ProgressDialog`, `DatePickerDialog`, or `TimePickerDialog` classes, or create custom dialog.

Call `showDialog(int)` to display the dialog. Call Dialog's `dismiss()` or activity's `dismissDialog(int)` to close it. Implement `DialogInterface.OnDismissListener` and/or `DialogInterface.OnCancelListener` for notification.

Consider using new fragments API for dialogs.

## ListView and ListActivity

- [ListActivity](http://developer.android.com/reference/android/app/ListActivity.html)
- [ListView](http://developer.android.com/reference/android/widget/ListView.html)
- [ListAdapter](http://developer.android.com/reference/android/widget/ListAdapter.html)
- [Hello, ListView tutorial](http://developer.android.com/resources/tutorials/views/hello-listview.html)

[R.layout](http://developer.android.com/reference/android/R.layout.html) lists standard list item layouts.

[CWAC MergeAdapter](http://github.com/commonsguy/cwac-merge) makes it easy to bind list items to different kinds of data.

Call adapter's `notifyDataSetChanged()` method when data changes, to force views and observers to update.

## Tabs

See the [Tab Layout tutorial](http://developer.android.com/resources/tutorials/views/hello-tabwidget.html)

Note that newer Android apps should use the ActionBar API rather than old-style tabs.
