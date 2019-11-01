#!/usr/bin/env python3

# Created by Evano Fotia
# Created on Sept 2019
# finding radius 


import constants


def main():
    # this function calculates circumference

    # input
    radius = int(input("Enter radius of the circle (mm): "))
    # process
    circumference = constants.TAU*radius
    # output
    print("")
    print("Circumference is {0}mm2".format(circumference))


if __name__ == "__main__":
    main()
