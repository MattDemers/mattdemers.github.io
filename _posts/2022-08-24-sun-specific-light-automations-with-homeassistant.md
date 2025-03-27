---
title: "Sun-specific light automations with HomeAssistant"
date: 2022-08-24
categories: 
  - "tutorial"
tags: 
  - "automation"
  - "homeassistant"
header:
  image: "/assets/images/homeassistant_automation_sunrise_sunset_tutorial.png"

layout: single
author: "Matt Demers"
author_profile: true
read_time: true
comments: true
share: true
related: true
---

Hey all; this one's going to be a little bit of a departure from a lot of my content, but I couldn't exactly find a resource for this problem online and I figured I should fix that.

I use HomeAssistant as an open-source, self-hosted alternative to a number of "Internet of Things" or smart-home devices. It allows me to set up automations based on these devices, and other things like weather, timing, and location. It kind of works like IFTTT or Zapier in that regard, except I don't have to pay for a premium account and I keep all the data private.

I've set up automations for the lights in my ceiling, which change from a brighter white colour to a more warm orange colour at sunset. This is to protect my eyes a bit; I don't know if it actually does anything, but it's nice to think it does.

Below are the automations I've put together for them. I had to split it into four separate ones:

- A pair for "Light is already on and the sun sets or rises, so change the lights"
- Another pair for "Light is turned on, and the sun is above/below the horizon"

What confused me for a while was the semantics of these automations; HomeAssistant has a "Sunrise/Sunset" trigger, but this is something that is "watched for" and then acted on when it happens. This means if my lights were off at the time of sunrise/sunset, and were meant to _stay off_ until I turned them on, nothing would change (since the event of rise/set had already passed).

Instead, I needed to focus on the `state` of the `sun` entity in order for HomeAssistant to make the decision based on where the sun _currently was_, instead of the change that was made at one time.

#### Important Note

If you're more knowledgeable about HomeAssistant than me, please leave me a comment correcting my process. Like I said, I'm mostly acting on what hasn't worked in the past; if the "before Sunrise, after Sunset" radial buttons are supposed to work, they aren't for me.

## Creating a scene

Before we create the automations, we need to create a scene for them to change to. You can go to `Configuration > Automations & Scenes` in HomeAssistant, and then the `Scenes` tab.

![](/assets/images/brave_VkCDuRuG1k-1024x716.png)

As you can see, a new scene has fields for the name and the icon associated.

The "Devices" field lets you add your lights (as I have here).

However, to save the scene, you must click on the icons to the right of the name (in this case, lightbulbs) and set up those bulbs how you'd like them to be in the scene.

![](/assets/images/brave_1yPVZOskNP.png)

In this case, I would move my "Color Temperature" slider to a warmer colour if I'm going to be making a "Sunset" scene. Once that's finished for all the bulbs, save the scene. Also important to note is that my ceiling lights are a group of two.

## Change scene if light is already on at sunset/sunrise

I figure the easiest way to do this is to display the screenshots of my automation, along with the YAML code, just in case.

### Automation YAML

```
alias: Office lights change at sunset
description: ''
trigger:
  - platform: sun
    event: sunset
    offset: 0
condition:
  - condition: device
    type: is_on
    device_id: DEVICE ID
    entity_id: ENTITY ID
    domain: light
action:
  - service: scene.turn_on
    target:
      entity_id: SCENE GOES HERE
    metadata: {}
mode: single
```

I've scrubbed my Device ID, Entity ID and Scene ID from the above.

### Automation on the Visual Editor

I'm going to type out the fields and how I've filled them out, rather than a big screenshot.

**Name**: Duh.  
**Mode**: Single (Default)

_Triggers_:

**Trigger Type**: Sun  
**Event**: Sunset

_Conditions_:

**Condition Type:** Device  
**Device**: \[Light 1\] (whatever you have one of your bulbs named)  
**Condition**: \[Light 1\] is on

_Actions_:

**Action type**: Activate scene  
**Entity**: \[Scene I made earlier\]

## Change scene when turning on the lights, depending on after sunset or sunrise

#### Important note

I've realized as I'm writing this that I have a dimmer switch, also on my HomeAssistant system, and this might be atypical of a setup.

I have the dimmer switch because I ran into an issue of using the trigger "when lights turned on" because the lights may not have enough time to be connected to power after being switched on, connect to the wifi, and report that they've been turned on to HomeAssistant.

My solution was to "always have them 'on', but have their brightness be controlled by a dimmer switch." They are technically always connected to power, but their brightness is turned to 0 (turned "off") yet are still recognizable by HomeAssistant.

### Automation YAML

```
alias: Office after Sunset
description: ''
trigger:
  - device_id: DEVICE ID
    domain: 
    platform: device
    type: initial_press
    subtype: 1
    unique_id: 
condition:
  - condition: state
    entity_id: sun.sun
    state: below_horizon
action:
  - service: scene.turn_on
    target:
      entity_id: SCENE ID
    metadata: {}
mode: single
```

I've scrubbed my Device ID, Entity ID and Scene ID from the above. Again, (from the green box), the Trigger is a bit different because it's using the setup I've described; my lights are never truly "off", just turned to "Brightness = 0"; this means they can communicate with HomeAssistant.

### Automation on the Visual Editor

I'm going to type out the fields and how I've filled them out, rather than a big screenshot.

**Name**: Duh.  
**Mode**: Single (Default)

_Triggers_:

**Trigger Type**: Device  
**Device**: My dimmer switch  
**Trigger**: Button "first button" pressed initially

_Conditions_:

**Condition Type:** State  
**Entity**: Sun  
**State**: below\_horizon

_Actions_:

**Action type**: Activate scene  
**Entity**: \[Scene I made earlier\]

Some explanation:

- I've tried to use the Condition Type "Sun" before; it would have you choose that the condition would be "Before Sunset/Sunrise" and "After Sunset/Sunrise", but I've found this to be a bit inconsistent, or sometimes doesn't work. I don't have a reason for that, and people are free to correct me.
- Instead, I've used HomeAssistant's **entity** for the sun, called `sun`, which has a binary state that's called `above_horizon` or `below_horizon`. I figure this works, because I just need to query what state it's in: one or the other.
- To invert this automation, you'd type in `above_horizon` for pre-sunset, or daytime.

## Closing

My second automation can be tweaked in order to have different triggers, but I've found this one is the best. I could've had it be triggered by "when \[Light\] is turned on" instead of "when I hit a button on my switch"; this would prevent the automation from not firing if I used my phone to turn on/off the lights.

I realize this is a bit of a niche tutorial, but it's what worked for me. This is probably one of the simplest usecases for HomeAssistant, and I found it difficult to search and experiment to get to this point; this isn't an indictment of the product or community, but with these kind of products, there's always room for more resources and clarity.

Cheers!
