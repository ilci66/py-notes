# class PartyAnimal:
#     x = 0

#     # Serves as the constructor
#     def party(self):
#         self.x = self.x + 1
#         print("So far ", self.x)


# # With every call gonna be incrementing the x

# an = PartyAnimal()

# an.party() # ==> this is the same as saying PartyAnimal().party(an), "self" is very useful
# an.party()
# an.party()
# an.party()

# ==> The professor describes this as "a nerdy way to find capabilities" 
# x = list()
# print(dir(x))

# igonre the ones with underscores tose are used by python itself
# but the rest are real operations that the object can perform
# it's like type(), tells us something about a variable 

# s = 'stuff'
# print(dir(s))

# ==> Now with using these on my class
# print("Type ", type(an))
# print("Dir ", dir(an))
# for now the only available ones for my use are x and party (an.x, an.party())

# ==========> Rewriting my class with more methods got more examples<========== 
# class PartyAnimal:
#     x = 0

#     def __init__(self):
#         print('I am constructed')

#     def party(self):
#         self.x = self.x + 1
#         print('So far', self.x)

#     def __del__(self):
#         print('I am deconstrcuted', self.x)

# # constructing here, an is an instance of party animal
# an = PartyAnimal()
# an.party()
# an.party()
# # now deconstructing it by assigning another value to variable an
# an = 42
# print('an contains', an)

# ==========> Rewriting my class with more methods got more examples<========== 
# class PartyAnimal:
#     x = 0
#     name = ""
#     def __init__(self, z):
#         self.name = z
#         print(self.name, 'has been constructed')

#     def party(self):
#         self.x = self.x + 1
#         print(self.name, '\'s party count so far ==>', self.x)

# s = PartyAnimal("Sally")
# s.party()

# j = PartyAnimal("Jerry")
# j.party()
# s.party()

# ======> Extending for Inheritance examples

class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, z):
        self.name = z
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count ==>', self.x)

# Extending the PartyAnimal class
class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        # calling party() here so That's the reason for printing double, got confused for a sec
        self.party()
        # when constructed added 7, every time touchdown is called will add 7
        print(self.name, "points", self.points)


s = PartyAnimal("Sally")
s.party()

j = FootballFan("Jerry")
j.party()
j.touchdown()
j.touchdown()

# print(dir(j))
