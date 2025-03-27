---
title: "Tutorial: Using Twitch automation with IFTTT"
date: 2017-02-22
categories: 
  - "tutorial"
tags: 
  - "automation"
  - "ifttt"
  - "twitch"
coverImage: "twitch_automation_banner.png"
---

I've written about automation earlier with social media, but I got some great news today when IFTTT ("If This, Then That") added Twitch integration to its list of supported apps. Like Zapier, the service I used for Discord automation, IFTTT follows a simple formula:

1. Pick a trigger to activate your applet
2. Once triggered, have your applet perform an action

Today's announcement means that Twitch has been added to step #1: you can now use Twitch events to trigger actions. Currently there **are not** actions that you can perform with Twitch; I'd love for them to add the functionality to post to your Twitch Channel Feed, because it would enable some better uses of that.

Anyways.

Here are the Twitch events you can use to trigger actions:

1. Stream going live for a channel you follow
2. New stream started by you
3. New video posted by a channel you follow (any, highlights or broadcasts)
4. New video posted by you (any, highlights or broadcasts)
5. You follow a new channel
6. A user followed a channel
7. New follower on your channel
8. New top video of the week

While this is pretty versatile, it doesn't cover all the same things that Streamlabs does: for instance, have someone subscribing to you be a trigger.

So, what are you looking to do with these?

The thing is, IFTTT's supported apps are pretty deep, and at this point the actions you can take with your trigger depends on what your aim is. If you're a streamer, this is a great way to cross-promote things, as you can hook up your Twitter, Facebook Page or anything else to post automatically when your stream goes live.

What I would _not_ recommend, however, is posting every time someone follows your channel. This will get extremely spammy and annoying quickly, and also has the problem of the message being posted looking identical. I would also caution **against** tweeting out something automatically when you go live, as, again, the message is going to be the same. You want to be able to promote yourself by being organic and authentic.

For secondary social media platforms, though (say, Facebook), the automated message makes sure you get some coverage where you might normally forget. The same is true with Twitch videos: tweeting a generic message when you say, make a new video highlight, means you're less likely to forget.

![](/assets/images/IFTTT_banner.png)

The custom part of this dialog is pretty important, as it allows you to add **ingredients**, which are variables that change every time you perform the action. In this case, the video title and URL are going to be unique every time, so they need to be slotted in appropriately. An example of this would be for a Facebook page, where you could craft something a little more unique:

![automation](images/IFTTT_2.png)

From here, the possibilities are kind of up to you: do you use Twitter to send out messages? Facebook to send out posts? Do you post unique messages to Slack or schedule posts with Buffer? Hell, if you really wanted to you can turn your lights off when you went live if you used a supported lightbulb, or turn on a wifi-enabled oven.

The lovely part of IFTTT is that it doesn't limit your actions to what is logical: you just choose from their list of supported apps, and go from there. IFTTT also has custom recipes that other people have posted, which can give you inspiration as to how to use the tool further.

![](/assets/images/chrome_2017-02-22_21-55-49.jpg)

Best of luck, and let me know in the comments how you end up using it! You can also view my guide on automating Discord for more ideas.
