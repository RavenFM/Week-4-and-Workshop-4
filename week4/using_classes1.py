# class Player:
#     max_hp = 4000

#     # Creates simple class with the name "Player"
#     # Class names are capitalized by convention "Player".
#     #Inside it, a class attribute of max_hp has been assigned with the value of "4000"
#     #Any objects that are instantiated from Player class will have this attribute and value
# player1 = Player()
# print(player1.max_hp)

#     #1st line will create a variable named "player1", then assigns to it an object from "Player" class
#     #2nd line will print the "max_hp" attribute of the object named "player1"
#     #We can make another object from the same class, and will have the same "max_hp" attribute
# player2 = Player()
# print(player2.max_hp)

# Player.max_hp = 5000
# print(player1.max_hp)
# print(player2.max_hp)

class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.score = 0

player1 = Player("Aaron",1200)
player2 = Player("Irene",1300)
print("--P1: ", player1.name, "--HP: ", player1.hp, "--SCORE: ", player1.score)
print("--P2: ", player2.name, "--HP: ", player2.hp, "--SCORE: ", player2.score)

player1.hp += 500
player1.score += 10
print("--P1: ", player1.name, "--HP: ", player1.hp, "--SCORE: ", player1.score)
print("--P2: ", player2.name, "--HP: ", player2.hp, "--SCORE: ", player2.score)

