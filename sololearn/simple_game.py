# Let's have a small game using OOP concept in Python
"""
Object-orientation is very useful when managing different objects and their relations. That is especially useful when
you are developing games with different characters and features.

Let's look at an example project that shows how classes are used in game development.
The game to be developed is an old fashioned text-based adventure game.
Below is the function handling input and simple parsing.
"""

def get_input():
    command = input(": ").split()
    verb_word = command[0]
    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    else:
        print("Unknown verb {}". format(verb_word))
        return

    if len(command) >= 2:
        noun_word = command[1]
        print (verb(noun_word))
    else:
    print(verb("nothing"))

def say(noun):
    return 'You said "{}"'.format(noun)

def hello(noun):
    return 'Hello "{}"'.format(noun)

verb_dict = {
    "Say" : say,
    "Salute" : hello,
    "Examine" : examine}

class GameObject:
  class_name = ""
  desc = ""
  objects = {}

  def __init__(self, name):
    self.name = name
    GameObject.objects[self.class_name] = self

  def get_desc(self):
    return self.class_name + "\n" + self.desc

class Goblin(GameObject):

    def __init__(self, name):
        self.class_name = "goblin"
        self.desc = "A foul creature"
        self.health = 3
        super(Goblin, self).__init__()

    @property
    def desc(self):
        if self.health >= 3:
            return self._desc
        elif self.health == 2:
            health_line = "It has a wound on its knee."
        elif self.health == 1:
            health_line = "Its left arm has been cut off!"
        elif self.health <= 0:
            health_line = "It is dead."
        return self._desc + "\n" + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value

goblin = Goblin("Gobbly")

def examine(noun):
  if noun in GameObject.objects:
    return GameObject.objects[noun].get_desc()
  else:
    return "There is no {} here.".format(noun)

def hit(noun):
  if noun in GameObject.objects:
    thing = GameObject.objects[noun]
    if type(thing) == Goblin:
      thing.health = thing.health - 1
      if thing.health <= 0:
        msg = "You killed the goblin!"
      else:
        msg = "You hit the {}".format(thing.class_name)
  else:
    msg ="There is no {} here.".format(noun)
  return msg

while True:
    get_input()