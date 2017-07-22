"""
age_in_days is a Jinja2 filter that given a datetime
returns the number of days since that time.
"""

from datetime import datetime, timedelta

def age_in_days(dt):
    """Return a number of days between now and a specified datetime."""
    now = datetime.now(dt.tzinfo)
    delta = now - dt
    return delta.days

