Title: Simple NSMachPort Example
Slug: simple-nsmachport-example
Date: 2017-07-08 22:35:49.999501
Category: Blog
Tags: macos cocoa nsmachport ipc

I recently had a need to use [NSMachPort][https://developer.apple.com/documentation/foundation/nsmachport) for some interprocess communication on macOS.  However, these days it is hard to find examples of how to use it in any of Apple's official documentation, as they are steering everyone toward [XPC services](https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingXPCServices.html) and [NSXPCConnection](https://developer.apple.com/documentation/foundation/nsxpcconnection) for "secure" sandboxed IPC.

So, I wrote my own simple example code for NSMachPort.  If you need it, you can find it at <https://github.com/kristopherjohnson/KJMachPortServer>.
