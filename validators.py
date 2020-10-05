def ValidateSeasonYear(input):
  #  print(input)
    new_input = input.strip(' ')
    input = new_input
  #  print(input)
    length = len(input)
  #  print(length)
    if(length != 7):
        return False
    elif(length == 7):
        first = slice(0,2)
        new_one = input[first]
        second = slice(2,4)
        new_second = input[second]
        third = slice(4,5)
        new_third = input[third]
        fourth = slice(5,7)
        new_fourth = input[fourth]
        beg = 20
        convert_first = int(new_one)
        convert_second = int(new_second)
        convert_fourth = int(new_fourth)
        convert_third = input[third]
       # print(convert_first)
       # print(convert_second)
       # print(convert_fourth)
       # print()
        hyp = '-'
        if(convert_first == beg and convert_second == (convert_fourth-1) and hyp ==convert_third):
        #    print("here")
            return True
        else:
        #    print("not here")
            return False

def ValidatePositions(input):
    new_inp = input.replace(" ","")
  #  print(new_inp)
    if(new_inp.isalpha()):
        return True
    else:
        return False
