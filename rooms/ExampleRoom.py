import random
import string
from EscapeRoom import EscapeRoom


class ExampleRoom(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Mark", __name__)
        self.add_level(self.create_level1())

    ### LEVELS ###

    def create_level1(self):
        secret = random.choice(["Even Some Clowns Smell It For Days",
                                "Gangsters Detect Secret Essences in Mails"])

        task_messages = [
            "The following text is written on a piece of paper:",
            "<b>"+secret+"</b>",
            "Is there a secret here?"
        ]
        hints = [
            "Take a look at the initials!"
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.first_letters, "data": secret}

    ### SOLUTIONS ###

    def first_letters(self, secret):
        words = secret.split(" ")
        result = ""
        for word in words:
            result += word[0]
        return result
