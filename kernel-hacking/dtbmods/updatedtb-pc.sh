#!/bin/bash

LINUXROOT=/home/<username on PC>/linux-sdm670-v6.16.3
DEVICEIP=<phone IP address, I use wifi but any consistent IP works>
USER=<username on phone>
cd $LINUXROOT
ARCH=arm64 make dtbs
scp $LINUXROOT/arch/arm64/boot/dts/qcom/sdm670-google-sargo.dtb $USER@$DEVICEIP:/home/$USER/sdm670-google-sargo.dtb
ssh -t $USER@$DEVICEIP sudo sh /home/$USER/updatedtb-phone.sh
