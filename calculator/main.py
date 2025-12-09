
from functions.add import add_nums
from functions.sub import sub_nums
from functions.mult import mult_nums
from functions.div import div_nums

func_dict = {
    "add": add_nums,
    "sub": sub_nums,
    "mult": mult_nums,
    "div": div_nums
}


# Entry point for calc app
if __name__ == "__main__":
    # error handling loop
    while True:
        user_input = input("input a number" + "\n")
        try:
            user_input = int(user_input)
        except:
            print("must be an integer")
            continue

        user_input2 = input("input another number" + "\n")
        try:
            user_input2 = int(user_input2)
        except:
            print("must be an integer")
            continue

        # Ask the user if they want to add subtract mult or div
        user_input_func = ""
        while True:
            user_input_func = input("do you want to add sub mult or div" + "\n")
            if not user_input_func in list(func_dict.keys()):
                print("must type \"add\" \"sub\" \"mult\" \"div\"")
                continue
            else:
                break


        out = func_dict[user_input_func](user_input, user_input2)



        print(out)
        break