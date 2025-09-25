Feedbackd Notification Connector:
Intercepts user D-bus notifications and triggers vibration
using feedbackd. Modify the python script to adjust the
vibration pattern or the type(s) of notifications which
trigger vibration. This is a "works on my phone" script,
I've set it to work with notifications from Telegram
Desktop since that's what I really care about. You could
deactivate the service and run the python script manually
to figure out what the correct recognition string looks
like for your notification. It should print out a string
every time a notification comes through. Note that this is
user-specific, so you will need to install it for every
user on the phone (not that I know of anyone who would be
in this situation.) Test it with
'notify-send "Test notification" "This is a test"'
