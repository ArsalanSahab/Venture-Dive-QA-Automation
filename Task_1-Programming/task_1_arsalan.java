import java.io.*;
import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Scanner;

public class task_1_arsalan {

    // Question # 1 : Write a Program that takes two numbers as input and displays the product?
    static void display_product() {

        int num_a = 5;
        int num_b = 7;

        int product = num_a * num_b;

        System.out.println(String.format("Product of %d and %d is %d", num_a, num_b, product));
    }

    // Question # 2 : Write a Program to calculate the sum of two integers, and return true if the sum is equal to a third integer?
    static void sum_equals_third() {

        int num_a = 5, num_b = 7, num_c = 2;

        int sum = num_a + num_b;

        if( sum == num_c) {

            System.out.println(String.format("Sum of %d and %d is Equal to %d", num_a, num_b, num_c));
        }

        else {

            System.out.println(String.format("Sum of %d and %d is not Equal to %d", num_a, num_b, num_c));
        }
    }

    // Question # 3 : Write a Program to Reverse a String?

    static void reverse_string() {

        String str = "abcdef", rev_str = "";
        char character;

        for (int i = 0; i < str.length(); i++) {

            character = str.charAt(i);
            rev_str = character + rev_str;

        }

        System.out.println("Reversed String = " + rev_str);


    }

    // Question # 4 : Write a Program to sort the string/list in ascending order?

    static void sort_list_asc() {

        int[] my_list = new int[]{5, 9, 2, 5, 0, 5, 3, 1, 10};


        for (int x = 0; x < my_list.length; x++) {

            for (int y = x + 1; y < my_list.length; y++) {

                int temp = 0;

                if (my_list[x] > my_list[y]) {

                    temp = my_list[x];
                    my_list[x] = my_list[y];
                    my_list[y] = temp;
                }
            }

        }

        System.out.println("Sorted List = " + Arrays.toString(my_list));

    }

    // Question # 5 : Write a Program to sort the string/list in descending order?

    static void sort_list_dsc() {

        int[] my_list = new int[]{5, 9, 2, 5, 0, 5, 3, 1, 10};

        for (int x = 0; x < my_list.length; x++) {

            for (int y = x + 1; y < my_list.length; y++) {

                int temp = 0;

                if (my_list[x] < my_list[y]) {

                    temp = my_list[x];
                    my_list[x] = my_list[y];
                    my_list[y] = temp;
                }
            }

        }

        System.out.println("Sorted List = " + Arrays.toString(my_list));

    }

    // Question # 6 : Write a Program to find the Second Highest Number from an Array?
    static void get_second_highest() {

        // Sort List
        int[] my_list = new int[]{5, 9, 2, 5, 0, 5, 3, 1, 10, 10};


        for (int x = 0; x < my_list.length; x++) {

            for (int y = x + 1; y < my_list.length; y++) {

                int temp = 0;

                if (my_list[x] < my_list[y]) {

                    temp = my_list[x];
                    my_list[x] = my_list[y];
                    my_list[y] = temp;
                }
            }

        }

        // remove duplicates

        int length = my_list.length;
        int j = 0;
        for (int i=0; i < length - 1; i++){
            if (my_list[i] != my_list[i+1]){
                my_list[j++] = my_list[i];
            }
        }
        my_list[j++] = my_list[length-1];


        System.out.println("Second Highest Number is = " + my_list[1]);


    }

    // Question # 7 : Write a Program to swap 2 integer values wihout using a third variable?
    static void swap_no_temp() {

        int num_a = 7, num_b = 3;

        System.out.println(String.format("Number a = %d, Number b = %d", num_a, num_b));

        num_a = num_a + num_b;
        num_b = num_a - num_b;
        num_a = num_a - num_b;

        System.out.println(String.format("Number a = %d, Number b = %d", num_a, num_b));

    }

    // Question # 8 : Write a Progrm to find if given input number is Prime or Not?

    static void prime_or_not() {

        int num = 7;
        boolean isPrime = true;

        if(num > 1) {

            for(int i = 2; i < num; i++) {

                if(num % i == 0) {

                    isPrime = false;
                    break;

                }
            }
        }

        if(isPrime == true) {

            System.out.println(String.format("Input Number %d is a Prime", num));
        }

        else {

            System.out.println(String.format("Input Number %d is not a Prime", num));
        }
    }


    // Question # 9 : Write a Program to print a Pyramid?

    static void print_pyramid() {

        int num = 5;

        for(int x = 1; x <= num; ++x) {
            for(int y = 1; y <= x; ++y) {

                System.out.print(y + " ");
            }
            System.out.println();
        }

    }

    //  Question # 10 : Write a Program to Print if input number is even or odd?

    static void even_or_odd() {

        int num = 6;

        if(num % 2 == 0) {

            System.out.println(String.format("Number %d is Even", num));
        }

        else {

            System.out.println(String.format("Number %d is Odd", num));
        }
    }




    public static void main(String args[]) {

        System.out.println("Answer # 1");
        display_product();

        System.out.println("Answer # 2");
        sum_equals_third();

        System.out.println("Answer # 3");
        reverse_string();

        System.out.println("Answer # 4");
        sort_list_asc();

        System.out.println("Answer # 5");
        sort_list_dsc();

        System.out.println("Answer # 6");
        get_second_highest();

        System.out.println("Answer # 7");
        swap_no_temp();

        System.out.println("Answer # 8");
        prime_or_not();

        System.out.println("Answer # 9");
        print_pyramid();

        System.out.println("Answer # 10");
        even_or_odd();

    }


}
