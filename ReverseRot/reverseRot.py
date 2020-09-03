'''
---------------------------------------
    Author: Runquan(Jerry) Ye
    Date: October 2018
---------------------------------------
'''
#character is the input chararcter
#reverseNum is the reverse space
def reverse(character, reverseNum):

    #set up the list scheme
    letter = ["A", "B", 'C', 'D', 'E', 'F',  'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
     'T', 'U', 'V' ,'W' , 'X', 'Y' , 'Z' ,'_', '.']

    #the upper() method makes sure chararcter will be a capital letter
    character = character.upper()

    #create a output array
    output = []

    #use for loop to reverse each element from the input string, and put into output
    for i in character:
        if(i in letter):
            output.append(letter[(letter.index(i) + int(reverseNum)) % len(letter)])

    #reverse the output list
    output.reverse()

    #print out the output array elements without space, as a string.
    return(''.join(str(i) for i in output))



def main(inputFile):
    #open file in the read mode
    file = open(inputFile, "r")

    #read the file content lines by lines
    lines = file.readlines()
    #lines = file.read()

    #create veriable to hold the read string and read reverseNum
    reverseSpace = None
    reverseString = None

    #create an array to hold the result
    result = []
    
    for elements in lines:
        for word in elements.split(' '):
            #is_integer() method the element is or is not an is_integer
            #  -Note: in is_integer() method "5" and "5.0" and consider to be true, "5.1" is false
            #-------------------------------------------------------------------------------------
            #isinstance(input_element, input_type), return True or False
            #  -Note: in this method isinstance(25, int) -> True
            #                        isinstance(25.0, int) -> False
            #                        isinstance("25", int) -> False
            #------------------------------------------------------------------------------------
            #isdigit() method check the element is really an is_integer
            #  -Note: "2".isdigit() -> True
            #         "2.0".isdigit() -> False
            if(word.isdigit()):
                if(int(word) == 0):
                    break
                else:
                    reverseSpace = int(word)
            else:
                reverseString = word

            if(reverseSpace is not None and reverseString is not None):
                result.append(reverse(reverseString, reverseSpace))
                reverseSpace = None
                reverseString = None
                
    #print out the result split with newline
    print('\n'.join(str(i) for i in result))

    #close the file
    file.close()





if __name__ == "__main__":
    main("reverseRotInput.txt")
