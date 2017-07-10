Title: Measuring "Simplest"
Date: 2004-01-09 18:16
Author: Kristopher Johnson
Tags: programming
Slug: measuring-simplest

[Joseph Pelrine](http://www.metaprog.com/blogs/index.php?p=63&more=1&c=1&tb=1&pb=1)
notes that "as Alistair Cockburn rightly states, 'simplest' has no
metric. It is not a quantifiable amount." While it is true that one
cannot put a number on it, there is an obvious test: you have the
simplest solution if nobody can think of anything simpler.

Of course, different people have different ideas of what simple is. For
example, C++ templates provide simple solutions to many C++ problems,
but many C++ programmers will consider any use of templates to be
"complicated". (And some would say that C++ provides no simple solutions
for any problem!) Similarly, some prefer break up a class into many
small classes to make things simpler, whereas others think that a small
number of big classes is simpler. Who's right?

Ward Cunningham wrote somewhere that his definition of *simple* is
whatever is easiest to reason about. I would add that it is also
whatever is easiest to communicate to others. If you are trying to
explain your "simple" solution to others, and they don't get it, that is
a good sign that you haven't really found a simple solution. The reason
that XP advocates simplicity is that simple code is easier for somebody
else to understand and to modify in the future.

So, when judging the simplicity of a solution, it is important to
remember that you are writing code for an audience. You have to make
some assumptions about that audience. Do they understand the language
features that you are using? Are they going to understand the idioms?
Does the code you are writing fit in with the rest of the project's code
in a way that will make sense to them?

Always remember that the value of simplicity is that it makes future
change easier. The simplest solution is the one that will be easiest to
replace.

