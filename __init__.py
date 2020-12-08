from mycroft import MycroftSkill, intent_file_handler


class BibleVerse(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('verse.bible.intent')
    def handle_verse_bible(self, message):
        self.speak_dialog('verse.bible')


def create_skill():
    return BibleVerse()

