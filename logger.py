#!/usr/bin/python3

import sys
from datetime import datetime, date
from os import path
from sense_hat import SenseHat

if not len(sys.argv) == 2:
    exit("usage: logger.py <log directory>")

logDir = sys.argv[1]

if not path.isdir(logDir):
    exit("ERROR: {} path to log directory specified is not a directory")

filename = "{}/{}.senseHatData.log".format(logDir, date.today())

try:
    with open(filename, 'a+') as log_file:
        sense = SenseHat()
        log_file.write("{},{},{},{}\n".format(datetime.now().isoformat(), sense.temp, sense.humidity, sense.pressure))
except IOError as file_error:
    exit("ERROR: {} failed to open {}: {}".format(sys.argv[0], filename, file_error.strerror))
