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

# Print usage if argument is not parsed
if not(argument_parsed):
    print("Usage:")
    print("\t\tmycc -mode infile")
    print("Valid modes: ")
    print("\t\t-0: Version information only")
    print("\t\t-1: Part 1 (not yet implemented)")
