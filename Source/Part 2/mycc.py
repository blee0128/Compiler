# Name: Benjamin Lee
# COMS540 - Spring 2023 Part 2

import sys

# Boolean to be set if valid flag is entered
argument_parsed = False

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
        real_literal_dot_check = False

        # line_comment_check = boolean variable set to true when it reads the start of the line comment
        # open_comment_check = boolean variable set to true when it reads an opening comment
        # open_comment_check = boolean variable set to true when it reads a closing comment
        line_comment_check = False
        open_comment_check = False
        close_comment_check = False
        open_comment_check_num = 0
        close_comment_check_num = 0

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

                if comment_check == True and (check_alphabet == True or digit_check == True):
                    if(check_alphabet == True):
                        alpha_end[1] = j - 2
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

                    # check digit before the C++ comment
                    elif(digit_check == True):
                        digit_check = False
                        digit_end[0] = i
                        digit_end[1] = j - 2

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

                # check for C style comment or C++ comment
                if (j + 1 < len(line_character[i])):
                    if (line_character[i][j] == '/' and line_character[i][j+1] == '*' and comment_check == False):
                        comment_check = True
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
                    # open_comment_check_num += 1
                    continue

                if (line_character[i][j-1] == '*' and line_character[i][j] == '/' and comment_check == True and close_comment_check == True and open_comment_check == True):
                    # close_comment_check_num += 1
                    # if open_comment_check_num == close_comment_check_num:
                    comment_check = False
                    open_comment_check = False
                    close_comment_check = False
                    # open_comment_check_num = 0
                    # close_comment_check_num = 0
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

                    if (line_character[i][j] == "\'" and comment_check == False and check_string == False):
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

                        # check for identifier, type or keywords
                    # start of reading an alphabet by using .isalpha()
                    if((line_character[i][j].isalpha() == True or line_character[i][j] == '_') and check_alphabet == False and check_string == False and check_char == False and digit_check == False and comment_check == False):
                        alpha_start[0] = i
                        alpha_start[1] = j
                        check_alphabet = True

                    # end of reading an alphabet by using .isalpha()
                    if(line_character[i][j].isalpha() == False and line_character[i][j] != '_' and check_alphabet == True and check_char == False and digit_check == False and comment_check == False):
                        if(line_character[i][j] >= '0' and line_character[i][j] <= '9'):
                            continue
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
                                        elif(ch.isalpha() == False and ch != "_" and ch.isdigit()):
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
                            if line_character[i][j] == '.':
                                real_literal_dot_check = True
                            real_literal_check = True

                    if j + 1 < len(line_character[i]):
                        if line_character[i][j+1] == '.' and real_literal_dot_check == True:
                            digit_check = False
                            digit_end[0] = i
                            digit_end[1] = j+1
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
                                real_literal_dot_check = False
                            else:
                                output.append("File " + file_name + " Line " + str(i+1) + " Token 303" +
                                            " Text " + number)

                            real_literal_check = False
                            number = ""

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
                            real_literal_dot_check = False
                        else:
                            output.append("File " + file_name + " Line " + str(i+1) + " Token 303" +
                                        " Text " + number)

                        real_literal_check = False
                        number = ""

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
        # for i in final_output:
        #     print(i)
        if final_output != []:
            f = open(str(new_file) + ".lexer", "w")
            for j in output_file:
                f.write(j + "\n")
            f.close()
            return output_file
        


# -----------------------  Part 2  ----------------------------------------


