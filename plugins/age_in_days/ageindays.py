from datetime import datetime

def age_in_days(dt):
    """Return a number of days between now and an earlier datetime."""
    now = datetime.now(dt.tzinfo)
    delta = now - dt
    return delta.days

