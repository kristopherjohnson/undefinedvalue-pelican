Title: Remoting.Corba
Date: 2009-08-26 10:04
Category: Blog
Slug: remotingcorba
Alias: 2003/12/29/remotingcorba/
Tags: dotnet, corba


<p>[Note: The Remoting.Corba project is "dead", and has not been active for several years.  If you need .NET-CORBA interoperability, I recommend checking out <a href="http://iiop-net.sourceforge.net">IIOP.NET</a>.  Archived Remoting.Corba documentation is still available via <a href="http://tinyurl.com/remoting-corba">The Wayback Machine</a>.]</p>
<p><a href="http://remoting-corba.sourceforge.net">Remoting.Corba</a> is an open-source .NET library that provides interoperability between the .NET Framework and CORBA servers/clients, using the .NET Remoting architecture.
<p>
I started this project to learn more about .NET Remoting and to apply my knowledge of CORBA. My basic goal was to be able to write .NET programs that interacted with CORBA-based applications using typical .NET Remoting code.  For example, if a CORBA server supported this IDL:
<p>
<pre>
// CORBA IDL
interface Adder {
    long add_longs(in long arg1, in long arg2);
    double add_doubles(in double arg1, in double arg2);
};</pre>
<p>
then one could write a C# program that invoked the server, without need for an ORB, using code something like this:
<p>
<pre>
// standard .NET Remoting stuff
using System;
using System.IO;
using System.Runtime.Remoting.Channels;
using System.Runtime.Remoting.Messaging;

// Remoting.Corba
using Remoting.Corba.Channels.Iiop;

namespace MyExample
{
    // define .NET interface mapping for IDL interface
    interface Adder {
        int add_longs(int arg1, int arg2);
        double add_doubles(double arg1, double arg2);
    };

    class App {
        // entry point
        static void Main(string[] args)
        {
            try
            {
                // register IIOP channel with Remoting
                ChannelServices.RegisterChannel(new IiopClientChannel());

                // Use a standard CORBA stringified object reference for the server
                string ior = "corbaloc:iiop:localhost:9999/Adder";

                // create the proxy to the server object
                Adder server = (Adder) Activator.GetObject(typeof(Adder), ior);

                // execute some methods on the remote object
                Console.Out.WriteLine("1 + 2 = {0}", server.add_longs(1, 2));
                Console.Out.WriteLine("1.0 + 2.0 = {0}", server.add_doubles(1.0, 2.0));
            }
            catch (Exception ex)
            {
                Console.Error.WriteLine("Exception: " + ex.ToString());
            }
        }
    }
}</pre>
<p>
The IiopClientChannel class from the R.C library takes care of generating and interpreting the CORBA IIOP (Internet Inter-ORB Protocol) messages and pumping them through the .NET runtime. There is also an IiopServerChannel class that can be used to implement CORBA servers using .NET Remoting.
<p>
It was pretty cool when it worked.  The .NET Framework's Remoting architecture is very open, allowing programmers to plug in their own network protocols and messaging formats.  I used some custom attributes to provide information needed by the CORBA engine that could not be gleaned via data types and reflection mechanisms.
<p>
Unfortunately, while the .NET Remoting architecture is open, it is not well documented.  If all you want to do is send a SOAP message via some protocol other than HTTP (for example, via UDP, via message queues, via e-mail, etc.), then it is pretty easy to plug your own stuff in.  But if you are doing anything more complicated, then you will quickly discover that the only way to figure out what's going on inside .NET is to look at the <a href="http://www.microsoft.com/downloads/details.aspx?FamilyId=3A1C93FA-7462-47D0-8E56-8DD34C6292F0&displaylang=en">Rotor</a> source code.
<p>
The project was valuable to me in that I learned a lot about .NET and C#. It was also gratifying to see other people using it and expressing interest in it. I was especially excited when it was mentioned in Don Box's Spoutlet, and when Miguel Icaza started playing around with it in Mono. It even got a few pages devoted to it in a <a href="http://www.amazon.com/exec/obidos/tg/detail/-/0735619220/qid=1069133497/sr=1-1/ref=sr_1_1/104-4292430-8931121?v=glance&s=books">Microsoft Press book</a>!
<p>
I wrote this code during a period when I was not working any paying jobs, so I was always hoping I would find somebody willing to pay me to add features.  There were a few nibbles, but users were generally able to add features themselves instead of hiring me to do so.  I talked to some people at Microsoft and Inprise about potential deals, but nothing came of it.
<p>
I have put a few projects on SourceForge, but this was the first one where I got any significant contributions from other developers. Michael Sawczyn created an IDL compiler.  Other developers did some bug fixing, refactoring, and feature additions.  It never reached the "critical mass" needed to keep it going after I lost interest, but I think it was close.
<p>
I worked on R.C for a few months. I lost interest in it due to several factors:
<ul>
<li>No paying customers.</li>
<li>No real need to use it myself.</li>
<li>All the low-hanging fruit was gone; further development would have involved a lot of very technical work with little tangible benefit.</li>
<li>The appearance of commercial CORBA ORBs for .NET from Borland and others.</li>
<li>Limitations of the .NET framework</li>
</ul>
<p>
We hit limitations of the .NET framework when trying to figure out how to map remote object references back to objects in the same process. The only way to do it was to use reflection to invoke private methods of internal .NET classes.  That prospect triggered enough of an "Ewww!" response that I decided further work was only going to make me feel worse.
<p>
I used a <a href="http://web.archive.org/web/20041213054715/kristopherjohnson.net/cgi-bin/rc/wiki.pl?Remoting.Corba_Wiki">wiki</a> to distribute the "documentation" for the project.  I liked how the wiki turned out, but there were few contributions to it from anyone except myself.
<p>
So what did I get out of Remoting.Corba? Obviously, I learned about .NET Remoting and some more about the internals of CORBA. I got practice writing C# networking code. I made some contacts in the industry. I wish I could have used R.C on a real project, but that might have taken the fun out of it.
