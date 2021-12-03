from mycroft import MycroftSkill, intent_file_handler
from mycroft.messagebus.message import Message

import RPi.GPIO as GPIO

# GPIO pins
LED = 21


class UniversityOfHagenberg(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        
    #For LED Handling
    def initialize(self):
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(LED, GPIO.OUT)
            #GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            #GPIO.add_event_detect(BUTTON, GPIO.FALLING, bouncetime = 500)
        except GPIO.error:
            self.log.warning("Can't initialize GPIO - skill will not load")
            #self.speak_dialog("error.initialise")
        finally:
            #self.schedule_repeating_event(self.handle_button, None, 0.1, 'GoogleAIY')
            self.add_event('recognizer_loop:record_begin',
                           self.handle_listener_started)
            self.add_event('recognizer_loop:record_end',
                           self.handle_listener_ended)


    @intent_file_handler('hagenberg.of.university.intent')
    def handle_hagenberg_of_university(self, message):
        self.speak_dialog('hagenberg.of.university')
        
    @intent_file_handler('turn.on.led.intent')
    def handle_hagenberg_of_university(self, message):
        self.bus.emit(Message("mycroft.mic.listen"))
        self.speak_dialog('turn.on.led')    
        
    def handle_listener_started(self, message):
        # code to excecute when active listening begins...
        GPIO.output(LED, GPIO.HIGH)

    def handle_listener_ended(self, message):
        GPIO.output(LED, GPIO.LOW)

def create_skill():
    return UniversityOfHagenberg()

