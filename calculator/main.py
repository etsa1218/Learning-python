def add_nums(n1: int, n2: int) -> int:
    return n1 + n2






func_dict = {
    "add": add_nums,
}


# Entry point for calc app
if __name__ == "__main__":
    user_input = int(input("input a number"))

    # Ask the user if they want to add subtract mult or div
    user_input_func = input("do you want to add subtract multiply or divide")

    out = func_dict[user_input_func](user_input, 5)



    print(out)