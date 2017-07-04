Title: .NET Event Logging
Date: 2007-09-20 19:49:00
Category: Blog
Slug: net-event-logging
Alias: 2007/09/20/net-event-logging/
Tags: dotnet


<p>
(Nobody else will care about this.  Move along.  Nothing to see here now.  Maybe I'll clean this up for public consumption later.)
</p>
<p>
After spending way too much time figuring out how to change the name of a custom event log my .NET-based service was writing messages to, I decided I need to save the snippet of code that finally worked.
</p>
<p>
For more info about the confusing world of .NET's EventLog class, see <a href="http://www.informit.com/guides/printerfriendly.aspx?g=dotnet&seqNum=238">http://www.informit.com/guides/printerfriendly.aspx?g=dotnet&seqNum=238</a>.
</p>
<pre>
namespace BlahBlahBlah
{
    class Log
    {
        // Lots of stuff left out here.
        // ...

        private static EventLog eventLog = null;

        private static readonly string eventSource         = "My Service";
        private static readonly string eventLogName        = "My Log";
        private static readonly string eventLogMachineName = ".";  // local
        
        /// <summary>
        /// Initializer for Log class
        /// </summary>
        static Log()
        {
            // Register this event source if necessary
            try
            {
                bool needCreate = false;
                if (EventLog.SourceExists(eventSource))
                {
                    string logName = EventLog.LogNameFromSourceName(eventSource,
                                                                    eventLogMachineName);
                    if (logName != eventLogName)
                    {
                        EventLog.DeleteEventSource(eventSource);
                        needCreate = true;
                    }
                }
                else
                {
                    needCreate = true;
                }

                if (needCreate)
                {
                    EventLog.CreateEventSource(eventSource, eventLogName);
                }
            }
            catch
            {
                // Ignore failure
            }

            // Initialize our EventLog instance
            try
            {
                eventLog = new EventLog(eventLogName, eventLogMachineName, eventSource);

                // Ensure our event log has the "overwrite as needed" setting
                eventLog.ModifyOverflowPolicy(OverflowAction.OverwriteAsNeeded,
                                              eventLog.MinimumRetentionDays);
            }
            catch
            {
                // Ignore failure
            }
        }

        // Lots more stuff left out
        // ...
    }
}
</pre>
