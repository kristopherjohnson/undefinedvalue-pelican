Title: Measuring Elapsed Time in C# Methods
Date: 2012-02-10 01:12:02
Category: Blog
Slug: measuring-elapsed-time-c-methods
Alias: 2012/02/09/measuring-elapsed-time-c-methods/
Tags: codesnippet, c#, .NET


When determining why some damned thing in my .NET programs is taking so damned long, it is useful to be able to look at the elapsed time for various sections of code.  The straightforward way to do this is to create an instance of `System.Diagnostics.Stopwatch`, start it, do the thing, then stop the `Stopwatch` and print out the elapsed time.

But it gets tedious to keep adding those `var stopwatch = new Stopwatch(); stopwatch.Start();` and `stopwatch.Stop(); Print(stopwatch.ElapsedMilliseconds);` lines all over the place, and it also makes the code less readable, so I made a little class to simplify things.
<!--break-->
Here is the class:

    public static class Timed
    {
        /// <summary>
        /// Execute action then invoke reporting action with elapsed time
        /// </summary>
        /// <param name="timedAction">action to be executed and elapsed time measured</param>
        /// <param name="reportAction">action to be executed with the elapsed number of milliseconds passed as a parameter</param>
        /// <returns>number of milliseconds elapsed during timedAction</returns>
        public static long Execute(Action timedAction, Action<long> reportAction)
        {
            var stopwatch = new System.Diagnostics.Stopwatch();

            stopwatch.Start();
            timedAction();
            stopwatch.Stop();

            var elapsedMilliseconds = stopwatch.ElapsedMilliseconds;

            if (reportAction != null)
            {
                reportAction(elapsedMilliseconds);
            }

            return elapsedMilliseconds;
        }

        /// <summary>
        /// Invoke specified action and return number of milliseconds elapsed
        /// </summary>
        /// <param name="timedAction">timed action to be executed</param>
        /// <returns>number of milliseconds elapsed</returns>
        public static long Execute(Action timedAction)
        {
            return Timed.Execute(timedAction, null);
        }
    }

So, for example, if one wanted to measure the time used by the loop in this method:

    public void BlurpAllFrables()
    {
        foreach (var frable in GetFrables())
            frable.Blurp();
    }

one could do this:

    public void BlurpAllFrables()
    {
        Timed.Execute(() =>
        {
            foreach (var frable in GetFrables())
                frable.Blurp();
        },
        (long millis) =>
        {
            Trace.WriteLine(String.Format("Blurping frables took {0} ms", millis.ToString()));
        });
    }

or one could do this:

    public void BlurpAllFrables()
    {
        var millis = Timed.Execute(() =>
        {
            foreach (var frable in GetFrables())
                frable.Blurp();
        });
        
        Trace.WriteLine(String.Format("Blurping frables took {0} ms", millis.ToString()));
    }

(Or one could use an actual profiler.)
