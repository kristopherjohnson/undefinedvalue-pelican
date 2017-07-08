#!/usr/bin/env python3

"""
Creates a new post.

Given a title, creates a new Markdown file with appropriate front-matter
in the appropriate subdirectory.

If the EDITOR environment variable is set, then the editor will
be opened to edit the new file.
"""

from sys import argv, exit
from datetime import datetime
from jinja2 import Template
import os
import os.path
import re

postTemplate = """Title: {{ post.title }}
Slug: {{ post.slug }}
Date: {{ post.created }}
Category: Blog
Tags: untagged

TODO: Set Tags above, then Write the post.

"""

def slugify(title):
    """Converts title to a valid filename."""
    title = (re.sub('[^\w\s-]', '', title).strip().lower())
    title = re.sub('[-\s]+', '-', title)
    if len(title) == 0:
        raise ValueError('cannot slugify that title')
    return title

def create_new_post(title):
    slug = slugify(title)

    now = datetime.now()
    yearString = "%04d" % now.year
    monthString = "%02d" % now.month
    dayString = "%02d" % now.day

    post = {
        "title" : title,
        "created" : datetime.now(),
        "slug" : slug
    }
    template = Template(postTemplate)
    renderedText = template.render(post=post)

    dirpath = os.path.join('.', 'undefinedvalue', 'content', yearString, monthString, dayString)
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)
    filepath = os.path.join(dirpath, slug + '.md')
    with open(filepath, 'w') as f:
        f.write(renderedText)

    print(f"Created {filepath}")

    editor = os.getenv('EDITOR')
    if editor:
        os.system(f"{editor} {filepath}")

def main():
    if len(argv) < 2:
        create_new_post(input("Title> "))
    else:
        for arg in argv[1:]:
            create_new_post(arg)

if __name__ == "__main__":
    main()

