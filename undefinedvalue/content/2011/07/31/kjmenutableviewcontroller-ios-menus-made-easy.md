Title: KJMenuTableViewController - iOS Menus Made Easy
Date: 2011-07-31 21:22:17
Category: Blog
Slug: kjmenutableviewcontroller-ios-menus-made-easy
Alias: 2011/07/31/kjmenutableviewcontroller-ios-menus-made-easy/
Tags: UITableViewController, ios


I have a new open-source library on Github for use by iOS developers: [KJMenuTableViewController](https://github.com/kristopherjohnson/KJMenuTableViewController).

KJMenuTableViewController is an Xcode project that contains set of classes that simplifies the
creation of "menus" in iOS applications using `UITableViewController`.

The `UITableViewController` class is a generic mechanism for presenting a scrollable list of
rows of items.  It is powerful and extensible, but it can be a chore to present a simple
list of button-like objects that react when tapped.  One must provide implementations of several
methods of the `UITableViewDataSource` and `UITableViewDelegate` classes, each of which will
probably have a `case` statement to handle each of the individual items. It's not difficult, but it is
tedious and error-prone.

The KJMenuTableViewController classes simplify this usage case.  One simply defines a subclass of
`KJMenuTableViewController` and overrides the `viewDidLoad` method to create sections and row items.
`KJMenuTableViewController` implements the table view delegate and data source methods to
appropriately display the sections and rows, and will take action when a row is tapped.

The code to be executed when an item is tapped are written as a block.
When the block is invoked, a `KJMenuItemInvocation` structure is passed to it. This structure
contains pointers to the menu item, cell, and controller, so there is no reason for the block
to retain any of these objects itself.  (Beware of retain cycles if the block _does_ reference
the menu item, cell, or controller.)
<!--break-->
## Usage

Someday, this will be a proper library, but right now the library is distributed as a demo
application that contains reusable classes.

To make use of the reusable classes, copy the following source files from the demo project into
your own application:

* `KJMenuTableViewController.h` and `KJMenuTableViewController.m`
* `KJMenuSection.h` and `KJMenuSection.m`
* `KJMenuItem.h` and `KJMenuItem.m`

## Example

In this example snippet, the controller is a subclass of `KJMenuTableViewController`, which is itself
a subclass of `UITableViewController`.  In the `viewDidLoad` method, we add a first section with
two items, each of which displays its text in an alert box, and a second section that has
an item that pushes a new controller onto the navigation stack.

    - (void)viewDidLoad {
        [super viewDidLoad];
        
        // Add first section
        
        KJMenuSection *section = [KJMenuSection sectionWithHeaderTitle:@"First Section"];
        section.footerTitle = @"Select item above to display alert";
        [self addSection:section];    
        
        KJMenuItem *item;
        
        item = [KJMenuItem itemWithTitle:@"First"];
        item.detailText = @"This is the first item";
        item.block = ^(KJMenuItemInvocation inv) {
            RootViewController *controller = (RootViewController *)inv.controller;
            NSString *title = inv.item.titleText;
            NSString *message = inv.item.detailText;
            [controller displayAlertWithTitle:title message:message];
        };
        [section addItem:item];
        
        item = [KJMenuItem itemWithTitle:@"Second"];
        item.detailText = @"This is the second item";
        item.block = ^(KJMenuItemInvocation inv) {
            RootViewController *controller = (RootViewController *)inv.controller;
            NSString *title = inv.item.titleText;
            NSString *message = inv.item.detailText;
            [controller displayAlertWithTitle:title message:message];
        };
        [section addItem:item];
        
        // Add second section
        
        section = [KJMenuSection sectionWithHeaderTitle:@"Second Section"];
        [self addSection:section];
        
        item = [KJMenuItem itemWithTitle:@"Push view"
                           accessoryType:UITableViewCellAccessoryDisclosureIndicator];
        item.autoDeselectAfterSelect = NO;
        item.block = ^(KJMenuItemInvocation inv) {
            MyViewController *subcontroller = [[MyViewController alloc]
                                               initWithNibName:@"MyViewController" bundle:nil];
            [inv.controller.navigationController pushViewController:subcontroller animated:YES];
        };
        [section addItem:item];
    }

For a complete example, see the demo application's [RootViewController.m](https://github.com/kristopherjohnson/KJMenuTableViewController/blob/master/KJMenuTableViewController/RootViewController.m).

## Future Directions

The following features are planned:

* Add convenience methods to reduce the verbosity of setting up a menu.
* Make it possible to add/remove menu items and change their attributes after menu has already been displayed. (As-is, you need to call the table view's `reloadData` method if you change anything after `viewDidLoad`.)
* Provide a mechanism so that only one item within a section has a checkmark, and when user selects another item the originally checked item is unchecked.
* Provide the ability to define a menu hierarchy that is handled by a single view controller.
* Add support for compilation with ARC enabled
