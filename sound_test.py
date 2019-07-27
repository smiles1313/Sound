#sound_test

import pygame
pygame.init()
#from pygame.locals import *
pygame.mixer.init()

soundObj = pygame.mixer.Sound('/Users/s.miles1313/Desktop/beep-01a.wav')
soundObj.play()
import time
time.sleep(1) # wait and let the sound play for 1 second
soundObj.stop()