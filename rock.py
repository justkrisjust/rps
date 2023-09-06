"""
so now we have to create rock paper scissor game and we have to play with computer the thing is i can create game for
like two ppl but idk how to make pc pick a word i can use random fun for random pick but how should i make pc pick one
too hmmmmm ok there are some conditions to create this game
1. it should be in while looop and the game should be played ten times
2.  we have to maintain record of how many times we win and pc win
3. response should be given from pc at last who win after compaerd all loos and wins
these three conditions are ok can do but how sould i make pc pick the word
"""
import time

t=time.time()
import random  # i imported random
words = ["rock", "paper", "scissors"]
""" so the logic is rock wins over scissor  
    for paper , paper wins over rock 
    and scissor wins over paper 

"""
print("hello welcome to the rock paper scissor game \n lets play ten matches and see who wins the most")
print("the RULES are : Rock beats scissor , Paper beats rock , Scissor beats paper ")
print("lets plaaayyyyy!")
print("pick one word among the given words and ill pick one \n rock : paper : scissors ")
chances = 0
chance = 10
your_points = 0
my_points = 0
rock_words_on_winnig_bypc = ["haha got u with the rock YOU LOST ", "ohoh you lost cause i picke  DWAYNE the ROCK JHONSON "
                             , "hmm seems like imma win this game boy !", "damn im ROCKing today lol "
                             , "oh hello ! anyone there who can win against mee"]
paper_words_on_winning_bypc =["i wonder how good iam or how bad you are lol"
                              ,"emooooootional daamaage for you!","GEEEEEEEEEEGEEEEEEEEEEEEEEEE"
                              ,"i knew i picked the right one","my win is an art on the PAPER!!"]
scissor_words_on_winnig_bypc = ["ima cut your points with SCISSORS ","try to win next round"
                                , "hey game is not always about winnnig or loosing sometimes its also about having fun so dont get frustated after i deafeat you nooooob haha",
                                 "gg"]
rock_words_on_loosing_by_pc = ["its just luck for you"
                               "damn youa re ROCKing","how did i loose ","you must be cheating","i will win next round"]
paper_words_on_loosing_bypc = ["lol i lost","u cheating?"," hey thats not fair ","ok now i think i understand you "]

scissor_words_on_loosing_bypc = ["damn you are amazing",
                                 "i know i lost but i will win","haha u cut my points with SCISSORS","gg"]
#pick = input("tell the word u picked ")
while chances < 11:
    pick = input("tell the word u picked \n")
    pc_picking = random.choice(words)
    if pick == "rock" and pc_picking == "rock":
        print("we both selected rock ","its a tie ")
        print("your points :", your_points)
        print("my points :", my_points)
        print("Rounds left :", 10 - chances)
        chances = chances + 1
    elif pick == "rock" and pc_picking == "paper":
        random_pick = random.choice(paper_words_on_winning_bypc)
        print(random_pick)
        my_points = my_points+1
        print("your points :",your_points)
        print("my points :", my_points)
        print("Rounds left :",10-chances)
        chances=chances+1
    elif pick == "rock" and pc_picking == "scissors":
        random_pick = random.choice(scissor_words_on_loosing_bypc)
        print(random_pick)
        your_points = your_points+1
        print("your points :",your_points)
        print("my points : ",my_points)
        print("Rounds left :",10-chances)
        chances= chances+1
    elif pick == "paper" and pc_picking =="rock":
        random_pick = random.choice(rock_words_on_loosing_by_pc)
        print(random_pick)
        your_points = your_points + 1
        print("your points :", your_points)
        print("my points : ", my_points)
        print("Rounds left :",10- chances)
        chances = chances + 1
    elif pick == "paper" and pc_picking =="paper":
        print("its a tie ")
        print("your points :", your_points)
        print("my points :", my_points)
        print("Rounds left :", 10 - chances)
        chances = chances + 1
    elif pick == "paper" and pc_picking == "scissors":
        random_pick = random.choice(scissor_words_on_winnig_bypc)
        print(random_pick)
        my_points = my_points + 1
        print("your points :", your_points)
        print("my points :", my_points)
        print("Rounds left :", 10 - chances)
        chances = chances + 1
    elif pick == "scissors" and pc_picking == "rock":
        random_pick =random.choice(rock_words_on_winnig_bypc)
        print(random_pick)
        my_points = my_points + 1
        print("your points :", your_points)
        print("my points :", my_points)
        print("Rounds left :", 10 - chances)
        chances = chances + 1
    elif pick == "scissors" and pc_picking == "paper":
        random_pick = random.choice(paper_words_on_loosing_bypc)
        print(random_pick)
        your_points = your_points + 1
        print("your points :", your_points)
        print("my points : ", my_points)
        print("Rounds left :",10- chances)
        chances = chances + 1
    elif pick == "scissors" and pc_picking == "scissors":
        print("its a tie ")
        print("your points :", your_points)
        print("my points :", my_points)
        print("Rounds left :", 10 - chances)
        chances = chances + 1
    else:
        print(" u entered wrong name \n please enter rock paper scissors ")
print("your points ",your_points , " : ","my points ",my_points)
if chances == chance :
    print("GAME OVER !!!" )
else:
    print("game over !!!")

if your_points > my_points:
    print("damn you beat me in the game congratulations \n lets play again ")
elif your_points < my_points:
    print("I WON \n wanna go again ?")
else:
    print("its a tie \n lets play again")

print(f"time took for this program is {time.time()-t}")




