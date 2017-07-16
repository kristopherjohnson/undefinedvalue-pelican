Title: Changing Background Color and Section Header Text Color in a Grouped-style UITableView
Date: 2009-08-26 00:10:40
Category: Blog
Slug: changing-background-color-and-section-header-text-color-grouped-style-uitableview
Alias: 2009/08/25/changing-background-color-and-section-header-text-color-grouped-style-uitableview/
Tags: samplecode, programming, iphone, code, cocoa, iosdev
AdSense: yes


While working on an iPhone application, I decided I wanted to change the colors of the background and section headers of a `UITableView` with the `UITableViewStyleGrouped` style. It took a lot more work than I expected, so I'm sharing what I learned with anyone else who needs to do this.

To review: when you create a table view with the grouped style, each section of the table shows up as a rounded rectangle, section titles are displayed as dark gray text between the rectangles, and the background is gray. I wanted the background to be a pale pastel color, so I looked into how to change that.

Of course, I first looked at the options in Interface Builder.  A table view has a background color that can be set in IB, but setting that didn't accomplish anything.

With a bit of Googling, I learned that the way to give a table view a background color is to set the background color to `[UIColor clearColor]`, and let the color (or image) of whatever is behind the table view show through. So, I set my window's `backgroundColor` to the color I wanted, and then added this to my table view's controller class:

    #define TableViewTag 8888

    - (void)viewDidLoad {
        [super viewDidLoad];

        // Make table view's background transparent to allow window background to be visible
        UITableView *tableView = (UITableView *)[self.view viewWithTag:TableViewTag];
        tableView.backgroundColor = [UIColor clearColor];
    }

In Interface Builder, I set the tag of the table view to 8888. Another way to do this would be to have an outlet for the table view, but I didn't want to do that in this particular case.

So, that gave the table the background color I wanted, but I then noticed that the dark-gray section titles didn't look good against that color. I started looking for some sort of "`sectionHeaderTextColor`" property on the table view, but of course, there was no such thing.

After more Googling, I concluded that there was no way to just set the color. What you have to do is provide your own custom section header view containing a text label. With that, you can set whatever colors you want. So, I added these implementations of `UITableViewDataSource` protocol methods to my table view controller:

    #define SectionHeaderHeight 40
    
    
    - (CGFloat)tableView:(UITableView *)tableView heightForHeaderInSection:(NSInteger)section {
        if ([self tableView:tableView titleForHeaderInSection:section] != nil) {
            return SectionHeaderHeight;
        }
        else {
            // If no section header title, no section header needed
            return 0;
        }
    }
    
    
    - (UIView *)tableView:(UITableView *)tableView viewForHeaderInSection:(NSInteger)section {
        NSString *sectionTitle = [self tableView:tableView titleForHeaderInSection:section];
        if (sectionTitle == nil) {
            return nil;
        }
    
        // Create label with section title
        UILabel *label = [[[UILabel alloc] init] autorelease];
        label.frame = CGRectMake(20, 6, 300, 30);
        label.backgroundColor = [UIColor clearColor];
        label.textColor = [UIColor colorWithHue:(136.0/360.0)  // Slightly bluish green
                                     saturation:1.0
                                     brightness:0.60
                                          alpha:1.0];
        label.shadowColor = [UIColor whiteColor];
        label.shadowOffset = CGSizeMake(0.0, 1.0);
        label.font = [UIFont boldSystemFontOfSize:16];
        label.text = sectionTitle;
    
        // Create header view and add label as a subview
        UIView *view = [[UIView alloc] initWithFrame:CGRectMake(0, 0, 320, SectionHeaderHeight)];
        [view autorelease];
        [view addSubview:label];
    
        return view;
    }

I also added a suitable implementation of `tableView:titleForHeaderInSection:`, and everything worked.

If there is a simpler way to do this, I'd love to hear about it.
