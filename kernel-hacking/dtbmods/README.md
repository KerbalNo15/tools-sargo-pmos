**Rapid DTB iteration**

See disclaimer in the kernel-hacking folder.

These shell scripts will help you quickly iterate if you're working on DTB improvements. I got sick of compiling the kernel every time
I made a change. This cuts turnaround time from ~20 minutes to under two minutes, depending on how quickly your phone boots. To use
it, copy updatedtb-phone.sh to your home directory on your phone, and put updatedtb-pc.sh somewhere convenient on your computer.
You'll need to make some changes to updatedtb-pc.sh. Open it up and fill in the fields in <angle brackets>, namely your username on your
phone and the phone's IP address on an interface which
- Has a stable IP address across reboots
- Auto-connects on boot
- Permits SSH access

I use my wifi adapter.

***Intermission***

Now would be a great time for me to tell you that this entire tool is a terrible idea. You're essentially testing
your hardware definitions in prod and you have no backup. If you mess up the dtb file and the phone doesn't boot, you will literally
have to boot from fastboot with "pmbootstrap flasher boot" to get a working kernel and undo your changes. That being said, I don't find
such an eventuality terribly inconvenient.

***Intermission Over***

Now you need to get the kernel sources. Considering that it'll probably be helpful later, I recommend you do this with pmbootstrap.
Install it if you haven't already. [Here's a link](https://gitlab.com/sdm670-mainline/linux) to the kernel repo if you'd rather not deal
with pmbootstrap. Assuming you do use pmbootstrap, run "pmbootstrap init" and follow the prompts to set up for google-sargo. 
Write down the location you chose for pmbootstrap to store its cache. Then run "pmbootstrap build linux-postmarketos-qcom-sdm670 --force"
to download the kernel zip (this zip will be smaller than downloading the repo, since I think they don't include the .git directory in
the tarball download.) You can stop the build once it gets to the actual kernel build, unless you want to have a working build as a
backup for if the device doesn't boot. Now that the kernel zip is downloaded, you can find it in the pmbootstrap cache directory under
init_location/cache_distfiles/linux-sdm670-version.tar.gz

Copy that to a working directory somewhere (probably with updatedtb-pc.sh that you downloaded earlier) and extract it.
Now, in updatedtb-pc.sh, update LINUXROOT= to be the full path to the linux kernel src root. 
Run "make menuconfig" to get the kernel config menu. You don't need to change anything (I think). Simply exit out and save your changes
to get a .config file written.
The first dtb build you should really do yourself, since the kernel build system will ask you a bunch of questions that you need to
answer for the first build. Run "ARCH=arm64 make dtbs" from the kernel root dir and chose defaults **EXCEPT** Qualcomm Platforms (ARCH_QCOM)
which you **MUST** choose "y" for. This is one of the first questions, under Platform Selection.
You can pick defaults for the rest of the options (I think). Yes, I know it's a lot of options. You only have to do this once and you can
hold down the return key. I'm not a dtb expert, but it seems to work fine with no changes other than to enable Qualcomm (so that those
dtbs build.)

Almost done. I recommend you copy your SSH public keys to your phone with "ssh-copy-id" to save yourself some password prompts, but
it's not strictly necessary.

After that's done, you should be able to run the PC script. It will (re)build the dtb files, copy the google-sargo dtb to the phone,
and prompt you for administrator credentials to install it and reboot. For your convenience, the main SOC dtb is located in
arch/arm64/boot/dts/qcom/sdm670.dtsi though there are others specifically for the phone itself - search for "sargo" in that folder.

I've experimented with GPU frequency targets to try and improve responsiveness. You can work on whatever you'd like, of course.
I hope that someday the fingerprint sensor works, as well as the camera focus motor; I don't know whether those need work to be done
on the DTB or not.


***The DTB File in this Repo***
May be outdated when you find it! Don't just install it! At the time of writing, the main changes from upstream are:
- I'm trying to get QSEECOM working, so that I can get the fingerprint sensor driver working, so that I can hack support into fprintd.
As of right now, it does not work. In fact, it may be worse off than the unmodified DTB.
- The GPU frequency targets have been adjusted. The lowest clock is 125MHZ, much lower than stock. Importantly, it has an intentionally
restrictive max kbps at that frequency level. The intention of this is to have the GPU drawing less power to render static content, but
immediately boost out of that power level once things start happening on screen. The next power level is 190MHZ, 10MHZ above the stock
base clock speed. After that, it immediately boosts to 320MHZ, then 355, then 430. GNOME shell on mobile takes too much GPU muscle to
be stuck with the stock clock targets, unfortunately (imo; you might think it's fine.)

If you do want to install it, just put it in the same directory as updatedtb-phone.sh and run that script as root. It will overwrite the
dtb in the boot directory and update the boot image. This script reboots your phone, make sure to save your work. If you want to go back
to stock, **You will need to make a backup of the stock dtb or reflash the kernel with pmbootstrap**.