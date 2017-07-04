Title: Visual Studio 2008 Code Snippet for Inserting a String.Format() call
Date: 2011-02-20 00:57:51
Category: Blog
Slug: visual-studio-2008-code-snippet-inserting-stringformat-call
Alias: 2011/02/19/visual-studio-2008-code-snippet-inserting-stringformat-call/
Tags: vs2008, visualstudio


Over the past year I've been (re-)learning how to use Visual&nbsp;Studio&nbsp;2008. I did a lot of work in the 90's and early 00's with Visual&nbsp;Studios 5, 6, and 2003, but then I had a few years away from Windows development, and I've had limited experience with .NET development.  So I'm constantly discovering "new things" about Visual&nbsp;Studio that my coworkers already know.

One nifty feature of Visual&nbsp;Studio is "code snippets", which are basically little bits of code that can be quickly inserted into a source file using Intellisense.  The inserted code includes placeholders that can be replaced with whatever you need.  For example, if you are typing away in a C# source file and type the keyword `for`, you'll see the Intellsense window pop up with "for" as the selected item, and if you hit the Tab key a couple of times a complete `for` statement with braces, a loop variable, and everything will be inserted.  You can then hit Tab to move to the loop variable name (in case you don't like `i`) and again to go into the loop body.

(Other IDEs have similar features, calling them _abbreviations_, _macros_, etc.  You don't need to tell me that Visual&nbsp;Studio isn't magically unique.)

Visual&nbsp;Studio has a whole bunch of these snippets built in, but you can also define your own by writing an XML file and saving it where Visual&nbsp;Studio can find it.  For example, here is a snippet I wrote to quickly insert `String.Format()` expressions:

    <?xml version="1.0" encoding="utf-8" ?>
    <CodeSnippets xmlns="http://schemas.microsoft.com/VisualStudio/2005/CodeSnippet">
      <CodeSnippet Format="1.0.0">
        <Header>
          <Title>String.Format</Title>
          <Description>Creates a String.Format() call</Description>
          <Author>Kristopher Johnson</Author>
          <SnippetTypes>
            <SnippetType>Expansion</SnippetType>
          </SnippetTypes>
          <Shortcut>sf</Shortcut>
        </Header>
        <Snippet>
          <Declarations>
            <Literal>
              <ID>format</ID>
              <ToolTip>Replace with format string</ToolTip>
              <Default>format</Default>
            </Literal>
            <Literal>
              <ID>arguments</ID>
              <ToolTip>Replace with arguments</ToolTip>
              <Default>arguments</Default>
            </Literal>
          </Declarations>
          <Code Language="CSharp">
            <![CDATA[String.Format("$format$", $arguments$)$end$]]>
          </Code>
        </Snippet>
      </CodeSnippet>
    </CodeSnippets>

Just save this as a file called `StringFormat.snippet` in your `Documents\Visual Studio 2008\Code Snippets\Visual C#\My Code Snippets` folder.  (You can specify another location using the _Code Snippets Manager_ in the _Tools_ menu.)  Then, when editing a C# source file, if you type `sf` and hit Tab a couple of times, this will magically appear in your code:

`String.Format("` *format* `",` *arguments* `)`

The _format_ placeholder will be selected, so you can replace it with your format string, then hit Tab and the _arguments_ placeholder will be selected, so you can replace it.  You can keep hitting Tab to go back and forth between the placeholders.  When finished, hit Return and the cursor will go to the end of the line.

Alas, snippets only work for C#, Visual&nbsp;Basic, and XML editing. Most of my work is in C++, so I have to keep writing code the old-fashioned way there (or use macros).

Note that I have been talking about Visual&nbsp;Studio&nbsp;2008.  "Why aren't you using Visual Studio&nbsp;2010?" some will ask.  Shut&nbsp;up.

For a more comprehensive tutorial on creating code snippets, see [Switch On The Code: C# Tutorial - Visual Studio Code Snippets](http://www.switchonthecode.com/tutorials/csharp-tutorial-visual-studio-code-snippets).
