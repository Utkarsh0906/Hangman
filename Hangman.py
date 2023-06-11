import random
import stages
import word_list

word = random.choice(word_list.words)
life = 5
list = ["_"]*len(word)
print("Guess The Word\n")
print(" ".join(list)) 

while(True):
    n = input("\n\nEnter Your Choice: ").lower() 
    c = 0
    
    if(n in list):
        print(f"\nYou have already guess the letter {n}")
    
    for i in range(len(word)):
        if word[i] == n:
            list[i] = n
            c = 1
    
    if c == 0:
        life -=1   
    
    print(stages.stages[life])
    print(" ".join(list))
    
    if(life == 0):
        print(f"\nGame Over! You loose!!\nThe word was {word}")
        break
    
    elif("_" not in list):
        print("\nCongratulations!!!\nYou Won!!!")
        break
    
    print(f"\nYou have {life} lives")
