#!/usr/bin/env python

DRIVETIME = 1 #seconds

import create2api
import time
import json

# Create a Create2. This will automatically try to connect to your robot over serial
bot = create2api.Create2()

# Start the Create2
bot.start()

# Put the Create2 into 'safe' mode so we can drive it
bot.safe()

# Tell the Create2 to drive straight forward at a speed of 100 mm/s
bot.drive_straight(100)

# Wait for a few seconds
time.sleep(DRIVETIME)

# Tell the Create2 to drive straight backward at a speed of 100 mm/s
bot.drive_straight(-100)

# Wait for a few seconds
time.sleep(DRIVETIME)

# Stop the bot
bot.drive_straight(0)

# Listen for a bumper hit
while True:
    
    #Packet 100 contains all sensor data.
    bot.get_packet(100)

    #print json.dumps(bot.sensor_state, indent=4, sort_keys=False)
    sensors = bot.sensor_state # a dictionary
    for key in sensors.keys():
        if key == 'wheel drop and bumps':
        #if 'bump' in key:
            print(key, sensors[key])
    print('-------------------------------')

    time.sleep(.5)

# Close the connection
bot.destroy()
