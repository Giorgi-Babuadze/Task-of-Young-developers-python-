class animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print("The " + self.name + " says " + self.sound)
        
dog = animal("Dog", "Bark")
dog.make_sound()
# Output: The Dog says Bark
cat = animal("Cat", "Meow")
cat.make_sound()
# Output: The Cat says Meow