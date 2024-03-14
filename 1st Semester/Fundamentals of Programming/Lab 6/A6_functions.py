
from random import randrange

#------------------------------------------------------------------------------------------------------------------------------------------------------#

#Global Functions

def remove(complexelem):
    '''
    variables received: the list complexelem, which represents the sequence of complex numbers
    the program clears the list of all previous elements then returns the empty list
    '''
    complexelem.clear()
    return complexelem

def read_real():
    x = float(input("Select the real part: "))
    return x

def read_imag():
    y = float(input("Select the imaginary part: "))
    return y

def get_real(complexelem, n):
    return complexelem[n][0]

def get_imag(complexelem, n):
    return complexelem[n][1]

def do_check_subarray(sub, z):
    '''
    variables received: the list sub and the complex number z
    The program checks wether the element z is already placed within the list sub
    returns True when element z is in list sub and False if otherwise
    '''
    for i in range(0, len(sub)):
        if get_real(sub, i) == z[0] and z == get_imag(sub, i):
            return True
    return False

def do_subarray_4(complexelem):
    '''
    variables received: the list complexelem, which represents the sequence of complex numbers
    the program creates the sublist sub in which it creates the new subarray
    it then goes through all the elements of complexelem and checks wether that element is in sub using the check_subarray function. 
    The programm checks for 3 distinct elements using the nrdistinct variable. the moment it reaches 3, it no longer allows you to add
    distinct elements inside sub
    it returns sub and it's length, the complete subarray that does the exercise 4
    '''
    sub = []
    i = 0
    nrdistinct = 0
    while i < len(complexelem) and nrdistinct != 3 :
        if do_check_subarray(sub, complexelem[i]) == False:
            sub.append(complexelem[i])
            nrdistinct = nrdistinct + 1
        if do_check_subarray(sub, complexelem[i]) == True:
            sub.append(complexelem[i])
        i = i + 1
    return turn_to_string(complexelem), len(sub)

def do_subsequence_10(complexelem):
    '''
    variables received: the list complexelem representing the sequence of complex elements
    the program creates listsub, an auxilary list for which you check the longest increasing sequence and minisub in which you
    you place all possible subsequences. Within maximum length it stores tha maximum value within listsub and in subsequence it stores the
    list from minisub of max length
    returns the list subsequence and it's length within maximumlength
    '''
    length = len(complexelem)
    listsub = [1]*length
    minisub = [[] for i in range(length)]
    minisub[0].append(complexelem[0])
    for i in range(1, length):
        for j in range(0, i):
            if get_real(complexelem,j) < get_real(complexelem,i) and listsub[i] < listsub[j] + 1:
                listsub[i] = listsub[j]+1
                minisub[i] = minisub[j].copy()
        minisub[i].append(complexelem[i])
    subsequence = minisub[0]
    maximumlength = 0
    for i in range(length):
        maximumlength = max(maximumlength, listsub[i])
    for x in minisub:
        if len(x) > len(subsequence):
            subsequence = x
    return turn_to_string(complexelem), maximumlength

def turn_to_string(complexelem):
    final_string = ""
    for i in range(0, len(complexelem)):
        first_symbol = ""
        second_symbol = "+"
        existi = "i"
        if get_real(complexelem, i) < 0:
            first_symbol = "-"
        first_number = str(abs(get_real(complexelem, i)))
        if get_real(complexelem, i) == 0 and get_imag(complexelem, i) > 0:
            second_symbol = ""
        if get_imag(complexelem, i) < 0:
            second_symbol = "-"
        if get_imag(complexelem, i) == 0:
            existi = ""
        second_number = str(abs(get_imag(complexelem, i)))
        final_string+= first_symbol + first_number + second_symbol + second_number + existi
        if i != len(complexelem)-1:
            final_string += ", "
    return final_string
            
def set_real(complexelem, poz, x):
    complexelem[poz][0] = x
    return complexelem

def set_imag(complexelem, poz, y):
    complexelem[poz][1] = y
    return complexelem

#------------------------------------------------------------------------------------------------------------------------------------------------------#

#FUNCTIONS FOR LISTS

def create_list(complexelem):
    '''
    variables received: the list complexelem, which represents the sequence of complex numbers
    the program randomly creates real and imaginary values within x and y and creates the complex number z using x and y,
    then proceeds to add the complex number to the list
    returns the complete list with the added elements
    '''
    for i in range(0, 10):
        x = float(randrange(-100, 100))
        y = float(randrange(-100, 100))
        list = [x,y]
        complexelem.append(list)
    return complexelem

def read_list(complexelem, n):
    '''
    variables received: the list complexelem, which represents the sequence of complex numbers and n, a number inputed
    the program adds a number of n elements z which you input using the read_complex_number function. It proceeds to add the complex
    number to the list
    returns the complete list with the added elements
    '''
    for i in range(0, n):
        x = read_real()
        y = read_imag()
        list = [x,y]
        complexelem.append(list)
    return complexelem

#------------------------------------------------------------------------------------------------------------------------------------------------------#

#FUNCTIONS FOR DICTIONARIES

def create_dict(complexelem):
    '''
    variables received: the dictionary complexelem, which represents the sequence of complex numbers
    the program randomly creates real and imaginary values within x and y and creates the complex number z using x and y,
    then proceeds to add the complex number to the dictionary
    returns the complete dictionary with the added elements
    '''
    for i in range(0, 10):
        x = float(randrange(-100, 100))
        y = float(randrange(-100, 100))
        dict = {
            0: x,
            1: y
        }
        complexelem.append(dict)
    return complexelem

def read_dictionary(complexelem, n):
    '''
    variables received: the dictionary complexelem, which represents the sequence of complex numbers and n, a number inputed
    the program adds a number of n elements z which you input using the read_complex_number function. It proceeds to add the complex
    number to the dictionary
    returns the complete dictionary with the added elements
    '''
    for i in range(0, n):
        x = read_real()
        y = read_imag()
        dict = {x,y}
        complexelem.append(dict)
    return complexelem

#------------------------------------------------------------------------------------------------------------------------------------------------------#