#!/usr/bin/env python3

import sys

number_string = sys.argv[1]

if sys.argv[1] == "-h":
  print("""
  Usage:

    bvert <number> <starting base> <base to output>

  Example:

    bvert ff 16 10

    Output:

      255""")
  quit()

from_base = int(sys.argv[2])

# Convert the number to an integer using the specified base
number = int(number_string, from_base)

# Get the base to convert the number to from the command line arguments
to_base = int(sys.argv[3])

converted_number = ''
while number > 0:
    remainder = number % to_base
    if remainder < 10:
        # Use the corresponding digit for remainders less than 10
        converted_number = str(remainder) + converted_number
    else:
        # Use the corresponding letter for remainders greater than 9
        converted_number = chr(ord('A') + remainder - 10) + converted_number
    number = number // to_base

print(converted_number)