Title: Adding a Jinja2 Filter with a Pelican Plugin
Slug: adding-a-jinja2-filter-with-a-pelican-plugin
Date: 2017-07-22 10:58
Category: Blog
Tags: blog, pelican, jinja, python

With my [new blog setup](https://undefinedvalue.com/rebuilding-my-blog-again.html), I decided to give [Google AdSense](https://en.wikipedia.org/wiki/AdSense) a try.  I don't have many regular readers, but I do have a few pages that attract search-engine traffic.  So, to monetize those older pages without shoving ads in my regular readers' faces, I decided to show ads on posts that were over a month old.  That should be easy enough to add to the [article.html](https://github.com/kristopherjohnson/undefinedvalue-pelican/blob/master/themes/undefinedvalue/templates/article.html) template:

    {% if article.date|age_in_days > 30 %}
        <!-- ... Include AdSense code ... -->
    {% endif %}

Only one problem: there is no `age_in_days` filter provided by Pelican or Jinja.  I'd have to write a custom filter myself.

A Jinja [custom filter](http://jinja.pocoo.org/docs/2.9/api/#custom-filters) is just a Python function that takes an argument and produces a result.  My filter function is pretty simple:

    :::python
    from datetime import datetime

    def age_in_days(dt):
        """Return a number of days between now and a specified datetime."""
        now = datetime.now(dt.tzinfo)
        delta = now - dt
        return delta.days

I had to figure out how to add that to Pelican's Jinja2 template-rendering environment.  I found a [How to add a custom Jinja filter to Pelican post](https://linkpeek.com/blog/how-to-add-a-custom-jinja-filter-to-pelican.html) that showed how to import a function and set the Pelican's `JINJA_FILTERS` variable in `pelicanconf.py`, but I didn't like the idea of adding imports and functions to a configuration file.  I decided it would be cleaner (and more fun) to figure out how to make a [Pelican plugin](http://docs.getpelican.com/en/3.7.1/plugins.html) that provided my filter.

It wasn't hard to figure this out, because I found a [Jinja Filters plugin](https://github.com/MinchinWeb/minchin.pelican.jinja_filters) that provides a set of filters, so I could just copy the little bits I needed from that for registering my filter. A Pelican plugin must [provide a `register()` function](http://docs.getpelican.com/en/3.7.1/plugins.html#how-to-create-plugins) that sets up a mapping of Pelican "signals" to functions that are to be called.  My plugin handles the `generator_init` signal by adding the `age_in_days` filter to Pelican's Jinja environment:

    :::python
    from pelican import signals
    from . import ageindays

    def add_filter(pelican):
        """Add age_in_days filter to Pelican."""
        pelican.env.filters.update({'age_in_days': ageindays.age_in_days})

    def register():
        """Plugin registration."""
        signals.generator_init.connect(add_filter)

Then I had to update my `pelicanconf.py` to load this plugin in addition to the other plugins I use:

    :::python
    PLUGIN_PATHS = ['../plugins', '../pelican-plugins']
    PLUGINS = ['age_in_days', 'pelican_alias', 'neighbors', 'sitemap']

And that's it.

You can see the whole plugin here: <https://github.com/kristopherjohnson/undefinedvalue-pelican/tree/master/plugins/age_in_days>

