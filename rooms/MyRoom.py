import random
import string
from EscapeRoom import EscapeRoom


class MyRoom(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Soham", __name__)
        self.add_level(self.create_level1())
        self.add_level(self.create_level2())

    ### LEVELS ###

    def create_level1(self):
        mysterious_letters = self.random_letters()

        task_messages = [
            "In a hidden corner you will see a display and a button. Each time you press a button, a different sequence of letters appears. "
            "What does that mean?",
            "The sequence of letters is: <b>"+mysterious_letters+"</b",
            "Behind a picture hung on the wall you will now see an input panel for a 6-digit code.",
            "Write a method <code>run('"+mysterious_letters +
            "')</code>, which generates the correct code from the letters."
        ]
        hints = [
            "How can a 6-digit numeric code be derived from 3 letters?",
            "What is the ASCII code for a letter?"
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.get_number_from_letters, "data": mysterious_letters}

    def create_level2(self):
        task_messages = [
            "After entering the code correctly, mysterious music will now play and a voice will say multiple times: 'Vowels forbidden'"
        ]
        hints = [
            "What is the saying 'Vowels forbidden' when vowels are forbidden?",
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.remove_vowels, "data": "Vokale verboten"}

    def random_letters(self):
        letters = ""
        for _ in range(3):
            letters = letters + random.choice(string.ascii_uppercase)
        return letters

    ### SOLUTIONS ###

    def get_number_from_letters(self, letters):
        numberstring = ""
        for c in letters:
            numberstring = numberstring + str(ord(c))
        return numberstring

    def remove_vowels(self, word):
        result = ""
        vowels = ["a", "e", "i", "o", "u"]
        for c in word:
            if not c in vowels:
                result = result + c
        return result
