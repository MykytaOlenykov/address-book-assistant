# address-book-assistant-MCS3-team1

## Installation instructions

### Clone a repository

`git clone https://github.com/MykytaOlenykov/address-book-assistant-MCS3-team1`

### Change directory to project folder

`cd address-book-assistant-MCS3-team1`

### Install as a package

`python3 -m venv .env`

Linux, Mac OS: `source .env/bin/activate`
Windows: `.env/Scripts/activate`

`pip install .`

### Launch app: enter the keyword into the terminal

`bot-assistant`

### Below is a list of possible commands

COMMANDS:
----------------------------------------main------------------------------------------------------------
hello                                                   |  greeting
exit                                                    |  exit the program
close                                                   |  exit the program
help                                                    |  show help information
----------------------------------------contacts--------------------------------------------------------
all                                                     |  contacts with phones and birthdays
show-contact <name>                                     |  show a contact
add-contact <name> <phone>                              |  add a contact and phone number (XXX)-XXX-XXXX
change-contact <name> <old phone> <new phone>           |  change a contact
delete-contact <name>                                   |  delete contact/contact number
----------------------------------------phone number----------------------------------------------------
show-phone <name>                                       |  show phone of a contact
remove-phone <name> <phone>                             |  remove phone of a contact
----------------------------------------email address---------------------------------------------------
show-email <name>                                       |  show email of a contact
add-email <name> <email>                                |  add email to a contact
change-email <name> <old email> <new email>             |  change email in a contact
remove-email <name> <email>                             |  remove email of a contact
----------------------------------------address---------------------------------------------------------
show-address <name>                                     |  show address of a contact
add-address <name> <address>                            |  add address to a contact
change-address <name> <old address> <new address>       |  change address of a contact 
remove-address <name> <address>                         |  remove address of a contact 
----------------------------------------note------------------------------------------------------------
show-note <name>                                        |  show a note
find-notes <tags>                                       |  find a note
add-note <name> <note>                                  |  add a note
delete-note <name>                                      |  delete a note
add-tags <name> <tags>                                  |  add tags to a note
change-tag <name> <old tag> <new tag>                   |  change a tag of a note
remove-tags <name> <tags>                               |  remove tags of a note
----------------------------------------birthday--------------------------------------------------------
birthdays                                               |  show birthdays for next 7 days
show-birthday <name>                                    |  show birthday of a contact 
add-birthday <name> <birthday>                          |  add birthday of a contact 

### General information

#### The assistant bot has 2 main functions: creating contacts and notes.

#### Using the bot, the user can create, save, edit and delete names, phone numbers, dates of birth, emails and notes.