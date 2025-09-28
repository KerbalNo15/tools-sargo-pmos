**How to get VoLTE Working**

***What is VoLTE?***

Simply put, it's an improved way of handling calls. As 2G and 3G networks get deprecated, more and more carriers are requiring support for VoLTE in order to make
and receive phone calls. This is an issue for the open source community, since VoLTE support is not very good at the moment. We are slowly building up an
ecosystem of tools for handling VoLTE support on Linux. What follows is a summary of the most helpful information I found on the topic.

***The high-level control flow***

Something that doesn't seem to be well-understood is that the modem is actually responsible for enabling VoLTE. It's not some sort of userspace VOIP implementation.
There is some amount of configuration that needs to be handled in userspace, but
it's not nearly as bad as it looks. On Qualcomm devices (like the Pixel 3a), The modem is the primary responsible party for handling VoLTE. With the advent of
the 81voltd (please don't stop reading, I promise it works,) VoLTE support is almost a plug-and play experience on postmarketOS. If some conditions are satisfied.
They weren't for me, and they might not be for you either; trying to troubleshoot what's wrong is a nightmare. There's very little documentation yet. What finally
made everything click was finding [This issue on Gitlab](https://gitlab.com/postmarketOS/pmaports/-/issues/1878). MEGA THANK YOU to Dylan for taking the time to
write down everything in a much better way than I could (but please keep reading.) If you enabled 81voltd, put your SIM in your Pixel, and nothing happened- This
was my experience too. Here's why: The modem (probably) doesn't have a VoLTE profile installed for your carrier. You can actually check! Per Dylan,
you can run this command to list the installed profiles on your modem:

    qmicli -p --device=qrtr://0 --pdc-list-configs=software

If you see your carrier listed, but the profile doesn't have VoLTE in the description, it probably won't work. Dylan has commands in that thread that may work to
install new profiles; unfortunately, when I tried this qmicli segfaulted.

***What you actually need to do***

If you didn't test phone calls before flashing postmarketOS:
This used to be an issue with Android ROMs back in the day! If you remember when ROMs would instruct you to make sure VoLTE works on your phone BEFORE installing
the ROM, this may have been the same issue. Stock Android had the tools to install new profiles on the modem, and it does so automatically.

I flashed stock android back to the phone. After the initial setup, put "\*#\*#4636\*#\*#" into the dialer. This brings up a debug menu. Click the top option, labeled
something like "Phone information", and you can see all the debug information for the SIM and radio. Click the menu button in the top right corner, and click
"IMS Service Status". Make sure that "Voice over LTE" says "Available". If it doesn't, go to SIM settings in the Settings app and make sure that VoLTE is turned on.
You could toggle it off and back on again to make sure, and make a test call to be extremely confident.

Now you can flash postmarketOS again, and you should have working VoLTE for calls after "systemctl enable 81voltd" and a reboot.

***If this phone used to be your daily driver***

You might have a different issue. If you're sure you used to be making VoLTE calls before flashing postmarketOS, this guide might not help you. I don't really know
where to start in that case, but I would check that the profile is missing from the modem before wiping out your data to try this method.