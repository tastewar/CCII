on bootup, device will find a unique device id.
it will query a known web server, and pull down a unique config file
config file contains data such as:
 * time zone offset
 * DST setting
 * school bell time offset from real time (seconds)
 * maybe NTP server? (should override default)
 * countdown minutes

Finally, there need to be schedule and calendar data, as well as clock style definitions

Schedule data describes the periods of the school day:
 * begin time
 * end time
 * label (1 character)
 * label color

Calendar describes the school year, and lists the days, and for each
school day, documents
 * day label (1 character)
 * label color
 * schedule for the day (relates back to the above)

Clock styles include settings like colors, fade-in/our, rainbow, etc.