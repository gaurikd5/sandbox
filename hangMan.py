#hang man game
word='apple'
#3 chances to guess letter
lives=3

#_____
answer='_'*len(word)
print("welcome come to hamgman.\n you need to guess the word \n If you guess the world in given lies you won the game")
print()
print("your word is")
print(answer)
print()
print('_'*100)

while lives>0:

    #input function to get data from user
    letter=input("guess the letter:")
    print(f"you gussed a letter={letter}")

    if (letter in word) and (letter not in answer):
        print(f"your guess is right")
        #list is mutable hence here we use list
        character=list(answer)
        #print(character)
        index=0
        for char in word:
            #check if users letter is present in the word
            if char==letter:
            #replace the position with right letter
                character[index]=letter
            index+=1
        #print(character)
        #construct string again
        answer=''.join(character)
        print(answer)
        if '_' not in answer:
            print(f"congratulations!!! you won the game")
            break
    else:
        print(f"your guess is wrong you lose one lives")
        lives-=1

        if lives==0:
            print(f"you lost the game")

    print('_'*100)