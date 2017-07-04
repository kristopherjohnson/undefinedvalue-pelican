Title: How Not to Refactor a Function That Has Too Many Parameters
Date: 2009-06-28 16:13:31
Category: Blog
Slug: how-not-refactor-function-has-too-many-parameters
Alias: 2009/06/28/how-not-refactor-function-has-too-many-parameters/
Tags: programming


Most programmers know that having functions with too many parameters can be confusing. However, fixing such problems requires some intelligence. A programmer once saw some code like this:

    SetObjectParams(obj, foo, bar, baz, quux, xyzzy, abra, cadabra, hocus, pocus, presto, shazam);

Finding a stylistic rule somewhere that said a function should have no more than five parameters, the programmer &ldquo;refactored&rdquo; it to this:

    SetObjectParams1(obj, foo, bar, baz, quux);
    SetObjectParams2(obj, xyzzy, abra, cadabra, hocus);
    SetObjectParams3(obj, pocus, presto, shazam);

No, that's not how one resolves this problem. You fix this problem by defining functions that each do something simple, give each function a name that describes what it does, and let them take however many parameters make sense.
