#the game () function in aprogam lets a user play a game 
# and returns the score as an integer. you need to read a file  
#'hi - score.txt' which is either  blank or contains the previous 
#Hi-score. you need to write a program to update the 
#Hi-score whenever the game() function to breaks the 
#Hi score .

import random
def game () :
    print ( "you are paling the game...")
    score = random.randint ( 1, 100)

    # fetch the hiscore
    with open ( "hiscore.txt for question_2.py") as f :
        hiscore = f.read() 
        if (hiscore !=  ""):
            hiscore =int ( hiscore )
        else :
            hiscore = 0

    print(f"your score : {score}")
    if ( score > hiscore ):
        
        # write this hiscore to the file 
        with open ( "hiscore.txt for question_2.py", "w")as  f :
            f.write ( str(score))

    return score 

game () 
