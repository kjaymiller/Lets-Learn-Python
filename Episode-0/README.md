# Episode 0 Jamie's Notes

### Setting up Python on my Mac

Because I was using my Mac to record the episode with Jay, I had to install Python 3.7 using [Homebrew](https://brew.sh/). MacOS currently (at the time of recording the episode: Jan 1st 2019) shipps with Python 2.7 installed, but support for that version is rapidly running out.

Installing Python 3.7 was as easy as running two commands:

- `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

This command installs Homebrew on to your Mac, and can be incredibly useful for installing things very quickly from within the terminal.

- `brew install python`

This is the command required to install Python 3.7 on my Mac. Once this is done, I checked which version of Python I had installed by running the following `python --version` which told me that I was running 3.7.

### My First Python Application

The [python code](./jamies-code.py) which I wrote whilst we were recording episode one is also listed below.

I've added comments to it, so that I can come back to this code if I forget what an f-string is or how they are formatted.

I started by writing the application that almost any programmer writes when learning a new language: ["Hello, World!"](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program)

``` python
# This line is a comment, as it starts with a pound symbol/hash character

# The following line is a statement, it prints the literal string
# "hello, world!" to the console
print('hello, world!')

# This pair of statements creates a variable (called 'name') and assigns
# it the value of "GaProgMan", then the value of the 'name' variable is used
# as part of an f-string within the print statement.
name = 'GaProgMan'
print(f"hello, {name}")

# At runtime, the Python engine combines the string literal (i.e 'hello, ')
# with the value of the variable (i.e. name, which has a value of "GaProgMan")
# before sending the combined value to the print method
```

Running this code was as simple as creating a file on disk called `jamie-code.py` then running the following command (in the same directory as the py file): `python3 jamies-code.py`

Running caused the following output in terminal:

``` shell
hello, world!
hello, GaProgMan
```

### VS Code Gotcha

Because of the fact that MacOS ships with version 2.7 of Python, I had to call `python3` when using the VS Code intergrated terminal (I had to use this when using the MacOS terminal, too). When I called `python`, version 2.7.10 was used to execute my application, and the following was outputted to the terminal:

``` shell
  File "jamies-code.py", line 11
    print(f"hello, {name}")
                         ^
SyntaxError: invalid syntax
```

This is because f-strings are a feature of Pyton 3.6, and as such the default installation of Python (which is 2.7.10 in my Mac) was unable to figure out what an f-string was.
