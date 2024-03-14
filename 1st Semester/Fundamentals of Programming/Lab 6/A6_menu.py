import A6_functions 

#------------------------------------------------------------------------------------------------------------------------------------------------------#

def menu():

#------------------------------------------------------------------------------------------------------------------------------------------------------#

    complexelemlist = []
    complexelem = A6_functions.create_list(complexelemlist)
    print()
    complexelemdict = []
    complexelem = A6_functions.create_dict(complexelemdict)
    

#------------------------------------------------------------------------------------------------------------------------------------------------------#

    ok = True
    while ok == True:

        print("Select one of these keys below in order to progress:")
        print("1. Read or set complex numbers")
        print("2. Display the list from the console")
        print("3. Find the length and elements of a longest subarray of numbers that contain at most 3 distinct values OR ")
        print("Find the length and elements of a longest increasing subsequence, when considering each number's real part")
        print("4. Exit the application")
        choice = input("Select now: ")
        print()

#------------------------------------------------------------------------------------------------------------------------------------------------------#
       
        if choice == '1':

            print("a. Read complex numbers")
            print("b. Set complex numbers")
            print("Select wether you want to do the first or second exercise. In order to do that, press a or b")
            exchoice = input("Select now: ")
            exok = True
            if exchoice == 'a':
                n = int(input("select how many elements you want to read: "))
                print()
                exexchoice = input("Press 1 if you wish to remove the old numbers, any other key if not: ")
                print()

                if exexchoice == '1':
                    print("The dictionary and the list are now empty.")
                    complexelemlist = A6_functions.remove(complexelemlist)
                    complexelemdict = A6_functions.remove(complexelemdict)
                    print(A6_functions.turn_to_string(complexelemdict))
                    print(A6_functions.turn_to_string(complexelemlist))
                print("reading into the list...")
                complexelemlist = A6_functions.read_list(complexelemlist, n)
                print()
                print("Reading into dictionary...")
                complexelemdict = A6_functions.read_dictionary(complexelemdict, n)
                print("Reading into dictionary and list completed.")
                print()
            elif exchoice == 'b':
                print()
                n = int(input("Select how many elements you want to set: "))
                print()
                i = 0
                while i < n:
                    poz = int(input("Select the position on which you wish to set the number: "))
                    if poz < len(complexelemlist):
                        exexchoice = input("Press Y if you wish to set the real part of a number, any other key if you don't: ")
                        if exexchoice == 'Y':
                            x = float(input("Select the real part: "))
                            complexelemlist = A6_functions.set_real(complexelemlist, n, x)
                            complexelemdict = A6_functions.set_real(complexelemdict, n, x)
                        exexchoice = input("Press Y if you wish to set the iamginary part of a number, any other key if you don't: ")
                        if exexchoice == 'Y':
                            y = float(input("Select the imaginary part: "))
                            complexelemdict = A6_functions.set_imag(complexelemdict, n, y)
                            complexelemlist = A6_functions.set_imag(complexelemlist, n, y)
                    else:
                        print("You did not choose a valid position")
                        i = i - 1
                    print()
                    i = i + 1

#------------------------------------------------------------------------------------------------------------------------------------------------------#
        
        elif choice == '2':
            print("The current list of complex numbers is: ")
            print(complexelemlist)
            print()
            print("The current dictionary of complex numbers is: ")
            print(complexelemdict)
            print()

#------------------------------------------------------------------------------------------------------------------------------------------------------#
       
        elif choice == '3':

            print("a. Find the length and elements of a longest subarray of numbers that contain at most 3 distinct values")
            print("b. Find the length and elements of a longest increasing subsequence, when considering each number's real part")
            print("Select wether you want to do the first or second exercise. In order to do that, press a or b")
            exchoice = input("Select now: ")
            exok = True
            print()

            while exok == True:
                if exchoice == 'a':
                    print("The subarray selected from the list and it's length are: ")
                    print(A6_functions.do_subarray_4(complexelemlist))
                    print()
                    print("The subarray selected from the list is: ")
                    print(A6_functions.do_subarray_4(complexelemdict))
                    exok = False
                elif exchoice == 'b':
                    print("The subsequence selected from the list and it's length are: ")
                    print(A6_functions.do_subsequence_10(complexelemlist))
                    print()
                    print("The subsequence selected from the list and it's length are: ")
                    print(A6_functions.do_subsequence_10(complexelemdict))
                    exok = False
                else:
                    print("Select one of the 2 keys above.")
                print()

#------------------------------------------------------------------------------------------------------------------------------------------------------#
       
        elif choice == '4':

            exchoice = input("Are you sure? Y/N ")

            if exchoice == 'Y':
                ok = False
                print("Closing the program. Thank you!")
            elif exchoice == 'N':
                print("Resuming the program")
            else:
                print("Select one of the keys above")
                print()
        else: 
            print("Select one of the keys above")
            print()

#------------------------------------------------------------------------------------------------------------------------------------------------------#

menu()