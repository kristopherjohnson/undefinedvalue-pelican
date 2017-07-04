Title: Creating .NET Remoting IPC Channels
Date: 2011-12-14 14:36:55
Category: Blog
Slug: creating-net-remoting-ipc-channels
Alias: 2011/12/14/creating-net-remoting-ipc-channels/
Tags: remoting, .NET


Yet another C# code snippet.  I'm developing a service and an accompanying UI that always run on the same physical box, and it was suggested that I implement the communication between them using .NET Remoting and the _IPC_ channel type, which is a supposedly-easy way to get processes on the same machine to talk to one another.

Of course, it wasn't easy, because if you simply create and register an `IpcChannel` with default parameters, you get security-related exceptions when you try to do anything with it.  You have to delve through documentation and online forums to figure out what underdocumented magic is required to get the stuff to actually work.  

There were two obstacles I had to overcome:

- By default, user-defined types will not be deserialized, to prevent deserialization-based attacks by malicious clients. To disable this "feature", one must set the `TypeFilterLevel` to `Full`.
- My service runs as the LocalSystem user, whereas the client application runs in the logged-in user's security context. By default, the user's account would not be able open the IPC port that the service creates. The fix to this is to set the channel's `authorizedGroup` to the name of a user group that is allowed to open the port.

So, as usual, the resulting code looks simple, but it took a couple of hours to figure out what had to be written.
<!--break-->
Here's the code, which is intended to work on .NET Framework 2.0 and higher on Windows XP and newer operating systems:

<script src="https://gist.github.com/3047562.js?file=IpcRemotingUtil.cs"></script>

On the server side, I use it like this:

    var channel = IpcRemotingUtil.CreateIpcChannel(MyServer.IpcPortName);
    ChannelServices.RegisterChannel(channel, true);

    var entry = new WellKnownServiceTypeEntry(
        typeof(MyRemoteObject),
        "MyRemoteObject.rem",
        WellKnownObjectMode.Singleton);
    RemotingConfiguration.RegisterWellKnownServiceType(entry);

And on the client side, I use it like this:

    var channel = IpcRemotingUtil.CreateIpcChannelWithUniquePortName();
    ChannelServices.RegisterChannel(channel, true);

    var objectUri = String.Format("ipc://{0}/MyRemoteObject.rem",
        MyServer.IpcPortName);
    var remoteObject = (MyRemoteObject)Activator.GetObject(
        typeof(MyRemoteObject), objectUri);
    try
    {
        remoteObject.FooBarAndBaz();
    }
    catch (Exception ex)
    {
        // aaaiiiyyyeee
    }

Note that both sides use `IpcChannel` so that the server can invoke callbacks in the client.  If you don't need callbacks, you could use `IpcServerChannel` and `IpcClientChannel` instead of `IpcChannel`.  If you do that, you need to make sure you set the `TypeFilterLevel` and `authorizedGroup` on the `IpcServerChannel` as is done above for the `IpcChannel`.
