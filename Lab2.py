

def display_main_menu():
    print("display_main-menu")
    print("Enter some numbers separated by commas (e.g. 5,67,32)")

def get_user_input():
    print("get_user_input")
    inputstr = input()
    print("Raw Input = " + inputstr)

    #split the input string into segments of strings using comma as spliiter
    splitlist = inputstr.split(",") 
    print("After splitting = ", splitlist)

    #Next step is to convert each short string in the list into float
    floatlist = [] #define an empty list of float numbers
    for x in splitlist:
        floatnum = float(x)  #Convert string into float
        floatlist.append(floatnum)  #Add the float to the floatlist
    print("floatlist = ", floatlist)    
    return floatlist

def cal_average(input_list):
    print("calc_average")

def find_min_max(input_list):
    print("find_min_max")

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
