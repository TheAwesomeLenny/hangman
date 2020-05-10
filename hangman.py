import getpass
import re
keepplaying = True
while keepplaying:
    rsentence = getpass.getpass("What would you like the sentence to be? ")
    rsentence = re.sub(r'[^a-zA-Z ]', '', rsentence)
    difficulty = input("Would you like to make hangman 'easy' or 'hard'? ")
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    wait = input(" ")
    sentence = list(rsentence)
    for i in list(range(0, len(sentence))):
        if sentence[i] == " ":
            continue
        else:
            sentence[i]="_"
        dashedSentence =  "".join(sentence)
    hangmans = ["""
     _____
    |  (    )
    |    
    |""",
    """
     _____
    |  (  ͜  )
    |    
    |""",
    """
     _____
    |  (  ͜ʖ )
    |    
    |""",
    """
     _____
    |  (° ͜ʖ )
    |    
    |""", 
    """
     _____
    |  (° ͜ʖ°)
    |    
    |""",
    """
     _____
    |  (° ͜ʖ°)
    |    |
    |""", 
    """
     _____
    |  (° ͜ʖ°)
    |   -|
    |""",
    """
     _____
    |  (° ͜ʖ°)
    |   -|-
    |""",
    """
     _____
    |  (° ͜ʖ°)
    |   -|-
    |   /""",
    """
     _____
    |  (X-X)
    |   -|-
    |   / l"""]
    hangmanNorm = ["""
     _____
    |    O
    |
    |""",
    """
     _____
    |    O
    |    |
    |""",   
    """
     _____
    |    O
    |   -|
    |""", 
    """
     _____
    |    O
    |   -|-
    |""", 
    """
     _____
    |    O
    |   -|-
    |   / """, 
    """
     _____
    |  (X-X)
    |   -|-
    |   / l""", ]
    if difficulty == 'easy':
        numTries = 10
    elif difficulty == 'hard':
        numTries = 6        
    winstuff = 0
    hangcount = 0
    print("""Here are the gallows for your hangman:
     _____ _____ _____
    |     |     |     |
    |     O     O     |  
    |                 |""")
    print(dashedSentence)
    while "_" in dashedSentence:
        goodGuess = 1 
        letter = input("Choose a letter to guess. ")
        if letter in alphabet:
            alphabet.remove(letter)
        else:
            print("Please choose a single letter that you have not guessed yet.")
            goodGuess = 0
        if goodGuess:    
            jitsu = ()
            count=0
            for j in rsentence:
                if j.lower() == letter:
                    ljitsu = list(jitsu)
                    ljitsu.append(count)
                    jitsu = tuple(ljitsu)
                count +=1
            if not jitsu:
                    print("Bad guess.")
                    if difficulty == 'easy':
                        print("Here is your hangman now: {}".format(hangmans[hangcount]))
                    elif difficulty == 'hard':
                        print("Here is your hangman now: {}".format(hangmanNorm[hangcount]))
                    hangcount+=1
                    if hangcount == numTries:
                        winstuff = 1
                        print("You bum! Your hangman has died!")
                        print("The sentence was {}".format(rsentence))
                        break
            ldashedSentence = list(dashedSentence)
            for k in jitsu:
                ldashedSentence[k] = letter
            dashedSentence = "".join(ldashedSentence)
            print(dashedSentence)
    if not winstuff:
        print("Congratulations! You won!!!!!!!!")            
    hello = input('Do you want to keep playing? (T/F)')
    if hello == 'T':
        keepplaying = True
    else:
        keepplaying = False
