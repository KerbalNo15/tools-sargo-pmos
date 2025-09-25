#!/bin/python3
from gi.repository import GLib as glib
import dbus
import os
from dbus.mainloop.glib import DBusGMainLoop
print("XDG_RUNTIME_DIR =", os.getenv("XDG_RUNTIME_DIR"))
print("DBUS_SESSION_BUS_ADDRESS =", os.getenv("DBUS_SESSION_BUS_ADDRESS"))

def notifications(bus, message):
    print(message)
    #if(message == "<dbus.lowlevel.MethodCallMessage path: /org/freedesktop/Notifications, iface: org.freedesktop.Notifications, member: Notify dest: :1.30>"):
    os.system("busctl call --user org.sigxcpu.Feedback /org/sigxcpu/Feedback org.sigxcpu.Feedback.Haptic Vibrate 'sa(du)' org.foo.app 3 1.0 250  0.0 200  1.0 250")
DBusGMainLoop(set_as_default=True)

bus = dbus.SessionBus()
bus.add_match_string_non_blocking("eavesdrop=true, interface='org.freedesktop.Notifications', member='Notify'")
bus.add_message_filter(notifications)

mainloop = glib.MainLoop()
mainloop.run()
