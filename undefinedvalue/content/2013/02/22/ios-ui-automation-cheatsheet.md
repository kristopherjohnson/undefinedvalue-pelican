Title: iOS UI Automation Cheatsheet
Date: 2013-02-22 16:00:46
Category: Blog
Slug: ios-ui-automation-cheatsheet
Alias: 2013/02/22/ios-ui-automation-cheatsheet/
Tags: unittesting, iosdev, cheatsheet


I have just learned about Apple's UI Automation testing framework. Unfortunately, I don't have an iOS project to work on at the moment, so I am probably going to forget all about it. This is my cheatsheet. It may not help you at all.

## Tutorials

- <http://blog.manbolo.com/2012/04/08/ios-automated-tests-with-uiautomation>
- <http://alexvollmer.com/posts/2010/07/03/working-with-uiautomation/>
- [WWDC 2010 Session 306 - Automating User Interface Testing with Instruments](https://developer.apple.com/videos/wwdc/2010/)

## Documentation

- [UI Automation JavaScript Reference](http://developer.apple.com/library/ios/#documentation/DeveloperTools/Reference/UIAutomationRef/_index.html)
- [Instruments User Guide: Automating UI Testing](http://developer.apple.com/library/ios/#documentation/DeveloperTools/Conceptual/InstrumentsUserGuide/UsingtheAutomationInstrument/UsingtheAutomationInstrument.html)

## Tips

- Use the Tuneup library: <https://github.com/alexvollmer/tuneup_js>
- Assign an `accessibilityIdentifier` to each UI element.
- Set `UIATarget.onAlert` to handle externally generated alerts.
- Use `UIAElement.logElementTree()` to figure out how to navigate the visual hierarchy.
- If a value doesn't change when expected, try adding `UIATarget.delay(1);`

