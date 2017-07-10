Title: Confessional
Date: 2004-01-07 03:23
Author: Kristopher Johnson
Tags: self-indulgence, programming
Slug: confessional

I committed several developer sins today. (Actually, I only committed a
couple today; the others were committed in the past but came to light
today.)

First, I assumed that the bug was in the other guy's code. I was sure
there could be nothing wrong in my simple straightforward
object-oriented code, so it must have been in his quagmire of
multi-threaded straight ANSI C. So I spent most of my time trying to
read his code instead of examining my own more carefully. I cursed him
for not providing documentation or unit tests.

Second, I put off as long as possible the arduous task of reading
through the voluminous logging information his code generated. After
all, if he is a bad programmer it stands to reason that his log will
hold only useless information. When I finally did read through the log,
it became clear that the code I had copied-and-pasted from another
program was doing bad things.

Yes, that was the original sin: I copied-and-pasted code from another
program without reviewing it sufficiently. I know it's wrong. I scream
at people when I see them do this. But it was the easiest thing to do at
the time.

And when i discovered the copied-and-pasted bug, my first instinct was
to curse the name of the writer of that code I had copied. But of
course, he does not deserve my ire. The real culprit is my boss, who
suggested that copying and pasting was the fastest way to get the
feature implemented! No, that isn't right either. I committed the act;
it is my responsibility.

I keep thinking I am getting better at this stuff. I think I have better
habits than others. I only break my own rules when I think it really
won't hurt anything.

I am ashamed. I ask forgiveness.

