#!/usr/bin/env python3

import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""

# colors for headers
White = '\033[0m'
Red = '\033[31m'
Green = '\033[32m'
Orange = '\033[33m'
Blue = '\033[34m'
Purple = '\033[35m'

colors = [White, Red, Green, Orange, Blue, Purple]


def randomColorTxt(text):
    output = ""
    for letter in text:
        output += letter + random.choice(colors)
    return output + White


class Player:
    def __init__(self):
        self.my_last_move = ""
        self.their_last_move = ""

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_last_move = my_move
        self.their_last_move = their_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def __init__(self):
        super(HumanPlayer, self).__init__()

    def move(self):
        # allow user to repeat last move is one exists
        if self.my_last_move != "":
            move = input("Rock, paper or scissors?\n\
(Press ENTER to repeat your last move) > ")
            if move == "":
                move = self.my_last_move
        else:
            move = input("Rock, paper or scissors? > ")
        # validate input
        while move.casefold() not in moves:
            move = input("Check your spelling and try again! > ")
        return move


class ReflectPlayer(Player):
    def __init__(self):
        super(ReflectPlayer, self).__init__()

    def move(self):
        if self.their_last_move == "":
            return random.choice(moves)
        else:
            return self.their_last_move


class CyclePlayer(Player):
    def __init__(self):
        super(CyclePlayer, self).__init__()

    def move(self):
        if self.my_last_move == "":
            return random.choice(moves)
        else:
            next_move = moves.index(self.my_last_move) + 1
            next_move %= 3
            return moves[next_move]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0
        self.p1_win = randomColorTxt("|*** PLAYER ONE WINS! ***|")
        self.p2_win = randomColorTxt("|*** PLAYER TWO WINS! ***|")
        self.draw = randomColorTxt("|********* DRAW *********|")
        self.spacer = randomColorTxt("|************************|")

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print(f"\nYou played {move1}")
        print(f"Opponent played {move2}\n")
        if beats(move1, move2) is True:
            print(self.p1_win)
            self.p1_score += 1
        else:
            if beats(move2, move1) is True:
                print(self.p2_win)
                self.p2_score += 1
            else:
                print(self.draw)
        print(f"|SCORES | P1 = {self.p1_score} | P2 = {self.p2_score}|")

    def play_game(self):
        print(randomColorTxt("\n||ROCK!|PAPER!|SCISSORS!||\n"))
        # ask player how many rounds to play
        rounds = input("How many rounds\nwould you like to Play? > ")
        # validate input and ask user to fix
        while rounds.isdigit() is False:
            rounds = input("Please enter a number > ")
        print(randomColorTxt("\n|***** GAME START!! *****|"))
        for round in range(int(rounds)):
            print(f"\nRound {round + 1}:")
            self.play_round()
        print(randomColorTxt("\n\n|****** GAME OVER! ******|"))
        print(self.spacer)
        print(f"|SCORES | P1 = {self.p1_score} | P2 = {self.p2_score}|")
        print(self.spacer)
        if self.p1_score > self.p2_score:
            print(self.p1_win)
        elif self.p1_score < self.p2_score:
            print(self.p2_win)
        elif self.p1_score == self.p2_score:
            print(self.draw)
        print(self.spacer)


if __name__ == '__main__':
    # list oponents
    cpu_players = [RandomPlayer(), ReflectPlayer(), CyclePlayer()]
    # select oponent
    p2_selection = random.choice(cpu_players)
    # start the game
    game = Game(HumanPlayer(), p2_selection)
    game.play_game()
