import random

#Types: Chinese, Italian, Mexican, Japanese 

chinese_food = ["House of China" , "Main Moon", "China Star"]
italian_food = ["Olive Garden", "Antone's Kitchen", "Belleria"]
mexican_food = ["Los Gallos", "Norma's Casa De Tacos", "Chipotle"]
japanese_food = ["Asuka Japanese Cuisine", "Mizu Sushi", "Sawa Japanese Cuisine"]

def what_to_eat():
    place = input ("Where would you like to eat? ")
    if place == "Chinese":
        print("alright, let me decide a place for you")
        print("You should eat at: "+random.choice(chinese_food))
    elif place == "Italian":
        print("Sounds good, lets get you going")
        print("You should eat at: "+random.choice(italian_food))
    elif place == "Mexican":
        print("sweet, now where to go")
        print("You should eat at: "+random.choice(mexican_food))
    elif place == "Japanese":
        print("awesome, one last thing to decide")
        print("You should eat at: "+random.choice(japanese_food))
    else:
        print (input("thats cool, not everyone can decide, ill find you a place, enter a number 1-4: "))
        random_choice = random.randint(1,4)
        if random_choice == 1:
                print("Nice, you should eat at: " +random.choice(chinese_food))
        elif random_choice == 2:
            print("Nice, you should eat at: " +random.choice(italian_food))
        elif random_choice == 3:
            print("Nice, you should eat at: " +random.choice(mexican_food))
        elif random_choice == 4:
            print("Nice, you should eat at: " +random.choice(japanese_food))
        else:
            print("Did you not enter a number like i asked??")

what_to_eat()
