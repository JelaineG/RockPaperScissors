#!/usr/bin/env python3
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random
moves = ['rock', 'paper', 'scissors']
"""The Player class is the parent class for all of the Players
in this game"""
class Player:
    def move(self):
        return "rock"
    def learn(self, my_move, their_move):
        pass
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)
class HumanPlayer(Player):
    def move(self):
        move1 = input("rock, paper, or scissors? > ")
        while move1 not in moves:
            move1 = input("rock, paper, or scissors? > ")
        return move1 
class ReflectPlayer(Player):
    def __init__(self):
        self.my_move = "rock"    
    def move(self):
        return self.my_move
    def learn(self, my_move, their_move):
        self.my_move = their_move
class CyclePlayer(Player):
    current_move_index = 0
    def move(self):
        next_move = moves[self.current_move_index]
        self.current_move_index = \
            (self.current_move_index + 1) % len(moves)
        return next_move    
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))
class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.scores = {"p1":0, "p2":0}
    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played {move1}, Opponent played {move2}.")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        beats(move1, move2)
        beats(move2, move1)
        if beats(move1, move2):
            self.scores["p1"] += 1
            print("You win!")
        elif beats(move2, move1):
            self.scores["p2"] += 1
            print("Player Two wins!")
        else:
            print("***TIE***")
        print(f"SCORE: Player One: {self.scores['p1']}, Player Two: {self.scores['p2']}")
    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        if self.scores["p1"] > self.scores["p2"]:
            print ("You WIN!")
        elif self.scores["p1"] > self.scores["p2"]:
            print ("Player Two WINS!")
        else:
            print("It's a TIE")
        print("Game over!")     
if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
