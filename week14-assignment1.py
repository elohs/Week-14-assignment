# Ethan Lohs
# Week14-Assignment1

# This program inputs names of states from a given file, states.txt, and 
# turns the contents of the file into a list. After this, the program
# alphabetically orders the names of states, then turns them back into
# a string. It then takes this string of state's names and outputs them
# to a new file.

# This is the function that this program uses.
def main():
    # Here the input file is opened in read mode.
    input_file = open('states.txt' , 'r')

    # The variable is created to represent the contents of the input
    # file and hold this info in RAM after this file is closed. The
    # date from the file is read line by line.
    states_file_contents = input_file.readlines()

    # Here the data from the file is put into alphabetical order.
    states_file_contents.sort()

    # This print statement is here to help verify that what I 
    # intend to happen is happening.
    print(states_file_contents)

    # The input file is closed.
    input_file.close()

    # This is a variable created for use in converting the list back to a string.
    sorted_string = ""

    # This for loop converts the ordered data from the input file back into a string.
    for state in states_file_contents:
        sorted_string += state

    # This is another point where I am validating what is happening to the data.
    print(sorted_string)    

    # Here a new file is created. This file will accepted the ordered list of state
    # names that is now converted back to a string. This file is opened in write 
    # mode.
    output_file = open('ordered_states.txt' , 'w')

    # The sorted data in a string is written into the new file.
    output_file.write(sorted_string)

    # Here the output file is closed.
    output_file.close()

# The function is called, this is the main body of the program.
main()    