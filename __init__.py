from mycroft import MycroftSkill, intent_file_handler
# For NeoPixels on Raspberry Pi
import time
import board
import neopixel


# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D21
# The number of NeoPixels
num_pixels = 24
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=ORDER
)

class UniversityOfHagenberg(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        
    def _turnOnLED(self):
        time.sleep(1)

    @intent_file_handler('hagenberg.of.university.intent')
    def handle_hagenberg_of_university(self, message):
        self.speak_dialog('hagenberg.of.university')
        
    @intent_file_handler('turn.on.led.intent')
    def handle_hagenberg_of_university(self, message):
        self._turnOnLED()
        self.speak_dialog('turn.on.led')    

def create_skill():
    return UniversityOfHagenberg()
