class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    # One of the ways to write getters and setters in python
    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0

    lives = property(_get_lives, _set_lives)

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            levelup = level - self._level
            self._score += levelup * 1000
            self._level = level
        else:
            print("You can't go below level 1")
            self._level = 1

    level = property(_get_level, _set_level)

    # Alternative syntax for getters and setters in python
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    # When you print the an object in the class Player it prints below. Self is the object in the class i.e. `mitchell`
    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}".format(self)

