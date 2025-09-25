#!/bin/sh
cp feedbackdnotifications.service ~/.config/systemd/user
sudo cp feedbackdnotifications.py /usr/local/bin
systemctl enable --user --now feedbackdnotifications
