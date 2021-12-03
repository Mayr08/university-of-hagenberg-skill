from mycroft import MycroftSkill, intent_file_handler


class UniversityOfHagenberg(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('hagenberg.of.university.intent')
    def handle_hagenberg_of_university(self, message):
        self.speak_dialog('hagenberg.of.university')
        
    @intent_file_handler('turn.on.led.intent')
    def handle_hagenberg_of_university(self, message):
        self.speak_dialog('turn.on.led')    

def create_skill():
    return UniversityOfHagenberg()

