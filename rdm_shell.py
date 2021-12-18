#!/usr/bin/env python3

## Customs Package ##

from argparse import ArgumentParser
from os import system, name, sys
import yaml
import pathlib
from random import *

## Global Variables ##

__Author__ = "Pierre.B"

## Usage ##

def prompt(b):
    print("  ______   __                  __  __        _______                                                                ")
    print(" /      \ /  |                /  |/  |      /       \                                                               ")
    print("/$$$$$$  |$$ |____    ______  $$ |$$ |      $$$$$$$  | ______    ______    ______    ______   ______   _____  ____  ")
    print("$$ \__$$/ $$      \  /      \ $$ |$$ |      $$ |__$$ |/      \  /      \  /      \  /      \ /      \ /     \/    \ ")
    print("$$      \ $$$$$$$  |/$$$$$$  |$$ |$$ |      $$    $$//$$$$$$  |/$$$$$$  |/$$$$$$  |/$$$$$$  |$$$$$$  |$$$$$$ $$$$  |")
    print(" $$$$$$  |$$ |  $$ |$$    $$ |$$ |$$ |      $$$$$$$/ $$ |  $$/ $$ |  $$ |$$ |  $$ |$$ |  $$/ /    $$ |$$ | $$ | $$ |")
    print("/  \__$$ |$$ |  $$ |$$$$$$$$/ $$ |$$ |      $$ |     $$ |      $$ \__$$ |$$ \__$$ |$$ |     /$$$$$$$ |$$ | $$ | $$ |")
    print("$$    $$/ $$ |  $$ |$$       |$$ |$$ |      $$ |     $$ |      $$    $$/ $$    $$ |$$ |     $$    $$ |$$ | $$ | $$ |")
    print(" $$$$$$/  $$/   $$/  $$$$$$$/ $$/ $$/       $$/      $$/        $$$$$$/   $$$$$$$ |$$/       $$$$$$$/ $$/  $$/  $$/ ")
    print("                                                                         /  \__$$ |                                 ")
    print("                                                                         $$    $$/                                  ")
    print("                                                                          $$$$$$/                                   ")


condition_operators=[ ("if", "then", "fi"),
                      ("while", "do", "done"),
                      ("until", "do", "done"),
#                      ("for", "in", "do", "done")
                    ]

var = [ "var1", "var2" ]

redirect_operator = [ ">", ">>", "<", "|", ">&" ]

int_test_operator = [ "-eq", "-ne", "-ge", "-gt", "-le", "-lt" ]

bool_operator=[ "true", "false", "0", "1" ]

function_operator = [ ("echo", 3),
                      ("ls", 0),
                      ("pwd", 0),
                      ("cd", 1),
                      ("cat", 1)
                    ]

binary_operator = [ "&&", "||" ]

lorem = [ "lorem", "ipsum", "albin", "jojo", "apero", "shell", "42sh",
          "moulette", "ingenieur", "informaticien", "cisco", "midlab", "Yaaaa",
          "Ocho", "DANS LA VALEE", "DE DANA", "Code Lyoko", "j'ai plus d'idee"
        ]

files = [ "foo", "bar", "baz", "boo" ]


## Functions  ##

# \brief: boolean can be classical boolean or function test [ INT -xx INT] #
def generate_boolean():
    # Boolean will be [ INT -xx INT ] function or boolean
    use_test = (randint(0, 2)) != 0
    bool_str = bool_operator[randint(0, len(bool_operator) - 1)]
    # Using Test function #
    if (use_test):
        bool_str = "[ " + str(randint(0, 10)) + " "
        bool_str += int_test_operator[randint(0, len(int_test_operator) - 1)] 
        bool_str += " " + str(randint(0, 10)) + " ]"
    return bool_str



# \brief: Generate a line of conditions that can be boolean or functions #
def generate_condition(sep):
    cd_str = ""
    # Condition will use boolean or function (more chance to have bool)
    has_bool = (randint(0, 3)) != 0
    # Building boolean #
    if (not has_bool):
        cd_str += build_a_command()
    else:
        cd_str += generate_boolean()
    cd_str += sep + " "
    return cd_str

def build_list_condition():
    s = ""
    cond_len = randint(0, 5)
    for i in range(cond_len):
        separator=";"
        if (i + 1 < cond_len) and (randint(0, 3) == 0):
            separator = " " + binary_operator[randint(0, len(binary_operator) - 1)]
        s += generate_condition(separator)
    return s

def build_list_function():
    s = ""
    for i in range(0, randint(1, 3)):
        s += "\t"
        s += build_a_command()
        s += "\n"
    return s


# \brief: Build a structure based on condition_operators list #
#         For each structure, it pass on all inside part (ex: then, else) #
def build_structure():
    stu_str = ""
    has_var = randint(0, 1) == 0
    if (has_var):
        stu_str += var[randint(0, len(var)-1)] + "=" + "4" + "\n"
    cond = condition_operators[randint(0, len(condition_operators)) - 1]
    stu_str += cond[0] + " "
    # Building i conditions #
    stu_str += build_list_condition()
    stu_str += cond[1] + " "
    stu_str +="\n"
    # Building j body elements #
    stu_str += build_list_function()
    # elif
    if (cond[0] == "if" and randint(0, 4) == 0):
        stu_str += "elif "
        stu_str += build_list_condition()
        stu_str += "then\n"
        stu_str += build_list_function()
    if (cond[0] == "if" and randint(0, 2) == 0):
        stu_str += "else\n"
        # Building jbody elements #
        for i in range(0, randint(1, 3)):
            stu_str += "\t"
            stu_str += build_a_command()
            stu_str += "\n"
    stu_str +=cond[2] + " "
    stu_str +="\n"
    return stu_str



# \brief: Build a command based on function_operator list and a random input #
#         based on the maximum input needed by each function #
def build_a_command():
    cmd = function_operator[randint(0, len(function_operator) - 1)]
    cmd_str = cmd[0] + " "
    cmd_argl= cmd[1]
    for i in range(cmd_argl):
        if (randint(0, 5) == 0):
            cmd_str += "$" + var[randint(0, len(var) - 1)]
        else:
            cmd_str += lorem[randint(0, len(lorem) - 1)]
        cmd_str += " "
#    cmd_str += "\n"
    return cmd_str

def build_redirect():
    s = build_a_command()
    s + redirect_operator[randint(0, len(redirect_operator) - 1)] + " "
    s += build_a_command()
    s += "\n"
    return s



## Main ##
def main(filepath):
    s = ""
    for i in range(randint(1, 10)):
        if randint(0, 2) == 0:
            s += build_structure()
        elif randint(0, 4) == 0:
            s += build_redirect()
        else:
            s += build_a_command()
        s += "\n"
    print(s)
    print("-"*72)
    format_s = s.replace("\n", " \\n ") 
    f = open(filepath, "w")
    f.write(s)
    f.close()
    print("input:", "\"", format_s, "\"")

## Call main with --output [FILE] args ##
if __name__ == "__main__":
    b="\x1b[33m"
    parser = ArgumentParser('42sh')
    parser.add_argument('--output', type=str, required=True)
    args = parser.parse_args()
    print(f'Output : {args.output}')
    system('clear')
    prompt(b)
    main(args.output)

## Build with Python 3.8.10 ##
