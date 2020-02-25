#!/usr/bin/env python3.8
# Hangman game
from random import randint
import pdb
import getpass
hangman_pics = ['''






=========''','''
       +
       |
       |
       |
       |
       |
=========''','''
   +---+
       |
       |
       |
       |
       |
=========''','''
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
words = ["adult", "aeroplane", "air", "aircraft", "airforce", "airport", "album", "alphabet", "apple", "arm", "army", "baby", "baby", "backpack", "balloon", "banana", "bank", "barbecue", "bathroom", "bathtub", "bed", "bed", "bee", "bible", "bible", "bird", "bomb", "book", "boss", "bottle", "bowl", "box", "boy", "brain", "bridge", "butterfly", "button", "cappuccino", "car", "carriage", "carpet", "carrot", "cave", "chair", "chessboard", "chief", "child", "chisel", "chocolates", "church", "church", "circle", "circus", "circus", "clock", "clown", "coffee", "coffin", "comet", "compact", "compass", "computer", "crystal", "cup", "cycle", "database", "desk", "diamond", "dress", "drill", "drink", "drum", "dung", "ears", "earth", "egg", "electricity", "elephant", "eraser", "explosive", "eyes", "family", "fan", "feather", "festival", "film", "finger", "fire", "floodlight", "flower", "foot", "fork", "freeway", "fruit", "fungus", "game", "garden", "gas", "gate", "gemstone", "girl", "gloves", "god", "grapes", "guitar", "hammer", "hat", "hieroglyph", "highway", "horoscope", "horse", "hose", "ice", "ice-cream", "insect", "jetfighter", "junk", "kaleidoscope", "kitchen", "knife", "leather", "leg", "library", "liquid", "magnet", "man", "map", "maze", "meat", "meteor", "microscope", "milk", "milkshake", "mist", "money", "monster", "mosquito", "mouth", "nail", "navy", "necklace", "needle", "onion", "paintbrush", "pants", "parachute", "passport", "pebble", "pendulum", "pepper", "perfume", "pillow", "plane", "planet", "pocket", "post-office", "potato", "printer", "prison", "pyramid", "radar", "rainbow", "record", "restaurant", "rifle", "ring", "robot", "rock", "rocket", "roof", "room", "rope", "saddle", "salt", "sandpaper", "sandwich", "satellite", "school", "sex", "ship", "shoes", "shop", "shower", "signature", "skeleton", "slave", "snail", "software", "solid", "space", "spectrum", "sphere", "spice", "spiral", "spoon", "sports-car", "spotlight", "square", "staircase", "star", "stomach", "sun", "sunglasses", "surveyor", "swimming", "sword", "table", "tapestry", "teeth", "telescope", "television", "tennis", "thermometer", "tiger", "toilet", "tongue", "torch", "torpedo", "train", "treadmill", "triangle", "tunnel", "typewriter", "umbrella", "vacuum", "vampire", "videotape", "vulture", "water", "weapon", "web", "wheelchair", "window", "woman", "worm", "x-ray"]
def get_random_word(list_of_words):
    return list_of_words[randint(0,(len(list_of_words)-1))]
def display_board(hangman_pics, letters_miss, letters_correct, secret_word):
    print(hangman_pics[len(letters_miss)])
    print()
    print("Missed letters: ")
    for letter in letters_miss:
        print(letter, end = " ")
    print()
    print("Secret word:", end = " ")
    blanks = "_" * len(secret_word)
    for s in range(len(secret_word)):
        if secret_word[s] in letters_correct:
            blanks = blanks[:s] + secret_word[s] + blanks[s+1:]
    for l in blanks:
        print(l + " ", end = " ")
    print("\n")
def letter_input(already_guessed):
    san_loop = True
    while san_loop == True:
        guess = input("Input a single letter: ")
        if len(guess) != 1:
            print("Please input a single, lowercase letter.")
            continue
        elif guess in already_guessed:
            print("You already did that, try again.")
            continue
        elif guess.isalpha() == False and guess.islower() == False:
            print("Please print a lowercase alphabet letter.")
            continue
        else:
            return guess
            san_loop = False
print("=====H A N G M A N======")
print("========================")
print("=====by THC in 2020=====")
game = True
guess_round = True
while game == True:
    letters_correct = ""
    letters_miss = ""
    mode = input("Single player or Two Player? (S/T): ")
    mode_loop = True
    while mode_loop == True:
        if mode == "S" or mode == "s":
            secret_word = get_random_word(words)
            mode_loop = False
            break
        elif mode == "T" or mode =="t":
            secret_word = getpass.getpass(prompt = "Player one is setter.\n" + "Please input a word, all lowercase: ")
            print("Second player, begin guessing:")
            mode_loop = False
            break
        else:
            print("Please input either S or T.")
            continue
    while guess_round == True:
        display_board(hangman_pics, letters_miss, letters_correct, secret_word)
        guess = letter_input(letters_correct + letters_miss)
        if guess in secret_word:
            letters_correct += guess
            word_correct = True
            for letter in range(len(secret_word)):
                if secret_word[letter] not in letters_correct:
                    word_correct = False
                    break
            if word_correct == True:
                print("Congratulations! You've guessed the complete word.")
                print("The secret word was: " + secret_word)
                guess_round == False
                break
        else:
            letters_miss += guess
            if len(letters_miss) == len(hangman_pics) - 1:
                print("Y O U   L O S E")
                print("You took " + str(len(letters_miss) + len(letters_correct)) + " guesses.")
                print("The secret word was " + secret_word + ".")
                print("""
                    :::!~!!!!!:.
                .xUHWH!! !!?M88WHX:.
             .X*#M@$!!  !X!M$$$$$$WWx:.
            :!!!!!!?H! :!$!$$$$$$$$$$8X:
            !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
            :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
            ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
            !:~~~ .:!M"T#$$$$WX??#MRRMMM!
            ~?WuxiW*`   `"#$$$$8!!!!??!!!
            :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
        :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~""")
                guess_round = False
    play_again = input("Play again? (Y/N): ")
    if play_again == "y" or play_again == "y":
        guess_round = True
        continue
    else:
        game = False
exit()
