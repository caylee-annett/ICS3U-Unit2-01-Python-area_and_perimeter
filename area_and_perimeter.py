#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: April 2021
# This program finds the area and perimeter of a circle with a
#   radius of 15 mm

import math


def main():
    # This function calculates the area and perimeter

    print("If a circle has a radius of 15 mm: ")
    print("")
    print("The area is: {} mm².".format(math.pi * 15 ** 2))
    print("The perimeter is: {} mm.".format(2 * math.pi * 15))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
