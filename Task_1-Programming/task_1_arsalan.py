'''
Venture Dive Task # 1

'''

# Question # 1 : Write a Program that takes two numbers as input and displays the product?
def display_product(num_a = 5, num_b = 7) :

    product = num_a * num_b
    print(product)


# Question # 2 : Write a Program to calculate the sum of two integers, and return true if the sum is equal to a third integer?
def sum_equals_third(num_a = 3, num_b = 6, num_c = 13) :

    sum = num_a + num_b

    if(sum == num_c) :
        print("The sum for {} and {} is Equal to {}".format(num_a, num_b, num_c))
        
    else :
        print("The sum for {} and {} does not Equal {}".format(num_a, num_b, num_c))

# Question # 3 : Write a Program to Reverse a String?
def reverse_string(str = "abcdef") :

    str_rev = str[::-1]
    print(str_rev)


# Question # 4 : Write a Program to sort the string/list in ascending order?

def sort_list_asc( my_list = [5, 9, 2, 5, 0, 5, 3, 1, 10] ) :

    sorted_list = []

    while my_list:

        cur_min_num = my_list[0]
        for num in my_list:
            if num < cur_min_num:
                cur_min_num = num
        sorted_list.append(cur_min_num)
        my_list.remove(cur_min_num)
   
    print(sorted_list)

# Question # 5 : Write a Program to sort a string/list in descending order?

def sort_list_dsc( my_list = [5, 9, 2, 5, 0, 5, 3, 1, 10] ) :

    sorted_list = []

    while my_list:

        cur_max_num = my_list[-1]

        for num in my_list:
            if num > cur_max_num:
                cur_max_num = num
        sorted_list.append(cur_max_num)
        my_list.remove(cur_max_num)
    
    print(sorted_list)

# Question # 6 : Write a Program to find the Second Highest Number from an Array?

def get_second_highest( my_list = [5, 9, 2, 5, 0, 5, 3, 1, 10, 10] ) :

    # Step 1 Sort in Descending
    
    sorted_list = []

    while my_list:

        cur_max_num = my_list[-1]

        for num in my_list:
            if num > cur_max_num:
                cur_max_num = num
        sorted_list.append(cur_max_num)
        my_list.remove(cur_max_num)

    # Remove repititions

    new_list =[]
    for num in sorted_list:
        if num not in new_list:
            new_list.append(num)

    print("Second Highest Number is : {}".format(new_list[1]))
   

# Question # 7 : Write a Program to swap 2 integer values wihout using a third variable?

def swap_no_temp(num_a = 6, num_b = 2):

    print("First Number is {}, Second Number is {}".format(num_a, num_b))

    num_a = num_a + num_b
    num_b = num_a - num_b
    num_a = num_a - num_b


    print("After Swapping, First Number is {}, Second Number is {}".format(num_a,num_b))


# Question # 8 : Write a Progrm to find if given input number is Prime or Not?

def prime_or_not(num = 7):

    isPrime = True

    # Check for Greater than 1
    if num > 1 :
        # Loop till num
        for i in range(2, num):
            if(( num % i ) == 0 ):
                isPrime = False
                break

    if( isPrime == True) :

        print("Input Number {} is a Prime".format(num))
    else :
        print("Input Number {} is Not a Prime".format(num))

# Question # 9 : Write a Program to print a Pyramid?

def print_pyramid(num = 6):

   for x in range(1,num):

       for y in range(1,x+1):
           print(y, end='')

       print('\r')

# Question # 10 : Write a Program to Print if input number is even or odd?

def even_or_odd(num = 6):

    if(num % 2 == 0) :
        print("Input Number {} is Even".format(num))
    else :
        print("Input Number {} is Odd".format(num))


def main() :

    print("Answer # 1")
    display_product()

    print("Answer # 2")
    sum_equals_third()

    print("Answer # 3")
    reverse_string()

    print("Answer # 4")
    sort_list_asc()

    print("Answer # 5")
    sort_list_dsc()

    print("Answer # 6")
    get_second_highest()

    print("Answer # 7")
    swap_no_temp()

    print("Answer # 8")
    prime_or_not()

    print("Answer # 9")
    print_pyramid()

    print("Answer # 10")
    even_or_odd()

if __name__ == '__main__' :
    main()