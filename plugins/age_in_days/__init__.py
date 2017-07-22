"""
The age_in_days plugin adds a Jinja filter, age_in_days, that
given a datetime value will return the number of days since
that time.

It is intended to be used in Pelican templates like this:

    {% if article.date|age_in_days > 30 %}
        ...
    {% endif %}
"""

from pelican import signals
from . import ageindays

def add_filter(pelican):
    """Add age_in_days filter to Pelican."""
    pelican.env.filters.update({'age_in_days': ageindays.age_in_days})

def register():
    """Plugin registration."""
    signals.generator_init.connect(add_filter)

