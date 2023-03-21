print("welcome to my first game!")
name = input("what is your name?\n")
age = int(input("what is your age?\n"))
print("hello", name, "you are", age, "years old")


def check(health):
    if 0 < health <= 10:
        return True
    else:
        return False


if age >= 18:
    print("you are old enough")
    wants_to_play = input("do you wanna play?\n").lower()
    if wants_to_play == "yes":
        print("lets play")
        health = 10
        print("you are starting with 10 health")
        weapon = input("pick a weapon(sword/baton):\n")
        left_or_right = input("first choice... left or right(left/right)\n").lower()
        if left_or_right == "left":
            ans1 = input(
                "nice you followed the path and reached lake ...do you swim across or go around(across/around)\n").lower()
            if ans1 == "around":
                print("you went around and reched the other side of the lake")

            elif ans1 == "across":
                print("you managed to get across and got bit by a fish and lost 5 lives")
                health -= 5

            ans1 = input("you notice a house and a river. which do you go to(river/house)?\n")
            if ans1 == "house":
                print("you go to the house you are greeted by the owner..... he doesn't like you")
                if weapon == 'sword':
                    print("you killed him")
                else:
                    print(" lost 5 lives")
                    health -= 5

                if check(health):
                    if health == 5:
                        print("you managed to survive")
                    else:
                        print("you win")




                else:
                    print("you lost the game")
            elif ans1 == "river":
                print("you fell in the river and lost.....")



        else:
            print("you fell down and lost")

    else:
        print('cya...')
else:
    print("you are not old enough to play")


