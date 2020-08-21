# 初めて受付した人は、新しくリストに追加する。(受付ごとに1ptを記録して、5ptごとに割引があるのでそれを該当者に通知する)
# かつ5ptでいくつかのgoodsと交換できるので、いくつかのオプションの中から欲しいければ選んでもらう。
# nameの登録は、ニックネームとして空白で開けない仕様にする、同姓同名の登録があれば、warningを発し、変更してもらう。

import termcolor
import sys

register_list = ["Shoma","Yusuke","Takumi","Ryota","Takeru"] #最大100人登録までとする。
register_point= [4,3,2,1,2]

print("Thank you for visiting our website!")

begin = """Are you a member or a non-member?
If you are member, you may choose {m}.
Otherwise, you may choose {n}. """

select_status = input("I am a (m/n):")
print("\n")

if select_status == "m":
    print("Thanks for your visits again")
    name = input("What's your nickname?:\n")
    if name in register_list:
        print("You are given 1pt now")
        register_point[register_list.index(name)] +=1
        print("Your total point is "+str(register_point[register_list.index(name)])+".\n")
        if register_point[register_list.index(name)] == 5:
            print("Because you got 5pt in total, you can have the options to chance the wonderful presents.")
            change_goods = input("Do you want to echange your point to any goods?(Y/N):")
            if change_goods == "Y" or change_goods =="y":
                present_lists = {1: "Ice Candy", 2: "1000¥ discount coupon", 3: "Taxi ticket"}
                print(present_lists)
                print("Choose just one number you like the most!!!")
                choose_item = input("Which items you want?(1,2,or3):")
                print("Thanks for your change, so your score is 0 for now.")
                register_point[register_list.index(name)] -= 5
                print("Have a nice watching.")
            else: print("You can exchange anytime you want! Have a nice watching.")

if select_status == "n":
    print("You need to register your information.")
    new_name = input("What' your nickname? You may decide anyting you like:")
    if new_name in register_list:
        print("Your name is used by another user. You must change.")
        new_name2 = input("What' your nickname? You may decide anything you like:")
        if new_name2 in register_list:
            print("You failed twice. Deactivated now, please start from beginning.")
            sys.exit()
    else:
        print("Thanks for your registration.")
        print("You are given 1pt now, so have a nice day.")











