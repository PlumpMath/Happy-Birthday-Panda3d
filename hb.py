# Happy Birthday in Panda3d
# by Mitchell Vitez
# 2013

import direct.directbase.DirectStart                                     
from direct.showbase.DirectObject import DirectObject
from direct.gui.DirectGui import OnscreenText

class HappyBirthday(DirectObject):
    def __init__(self):
        base.setBackgroundColor( .2, .8, .8 )
        birthdayMessage = OnscreenText(text = "Happy Birthday, NAME!", 
                                            pos = (0, 0), scale = .1, fg = (1, 1, 0, 1), shadow = (0, 0, 0, 1))
        music = loader.loadSfx("music.wav")
        music.play()

hb = HappyBirthday()
run()
