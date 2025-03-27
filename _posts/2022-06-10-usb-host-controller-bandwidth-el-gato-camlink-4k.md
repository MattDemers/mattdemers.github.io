---
title: "Explaining USB Host Controller issues (to troubleshoot El Gato Cam Links)"
date: 2022-06-10
categories: 
  - "tutorial"
tags: 
  - "cam-link"
  - "el-gato"
  - "hardware"
  - "streaming"
coverImage: "pexels-mart-production-8450475.jpg"
---

Today I had to talk to someone about streaming and Open Broadcaster Software. In the process I kind of came up with a metaphor on the spot about USB bandwidth when it comes to using devices like the El Gato Cam Link.

When you're dealing with setups involving Cam Links, I find that this concept is the thing that’s hardest to wrap your head around (especially for tech-disinclined people) because it requires a bit of abstraction. The usual devices they might use, like USB Flash Storage, “just work” and rarely output enough data to either slow down or stop functioning entirely.

However, the Cam Link and other devices (like VR Headsets) _do_ end up transferring massive amounts of data; for a USB capture card, it’s also trying to do that continuously, in real time.

A **USB Host Controller** handles some or all of the USB ports on your computer. If your computer has multiple Host Controllers, they will usually be assigned to groups of ports (like a group on the front panel of your computer, or the back).

I refer to these as **funnels**.

A Cam Link or another data-heavy device is pouring data (or **water**) through the **funnel** (your USB ports and controllers) to a final **container**, which is OBS, Premiere Pro, or other software.

If your water is flowing faster than the funnel can drain it into the container, the funnel is going to overflow. No one wants that.

If you have too much data going through a USB Host Controller at once, or too many devices competing for bandwidth, your devices aren’t going to perform as you need them to. No one wants that.

Your choices to fix this are:

- **Shrink the amount of water you need to drain** — change the camera settings to modify the resolution or bitrate of the video coming out of it. This means going from 4K video to 1080p or 720p, or 60Mbit/s bitrate to 30Mbit/s or 15Mbit/s. Each one of these changes will affect how much data is trying to be squeezed through the USB Bandwidth.
- **Split the water between multiple funnels you already have** — plug different devices into different host controllers to balance the bandwidth needed. For instance, since all my regular peripherals (mic, keyboard, mouse, memory) go through my PC’s back ports, I plugged my Cam Link into the front set, which has a different budget of bandwidth.
- **Buy more funnels** — USB Host Controllers can be bought and added to a computer to get more bandwidth. They look like this or this \[affiliate links\].

This water-funnel-container metaphor really seemed to work for the person I was talking to, and I think it’s a helpful summary of what was the hardest part of troubleshooting my Cam Link issues.

I hope it helps you, too.

_Image credit: MART PRODUCTION_
