Title: The Easiest Programming Bug I Spent Way Too Much Time Trying to Solve
Date: 2013-11-12 21:02:46
Category: Blog
Slug: easiest-programming-bug-i-spent-way-too-much-time-trying-solve
Alias: 2013/11/12/easiest-programming-bug-i-spent-way-too-much-time-trying-solve/
Tags: puzzle, programming, debugging


I ran across a question on Quora: [What's the easiest programming bug you spent way too much time trying to solve?](http://www.quora.com/Programming-Languages/Whats-the-easiest-programming-bug-you-spent-way-too-much-time-trying-to-solve).

Here is my answer to that question. Some time during my first few years of programming, I wrote code similar to this little snippet and expected it to print "FOO", but instead it prints "None of the above". It is written in C, but should be comprehensible to anyone who knows a language with similar syntax (C++, Java, JavaScript, C#, etc.). It took me about a half day of staring and single-stepping in a debugger to figure out what was wrong. When I looked at the disassembly listing, I was convinced I'd found a bug in the C compiler. Maybe you can figure it out faster than I could.

    #include <stdio.h>

    int main(int argc, char *argv[])
    {
        const int FOO = 1;
        const int BAR = 2;

        int n = FOO;
        
        switch (n)
        {
            FOO:
                printf("FOO");
                break;
            
            BAR:
                printf("BAR");
                break;
                
            default:
                printf("None of the above");
                break;
        }
        
        return 0;
    }

