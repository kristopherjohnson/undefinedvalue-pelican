Title: Pretty-formatting XML in C#
Date: 2011-11-17 22:13:28
Category: Blog
Slug: pretty-formatting-xml-c
Alias: 2011/11/17/pretty-formatting-xml-c/
Tags: xml, c#, .NET


I had a need to convert an XML string to a nice, indented format.  It was a little more complicated than I expected, so I'm posting this snippet here where I can find it again when I need it.

    using System;
    using System.Text;
    using System.Xml;
    using System.Xml.Linq;

    static string PrettyXml(string xml)
    {
        var stringBuilder = new StringBuilder();

        var element = XElement.Parse(xml);

        var settings = new XmlWriterSettings();
        settings.OmitXmlDeclaration = true;
        settings.Indent = true;
        settings.NewLineOnAttributes = true;

        using (var xmlWriter = XmlWriter.Create(stringBuilder, settings))
        {
            element.Save(xmlWriter);
        }

        return stringBuilder.ToString();
    }

Note that this method can throw exceptions for a variety of reasons.

