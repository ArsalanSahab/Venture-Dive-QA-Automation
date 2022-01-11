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

    my_list.sort()
   
    print(my_list)

# Question # 5 : Write a Program to sort a string/list in descending order?

def sort_list_dsc( my_list = [5, 9, 2, 5, 0, 5, 3, 1, 10] ) :

    my_list.sort(reverse=True)
    
    print(my_list)

# Question # 6 : Write a Program to find the Second Highest Number from an Array?

def get_second_highest( my_list = [5, 9, 2, 5, 0, 5, 3, 1, 10, 10] ) :

    # Step 1 Sort in Ascending
    my_list.sort()

    # COvert to Set to remove repititions

    my_set = set(my_list)

    # Convert Again

    my_list = list(my_set)

    print("Second Highest Number is : {}".format(my_list[-2]))
   

# Question # 7 : Write a Program to swap 2 integer values wihout using a third variable?

def swap_no_temp(num_a = 6, num_b = 2):

    print("I do not know how to solve this question")


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

   print("I do not know how to solve this question")

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