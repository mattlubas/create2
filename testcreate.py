#!/usr/bin/env python

DRIVETIME = 2 #seconds

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

#json.dumps(bot.sensor_state, indent=4)
#with open('config.json') as config_file:
    #config = json.load(config_file)

# Listen for a bumper hit
while True:
    
    bot.get_packet(100)
    #print(json.dumps(bot.sensor_state, indent=4, sort_keys=False))

    with open('config.json') as config_file:

        bumper_sensor= json.dumps(config_file)
        print(bumper_sensor['sensor'])

    print("Hit my bumper Please!")

    time.sleep(2)


# Close the connection
bot.destroy()
