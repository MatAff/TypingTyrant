#!/usr/bin/env python3

# TODD: update to latest pyxhook, if it exists
# TODO: allow users to configure
# TODO: make playing sound less verbose
# TODO: include differt sounds
# TODO: add install notes with required libraries
# TODO: make sound dependent on performance
# TODO: register commonly made mistakes (which char sequence is followed by bs)
# TODO: make the python version available for Windows
# DONE: host on github
# DONE: sort out licence, disentangle from keylogger

import os
import datetime
import pyxhook


def now():
    return datetime.datetime.now()


class Sound(object):

    def beep(sec, freq):
        os.system('play -n synth %s sin %s' % (sec, freq))


class Typing(object):

    def __init__(self):
        self.last = now()
        self.nr_char = 0
        self.run_long = 0  # the goal
        self.run_short = 50  # current

    def key_simple(self, k):
        if k == "BackSpace":
            print("Back space pressed.")
            Sound.beep(self.sec, self.freq)

    def key(self, k):
        if k == "BackSpace":
            time_delta = now() - self.last
            if time_delta > datetime.timedelta(seconds=1):
                self.run_long = self.run_long * 0.75 + self.nr_char * 0.25
                self.run_short = self.run_short * 0.5 + self.nr_char * 0.5

                print(f'Characters typed since last backspace: {self.nr_char}')
                print(f'Long running average: {self.run_long}')
                print(f'Short running average: {self.run_short}')

                self.nr_char = 0

                if self.run_short < 20:
                    Sound.beep(0.5, 600)
                if self.run_short < self.run_long:
                    Sound.beep(0.5, 400)

            self.last = now()
        else:
            self.nr_char += 1


if __name__ == '__main__':

    typing = Typing()

    def OnKeyPress(event):
        typing.key(event.Key)
        if event.Ascii == 96:  # the grave key (`)
            new_hook.cancel()

    new_hook = pyxhook.HookManager()  # instantiate HookManager class
    new_hook.KeyDown = OnKeyPress  # listen to all keystrokes
    new_hook.HookKeyboard()  # hook the keyboard
    new_hook.start()  # start the session
