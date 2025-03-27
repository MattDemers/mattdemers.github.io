---
title: "Tutorial: Free telestrator for Open Broadcaster Software"
date: 2015-12-11
categories: 
  - "tutorial"
tags: 
  - "broadcasting"
  - "obs"
  - "twitch"
coverImage: "pexels-magda-ehlers-1054713.png"

layout: single
author: "Matt Demers"
author_profile: true
read_time: true
comments: true
share: true
related: true
---

One system I've definitely wanted to use in analysis is the telestrator, or video marker. For those not familiar with the term, it's what sportscasters will use to take a free-frame of an instant replay and draw own it. We've seen it used by Riot Games and other eSports companies as part of a smart TV, but that can be expensive: I wanted to try to find something free and usable in a home/casual environment.

The big problem is usually making sure what you draw is visible to streaming/recording; usually, these type of programs will project a drawable layer on top of whatever you're annotating, and sometimes, depending on the capture, this can be hidden.

I've found **ZoomIt**, a freeware program, that works with Open Broadcaster Software as long as certain conditions are met. Here's how I got it working for my Dota analysis on Windows 7:

### Step 1: Download ZoomIt

ZoomIt is a freeware program created by Mark Russinovich. You can download it here on its home site, or on the mirror I made on Mega.nz.

After installing it, you should see a window like this.

![](/assets/images/tITUldD.png)

What you're looking for is under the **Draw** tab. I have the hotkey set to Ctrl + 3.

![](/assets/images/d5HCkfE.png)

From here, any time you hit Ctrl + 3, the game or window will freeze, and your cursor will turn into a drawing cursor. You can change the colour of the marker by pressing the "O", "Y", "R", "B", "G" or "P" keys on your keyboard to change to orange, yellow, red, blue, green or pink, respectively.

You can then draw on whatever you want to show off. You can hold down shift while drawing to draw a straight line, and hit ESC to erase what you've drawn. Hold down CTRL and scroll up or down on your mousewheel to increase or decrease the width of the brush. Press T and type in order to get text.

![](/assets/images/qZ22rrH.jpg)

ZoomIt essentially lives in your taskbar minimized, like similar screenshotting programs like Puush. I usually close it when it's not needed, as the hotkeys tend to conflict with others.

### Step 2: Set up Open Broadcaster Software

OBS is a software that lets you capture multiple elements and arrange them for streaming or recording. I'm assuming that you know how to use it already, as there are multiple other tutorials for setting it up.

However, the important thing here is that **whatever game you are running will need to run and be captured in windowed mode**. This includes in OBS, where you will add a source for "Window Capture", **not "Game Capture."** The good thing about this is that if it's scaled properly, most people won't know the difference, as it usually captures the Inner Window by default.

This is because when the game is in Fullscreen or Windowed Borderless mode, the game gives priority to the cursor as it behaves inside the game. However, when in Windowed mode, it allows for a greater degree of control by outside forces like ZoomIt; when you trigger your Draw command, the game will freeze and continue in the background. When you hit ESC after drawing, the game will go back to "live."

This process is likely not to work for console games streamed via capture cards, as those are piped in as separate sources to your PC, not as a window that's influenced by the Windows OS. This system would likely work on emulators, but for console play you would likely need to have recorded videos.

_**2017 Update**: This method doesn't seem to work on certain games when it comes to Window Capture; it WILL work on Display Capture, which means you can use it for YouTube/VLC.  Might just be a Windows 10 thing, so it's kind of up to you to see if it works for you._

### Step 3: Workflow for Replay Analysis

In games with replay systems like Dota 2 or Starcraft, or with videos like YouTube or VLC, the standard workflow is to pause the game where you want to annotate. Then you would draw, explain your analysis, clear the drawings with ESC, then unpause the replay/video and continue on.

**Note**: I generally recommend using VLC as a video player for VOD analysis without a replay system, as you can hit the "E" key on your keyboard to advance the video by one frame to the future. This is an improvement over loading videos up on YouTube, as they tend to lack the fine frame-by-frame control that is often necessary.

By streaming this sequence with OBS, you will be able to provide analysis of moments to your audience in either a live setting or recording for local editing.

Hopefully, this will allow for a more easy jumping-on point for those of us who want to analyze both pro and personal play. By using free tools like OBS and ZoomIt, the barrier to creating broadcasts with value to the viewer should be smaller.