counter = -1
def part2(outer_file_name):
    new_p = p1()
    out = new_p.run_p1(outer_file_name)

    output = []
    for line in out:
        x = line.split()
        output.append(x)

    new_file = outer_file_name.split(".")
    new_file = new_file[0]

    output_arr = []
    # store the line number and token into an array from part 1
    for i in range(len(output)):
        output_arr.append([int(output[i][3]), output[i][7], int(output[i][5])])

    # type name to check variable
    type_name = ['void', 'char', 'int', 'float']
    # struct
    # struct_array = []

    unary_op = ['!', '~']
    binary_op = ['==', '!=', '>', '>=', '<', '<=',
                '+', '-', '*', '/', '%', '|', '&', '||', '&&']
    assignment_op = ['=', '+=', '-=', '*=', '/=']


  
    result = []
    
    # function look ahead to see what is the next token
    # the function will return type, char, int, real, string, ident, binary operator, unary operator, assignment operator
    # if it does not read any of the type, it will return the exact symbol
    # assuming that the lexer provides a valid token
    def lookAheadGetLex():
        temp_count = counter
        if temp_count + 1 < len(output_arr):
            temp_count += 1
            if output_arr[temp_count][2] == 301:
                return "type"
            if output_arr[temp_count][1] == 'struct':
                return "type"
            elif output_arr[temp_count][2] == 302:
                return "char"
            elif output_arr[temp_count][2] == 303:
                return "int"
            elif output_arr[temp_count][2] == 304:
                return "real"
            elif output_arr[temp_count][2] == 305:
                return "string"
            elif output_arr[temp_count][2] == 306:
                return "ident"
            elif output_arr[temp_count][1] in binary_op:
                return "binary_op"
            elif output_arr[temp_count][1] in unary_op:
                return "unary_op"
            elif output_arr[temp_count][1] in assignment_op:
                return "assignment_op"
            else:
                return output_arr[temp_count][1]
        else:
            return None

    def lookCurrentGetLex():
        temp_count = counter
        if temp_count < len(output_arr):
            if output_arr[temp_count][2] == 301:
                return "type"
            elif output_arr[temp_count][2] == 302:
                return "char"
            elif output_arr[temp_count][2] == 303:
                return "int"
            elif output_arr[temp_count][2] == 304:
                return "real"
            elif output_arr[temp_count][2] == 305:
                return "string"
            elif output_arr[temp_count][2] == 306:
                return "ident"
            elif output_arr[temp_count][1] in binary_op:
                return "binary_op"
            elif output_arr[temp_count][1] in unary_op:
                return "unary_op"
            elif output_arr[temp_count][1] in assignment_op:
                return "assignment_op"
            else:
                return output_arr[temp_count][1]
        else:
            return None

    # similar to lookAheadGetLex(), but instead look further ahead
    # will be used to check if it is a variable declaration or a function definition
    def lookExtraGetLex():
        temp_count = counter
        if temp_count + 3 < len(output_arr):
            temp_count += 3
            if output_arr[temp_count][2] == 301:
                return "type"
            elif output_arr[temp_count][2] == 302:
                return "char"
            elif output_arr[temp_count][2] == 303:
                return "int"
            elif output_arr[temp_count][2] == 304:
                return "real"
            elif output_arr[temp_count][2] == 305:
                return "string"
            elif output_arr[temp_count][2] == 306:
                return "ident"
            elif output_arr[temp_count][1] in binary_op:
                return "binary_op"
            elif output_arr[temp_count][1] in unary_op:
                return "unary_op"
            elif output_arr[temp_count][1] in assignment_op:
                return "assignment_op"
            else:
                return output_arr[temp_count][1]
        else:
            return None
    

    # similar to lookAheadGetLex(), but instead look further ahead
    # will be used to check if it is a variable declaration or a function definition
    def lookSuperGetLex():
        temp_count = counter
        if temp_count + 4 < len(output_arr):
            temp_count += 4
            if output_arr[temp_count][2] == 301:
                return "type"
            elif output_arr[temp_count][2] == 302:
                return "char"
            elif output_arr[temp_count][2] == 303:
                return "int"
            elif output_arr[temp_count][2] == 304:
                return "real"
            elif output_arr[temp_count][2] == 305:
                return "string"
            elif output_arr[temp_count][2] == 306:
                return "ident"
            elif output_arr[temp_count][1] in binary_op:
                return "binary_op"
            elif output_arr[temp_count][1] in unary_op:
                return "unary_op"
            elif output_arr[temp_count][1] in assignment_op:
                return "assignment_op"
            else:
                return output_arr[temp_count][1]
        else:
            return None

    # consume the token and move to the next token
    def consumeToken():
        global counter
        counter += 1

    # given a token, it will check if the next token is the same token as the token provided
    # if it matches, return True, else it is an error
    def match(token):
        if lookAheadGetLex() == token:
            return
        else:
            sys.stderr.write("Parser error in file {} line {} at text {}".format(
                outer_file_name, str(output_arr[counter+1][0]), output_arr[counter+1][1]))
            sys.stderr.write("\n\tExpected {}".format(token))
            sys.exit(1)

    # global variable declaration
    # a type name followed by a comma-separated list of one or more identifiers
    # each identifier optionally followed by a left bracket, an integer literal, and a right bracket
    # the list is terminated with a semicolon
    def variableDeclaration():
        if lookAheadGetLex() == 'type':
            if output_arr[counter+1][1] == 'struct':
                consumeToken()
                # print("consume struct")
                match('ident')
                consumeToken()
                # print("consume ident")
            else:
                consumeToken()
                # print("consume type")
            # extra credit feature (constants)
            if lookAheadGetLex() == 'const':
                consumeToken()
                # print("consume const")
            while True:
                if lookAheadGetLex() == 'ident':
                    consumeToken()
                    result.append("File {} Line {}: global variable {}".format(outer_file_name,
                                                                    output_arr[counter][0], output_arr[counter][1]))
                    # print("consume ident")
                    # check if it is correct array format [int]
                    if lookAheadGetLex() == '[':
                        consumeToken()
                        # print("consume [")
                        match('int')
                        consumeToken()
                        # print("consume int")
                        match(']')
                        consumeToken()
                        # print("consume ]")
                    # extra credit feature (variable initialization)
                    elif lookAheadGetLex() == 'assignment_op':
                        if output_arr[counter + 1][1] == '=':
                            consumeToken()
                            # print("consume =")
                            expression()
                    
                    if lookAheadGetLex() == ',':
                        consumeToken()
                        # print("consume ,")
                    elif lookAheadGetLex() == ';':
                        consumeToken()
                        # print("consume ;")
                        return True
                    else:
                        sys.stderr.write("Parser error in file {} line {} at text {}".format(
                            outer_file_name, str(output_arr[counter+1][0]), output_arr[counter+1][1]))
                        sys.stderr.write("\n\t Incorrect Global Variable Declaration")
                        sys.exit(1)

    # local variable declaration
    # a type name followed by a comma-separated list of one or more identifiers
    # each identifier optionally followed by a left bracket, an integer literal, and a right bracket
    # the list is terminated with a semicolon
    def localVariableDeclaration():
        if lookAheadGetLex() == 'type':
            if output_arr[counter+1][1] == 'struct':
                consumeToken()
                # print("consume struct")
                match('ident')
                consumeToken()
                # print("consume ident")
            else:
                consumeToken()
                # print("consume type")
            # extra credit feature (constants)
            if lookAheadGetLex() == 'const':
                consumeToken()
                # print("consume const")
            while True:
                if lookAheadGetLex() == 'ident':
                    consumeToken()
                    result.append("File {} Line {}: local variable {}".format(outer_file_name,
                                                                    output_arr[counter][0], output_arr[counter][1]))
                    # print("consume ident")
                    # check if it is correct array format [int]
                    if lookAheadGetLex() == '[':
                        consumeToken()
                        # print("consume [")
                        match('int')
                        consumeToken()
                        # print("consume int")
                        match(']')
                        consumeToken()
                        # print("consume ]")
                    # extra credit feature (variable initialization)
                    elif lookAheadGetLex() == 'assignment_op':
                        if output_arr[counter + 1][1] == '=':
                            consumeToken()
                            # print("consume =")
                            expression()
                    
                    if lookAheadGetLex() == ',':
                        consumeToken()
                        # print("consume ,")
                    elif lookAheadGetLex() == ';':
                        consumeToken()
                        # print("consume ;")
                        return True
                    else:
                        sys.stderr.write("Parser error in file {} line {} at text {}".format(
                            outer_file_name, str(output_arr[counter+1][0]), output_arr[counter+1][1]))
                        sys.stderr.write("\n\t Incorrect Local Variable Declaration")
                        sys.exit(1)


    # member variable declaration
    # a type name followed by a comma-separated list of one or more identifiers
    # each identifier optionally followed by a left bracket, an integer literal, and a right bracket
    # the list is terminated with a semicolon
    def memberDeclaration():
        if lookAheadGetLex() == 'type':
            if output_arr[counter+1][1] == 'struct':
                consumeToken()
                # print("consume struct")
                match('ident')
                consumeToken()
                # print("consume ident")
            else:
                consumeToken()
                # print("consume type")
            # extra credit feature (constants)
            if lookAheadGetLex() == 'const':
                consumeToken()
                # print("consume const")
            while True:
                if lookAheadGetLex() == 'ident':
                    consumeToken()
                    result.append("File {} Line {}: member {}".format(outer_file_name,
                                                                    output_arr[counter][0], output_arr[counter][1]))
                    # print("consume ident")
                    # check if it is correct array format [int]
                    if lookAheadGetLex() == '[':
                        consumeToken()
                        # print("consume [")
                        if lookAheadGetLex() == 'int':
                            consumeToken()
                            # print("consume int")
                            if lookAheadGetLex() == ']':
                                consumeToken()
                                # print("consume ]")
                    
                    if lookAheadGetLex() == ',':
                        consumeToken()
                        # print("consume ,")
                    elif lookAheadGetLex() == ';':
                        consumeToken()
                        # print("consume ;")
                        return True
                    else:
                        sys.stderr.write("Parser error in file {} line {} at text {}".format(
                            outer_file_name, str(output_arr[counter][0]), output_arr[counter][1]))
                        sys.stderr.write("\n\t Incorrect Local Variable Declaration")
                        sys.exit(1)


    # struct declaration
    # a keyword struct, followed by an identifier, a left brace, zero or more variable declarations 
    # (without initializations), a right brace, and a semicolon
    def UserdefinedStructs():
        if output_arr[counter+1][1] == 'struct':
            consumeToken()
            # print("consume struct")
            if lookAheadGetLex() == 'ident':
                consumeToken()
                result.append("File {} Line {}: global struct {}".format(outer_file_name,
                                                            output_arr[counter][0], output_arr[counter][1]))
                # print("consume ident")
                if lookAheadGetLex() == '{':
                    consumeToken()
                    # print("consume {")
                    if lookAheadGetLex() == '}':
                        consumeToken()
                        # print("consume }")
                        return True
                    while True:
                        if lookAheadGetLex() == 'type':
                            memberDeclaration()
                        else:
                            break
                    match('}')
                    consumeToken()
                    # print("consume }")
                    match(';')
                    consumeToken()
                    # print("consume ;")
                    return True
        sys.stderr.write("Parser error in file {} line {} at text {}".format(
            outer_file_name, str(output_arr[counter+1][0]), output_arr[counter+1][1]))
        sys.stderr.write("\n\t Incorrect user-defined struct")
        sys.exit(1)



    # local struct declaration
    # a keyword struct, followed by an identifier, a left brace, zero or more variable declarations 
    # (without initializations), a right brace, and a semicolon
    def localUserdefinedStructs():
        if output_arr[counter+1][1] == 'struct':
            consumeToken()
            # print("consume struct")
            if lookAheadGetLex() == 'ident':
                consumeToken()
                result.append("File {} Line {}: local struct {}".format(outer_file_name,
                                                            output_arr[counter][0], output_arr[counter][1]))
                # print("consume ident")
                if lookAheadGetLex() == '{':
                    consumeToken()
                    # print("consume {")
                    if lookAheadGetLex() == '}':
                        consumeToken()
                        # print("consume }")
                        return True
                    while True:
                        if lookAheadGetLex() == 'type':
                            memberDeclaration()
                        else:
                            break
                    match('}')
                    consumeToken()
                    # print("consume }")
                    match(';')
                    consumeToken()
                    # print("consume ;")
                    return True
        sys.stderr.write("Parser error in file {} line {} at text {}".format(
            outer_file_name, str(output_arr[counter+1][0]), output_arr[counter+1][1]))
        sys.stderr.write("\n\t Incorrect user-defined struct")
        sys.exit(1)


    # Formal parameter
    # a type name, followed by an identifier, and optionally followed by a left and right bracket

    def formalParameter():
        const_check = False
        # extra credit feature (constants)
        if lookAheadGetLex() == 'const' and const_check == False:
            const_check = True
            consumeToken()
            # print("consume const")
        if lookAheadGetLex() == 'type':
            if output_arr[counter+1][1] == 'struct':
                consumeToken()
                # print("consume struct")
                match('ident')
                consumeToken()
                # print("consume ident")
            else:
                consumeToken()
                # print("consume type")

            # extra credit feature (constants)
            if lookAheadGetLex() == 'const' and const_check == False:
                const_check = True
                consumeToken()
                # print("consume const")
            if lookAheadGetLex() == 'ident':
                consumeToken()
                result.append("File {} Line {}: parameter {}".format(outer_file_name,
                                                            output_arr[counter][0], output_arr[counter][1]))
                # print("consume ident")
                # check if it is correct array format [int] 
                if lookAheadGetLex() == '[':
                    consumeToken()
                    # print("consume [")
                    match(']')
                    consumeToken()
                    # print("consume ]")
                return
        sys.stderr.write("Parser error in file {} line {} at text {}".format(
            outer_file_name, str(output_arr[counter+1][0]), output_arr[counter+1][1]))
        sys.stderr.write("\n\t Incorrect Formal Parameter")
        sys.exit(1)

    # function declaration
    # a type name, followed by an identifier, a left parenthesis, an optional comma-separated list of
    # formal parameters, and a right parenthesis
    def functionDeclartion():
        if lookAheadGetLex() == 'type':
            if output_arr[counter+1][1] == 'struct':
                consumeToken()
                # print("consume struct")
                match('ident')
                consumeToken()
                # print("consume ident")
            else:
                consumeToken()
                # print("consume type")
            if lookAheadGetLex() == 'ident':
                consumeToken()
                result.append("File {} Line {}: function {}".format(outer_file_name,
                                                            output_arr[counter][0], output_arr[counter][1]))
                # print("consume ident")
                match('(')
                consumeToken()
                # print("consume (")
                if lookAheadGetLex() == ')':
                    consumeToken()
                    # print("consume )")
                    return True
                while True:
                    # extra credit feature (constants)
                    if lookAheadGetLex() == 'type' or lookAheadGetLex() == 'const':
                        formalParameter()
                        if lookAheadGetLex() == ',':
                            consumeToken()
                            # print("consume ,")
                        else:
                            break
                match(')')
                consumeToken()
                # print("consume )")
                return True
        sys.stderr.write("Parser error in file {} line {} at text {}".format(
            outer_file_name, str(output_arr[counter+1][0]), output_arr[counter+1][1]))
        sys.stderr.write("\n\t Incorrect Function Declaration")
        sys.exit(1)

    # function definition
    # a function declaration followed by a left brace, a sequence of zero or more 
    # variable declarations or statements, and a right brace
    def functionDefinition():
        if lookAheadGetLex() == 'type':
            functionDeclartion()
            # extra credit feature (function prototype)
            if lookAheadGetLex() == ';':
                consumeToken()
                # print("consume ;")
                return True
            match('{')
            consumeToken()
            # print("consume {")
            if lookAheadGetLex() == '}':
                consumeToken()
                # print("consume }")
                return True
            else:
                while True:
                    # extra credit feature (constants)
                    if lookAheadGetLex() == 'const':
                        consumeToken()
                        # print("consume const")
                        match('type')
                        localVariableDeclaration()
                        continue
                    elif lookAheadGetLex() == 'type':
                        if lookExtraGetLex() == '{':
                            localUserdefinedStructs()
                        else:
                            localVariableDeclaration()
                        continue
                    elif lookAheadGetLex() == '}':
                        consumeToken()
                        # print("consume }")
                        return True
                    else:
                        statement()

        sys.stderr.write("Parser error in file {} line {} at text {}".format(
            outer_file_name, str(output_arr[counter][0]), output_arr[counter][1]))
        sys.stderr.write("\n\t Incorrect Function Definition")
        sys.exit(1)

    # term
    # term -> number | ident | ident() | (type) exp | (exp) | ident(exp,exp, ....) | ident[exp]
    #         | unary-operator exp | ident++ | ident-- | ++ident | -- ident | ident[exp]++ | ident[exp]-- 
    #         | ++ident[exp] | -- ident[exp]
    # extra credit feature
    # term -> ident.ident | ident[exp].ident
    def term():
        if lookAheadGetLex() == 'ident':
            consumeToken()
            # print("consume ident")
            if lookAheadGetLex() == '(':
                consumeToken()
                # print("consume (")
                # ident()
                if lookAheadGetLex() == ')':
                    consumeToken()
                    # print("consume )")
                    return True
                # ident(string || char)
                elif lookAheadGetLex() == 'string' or lookAheadGetLex() == 'char':
                    consumeToken()
                    # print("consume string or char")
                    if lookAheadGetLex() == ',':
                        consumeToken()
                        # print("consume ,")
                        expression()
                    match(')')
                    consumeToken()
                    # print("consume )")
                    return True
                # ident(exp, exp, ...)
                else:
                    while True:
                        expression()
                        # print("enter")
                        if lookAheadGetLex() == ',':
                            consumeToken()
                            # print("consume ,")
                        else:
                            break
                    match(')')
                    consumeToken()
                    # print("consume )")
                    return True
            # ident[exp] | ident[exp]++ || ident[exp]-- | ident[exp].ident ...
            elif lookAheadGetLex() == '[':
                consumeToken()
                # print("consume [")
                if lookAheadGetLex() == '++' or lookAheadGetLex() == '--':
                    consumeToken()
                    # print("consume ++ or --")
                expression()
                match(']')
                consumeToken()
                # print("consume ]")
                if lookAheadGetLex() == '.':
                    consumeToken()
                    # print("consume .")
                    term()
                    return True
                if lookAheadGetLex() == '++' or lookAheadGetLex() == '--':
                    consumeToken()
                    # print("consume ++ or --")
                elif lookAheadGetLex() == 'assignment_op':
                    consumeToken()
                    # print("consume assignment operator")
                    expression()
                return True
            # ident.ident | ident.ident[exp]
            elif lookAheadGetLex() == '.':
                consumeToken()
                # print("consume .")
                term()
                return True
            # ident
            else:
                # ident++ or ident--
                if lookAheadGetLex() == '++' or lookAheadGetLex() == '--':
                    consumeToken()
                    # print("consume ++ or --")
                    return True
                else:
                    if lookAheadGetLex() == 'assignment_op':
                        consumeToken()
                        # print("consume assignment operator")
                        expression()
                    return True
        # (type) exp | (exp)
        elif lookAheadGetLex() == '(':
            consumeToken()
            # print("consume (")
            if lookAheadGetLex() == 'type':
                consumeToken()
                # print("consume type")
                match(')')
                consumeToken()
                # print("consume )")
                expression()
                return True
            # (exp)
            else:
                expression()
                match(')')
                consumeToken()
                # print("consume )")
                return True
        # int or real
        elif lookAheadGetLex() == 'int' or lookAheadGetLex() == 'real':
            consumeToken()
            # print("consume int or real")
            return True
        # ++ident | --ident | ++ident[exp] | --ident[exp]
        elif lookAheadGetLex() == '++' or lookAheadGetLex() == '--':
            consumeToken()
            # print("consume ++ or --")
            if lookAheadGetLex() == 'ident':
                consumeToken()
                # print("consume ident")
                if lookAheadGetLex() == '.':
                    consumeToken()
                    # print("consume .")
                    term()
                    return True
                if lookAheadGetLex() == '[':
                    consumeToken()
                    expression()
                    match(']')
                    consumeToken()
                    # print("consume ]")
                    if lookAheadGetLex() == '.':
                        consumeToken()
                        # print("consume .")
                        term()
                    return True
                else:
                    return True
        # unary-operator exp
        elif lookAheadGetLex() == 'binary_op':
            if output_arr[counter+1][1] == '-' and lookCurrentGetLex() != 'binary_op':
                consumeToken()
                # print("consume unary operator")
                expression()
                return True
        # unary-operator exp
        elif lookAheadGetLex() == 'unary_op':
            consumeToken()
            # print("consume unary operator")
            expression()
            return True
    
        sys.stderr.write("Parser error in file {} line {} at text {}".format(
            outer_file_name, str(output_arr[counter+1][0]), output_arr[counter+1][1]))
        sys.stderr.write("\n\t Incorrect expression")
        sys.exit(1)

    # expression
    # expression -> term binary_op exp | exp ? exp : exp
    def expression():
        check_term = term()
        if lookAheadGetLex() == ',' and check_term == True:
            return True
        if lookAheadGetLex() == ';' and check_term == True:
            return True
        if lookAheadGetLex() == ':' and check_term == True:
            return True
        if lookAheadGetLex() == ']' or lookAheadGetLex() == ')':
            return True
        if lookAheadGetLex() == '?':
            consumeToken()
            # print("consume ?")
            expression()
            match(':')
            consumeToken()
            # print("consume :")
            expression()
            return True
        
        if lookAheadGetLex() == "binary_op":
            consumeToken()
            # print("consume binary operator")
            expression()
            return True
        sys.stderr.write("Parser error in file {} line {} at text {}".format(
                    outer_file_name, str(output_arr[counter+1][0]), output_arr[counter+1][1]))
        sys.stderr.write("\n\tIncorrect expression")
        sys.exit(1)

    # break statement
    # keyword break followed by a semicolon
    def breakStatement():
        if lookAheadGetLex() == "break":
            consumeToken()
            # print("consume break")
            match(";")
            consumeToken()
            # print("consume ;")
            return
        sys.stderr.write("Parser error in file {} line {} at text {}".format(
            outer_file_name, str(output_arr[counter+1][0]), output_arr[counter+1][1]))
        sys.stderr.write("\n\tIncorrect break statement")
        sys.exit(1)

    # continue statement
    # keyword continue followed by a semicolon
    def continueStatement():
        if lookAheadGetLex() == "continue":
            consumeToken()
            # print("consume continue")
            match(";")
            consumeToken()
            # print("consume ;")
            return
        sys.stderr.write("Parser error in file {} line {} at text {}".format(
            outer_file_name, str(output_arr[counter+1][0]), output_arr[counter+1][1]))
        sys.stderr.write("\n\tIncorrect continue statement")
        exit(1)

    # return statement
    # keyword return followed by an optional expression, and a semicolon
    def returnStatement():
        if lookAheadGetLex() == "return":
            consumeToken()
            # print("consume return")
            if lookAheadGetLex() == ";":
                consumeToken()
                # print("consume ;")
                return
            else:
                expression()
                match(";")
                consumeToken()
                # print("consume ;")
                return

        sys.stderr.write("Parser error in file {} line {} at text {}".format(
            outer_file_name, str(output_arr[counter+1][0]), output_arr[counter+1][1]))
        sys.stderr.write("\n\tIncorrect return statement")
        sys.exit(1)

    # if statement
    # keyword if followed by a left parenthesis, an expression, and a right parenthesis, 
    # followed by either a statement block or a single statement. Then, optionally, 
    # keyword else, followed by either a statement block, or a single statement
    def ifStatement():
        if lookAheadGetLex() == "if":
            consumeToken()
            # print("consume if")
            match('(')
            consumeToken()
            # print("consume (")
            expression()
            match(')')
            consumeToken()
            # print("consume )")
            if lookAheadGetLex() == '{':
                statementBlock()
            else:
                statement()
            if lookAheadGetLex() == "else":
                elseStatement()
            return True
        sys.stderr.write("Parser error in file {} line {} at text {}".format(
            outer_file_name, str(output_arr[counter+1][0]), output_arr[counter+1][1]))
        sys.stderr.write("\n\tIncorrect if statement")
        sys.exit(1)

    # else statment
    # keyword else, followed by either a statement block, or a single statement
    def elseStatement():
        if lookAheadGetLex() == "else":
            consumeToken()
            # print("consume else")
            if lookAheadGetLex() == '{':
                statementBlock()
                return True
            else:
                statement()
                return True
        sys.stderr.write("Parser error in file {} line {} at text {}".format(
            outer_file_name, str(output_arr[counter+1][0]), output_arr[counter+1][1]))
        sys.stderr.write("\n\tIncorrect else statement")
        sys.exit(1)

    # statement block
    # a left brace, a sequence of zero or more statements, and a right brace
    def statementBlock():
        if lookAheadGetLex() == "{":
            consumeToken()
            # print("consume {")
            while True:
                if lookAheadGetLex() == "}":
                    consumeToken()
                    # print("consume }")
                    return
                else:
                    statement()
        sys.stderr.write("Parser error in file {} line {} at text {}".format(
            outer_file_name, str(output_arr[counter+1][0]), output_arr[counter+1][1]))
        sys.stderr.write("\n\tIncorrect statement block")
        sys.exit(1)

    # for statement
    # Keyword for, followed by a left parenthesis, an optional expression, a semicolon, an optional expression, 
    # a semicolon, an optional expression, a right parenthesis, and then either a statement block, or a single 
    # statement
    def forStatement():
        if lookAheadGetLex() == "for":
            consumeToken()
            # print("consume for")
            match('(')
            consumeToken()
            # print("consume (")
            if lookAheadGetLex() == ';':
                consumeToken()
                # print("consume ;")
            else:
                expression()
                match(';')
                consumeToken()
                # print("consume ;")
            if lookAheadGetLex() == ';':
                consumeToken()
                # print("consume ;")
            else:
                expression()
                match(';')
                consumeToken()
                # print("consume ;")
            if lookAheadGetLex() == ')':
                consumeToken()
            else:
                expression()
                match(')')
                consumeToken()
            if lookAheadGetLex() == '{':
                statementBlock()
                return
            else:
                statement()
                return
        sys.stderr.write("Parser error in file {} line {} at text {}".format(
            outer_file_name, str(output_arr[counter+1][0]), output_arr[counter+1][1]))
        sys.stderr.write("\n\tIncorrect for statement")
        sys.exit(1)

    # while statement
    # Keyword while, followed by a left parenthesis, an expression, and a right parenthesis, 
    # and then either a statement block, or a single statement
    def whileStatement():
        if lookAheadGetLex() == "while":
            consumeToken()
            # print("consume while")
            match('(')
            consumeToken()
            # print("consume (")
            expression()
            match(')')
            consumeToken()
            # print("consume )")
            if lookAheadGetLex() == '{':
                statementBlock()
                return
            else:
                statement()
                return
        sys.stderr.write("Parser error in file {} line {} at text {}".format(
            outer_file_name, str(output_arr[counter+1][0]), output_arr[counter+1][1]))
        sys.stderr.write("\n\tIncorrect while statement")
        sys.exit(1)

    # do statement
    # Keyword do, followed by either a statement block or a single statement, followed by 
    # keyword while, a left parenthesis, an expression, a right parenthesis, and a semicolon
    def doStatement():
        if lookAheadGetLex() == "do":
            consumeToken()
            # print("consume do")
            # single statement or statement 
            if lookAheadGetLex() == '{':
                statementBlock()
            else:
                statement()
            match("while")
            consumeToken()
            # print("consume while")
            match("(")
            consumeToken()
            # print("consume (")
            expression()
            match(")")
            consumeToken()
            # print("consume )")
            match(";")
            consumeToken()
            # print("consume ;")
            return
        sys.stderr.write("Parser error in file {} line {} at text {}".format(
            outer_file_name, str(output_arr[counter+1][0]), output_arr[counter+1][1]))
        sys.stderr.write("\n\tIncorrect do statement")
        sys.exit(1)

    # single statement
    def statement():
        # nothing, followed by a semicolon
        if lookAheadGetLex() == ';':
            consumeToken()
            # print("consume ;")
            return
        # execute break statement
        elif lookAheadGetLex() == "break":
            breakStatement()
            return
        # execute continue statement
        elif lookAheadGetLex() == "continue":
            continueStatement()
            return
        # execute return statement
        elif lookAheadGetLex() == "return":
            returnStatement()
            return
        # execute if statement
        elif lookAheadGetLex() == "if":
            ifStatement()
            return
        # execute for statement
        elif lookAheadGetLex() == "for":
            forStatement()
            return
        # execute while statement
        elif lookAheadGetLex() == "while":
            whileStatement()
            return
        # execute do statement
        elif lookAheadGetLex() == "do":
            doStatement()
            return
        # An expression followed by a semicolon
        else:
            expression()
            match(";")
            consumeToken()
            # print("consume ;")
            return


    check = True
    while check:
        if lookAheadGetLex() == 'const':
            consumeToken()
            # print("consume const")
            check = variableDeclaration()
            continue

        if lookAheadGetLex() == 'type':
            if lookExtraGetLex() == '(':
                check = functionDefinition()
            elif output_arr[counter+1][1] == 'struct':
                if lookExtraGetLex() == '{':
                    check = UserdefinedStructs()
                elif lookSuperGetLex() == '(':
                    # print("enter")
                    check = functionDefinition()
                else:
                    check = variableDeclaration()
            else:
                check = variableDeclaration()

            if lookAheadGetLex() == None:
                break
            else:
                continue
        sys.stderr.write("Parser error in file {} line {} at text {}".format(
            outer_file_name, str(output_arr[counter+1][0]), output_arr[counter+1][1]))
        sys.stderr.write("\n\tExpected variable declarations, function definitions or user-defined struct.")
        sys.exit(1)



    if result != []:
        f = open(str(new_file) + ".parser", "w")
        for j in result:
            f.write(j + "\n")
        f.close()


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
        new_p = p1()
        new_p.run_p1(outer_file_name)
        argument_parsed = True


    elif sys.argv[2] == "-2":
        outer_file_name = sys.argv[3]
        part2(outer_file_name)
        argument_parsed = True

# Print usage if argument is not parsed
if not(argument_parsed):
    print("Usage:")
    print("\t\tmycc -mode infile")
    print("Valid modes: ")
    print("\t\t-0: Version information only")
    print("\t\t-1: Part 1: Create a lexer for C")
    print("\t\t-2: Part 2: Create a parser for C")
