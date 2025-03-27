---
title: "Writers, here's why you should learn Markdown"
date: 2015-12-21
categories: 
  - "tutorial"
tags: 
  - "blogging"
  - "coding"
  - "markdown"
  - "writing"
coverImage: "pexels-burst-374720.png"

layout: single
author: "Matt Demers"
author_profile: true
read_time: true
comments: true
share: true
related: true
---

As a writer, I’ve become painfully aware that we don’t get many “toys.” Artists have stores devoted to different tools of their trade, while we have… keyboards — maybe some fancy notebooks.

Over the past couple years I’ve come to appreciate Markdown as something that makes my writing more efficient and better for the web. Markdown is a language that parses formatting a lot easier, and makes it simpler to type in code.

Why is this important, you might ask?

Let’s put it this way: the less time you have to worry about how a post is going to look on a site when you’re done with it, the more time you have to work on actually relevant things. Markdown lets you write in plain text to avoid all the stupidity that comes from copy/pasting from a Word or Google Docs document, and lets you control **exactly** what shows up while being easier to type than HTML.

The other thing about Markdown is that if you use Reddit, you’ve already used it: apart from some syntax that Reddit doesn’t like (namely, inline images), Markdown is the main tool for post formatting.

I simply like it because it minimizes the amount of keystrokes you need to do something, and because it allows me to make posts with confidence, instead of needing to worry about what will copy over.

If you want to make text bold in Markdown, you would surround that texts with two asterisks on either side. In HTML, you would need to type out `<strong>` tags on each side, and remember to close. Four keystrokes for Markdown (all the same key) versus 17 for HTML.

`**Bold text**`  
vs  
`<strong>Bold text</strong>`

Simple, right?

This gets even better when you either work with a CMS (like Anchor, which this blog uses) that supports Markdown; since the syntax is easy to remember, you can craft a whole post in Notepad and then just copy-paste it over. On CMS’ like WordPress, there are tools (like Showdown & Highlight) that will quickly convert your Markdown to crisp, clean HTML, so you can post it to the source.

![](/assets/images/pNSqOnR.png)

The above paragraph, in Markdown.

### Limitations

Like any other system, there are going to be some drawbacks with Markdown. The main things for me are **images** and **HTML options**.

Images, since they aren’t being integrated into your CMS, need to be added in WordPress, or hosted somewhere beforehand. Since Anchor’s image system doesn’t work very well, I host all the images for this blog on Imgur and reference them with Markdown. However, because of the next problem, I need to make sure they’re the exact dimensions to show up properly on the blog.

HTML options like `<a href="http://google.com/" target="blank"></a>` or `<img src="http://i.imgur.com/008NFf8.gif" width="100%"></img>` aren’t possible in Markdown, so you need to go in and manually do them. It’s nice, because any HTML you add to a Markdown document will be translated as normal, but if you’re counting on your CMS to do this stuff for you, you may have to do some memorization.

These shortcomings don’t really keep me from writing every post I do in Markdown, because there’s just a good feeling in knowing that what you write down is what’s going to show up. If you press Enter twice to get to a new paragraph, you will know that it will be surrounded by the proper `<p>` tags, instead of two `<br />`‘s.

While that last bit sounds _ultra_ nitpicky, it’s something that tends to _matter_ when you want your blog or site to look consistent and work across multiple platforms.

I’m a big fan of Tinyletter for newsletters, and one of the things a friend brought up to me was that the editor was absolutely **terrible** for inputting text. Every “Enter” press would be a line break, not a new paragraph, and it could break depending on the platform viewed. With Markdown, I **never have to worry about how bad a CMS’ editor is, as long as I can paste HTML somewhere**.

This kind of freedom helps so much when it comes to knowing I can write anywhere, and have what I format carry over with no questions asked.

If you’re a writer or blogger, I really urge you to learn Markdown. It _will_ speed up your writing, and give you a degree of control that you probably never knew you valued until it’s taken away. Go nuts.

### Word editors that support Markdown:

MarkdownPad is a free Windows program that I use and love. The paid version will even upload images to Imgur for you and fetch the link to use automatically.

Byword for OSX ($5.99) does many of the same things as MarkdownPad, but allows for greater syncing with Dropbox.

Markdown support can be added to Sublime Text for people who use that in their day-to-day.

Showdown & Highlight is a simple Javascript port of Markdown, and is amazing for beginners because the right pane can show you a cheat sheet, a preview of what your text looks like, or the HTML code for easy copy/pasting. Great for converting Markdown to HTML for your blog, if nothing else; doesn’t allow saving, though.

Dillinger.io takes elements of Showdown & Highlight and allows you to save/sync with Dropbox, which might be useful for people on the go. A bit more difficult to get the HTML conversion of a post, though, so I don’t really like it.
