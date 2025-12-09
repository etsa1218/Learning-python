
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
    user_input = int(input("input a number"))

    # Ask the user if they want to add subtract mult or div
    user_input_func = input("do you want to add sub mult or div")

    out = func_dict[user_input_func](user_input, 5)



    print(out)