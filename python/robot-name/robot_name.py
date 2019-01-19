import random
import string

class Robot(object):

    random_names = set()

    def __init__(self):
        if len(self.random_names) == 26 * 26 * 1000:
            raise Exception("All names are taken!")
        random_name = self.generate_random_name()
        while random_name in self.random_names:
            random_name = self.generate_random_name()
        self.name = random_name
        self.random_names.add(self.name)

    def generate_random_name(self):
        return chr(random.randint(65, 90)) + \
               chr(random.randint(65, 90)) + \
               str(random.randrange(0, 9)) + \
               str(random.randrange(0, 9)) + \
               str(random.randrange(0, 9))

    def reset(self):
        self.__init__()