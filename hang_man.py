import random
import os

def run():
    images = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    DB = ['JAVA','SQL']
    word = random.choice(DB)
    spaces = ["_"]*len(word)

    attempts = 6
    while True:
        os.system("cls")
        for character in spaces:
            print(character, end = " ")
        print(images[attempts])
        letter = input("letter-").upper()
        
        found = False
        for idx, character in enumerate(word):
            if character == letter:
                spaces[idx] = letter
                found = True
        
        if not found:
            attempts-=1
        
        if "_" not in spaces:
            os.system("cls")
            print("ganaste")
            break
            input()
        
        if attempts == 0:
            os.system("cls")
            print("perdiste")
            break
            input()



if __name__=='__main__':
    run()