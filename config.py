#! /usr/bin/env python

#    config.py
#
#    -Tony Sprayberry   04.28.13
#    -Tony Sprayberry   05.18.16


import plistlib
import sys


class config(object):
    """
    This class will parse a plist and make the Key/Values into class Properties
    """

    plist_location = "./configSample.plist"

    plist_file = None
    configAcquired = False

    def __init__(self, plist_location=plist_location):
        self.getPlist(plist_location)

    def getPlist(self, plist_location):
        try:
            self.plist_file = plistlib.readPlist(plist_location)
        except IOError:
            sys.stderr.write("plist could not be found")
        if self.plist_file:
            self.setConfig()
        else:
            return None

    def setConfig(self):
        for key in self.plist_file:
            setattr(self, key, self.plist_file[key])
        self.configAcquired = True

if __name__ == '__main__':
    Config = config()
