**Chromium and Chromium-based Browsers**

Switching to Chromium was what finally made this feel
like a "real phone" for me. Chromium is so much
more fluid and responsive than any other browser I've
found for postmarketOS, and having a working browser
means that you have access to PWAs (progressive web
apps) which help to fill the current application gap
on Linux phones. I made several configuration changes
to Chromium to optimize it for mobile, I hope you can
benefit from some or all of them.

---

***Tested version***

The official Chromium apk (Alpine Linux apk, not to be
confused with Android apks) version 140.0.7339.185.
I can't guarantee how long these changes will be valid,
but they should be good for a while at least.


***Window Size: Make the app fit on screen***

You'll need to do this in order to use Chromium at
all, unless you set the device scale to something
absurdly small and hard to read. My GNOME scale is 272%.
Essentially, you need to lauch Chromium with a scale
smaller than this value in order for the minimum window
width to fit on screen. I did this by forcing it back
into X11 rendering mode, where there exists a flag to
change the UI scaling. Copy chromium.desktop from
/usr/share/applications to ~/.local/share/applications
and edit the Exec= lines to add the flags
"--enable-features=UseOzonePlatform --ozone-platform=x11 --force-device-scale-factor=2.25"
You may also need to increment the
version number in the config file in order to get GNOME
to pick up the override. I had no end of trouble making
GNOME recognize my changes. If you don't feel
comfortable making all these changes, try copying
chromium.desktop from this repo to
~/.local/share/applications

It may not work if Chrome changes something, but it's
worth a shot at least.
You may also need to tweak the scale factor, but you
should just be able to change the value from 2.25 to
something better.

***Chrome Flags***

This is vanilla, desktop Chromium running on a phone.
Needless to say the experience could use a little
help. Here's what I've changed in chrome://flags:
- Override software rendering list: enabled
- Smooth Scrolling: enabled
- Overlay Scrollbars: enabled
- GPU Rasterization: enabled
- Touch UI Layout: enabled
- Desktop PWA Borderless: enabled
- Tab Scrolling: enabled
- Enable Experimental Prediction for Scroll Events: disabled

I'm still evaluating the battery impact from enabling
GPU rasterization, but scrolling felt smoother to me.

***Extensions***

I wish Chromium had a robust way of handling tabs in a form
factor like this. It really doesn't, so I'm working on
alternatives for the time being. Currently, I've
settled on the extension **"New tab, New Window"**
which, as the name implies, opens new tabs in new windows.

***Settings***

- Appearance -> Theme = classic
- Appearance -> Page zoom = 125%
- Performance -> Memory Saver = Maximum
