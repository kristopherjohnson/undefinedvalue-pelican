Title: Anti-pattern: The Overly Generic Interface
Date: 2009-07-04 14:43:25
Category: Blog
Slug: anti-pattern-overly-generic-interface
Alias: 2009/07/04/anti-pattern-overly-generic-interface/
Tags: programming


While learning about [Core Animation](http://en.wikipedia.org/wiki/Core_Animation), I was disappointed to find that it is plagued by the anti-pattern that I call the _Overly Generic Interface_.
<!--break-->
The Overly Generic Interface is an interface that provides a very small set of functions, but each function takes parameters that allow one to do a lot of different things.  For example, in C++ an overly generic interface would look like this:

    // A Value object can hold a string, an integer, a float, an object pointer, etc.
    class Value {
        // ...
    };

    class Object {
    public:
        // Return the value of a named property
        Value getProperty(const string& propertyName);

        // Set the value of a named property
        void setProperty(const string& propertyName,
                         const Value& newValue);

        // Set the values of multiple named properties with one call
        void setProperties(const map<string, Value> properties);

        // Invoke a named operation with a parameter list
        void performOperation(const string& operationName,
                              const list<Value>& parameters);
    };

And application code that uses the interface looks something like this:

    class Person: public Object { ... };

    enum Gender { Female, Male };

    // Initialize husband, using the set-one-property-at-a-time interface
    Person husband;
    husband.setProperty("firstName", ValueFromString("Kristopher"));
    husband.setProperty("lastName",  ValueFromString("Johnson"));
    husband.setProperty("gender",    ValueFromInt(Male));

    // Initialize wife, using the set-all-properties-in-one-operation interface
    Person wife;
    map<string, Value> wifeProperties
    wifeProperties["firstName"] = ValueFromString("Pebble");
    wifeProperties["lastName"]  = ValueFromString("Johnson");
    wifeProperties["Gender"]    = ValueFromInt(Female);
    wife.setProperties(wifeProperties);

    // Invoke the recordMarriage operation
    list params;
    params.push_back(ValueFromPointer(&husband));
    params.push_back(ValueFromPointer(&wife));
    recorder.performOperation("recordMarriage", params);

The supposed benefits (as far as I can tell) of a very generic interface are these:

- Changes to the interface are not needed as new properties and operations are added.
- If the set of properties and operations is huge, you don't need a huge class declaration.
- The set of available properties and operations can be different for different instances of a class.
- Property names and operation names can be "magic" things with powerful behavior.  (For example, maybe the above interface could let you specify something like `wifesName = husband.getProperty("findWife#name")`.)
- It makes it easy to create tools that bind things to other things, via names and string values.
- There can be performance benefits for the “set multiple properties in a single call” operation.
- There can be performance benefits if it maps directly to a lower-level interface (a device driver, for example).

However, I hate such interfaces, for these reasons:

- The code is ugly and hard to read.
- The compiler can't check whether you’ve correctly spelled all the property names or whether you have passed the right type of data for each one.  (For example, did you notice that I capitalized the name of the `gender` property inconsistently in the above example?  If not, how would you have found that bug?)
- The debugger can't easily show you the values of properties in an object, because they are not exposed as simple instance variables.
- Somewhere external to code, you need to maintain documentation about what all the valid names and values are.  And you need to constantly refer to that external documentation, because your IDE won't be able to help you with auto-completion and other time-saving features.
- Magic is not always helpful. The magic names often have a syntax that is different from that of the “host language,” so programmers essentially have another language to learn.

As an illustration of the first objection, I think the following would be a lot more readable and easier to maintain than the above:

    Person husband;
    husband.setFirstName("Kristopher");
    husband.setLastName("Johnson");
    husband.setGender(Male);

    Person wife;
    wife.setFirstName("Pebble");
    wife.setLastName("Johnson");
    wife.setGender(Female);

    recorder.recordMarriage(husband, wife);

Note that the `Person` class here could be derived from `Object`, like this:

    class Person: public Object {
    public:
        string getFirstName();
        void setFirstName(const string& newValue);

        string getLastName();
        void setLastName(const string& newValue);

        // and so on, for all properties
    };

and in this case you would have both the generic `Object` interface and the specific `Person` interfaces available.  I have no objection to that.

A generic interface is often useful (e.g., [Cocoa Bindings](http://developer.apple.com/documentation/Cocoa/Reference/CocoaBindingsRef/CocoaBindingsRef.html)). My objection is to those API’s that _only_ provide the generic interface. In Core&nbsp;Animation, practically everything is done by creating `NSDictionary` objects, populating them with obscure keys and objects, and then passing them to the API. There are a few higher-level interfaces available, but they don't provide access to all of Core&nbsp;Animation's functionality, so using the low-level overly generic interface is a necessity.

Names are important, and therefore names should be explicitly declared.  Otherwise, they are hidden from the compiler, from the IDE, from the debugger, and from programmers who read class declarations.  Hidden names and magic names cause problems.

When confronted with an Overly Generic Interface, I almost always end up writing some sort of wrapper around it.  It would be nice if I didn't have to do so.
