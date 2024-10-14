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

### Commands:

#### Main:
| Command                   | Description                             |
|---------------------------|-----------------------------------------|
| `hello`                   | Greet the user                          |
| `exit` or `close`         | Exit the program                        |
| `help`                    | Show help information                   |

#### Contacts:
| Command                   | Description                             |
|---------------------------|-----------------------------------------|
| `all`                     | List all contacts with phones and birthdays     |
| `show-contact <name>`     | Show details of a contact               |
| `add-contact <name> <phone>` | Add a contact with phone number (XXX)-XXX-XXXX |
| `change-contact <name> <old phone> <new phone>` | Change a contact's phone number  |
| `delete-contact <name>`   | Delete a contact                        |

#### Phone Number:
| Command                   | Description                             |
|---------------------------|-----------------------------------------|
| `show-phone <name>`       | Show phone number of a contact          |
| `remove-phone <name> <phone>` | Remove phone number of a contact     |

#### Email Address:
| Command                   | Description                             |
|---------------------------|-----------------------------------------|
| `show-email <name>`       | Show email address of a contact         |
| `add-email <name> <email>` | Add email to a contact                 |
| `change-email <name> <old email> <new email>` | Change a contact's email address |
| `remove-email <name> <email>` | Remove email of a contact            |

#### Address:
| Command                   | Description                             |
|---------------------------|-----------------------------------------|
| `show-address <name>`     | Show address of a contact               |
| `add-address <name> <address>` | Add address to a contact            |
| `change-address <name> <old address> <new address>` | Change a contact's address    |
| `remove-address <name> <address>` | Remove address of a contact       |

#### Note:
| Command                   | Description                             |
|---------------------------|-----------------------------------------|
| `show-note <name>`        | Show a note                             |
| `find-notes <tags>`       | Find notes by tags                      |
| `add-note <name> <note>`  | Add a new note                          |
| `delete-note <name>`      | Delete a note                           |
| `add-tags <name> <tags>`  | Add tags to a note                      |
| `change-tag <name> <old tag> <new tag>` | Change a tag of a note           |
| `remove-tags <name> <tags>` | Remove tags from a note               |

#### Birthday:
| Command                   | Description                             |
|---------------------------|-----------------------------------------|
| `birthdays`               | Show birthdays for the next 7 days       |
| `show-birthday <name>`    | Show birthday of a contact              |
| `add-birthday <name> <birthday>` | Add birthday of a contact         |



### General information

#### The assistant bot has 2 main functions: creating contacts and notes.

#### Using the bot, the user can create, save, edit and delete names, phone numbers, dates of birth, emails and notes.
