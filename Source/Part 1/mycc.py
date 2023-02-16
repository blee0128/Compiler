# Name: Benjamin Lee
# COMS540 - Spring 2023 Part 0

import sys

# Boolean to be set if valid flag is entered
argument_parsed = False

# Check that minimum argument is provided
if len(sys.argv) >= 3:
    if sys.argv[2] == "-0":
        print("My bare-bones Python compiler (for COMS 540)")
        print("\t\tWritten by Benjamin Lee (ben97@iastate.edu)")
        print("\t\tVersion 2.1 released 5 January 2023")
        argument_parsed = True
    elif sys.argv[2] == "-1":
        outer_file_name = sys.argv[3]
        include_line_num = 0

        class p1:
            def read_file(self, file_name):
                line_character_arr = []
                with open(file_name, 'r') as file:
                    for line in file:
                        x = list(line)
                        line_character_arr.append(x)
                        # y = line.split()
                        # include_character.append(y)
                    return line_character_arr

            def part_1(self, file_name, line_character, output, error, include_counter):
                keyword = {"const": 401, "struct": 402, "for": 403, "while": 404, "do": 405, "if": 406, "else": 407,
                           "break": 408, "continue": 409, "return": 410, "switch": 411, "case": 412, "default": 413}

                single_character = {"!": 33, "%": 37, "&": 38, "(": 40, ")": 41, "*": 42, "+": 43,
                                    ",": 44, "-": 45, ".": 46, "/": 47, ":": 58, ";": 59, "<": 60, "=": 61, ">": 62, "?": 63, "[": 91,
                                    "]": 93, "{": 123, "|": 124, "}": 125, "~": 126}

                two_character = {"==": 351, "!=": 352, ">=": 353, "<=": 354, "++": 355,
                                 "--": 356, "||": 357, "&&": 358, "+=": 361, "-=": 362, "*=": 363, "/=": 364}

                attributes = {"void": 301, "char": 301,
                              "int": 301, "float": 301}

                special_symbol = {"\"", '\t', '\\', '#', '\'', '_'}

                # check if #include exceeds the limit by recursively calling the function
                if include_counter > 256:
                    error_check = True
                    # error.append("Lexer error in file " + outer_file_name +
                    #              " line " + include_line_num + " at text #...")
                    # error.append("\tInclude depth exceeds limit")
                    sys.stderr.write("Lexer error in file " + outer_file_name +
                                     " line " + include_line_num + " at text #...")
                    sys.stderr.write("\n\tInclude depth exceeds limit")

                # str_start = start of reading a string, str_end = end of a string,
                # check_string = boolean variable set to True when it reach the start of a string and set to False when it reach the end of a string
                # string = character in a string
                str_start = [0, 0]
                str_end = [0, 0]
                check_string = False
                string = ""

                # alpha_start = start of reading an alphabet, alpha_end = end of reading an alphabet,
                # check_alphabet = boolean variable set to True when it reads an alphabet and False when it does not read an alphabet
                alpha_start = [0, 0]
                alpha_end = [0, 0]
                check_alphabet = False

                # char_start = start of reading a character, char_end = end of reading a character,
                # check_char = boolean variable set to True when it reads a character and False when it does not read a character
                # char = character
                char_start = [0, 0]
                char_end = [0, 0]
                check_char = False
                char = ""

                # comment_check = boolean variable set to True when it reads an open comment and sets back to False when it reads a close comment
                # start_comment_line = keep track of where the comment line starts
                comment_check = False
                start_comment_line = 0

                # check_twochar = boolean variable set to true when it reads a double character symbols
                # check_onechar = boolean variable set to true when it reads a single character symbols
                # two_char = storing the two character
                check_twochar = False
                check_onechar = False
                two_char = ""

                # digit_check = boolean variable set to true when it reads a digit
                # digit_start = start of reading a digit, digit_end = end of reading a digit
                # real_literal_check = boolean variable set to true when it is a real number
                digit_check = False
                digit_start = [0, 0]
                digit_end = [0, 0]
                real_literal_check = False

                # line_comment_check = boolean variable set to true when it reads the start of the line comment
                # open_comment_check = boolean variable set to true when it reads an opening comment
                # open_comment_check = boolean variable set to true when it reads a closing comment
                line_comment_check = False
                open_comment_check = False
                close_comment_check = False

                # check_include = boolean variable set to true when it reads #include
                check_include = False

                # error_check = boolean variable set to true when it reads an error
                error_check = False

                for i in range(len(line_character)):
                    # if error, just exit the for loop
                    if error_check == True:
                        break
                    for j in range(len(line_character[i])):
                        # check if this is an unexpected symbol. If yes, break and output an error
                        if(line_character[i][j] != ' ' and line_character[i][j] != '\n'):
                            if(line_character[i][j] not in single_character and line_character[i][j] not in special_symbol and line_character[i][j].isalpha() == False and line_character[i][j].isdigit() == False):
                                error_check = True
                                # error.append("Lexer error in file " +
                                #              file_name + " line " + str(i+1) + " at text " + line_character[i][j])
                                # error.append("\tUnexpected symbol")
                                sys.stderr.write("Lexer error in file " +
                                                 file_name + " line " + str(i+1) + " at text " + line_character[i][j])
                                sys.stderr.write("\n\tUnexpected symbol")
                                break
                        # check #include directives
                        if line_character[i][j] == '#' and comment_check == False:
                            include_line = line_character[i]
                            # include_symbol = boolean variable set to true when it reads the # symbol
                            # include_word_check = boolean variable set to true when it reads the "include" word
                            # start_file_path = boolean variable set to true when it starts reading the first double quotes
                            # open_include = boolean variable set to true when you have a complete include file in double quotes
                            # include_start = start of reading a double quote
                            # include_end = end of reading a double quote
                            include_symbol = False
                            include_word_check = False
                            start_file_path = False
                            open_include = False
                            include_start = 0
                            include_end = 0

                            for li in range(len(include_line)):
                                if include_line[li] == '#':
                                    include_symbol = True

                                if include_line[li] == 'i' and include_symbol == True:
                                    include_word = "".join(
                                        include_line[li:li+7])
                                    if include_word == "include":
                                        include_line_num = i
                                        include_word_check = True

                                if include_line[li] == '\"' and start_file_path == True:
                                    include_end = li
                                    start_file_path = False
                                    include_word_check = False
                                    include_symbol = False
                                    include_file_path = "".join(
                                        include_line[include_start+1:include_end])
                                    # include_file_path = "/Users/benjaminlee/Desktop/Spring 2023/COMS540/Project/Part 1/incld1.h"
                                    open_include = True
                                    break

                                if include_line[li] == '\"' and start_file_path == False and include_word_check == True:
                                    include_start = li
                                    start_file_path = True
                            # recursively calling part_1 function when it reads a # include and use the include files as its file path
                            # stores the output and error in a temp array
                            if open_include == True:
                                include_character_arr = []
                                temp_include_error = []
                                temp_output_error = []
                                try:
                                    include_character_arr = self.read_file(
                                        include_file_path)
                                    if "/" in include_file_path:
                                        temp_include_file_path = include_file_path.split(
                                            "/")
                                        include_file_path = temp_include_file_path[-1]
                                    include_counter += 1
                                    include_output = self.part_1(
                                        include_file_path, include_character_arr, temp_output_error, temp_include_error, include_counter)
                                    if include_output == []:
                                        error_check = True
                                        output = []
                                        break

                                    # store the output and error from the temp array into the main output and error array
                                    # check for error in the output given in the include file
                                    include_error = False
                                    for inc in include_output:
                                        if 'error' in str(inc):
                                            include_error = True
                                            error_check = True

                                    if include_error == False:
                                        for inc in include_output:
                                            output.append(inc)
                                    else:
                                        for inc in include_output:
                                            error.append(inc)

                                except:
                                    error_check = True
                                    # error.append("Lexer error in file " +
                                    #              file_name + " line " + str(i + 1) + " at text #incldue ....")
                                    # error.append(
                                    #     "\tCouldn't open file " + include_file_path)
                                    output = []
                                    sys.stderr.write("Lexer error in file " +
                                                     file_name + " line " + str(i + 1) + " at text #include ....")
                                    sys.stderr.write(
                                        "\n\tCouldn't open file " + include_file_path)
                                    return output
                            break

                        # check for C style comment or C++ comment
                        if (j + 1 < len(line_character[i])):
                            if (line_character[i][j] == '/' and line_character[i][j+1] == '*'):
                                comment_check == True
                                start_comment_line = i
                                continue

                            if (line_character[i][j] == '*' and line_character[i][j+1] == '/' and comment_check == True and open_comment_check == True):
                                close_comment_check = True
                                continue

                            if (line_character[i][j] == '/' and line_character[i][j+1] == '/' and check_string == False):
                                continue

                        if (line_character[i][j-1] == '/' and line_character[i][j] == '*'):
                            comment_check = True
                            open_comment_check = True
                            continue

                        if (line_character[i][j-1] == '*' and line_character[i][j] == '/' and comment_check == True and close_comment_check == True and open_comment_check == True):
                            comment_check = False
                            open_comment_check = False
                            close_comment_check = False
                            continue

                        if (line_character[i][j] == '/' and line_character[i][j+1] == '/' and check_string == False):
                            line_comment_check = True
                            continue

                        # if it sees a C++ comment, it will check if there are anything before the C++ comment and break
                        if (line_character[i][j-1] == '/' and line_character[i][j] == '/' and check_string == False):
                            if(check_alphabet == False and digit_check == False):
                                break

                            # check alphabet before the C++ comment
                            elif(check_alphabet == True):
                                alpha_end[1] = j - 1
                                check_alphabet = False
                                word = ""

                                for x in range(alpha_start[1], alpha_end[1]):
                                    word += line_character[alpha_start[0]][x]

                                if(word in attributes):
                                    if(check_string == False):
                                        value = attributes[word]
                                        output.append("File " + file_name + " Line " + str(i+1) + " Token " + str(value) +
                                                      " Text " + word)
                                        alpha_start = [0, 0]
                                        alpha_end = [0, 0]
                                elif(word in keyword):
                                    if(check_string == False):
                                        value = keyword[word]
                                        output.append("File " + file_name + " Line " + str(i+1) + " Token " + str(value) +
                                                      " Text " + word)
                                        alpha_start = [0, 0]
                                        alpha_end = [0, 0]
                                else:
                                    if(check_string == False):
                                        if(alpha_end[1] - alpha_start[1] > 48):
                                            error_check = True
                                            # error.append("Lexer error in file " +
                                            #              file_name + " line " + str(i+1) + " at text " + line_character[i][j])
                                            # error.append(
                                            #     "\tIdentifier is too long")
                                            sys.stderr.write("Lexer error in file " +
                                                             file_name + " line " + str(i+1) + " at text " + line_character[i][j])
                                            sys.stderr.write(
                                                "\n\tIdentifier is too long")
                                            break
                                        else:
                                            test_word = ""
                                            for ch in word:
                                                if(ch.isalpha() == True):
                                                    test_word += ch
                                                elif(ch.isalpha() == False and test_word != ""):
                                                    output.append("File " + file_name + " Line " + str(i+1) +
                                                                  " Token 306 Text " + test_word)
                                                    test_word = ""
                                            if(test_word != ""):
                                                output.append("File " + file_name + " Line " + str(i+1) +
                                                              " Token 306 Text " + test_word)
                                            alpha_start = [0, 0]
                                            alpha_end = [0, 0]
                                break

                            # check digit before the C++ comment
                            elif(digit_check == True):
                                digit_check = False
                                digit_end[0] = i
                                digit_end[1] = j - 1

                                # output error if integer or real literals is too long
                                if(digit_end[1] - digit_start[1] > 48 and real_literal_check == False):
                                    error_check = True
                                    # error.append("Lexer error in file " +
                                    #              file_name + " line " + str(i+1) + " at text " + line_character[i][j])
                                    # error.append(
                                    #     "\tInteger literals is too long")
                                    sys.stderr.write("Lexer error in file " +
                                                     file_name + " line " + str(i+1) + " at text " + line_character[i][j])
                                    sys.stderr.write(
                                        "\n\tInteger literals is too long")
                                    break
                                if(digit_end[1] - digit_start[1] > 48 and real_literal_check == True):
                                    error_check = True
                                    # error.append("Lexer error in file " +
                                    #              file_name + " line " + str(i+1) + " at text " + line_character[i][j])
                                    # error.append("\tReal literal is too long")
                                    sys.stderr.write("Lexer error in file " +
                                                     file_name + " line " + str(i+1) + " at text " + line_character[i][j])
                                    sys.stderr.write(
                                        "\n\tReal literal is too long")
                                    break

                                number = ""

                                for num in range(digit_start[1], digit_end[1]):
                                    number += line_character[digit_start[0]][num]

                                if(real_literal_check == True):
                                    output.append("File " + file_name + " Line " + str(i+1) + " Token 304" +
                                                  " Text " + number)
                                else:
                                    output.append("File " + file_name + " Line " + str(i+1) + " Token 303" +
                                                  " Text " + number)

                                real_literal_check = False
                                number = ""
                                break

                        if(comment_check == False and check_include == False):
                            # check character
                            # check for closing ' in a character literal
                            if(j - char_start[1] == 2 and check_char == True):
                                if(line_character[i][j] != "\'" and line_character[i][char_start[1] + 1] != "\\"):
                                    error_check = True
                                    # error.append("Lexer error in file " +
                                    #              file_name + " line " + str(char_start[0] + 1) + " at text " + str(line_character[char_start[0]][char_start[1]]) + str(line_character[char_start[0]][char_start[1]+1]))
                                    # error.append(
                                    #     "\tExpected closing ' for character literal.")
                                    sys.stderr.write("Lexer error in file " +
                                                     file_name + " line " + str(char_start[0] + 1) + " at text " + str(line_character[char_start[0]][char_start[1]]) + str(line_character[char_start[0]][char_start[1]+1]))
                                    sys.stderr.write(
                                        "\n\tExpected closing ' for character literal.")

                            if(j - char_start[1] == 3 and check_char == True):
                                if(line_character[i][j] != "\'"):
                                    error_check = True
                                    # error.append("Lexer error in file " +
                                    #              file_name + " line " + str(char_start[0] + 1) + " at text " + str(line_character[char_start[0]][char_start[1]]) + str(line_character[char_start[0]][char_start[1]+1]) + str(line_character[char_start[0]][char_start[1]+2]))
                                    # error.append(
                                    #     "\tExpected closing ' for character literal.")
                                    sys.stderr.write("Lexer error in file " +
                                                     file_name + " line " + str(char_start[0] + 1) + " at text " + str(line_character[char_start[0]][char_start[1]]) + str(line_character[char_start[0]][char_start[1]+1]) + str(line_character[char_start[0]][char_start[1]+2]))
                                    sys.stderr.write(
                                        "\n\tExpected closing ' for character literal.")

                            if (line_character[i][j] == "\'" and comment_check == False):
                                # output character lietral for '\'' case
                                if(line_character[i][j] == "\'" and line_character[i][j-1] == "\'" and line_character[i][j-2] == "\\" and line_character[i][j-3] == "\'"):
                                    char = "\'\\\'\'"
                                    output.append("File " + file_name + " Line " + str(i+1) + " Token 302" +
                                                  " Text " + char)
                                    char_start = [0, 0]
                                    char_end = [0, 0]
                                    check_char = False
                                    continue

                                # reads the start of a character lietral
                                if(check_char == False):
                                    char_start[0] = i
                                    char_start[1] = j
                                    check_char = True
                                else:
                                    if(j+1 > len(line_character[i]) or line_character[i][j+1] != "\'" or line_character[i][j+1] == " "):
                                        char_end[0] = i
                                        char_end[1] = j
                                        check_char = False

                                        # output character lietral
                                        if (char_end[1] - char_start[1] == 2):
                                            temp_char = "".join(
                                                line_character[char_start[0]][char_start[1]:char_end[1]+1])
                                            char = temp_char
                                            output.append("File " + file_name + " Line " + str(i+1) + " Token 302" +
                                                          " Text " + char)
                                            char = ""
                                        elif (char_end[1] - char_start[1] == 3):
                                            # extra credit features for character literals
                                            escape = [
                                                'a', 'b', 'n', 'r', 't', '\\']
                                            if(line_character[char_start[0]][char_start[1] + 1] == '\\' and line_character[char_start[0]][char_start[1] + 2] in escape):
                                                temp_char = "".join(
                                                    line_character[char_start[0]][char_start[1]:char_end[1]+1])
                                                char = temp_char
                                                output.append("File " + file_name + " Line " + str(i+1) + " Token 302" +
                                                              " Text " + char)
                                                char = ""
                                            else:
                                                error_check = True
                                                # error.append("Lexer error in file " +
                                                #              file_name + " line " + str(i+1) + " at text " + line_character[i][j])
                                                # error.append(
                                                #     "character literal error")
                                                sys.stderr.write("Lexer error in file " +
                                                                 file_name + " line " + str(i+1) + " at text " + line_character[i][j])
                                                sys.stderr.write(
                                                    "\n\tCharacter literal error")

                            # check string
                            if (line_character[i][j] == "\"" and comment_check == False):
                                # start of the string, set boolean variable to True
                                if(check_string == False):
                                    str_start[0] = i
                                    str_start[1] = j
                                    check_string = True
                                else:
                                    # extra credit features for string literals
                                    # allow escape sequences
                                    if(line_character[i][j] == "\"" and line_character[i][j-1] == "\\" and line_character[i][j-2] == "\\"):
                                        pass
                                    elif(line_character[i][j] == "\"" and line_character[i][j-1] == "\\"):
                                        continue
                                    str_end[0] = i
                                    str_end[1] = j
                                    check_string = False

                                    # output error if string literals exceeds limit
                                    if(str_end[1] - str_start[1] > 48):
                                        error_check = True
                                        # error.append("Lexer error in file " +
                                        #              file_name + " line " + str(i+1) + " at text " + line_character[i][j])
                                        # error.append(
                                        #     "String literal exceeds limits")
                                        sys.stderr.write("Lexer error in file " +
                                                         file_name + " line " + str(i+1) + " at text " + line_character[i][j])
                                        sys.stderr.write(
                                            "\n\tString literal exceeds limits")
                                        break

                                    # output string literal
                                    if str_start[0] == str_end[0]:
                                        firstpart = "".join(
                                            line_character[str_start[0]][str_start[1]:str_end[1]+1])
                                        string = firstpart
                                        output.append("File " + file_name + " Line " + str(i+1) + " Token 305" +
                                                      " Text " + string)
                                        string = ""
                                    else:
                                        firstpart = "".join(
                                            line_character[str_start[0]][str_start[1]:])
                                        string = firstpart
                                        if(str_end[0] - str_start[0] == 1):
                                            secondpart = "".join(
                                                line_character[str_start[0]+1][:str_end[1]+1])
                                            string += secondpart
                                            output.append("File " + file_name + " Line " + str(i+1) + " Token 305" +
                                                          " Text " + string)
                                            firstpart = ""
                                            secondpart = ""
                                            string = ""
                                        else:
                                            for p in range(str_start[0]+1, str_end[0]):
                                                secondpart = "".join(
                                                    line_character[p][:])
                                                string += secondpart
                                                secondpart = ""
                                            lastpart = "".join(
                                                line_character[str_end[0]][:str_end[1]+1])
                                            string += lastpart
                                            output.append("File " + file_name + " Line " + str(i+1) + " Token 305" +
                                                          " Text " + string)
                                            firstpart = ""
                                            secondpart = ""
                                            lastpart = ""
                                            string = ""

                            # check if it is a digit
                            # start of a digit, set boolean variable to True
                            if((line_character[i][j] >= '0' and line_character[i][j] <= '9') and digit_check == False and check_alphabet == False and check_string == False and check_char == False and comment_check == False):
                                digit_check = True
                                digit_start[0] = i
                                digit_start[1] = j

                            # check if it is a real literal
                            # extra credit features for real literals
                            if((line_character[i][j] == '.' or line_character[i][j] == 'e' or line_character[i][j] == 'E') and digit_check == True and comment_check == False):
                                if(line_character[i][j] == 'e' or line_character[i][j] == 'E'):
                                    if(line_character[i][j+1] >= '0' and line_character[i][j+1] <= '9'):
                                        real_literal_check = True
                                    elif((line_character[i][j+1] == '+' or line_character[i][j+1] == '-') and line_character[i][j+2] >= '0' and line_character[i][j+2] <= '9'):
                                        real_literal_check = True
                                    else:
                                        error_check = True
                                        num_error = ""

                                        for no in range(digit_start[1], digit_start[1] + 5):
                                            num_error += line_character[digit_start[0]][no]

                                        # output error for wrong real literals pattern
                                        # error.append("Lexer error in file " +
                                        #              file_name + " line " + str(i+1) + " at text " + num_error + "...")
                                        # error.append("real literals error")
                                        sys.stderr.write("Lexer error in file " +
                                                         file_name + " line " + str(i+1) + " at text " + num_error + "...")
                                        sys.stderr.write(
                                            "\n\tReal literals error")
                                        break
                                else:
                                    real_literal_check = True

                            # check the end of an integer or real literal
                            if(not((line_character[i][j] >= '0' and line_character[i][j] <= '9') or line_character[i][j] == '.' or line_character[i][j] == 'e' or line_character[i][j] == 'E' or line_character[i][j] == '-' or line_character[i][j] == '+') and digit_check == True and check_alphabet == False and check_string == False and check_char == False and comment_check == False):
                                digit_check = False
                                digit_end[0] = i
                                digit_end[1] = j
                                num_error1 = ""

                                # output error for integer literals that is too long
                                if(digit_end[1] - digit_start[1] > 48 and real_literal_check == False):
                                    error_check = True

                                    for no1 in range(digit_start[1], digit_start[1] + 5):
                                        num_error1 += line_character[digit_start[0]][no1]

                                    # error.append("Lexer error in file " +
                                    #              file_name + " line " + str(i+1) + " at text " + num_error1 + "...")
                                    # error.append(
                                    #     "\tInteger literals is too long")
                                    sys.stderr.write("Lexer error in file " +
                                                     file_name + " line " + str(i+1) + " at text " + num_error1 + "...")
                                    sys.stderr.write(
                                        "\n\tInteger literals is too long")
                                    break

                                # output error for real literals that is too long
                                if(digit_end[1] - digit_start[1] > 48 and real_literal_check == True):
                                    error_check = True
                                    # error.append("Lexer error in file " +
                                    #              file_name + " line " + str(i+1) + " at text " + num_error1 + "...")
                                    # error.append("\tReal literal is too long")
                                    sys.stderr.write("Lexer error in file " +
                                                     file_name + " line " + str(i+1) + " at text " + num_error1 + "...")
                                    sys.stderr.write(
                                        "\n\tReal literals is too long")
                                    break

                                number = ""

                                for num in range(digit_start[1], digit_end[1]):
                                    number += line_character[digit_start[0]][num]

                                # output integer literals or real literals
                                if(real_literal_check == True):
                                    output.append("File " + file_name + " Line " + str(i+1) + " Token 304" +
                                                  " Text " + number)
                                else:
                                    output.append("File " + file_name + " Line " + str(i+1) + " Token 303" +
                                                  " Text " + number)

                                real_literal_check = False
                                number = ""

                            # check for identifier, type or keywords
                            # start of reading an alphabet by using .isalpha()
                            if(line_character[i][j].isalpha() == True and line_character[i][j] != '_' and check_alphabet == False and check_string == False and check_char == False and digit_check == False and comment_check == False):
                                alpha_start[0] = i
                                alpha_start[1] = j
                                check_alphabet = True

                            # end of reading an alphabet by using .isalpha()
                            if(line_character[i][j].isalpha() == False and line_character[i][j] != '_' and check_alphabet == True and check_char == False and digit_check == False and comment_check == False):
                                alpha_end[0] = i
                                alpha_end[1] = j
                                check_alphabet = False
                                word = ""

                                for x in range(alpha_start[1], alpha_end[1]):
                                    word += line_character[alpha_start[0]][x]

                                # check if the word is an attribute or keyword
                                # otherwise, it will be considered an identifier
                                if(word in attributes):
                                    if(check_string == False):
                                        value = attributes[word]
                                        output.append("File " + file_name + " Line " + str(i+1) + " Token " + str(value) +
                                                      " Text " + word)
                                        alpha_start = [0, 0]
                                        alpha_end = [0, 0]
                                elif(word in keyword):
                                    if(check_string == False):
                                        value = keyword[word]
                                        output.append("File " + file_name + " Line " + str(i+1) + " Token " + str(value) +
                                                      " Text " + word)
                                        alpha_start = [0, 0]
                                        alpha_end = [0, 0]
                                else:
                                    if(check_string == False):
                                        if(alpha_end[1] - alpha_start[1] > 48):
                                            error_check = True
                                            # error.append("Lexer error in file " +
                                            #              file_name + " line " + str(i+1) + " at text " + word[:5] + "...")
                                            # error.append(
                                            #     "\tIdentifier is too long")
                                            sys.stderr.write("Lexer error in file " +
                                                             file_name + " line " + str(i+1) + " at text " + word[:5] + "...")
                                            sys.stderr.write(
                                                "\n\tIdentifier is too long")
                                            break
                                        else:
                                            test_word = ""
                                            for ch in word:
                                                if(ch.isalpha() == True):
                                                    test_word += ch
                                                elif(ch.isalpha() == False and ch == "_"):
                                                    test_word += ch
                                                elif(ch.isalpha() == False and test_word != ""):
                                                    if(test_word in attributes):
                                                        value = attributes[test_word]
                                                        output.append("File " + file_name + " Line " + str(i+1) + " Token " + str(value) +
                                                                      " Text " + test_word)
                                                    elif(test_word in keyword):
                                                        value = keyword[test_word]
                                                        output.append("File " + file_name + " Line " + str(i+1) + " Token " + str(value) +
                                                                      " Text " + test_word)
                                                    else:
                                                        output.append("File " + file_name + " Line " + str(i+1) +
                                                                      " Token 306 Text " + test_word)
                                                    test_word = ""
                                            if(test_word != ""):
                                                output.append("File " + file_name + " Line " + str(i+1) +
                                                              " Token 306 Text " + test_word)
                                            alpha_start = [0, 0]
                                            alpha_end = [0, 0]

                            # check for single character symbols and operator with two characters
                            if(line_character[i][j] in single_character and check_string == False and check_char == False and digit_check == False and comment_check == False):
                                if(j + 1 < len(line_character[i])):
                                    if(line_character[i][j+1] in single_character and check_twochar == False):
                                        two_char = str(
                                            line_character[i][j]) + str(line_character[i][j+1])
                                        if(two_char in two_character):
                                            check_twochar = True
                                            continue
                                        check_onechar = True
                                    else:
                                        check_onechar = True
                                else:
                                    if(check_onechar == False):
                                        check_onechar = True

                                # output two character symbols as operator
                                if(line_character[i][j-1] in single_character and check_twochar == True):
                                    check_twochar = False
                                    check_onechar = False
                                    value = two_character[two_char]
                                    output.append("File " + file_name + " Line " + str(i+1) +
                                                  " Token " + str(value) + " Text " + two_char)
                                    two_char = ""
                                    continue

                            # check for single character symbols
                            # output the single character symbols
                            if (check_onechar == True):
                                check_onechar = False
                                value = single_character[line_character[i][j]]
                                output.append("File " + file_name + " Line " + str(i+1) + " Token " + str(value) +
                                              " Text " + line_character[i][j])
                    line_comment_check = False

                # check if there is an opening string but no closing string
                if(check_string == True):
                    error_check = True
                    # error.append("Lexer error in file " +
                    #              file_name + " line " + str(str_start[0] + 1) + " at text \"...")
                    # error.append("\tUnclosed string")
                    sys.stderr.write("Lexer error in file " +
                                     file_name + " line " + str(str_start[0] + 1) + " at text \"...")
                    sys.stderr.write("\n\tUnclosed string")

                # check if there is an opening comment but no closing comment
                if(comment_check == True):
                    error_check = True
                    # error.append("Lexer error in file " +
                    #              file_name + " line " + str(start_comment_line + 1) + " at text /*")
                    # error.append("\tUnclosed comment.")
                    sys.stderr.write("Lexer error in file " +
                                     file_name + " line " + str(start_comment_line + 1) + " at text /*")
                    sys.stderr.write("\n\tUnclosed comment.")

                if error_check == True:
                    output = []
                return output

            def run_p1(self, outer_file_name):
                error_file = []
                output_file = []

                read = self.read_file(outer_file_name)
                final_output = self.part_1(outer_file_name, read,
                                           output_file, error_file, 0)

                new_file = outer_file_name.split(".")
                new_file = new_file[0]
                if final_output != []:
                    f = open(str(new_file) + ".lexer", "w")
                    for j in output_file:
                        f.write(j + "\n")
                    f.close()

        new_p = p1()
        new_p.run_p1(outer_file_name)
        argument_parsed = True

# Print usage if argument is not parsed
if not(argument_parsed):
    print("Usage:")
    print("\t\tmycc -mode infile")
    print("Valid modes: ")
    print("\t\t-0: Version information only")
    print("\t\t-1: Part 1: Create a lexer for C")
