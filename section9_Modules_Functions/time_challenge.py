# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.
import datetime
import pytz

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

timezones = {'1': 'Europe/Stockholm',
             '2': 'Europe/Warsaw',
             '3': 'Asia/Kathmandu',
             '4': 'Africa/Tripoli',
             '5': 'Europe/Riga',
             '6': 'Asia/Kolkata',
             '7': 'Europe/Paris',
             '8': 'Europe/Brussels',
             '9': 'America/Aruba'}

print("Please choose a time zone. Select 0 to quit. ")
for place in sorted(timezones):
    print("\t{}. {}".format(place, timezones[place]))

while True:
    choice = input()

    if choice == "0":
        break
    if choice in timezones.keys():
        tz_to_display = pytz.timezone(timezones[choice])
        world_time = datetime.datetime.now(tz=tz_to_display)
        print("The time in {} is {} {}".format(timezones[choice], world_time.strftime('%A %x %X %z'), world_time.tzname()))
        print("local time is {}".format(datetime.datetime.now().strftime('%A %x %X')))
        print("UTC time is {}".format(datetime.datetime.utcnow().strftime('%A %x %X')))
        print()