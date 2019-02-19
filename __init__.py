from mycroft import MycroftSkill, intent_file_handler


class Spinturtleleft(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('spinturtleleft.intent')
    def handle_spinturtleleft(self, message):
        self.speak_dialog('spinturtleleft')


def create_skill():
    return Spinturtleleft()

