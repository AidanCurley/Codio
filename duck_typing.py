# If it walks like a duck, it's a duck
# When ojects have a method with the same name, it can be called
# on both, regardless of the type of object

import random

class BaseballPlayer:
    def hit(self):
        """Generate a random integer 1 to 4 and return the type of hit"""
        total_bases = random.randint(1, 4)
        if total_bases == 1:
            return "single"
        elif total_bases == 2:
            return "double"
        elif total_bases == 3:
            return "triple"
        else:
            return "home run"

class Song:
    def __init__(self, title, ranking):
        self.title = title
        self.ranking = ranking

    def hit(self):
        """A song is a hit if it appeared in a top 40 chart"""
        if self.ranking <= 40:
            return f"{self.title} is a hit song"
        else:
            return f"{self.title} is not a hit song"



def print_hit(obj):
    # If the object (whatever it is) has a hit method, it'll be called here
    print(obj.hit())

my_player = BaseballPlayer()
my_song = Song("Hey Jude", 12)


print_hit(my_player)
print_hit(my_song)