---
title: "HomeAssistant: Laundry Alarm Automation with Vibration Sensor"
date: 2024-08-31
categories: 
  - "tutorial"
tags: 
  - "home-automation"
  - "homeassistant"
  - "tutorial"
coverImage: "pexels-sinileunen-5661241-crop-laundry.jpg"

layout: single
author: "Matt Demers"
author_profile: true
read_time: true
comments: true
share: true
related: true
---

Hey all. I wanted to write a couple more basic HomeAssistant tutorials, mostly because they're a low-commitment way of making the community better; even if it helps one person, it's better than nothing.

I use HomeAssistant for a privacy-focused home automation solution; I also use it because I'm lazy, or my ADHD makes it harder to remember things. This post is a simple script/automation around a laundry alarm that notifies me when my washer-dryer has stopped running.

I live in an apartment with a combination washer-dryer, which doesn't have an alarm. It also has a booster fan (the type of fan to keep the laundry closet from getting too humid), which is way too sensitive. Previously, I'd use a power strip with an on/off switch to turn on this fan, but I felt there was a way to make it better.

With this automation:

1. The fan turns on when a vibration sensor recognizes that the washer or dryer is running

3. The fan turns off when the vibration sensor doesn't recognize a change within a certain amount of time

5. My phone gets a notification that goes through "silent"/vibration mode when the laundry is done

7. This notification doesn't go off after a certain time, so if I set the dryer to start before I go to bed, I don't get woken up

What I use:

1. I use a Third Reality 3RVS01031Z as a vibration sensor. I use this with Zigbee2MQTT, but I believe this can be paired with any Zigbee integration into HomeAssistant. There are also other models, but this one was the cheapest for my setup. The sensors it reports are real-time changes to X, Y and Z axis, but I only really use a binary "is it vibrating, or is it not?" sensor.  
      
    The vibration sensor I chose has a sensitivity switch to it, and I had to fine-tune what it felt was an active washing machine or not. I stuck the vibration sensor to my washer-dryer, and it detects when the machine is running.

3. I have a very old single Smart Socket that can be toggled on/off. The brand doesn't matter; you could use a similar power strip with WiFi capabilities. However, this is very much optional if you have a working ventilation system that doesn't need to be turned on/off, like mine.

5. I have the HomeAssistant iOS integration set up through the Companion App, so I can send notifications to my phone.

## The Automations - Turning On The Fan

I'm going to type in the YAML code for my automation, then I'll explain it a bit better. I've also replaced certain IDs with "\[obscured\]" just for privacy.

```
alias: Laundry has started
description: ""
trigger:
  - type: vibration
    platform: device
    device_id: [obscured]
    entity_id: [obscured]
    domain: binary_sensor
    for:
      hours: 0
      minutes: 0
      seconds: 20
condition:
  - condition: device
    type: is_off
    device_id: [obscured]
    entity_id: [obscured]
    domain: switch
action:
  - service: switch.turn_on
    data: {}
    target:
      entity_id: switch.smart_socket_socket_1
mode: single
```

Visually, through the HomeAssistant UI, it looks like this:

**When**: Device > My Vibration Sensor > Started Detecting Vibration > Duration (Optional): 20 sec

**And if**: Device > My Smart Socket > Is Off

**Then do**: Call Service > Switch: Turn On > Target: My Smart Socket

![](/assets/images/image-1024x767.png)

My only note here is that there is a "20 second duration" on the initial trigger because the automation would constantly fire without it. It's basically saying "If the sensor has detected a vibration for 20 straight seconds, fire the automation."

## The Automations - Turning Off The Fan and Notifying

```
alias: Laundry has finished
description: ""
trigger:
  - type: no_vibration
    platform: device
    device_id: [obscured]
    entity_id: [obscured]
    domain: binary_sensor
    for:
      hours: 0
      minutes: 2
      seconds: 0
condition:
  - condition: state
    entity_id: switch.smart_socket_socket_1
    state: "on"
    for:
      hours: 0
      minutes: 2
      seconds: 0
  - condition: time
    after: "08:00:00"
    before: "23:00:00"
    weekday:
      - fri
      - sat
      - thu
      - wed
      - mon
      - tue
      - sun
action:
  - service: switch.turn_off
    data: {}
    target:
      entity_id: switch.smart_socket_socket_1
  - service: notify.mobile_app_myphone
    data:
      title: Laundry is done!
      message: "Vibration is off for two minutes, and fan is off. "
      data:
        push:
          sound:
            name: default
            critical: 1
            volume: 1
mode: single
```

Visually, through the HomeAssistant UI, it looks like this:

**When**: Device > My Vibration Sensor > Has Stopped Detecting Vibration > Duration (Optional): 2 minutes

**And if**: Entity > Dryer Socket Fan > State is "On" > For: 2 minutes

Time > After (Fixed Time) 8:00 AM > Before (Fixed Time) > 11:00 PM > Monday Through Sunday

**Then do**: Call a service > Switch: Turn Off > My Dryer Socket

Call a service > Notifications: Send a notification via mobile\_app\_myphone > Message: "Vibration is off for two minutes, and the fan is off" > Title: "Laundry is done!" > Data: (see below)

```
push:
  sound:
    name: default
    critical: 1
    volume: 1
```

![](/assets/images/image-1-1024x623.png)

The extra `data` in the notification is to handle a Critical Notification in iOS, which will send a notification that bypasses Vibration Mode/Silent Mode on my phone. Since I keep my phone on these modes almost always, I wanted something that would notify me and make it hard to ignore.

The `critical: 1` flag makes it "urgent" and the `volume: 1` sets the volume to 100%.

From the documentation on critical alerts:

> For Android, notifications will appear immediately in most cases. However, in some cases (such as phone being stationary or when screen has been turned off for prolonged period of time), default notifications will not ring the phone until screen is turned on.
> 
> To override that behavior, set `priority: high` and `ttl: 0`.
> 
> By default they also do not override Do Not Disturb settings, if you would like to override this you will need to use notification channels.

As I don't use Android, I wouldn't want to misinform here, and I don't have a way of testing a similar notification. However, it looks like you can use the following `data` (YMMV).

```
data:
  ttl: 0
  priority: high
  channel: alarm_stream
```

## Talking through the automation

I like to "talk through" my automations just to make sure they make sense.

When my vibration sensor senses vibration for at least 20 consecutive seconds, it turns my dryer fan on. This will not fire if the fan is already on.

When my vibration sensor no longer senses vibration for 2 minutes, it will check what time it is, and that the dryer fan has been on for at least 2 minutes. If it doesn't pass these checks, it will not fire. If it passes the checks, it will send a high-priority notification to my phone, telling me the dryer is done.

The redundancy checks in both automations are there to keep them from firing over and over, or from firing if I jostle the washer/dryer for a second, am unloading clothes, etc.

## Wrapping it up

This was a fun little documentation project, and I hope you found it helpful. It isn't specific to any real system, and can be done with a combination of smart socket, vibration sensor, and phone, or optionally removing the entire dryer fan setup entirely.

If you wanted, you could just run the vibration sensor/notification aspect of it, and say "if the vibration sensor has not sensed vibration in two minutes, send a notification." For those of us who don't like the "singing" washer/dryer, or just aren't near our laundry, this gives us a way to keep on top of it.
