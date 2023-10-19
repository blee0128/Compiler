##PART 0

How to build and run the compiler

- There is a file name mycc.py in the source folder part 0. Use the command line to enter the source folder. Once you are in the source folder, you can give argument -0 and key in “python mycc.py mycc -0” in the terminal and it should output will display the version and author information.

My bare-bones Python compiler (for COMS 540)
         Written by Benjamin Lee (ben97@iastate.edu)
         Version 2.1 released 5 January 2023

- If no argument is given, then key in “python mycc.py mycc”, it will display the usage information, and summary of what is implemented.

Usage:
         mycc -mode infile
Valid modes: 
         -0: Version information only
         -1: Part 1 (not yet implemented)


How to build and run the documentation

- Go to the Documentation directory in the repository. When you are in the Documentation directory, key in "pdflatex developers.tex". This will output the developers.pdf.




##PART 1

How to build and run the compiler

- There is a file name mycc.py in the source folder part 1. Use the command line to enter the source folder. Once you are in the source folder, you can give argument -1 followed by a file. For example, using the file hello.c as input given in the assignment pdf, you will need to key in “python mycc.py mycc -1 hello.c” in the terminal. If there is no error, it should output a hello.lexer file with all the tokens. If there is an error, it will print to standard error in the terminal.

- If no argument is given, then key in “python mycc.py mycc”, it will display the usage information, and summary of what is implemented. This is an update on part 0.

Usage:
         mycc -mode infile
Valid modes: 
         -0: Version information only
         -1: Part 1: Create a lexer for C


- The LexTest.sh file was given by the professor also works in this format in the terminal as shown below.
./LexTest.sh "python mycc.py mycc" INPUTS/*



How to build and run the documentation

- Go to the Documentation directory in the repository. When you are in the Documentation directory, key in "pdflatex developers.tex". This will output the developers.pdf.

Features implemented

- Basic Lever features implemented
- All Extra features implemented

##PART 2

How to build and run the compiler

- There is a file name mycc.py in the source folder part 2. Use the command line to enter the source folder. Once you are in the source folder, you can give argument -2 followed by a file. For example, using the file hello.c as input given in the assignment pdf, you will need to key in “python mycc.py mycc -2 hello.c” in the terminal. If there is no error, it should output a hello.parser file with all the identifier. If there is an error, it will print to standard error in the terminal.

- If no argument is given, then key in “python mycc.py mycc”, it will display the usage information, and summary of what is implemented. This is an update on part 0.

Usage:
         mycc -mode infile
Valid modes: 
         -0: Version information only
         -1: Part 1: Create a lexer for C
	-2: Part 2: Create a parser for C


- The LexTest.sh file was given by the professor also works in this format in the terminal as shown below.
./ParseTest.sh "python mycc.py mycc" INPUTS/*



How to build and run the documentation

- Go to the Documentation directory in the repository. When you are in the Documentation directory, key in "pdflatex developers.tex". This will output the developers.pdf.

Features implemented

- All Basic Lever features implemented
- All Extra features implemented
