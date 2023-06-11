import random
import stages
import word_list
word = random.choice(word_list.words)
life = 5
list = ["_"]*len(word)
print("Guess The Word")
print(" ".join(list)) 
while(True):
    n = input("Enter Your Choice: ").lower() 
    c = 0
    for i in range(len(word)):
        if word[i] == n:
            list[i] = n
            c = 1
    if c == 0:
        life -=1   
    print(stages.stages[life])
    print(" ".join(list))
    if(life == 0):
        print(f"Game Over! You loose!!\nThe word was {word}")
        break
    elif("_" not in list):
        print("You Won!!!")
        break
    print(f"You have {life} lives")
    
    
    
