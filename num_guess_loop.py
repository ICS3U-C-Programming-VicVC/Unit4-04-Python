#!/usr/bin/env python3
# Created By: Victor Victor-Calixte
# Date: 11/17/26
# This program tells the user to guess a random number, using a while loop.

import random
import constants


def main():

    # Generating a random number
    rand_num = random.randint(constants.LEAST_RANGE, constants.MOST_RANNGE)

    while True:

        # Asking the user to guess a number from a range
        inpt_guess_str = input(
            constants.INPT_MSG.format(constants.LEAST_RANGE, constants.MOST_RANNGE)
        )

        # the try statement will make sure the code safely with invalid user inputs
        try:
            # Converting the input from a string to a integer
            guess_num = int(inpt_guess_str)

            # First check if the guess is correct
            if guess_num == rand_num:
                print(constants.CRT_ANS)
                break

            # check if the number is outside the range
            if guess_num < constants.LEAST_RANGE or guess_num > constants.MOST_RANNGE:
                print(
                    constants.RANG_MSG.format(
                        guess_num, constants.LEAST_RANGE, constants.MOST_RANNGE
                    )
                )
                print(constants.ATTMP_MSG)
            else:
                # If the if statements fail, it means that it's a wrong guess
                print(constants.ICRT_ANS)
                print(constants.ATTMP_MSG)

        except:
            print(constants.ERR_MSG.format(inpt_guess_str))
            print(constants.ATTMP_MSG)


if __name__ == "__main__":
    main()
