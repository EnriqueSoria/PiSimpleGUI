import random


class MockupLM75:

    def get_temp(self, celsius=True):
        return random.randrange(2500, 2790) / 100
