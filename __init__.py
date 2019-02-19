from mycroft import MycroftSkill, intent_file_handler
import subprocess


class Spinturtleleft(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('spinturtleleft.intent')
    def handle_spinturtleleft(self, message):
        self.speak_dialog('spinturtleleft')
        s = "rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist -- '[0.0, 2.0, 0.0]' '[2.0, 0.0, 0.0]'"
        subprocess.call([s],shell=True)

def create_skill():
    return Spinturtleleft()

