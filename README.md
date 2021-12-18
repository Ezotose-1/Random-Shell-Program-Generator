# Random Shell program Generator
# Usefull 42Sh tester

The Rnd_ShellPrg is a python program that will generate sequences of shell programs randomly.
This program can generate few structure different : if condition and while/until loops.
And it can call many functions, conditions or arithmetic/logic operators.

This program have been used to test our own ***42sh*** (school project to rebuild entierly from sratch a POSIX shell based on dash property).

# How to use :
* Download/Clone the file thank's to the github page
```shell$
$ git clone git@github.com:Ezotose-1/Rnd_ShellPrg.git
```
* Run the script by using this command in a shell :
```shell
$ ./rdm_shell.py --output [OUTPUT_FILE_PATH]
```

Operator availables :
| Structures            | Conditions        | Redirection   | Functions     |
| -----------           | -----------       | ---           | ---           |
| if/(else)/(elseif)/fi | Boolean           |  >            | Echo          |
| While                 | Int               |  <            | ls            |
| Until                 | Function          |  >>           | pwd           |
|                       | [INT -xx INT]     | \|            | cat           |
|                       |                   |  >&           | cd            |





License
----
Developped by Pierre B.
Languages : Python
Free to use
MIT


**Free Software**
