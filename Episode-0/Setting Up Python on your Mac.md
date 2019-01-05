# Setting up Python on my Mac

Because I was using my Mac to record the episode with Jay, I had to install Python 3.7 using Homebrew. MacOS currently (at the time of recording the episode: Jan 1st 2019) shipps with Python 2.7 installed, but support for that version is rapidly running out.

Installing Python 3.7 was as easy as running two commands:

ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
This command installs Homebrew on to your Mac, and can be incredibly useful for installing things very quickly from within the terminal.

brew install python
This is the command required to install Python 3.7 on my Mac. Once this is done, I checked which version of Python I had installed by running the following python --version which told me that I was running 3.7.
