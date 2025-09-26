**Easy Effects**

This application applies audio processing to inputs and outputs on the device. It's extremely helpful if you want to make the speakers sound better, for instance.
There are two versions of the app, and I would recommend the apk version. The flatpak version may or may not work, but I know the apk version does. "Works" is a
flexible term in this case. The UI is not mobile-friendly at all. You'll need to put the phone in landscape in order to use it, otherwise the top menu buttons are hidden.
 This is important because every new output device will need a profile associated to it or it takes the speaker profile by default. This
causes massively overemphasized bass since the speaker profile is optimized for tiny phone speakers. After expanding the window enough, you can click the
"pipewire" menu button to get to the presets autoloading menu. Unfortunately, I am unable to load presets at this time since the popup file picker doesn't have window
focus but closing it crashes the shell session. That is to say, figuring out how to load the preset is up to you.


***Disclaimer***

The profile I've posted here is optimized for ***audio quality**, not ***volume***. It caters to the poor bass response of the included speakers. ***I can't
guarantee that it will not cause damage to the speakers if played too loudly, nor that you'll like it more than the sound without processing. Use it at your
own risk.***

---
***Audio Crackling***

Is caused by Easy Effects. I suspect it's an issue with Pipewire latency. Might be fixed by adding a few ms of compensatory delay, not sure.
