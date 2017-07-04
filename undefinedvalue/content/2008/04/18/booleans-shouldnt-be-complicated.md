Title: Booleans Shouldn't Be Complicated
Date: 2008-04-18 18:17:00
Category: Blog
Slug: booleans-shouldnt-be-complicated
Alias: 2008/04/18/booleans-shouldnt-be-complicated/
Tags: programming, rant


<p><i>Warning: Geeky programmer content below.</i></p>
<p>
While learning a new codebase, I was a little disturbed when I saw this:
</p>
<pre>
  enum IsVerifying {
    IsVerifyingFalse,
    IsVerifyingTrue
  };

  enum IsVerified {
    IsVerifiedFalse,
    IsVerifiedTrue
  };

  enum IsEnabled {
    IsEnabledFalse,
    IsEnabledTrue
  };

  enum IsActive {
    IsActiveFalse,
    IsActiveTrue
  };

  enum IsOnline {
    IsOnlineFalse,
    IsOnlineTrue
  };

  /* etc. (There are about a dozen more of these.) */
</pre>
<p>
And there was a lot of verbose code for dealing with these types, such as
</p>
<pre>
  if (Verified()) {
    verified = IsVerifiedTrue;
  }
  else {
    verified = IsVerifiedFalse;
  }

  if (Enabled()) {
    enabled = IsEnabledTrue;
  }
  else {
    enabled = IsEnabledFalse;
  }

  /* etc. */
</pre>
<p>
What's wrong with using plain-old-Boolean values <tt>false</tt> and <tt>true</tt>, or 0 and 1?
</p>
<p>
Well, after poking around the code more, I did find the reason that the original programmer did this.  He has a lot of functions that take several flags as parameters, and something like this:
</p>
<pre>
  SetStates(IsVerifyingFalse,
            IsVerifiedTrue,
            IsEnabledTrue,
            IsActiveFalse,
            IsOnlineFalse);
</pre>
<p>
is easier to understand than something like this:
</p>
<pre>
  SetStates(false, true, true, false, false);
</pre>
<p>
But still, <i>yyeeaagghh</i> is the proper reaction to seeing something like this.
</p>
