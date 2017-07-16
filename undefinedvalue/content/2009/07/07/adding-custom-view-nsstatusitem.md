Title: Adding a Custom View to an NSStatusItem
Date: 2009-07-07 11:48:30
Category: Blog
Slug: adding-custom-view-nsstatusitem
Alias: 2009/07/07/adding-custom-view-nsstatusitem/
Tags: programming, menubarcountdown, code, cocoa, macdev
AdSense: yes


My [Menubar Countdown](http://capablehands.net/menubarcountdown) application uses an [NSStatusItem](http://developer.apple.com/documentation/Cocoa/Reference/ApplicationKit/Classes/NSStatusItem_Class/Reference/Reference.html) to display itself in the menu bar.  I recently had to add a custom view to that status item, and thought I'd share what I learned about the process here.
<!--break-->
A little background: a _status item_ is one of those little thingees you see on the right side of the Mac OS&nbsp;X menu bar, such as the clock, the Spotlight icon, the sound volume control, and so forth.  Programmatically, you create a status item by doing this:

    NSStatusBar *statusBar = [NSStatusBar systemStatusBar];
    NSStatusItem statusItem = [statusBar statusItemWithLength:NSVariableStatusItemLength];
    [statusItem retain];

Once you've created a status item, you can do these things with it:

- call the `setTitle:` method to display a string in the menu bar (or call `setAttributedTitle` to display an attributed string)
- call the `setMenu:` method so that a menu is displayed when the status item is clicked
- call the `setHighlightMode:` method with `YES` to cause the title to be highlighted appropriately when a menu is displayed
- call the `setTooltip:` method to set a tooltip to be displayed when the mouse hovers over the status item

There are other things you can do with a status item, but the above describes the features that Menubar&nbsp;Countdown uses.  When the timer is running, the application simply calls `setTitle:` once per second to display 00:25:00, 00:24:59, 00:24:58, and so on down to 00:00:00.  The user can click the item to display a menu that controls the application.

While the `setTitle` and `setImage` methods give many developers all the display functionality they need, NSStatusItem also offers the ability to set a custom view that displays in the menu bar.  I decided I wanted to add some animation, so I needed a view.  The problem is that if you set a custom view, you are responsible for all the drawing and event handling; NSStatusItem no longer does any of that for you.

After a couple of hours of Googling and experimentation, I wound up with something that worked.

I decided I wanted a view class with two properties: `statusItem`, which would be a pointer to the `NSStatusItem` associated with the view, and `title`, which would be the string displayed in the menu bar.  The `title` attribute would make it easy to update the app, as I could just change every instance of `[statusItem setTitle:...]` to `[statusItemView setTitle:...]`.

Here is my class declaration:

    @interface StatusItemView : NSView {
        NSStatusItem *statusItem;
        NSString *title;
        BOOL isMenuVisible;
    }
    @property (retain, nonatomic) NSStatusItem *statusItem;
    @property (retain, nonatomic) NSString *title;
    @end

(The purpose of the `isMenuVisible` instance variable will be explained later.)

The initialization and deallocation methods are straightforward:

    - (id)initWithFrame:(NSRect)frame {
        self = [super initWithFrame:frame];
        if (self) {
            statusItem = nil;
            title = @"";
            isMenuVisible = NO;
        }
        return self;
    }

    - (void)dealloc {
        [statusItem release];
        [title release];
        [super dealloc];
    }

The `statusItem` property can be simply synthesized:

    @synthesize statusItem;

Next, we'll tackle menu handling.  When our view is clicked, we want to display the menu, and while the menu is displayed, we want our item to be displayed in a highlighted state.  `NSStatusItem` provides the method `popUpStatusItemMenu:` to display the menu in the right place under the menu bar.  To deal with highlighting, we have an instance variable `isMenuVisible` that will be set to `YES` whenever the menu is being displayed, and `NO` when it is not.  We can use the [NSMenu](http://developer.apple.com/documentation/Cocoa/Reference/ApplicationKit/Classes/nsmenu_Class/Reference/Reference.html) delegate `menuWillOpen:` and `menuDidClose` methods to be notified when the menu is shown or closed.

    - (void)mouseDown:(NSEvent *)event {
        [[self menu] setDelegate:self];
        [statusItem popUpStatusItemMenu:[self menu]];
        [self setNeedsDisplay:YES];
    }

    - (void)rightMouseDown:(NSEvent *)event {
        // Treat right-click just like left-click
        [self mouseDown:event];
    }

    - (void)menuWillOpen:(NSMenu *)menu {
        isMenuVisible = YES;
        [self setNeedsDisplay:YES];
    }

    - (void)menuDidClose:(NSMenu *)menu {
        isMenuVisible = NO;
        [menu setDelegate:nil];    
        [self setNeedsDisplay:YES];
    }

The `title` property affects the display, so we can't just synthesize it.  When the `title` is set, we need to determine the bounding rectangle of the text, and then set the status item's `length` so that it can contain the text.  Setting the status item's length also updates the custom view's bounds.

After some experimentation and zooming, I figured out that when a normal `NSStatusItem` draws its title, there is a horizontal margin of six pixels between the side of the item's display and the text, and a margin of three pixels between the bottom of the display and the text.  We need those values to calculate status item size:

    #define StatusItemViewPaddingWidth  6
    #define StatusItemViewPaddingHeight 3

To determine the text's bounding rectangle, we can call `NSString`'s `boundingRectWithSize:options:attributes:` method, but to do that, we need to construct an _attributes_ dictionary that describes the font and other aspects of drawing.  We'll use the same attributes dictionary in our `drawRect:` method, so when we construct it we'll include the desired foreground drawing color in the attributes.

    - (NSColor *)titleForegroundColor {
        if (isMenuVisible) {
            return [NSColor whiteColor];
        }
        else {
            return [NSColor blackColor];
        }    
    }

    - (NSDictionary *)titleAttributes {
        // Use default menu bar font size
        NSFont *font = [NSFont menuBarFontOfSize:0];
    
        NSColor *foregroundColor = [self titleForegroundColor];
    
        return [NSDictionary dictionaryWithObjectsAndKeys:
                font,            NSFontAttributeName,
                foregroundColor, NSForegroundColorAttributeName,
                nil];
    }

    - (NSRect)titleBoundingRect {
        return [title boundingRectWithSize:NSMakeSize(1e100, 1e100)
                                   options:0
                                attributes:[self titleAttributes]];
    }

With the `titleBoundingRect` method defined, we can implement the `title` property:

    - (void)setTitle:(NSString *)newTitle {
        if (![title isEqual:newTitle]) {
            [newTitle retain];
            [title release];
            title = newTitle;
        
            // Update status item size (which will also update this view's bounds)
            NSRect titleBounds = [self titleBoundingRect];
            int newWidth = titleBounds.size.width + (2 * StatusItemViewPaddingWidth);
            [statusItem setLength:newWidth];
        
            [self setNeedsDisplay:YES];
        }
    }

    - (NSString *)title {
        return title;
    }

And finally, we can implement `drawRect:`.  `NSStatusItem` provides a method `drawStatusBarBackgroundInRect:withHighlight:` that will draw the appropriate background for a status item, so we just call that and then draw the title at the correct position.

    - (void)drawRect:(NSRect)rect {
        // Draw status bar background, highlighted if menu is showing
        [statusItem drawStatusBarBackgroundInRect:[self bounds]
                                    withHighlight:isMenuVisible];
    
        // Draw title string
        NSPoint origin = NSMakePoint(StatusItemViewPaddingWidth,
                                     StatusItemViewPaddingHeight);
        [title drawAtPoint:origin
            withAttributes:[self titleAttributes]];
    }

That's it for the view class.  Here is the code in my application controller that sets it all up:

    statusItem = [[NSStatusBar systemStatusBar] statusItemWithLength:NSVariableStatusItemLength];
    [statusItem retain];
    
    statusItemView = [[StatusItemView alloc] init];
    [statusItemView retain];
    statusItemView.statusItem = statusItem;
    [statusItemView setMenu:menu];
    [statusItemView setToolTip:NSLocalizedString(@"Menubar Countdown",
                                                 @"Status Item Tooltip")];
    [statusItem setView:statusItemView];
    [statusItemView setTitle:@"00:00:00"];

(There is a minor gotcha here: You have to call the status item's `setView:` before calling the view's `setTitle:`, because the view needs to call the status item's `setLength:` method.  I could have fixed that, but decided it wasn't worth the effort.)

Here, we are creating the view programmatically. I tried creating it in Interface Builder and setting all the connections that way, but the result was a view with funky `bounds` and `frame` properties that didn't display itself the right way.  Google found some other people with the same problem, and while some had found solutions, I didn't understand them. (Maybe someone can explain it to me.)

And so, after a couple of hours of work, I had a custom status item view that makes the status item look just like it did before I had the custom view.  Progress!

Of course, I didn't leave the view that way.  I called `setWantsLayer:` on the view and started doing Core&nbsp;Animation stuff.  Maybe I'll write about that next time.
