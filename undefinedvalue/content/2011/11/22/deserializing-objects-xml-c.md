Title: Deserializing Objects from XML in C#
Date: 2011-11-22 15:22:03
Category: Blog
Slug: deserializing-objects-xml-c
Alias: 2011/11/22/deserializing-objects-xml-c/
Tags: xml, c#


Here's another C# code snippet that takes me way too much time to recreate by just reading the documentation. 

This is a simple example of a class that can be serialized to/from XML.  In this case the "ServerConfig" XML string can contain a list of servers, looking like this:

    <ServerConfig loggingEnabled="1">
      <Servers>
        <Server host="test1.example.com" port="9999" />
        <Server host="test2.example.com" port="8888" />
      </Servers>
    </ServerConfig>

The client code can just do "`var serverConfig = ServerConfig.FromXmlString(s);`" to deserialize it into a `ServerConfig` object.

<script src="https://gist.github.com/3227483.js?file=XmlDeserializationExample.cs"></script>

(The method that would serialize a `ServerConfig` to an XML string is left as an exercise for the reader. I rarely need to do that.)
