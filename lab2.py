def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5,67,32)")

def get_user_input():
    print("get_user_input")
    inputstr = input()
    print ("Raw Input = "+inputstr)

    # Split the input string into a segments of strings separated by commas as splitter
    splitlist = inputstr.split(",")
    print ("After splitting = ", splitlist)

    # Next step is to convert eaach short string in the list into float
    floatlist = [] # Define an empty list of float numbers
    for x in splitlist:
        floatnum = float(x)  # onvert the string into float
        floatlist.append(floatnum)  # Add the float number to the floatlist
    print("Float list = ", floatlist)
    return floatlist


def calc_average(input_list):
    print("calc_average")
    total = sum(input_list)
    average = total/len(input_list)
    print("Average =", average)
    return average

def find_min_max(input_list):
    print("find_min_max")
    input_list.sort()
    resultlist = [input_list[0], input_list[-1]]
    return resultlist
    

def sort_temperature(input_list):
    print("sort_temperature")

def calc_median_temperature(input_list):
    print("calc_median_temperature")

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    floatlist = get_user_input()

if __name__ == "__main__":
    main()
