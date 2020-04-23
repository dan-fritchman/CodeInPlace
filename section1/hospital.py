"""
Discussion Session #1
Hospital Karel

* 1. Composition
  * Functions - calling & definition

* 2. Control Flow
  * Loops
    * for - over a set
    * while - condition
      * runs until condition not true
  * Conditionals
    * if/ else - condition
      * run *once*

A few "tools" we'll use:

* Comments
* Pseudo-code

"""


def place_three():
    for i in range(2):
        put_beeper()
        move()
    put_beeper()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def build_hospital():
    pick_beeper()
    turn_left()

    place_three()

    turn_right()
    move()
    turn_right()

    place_three()
    turn_left()


def main():
    while front_is_clear():
        if beepers_present():
            build_hospital()
        if front_is_clear():
            move()


if __name__ == '__main__':
    main()
