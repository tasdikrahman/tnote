## tnote

[![GitHub license](https://img.shields.io/pypi/l/pyzipcode-cli.svg)](https://img.shields.io/pypi/l/pyzipcode-cli.svg) [![Supported python versions](https://img.shields.io/pypi/pyversions/Django.svg)]([![PyPI](https://img.shields.io/pypi/pyversions/Django.svg)]()) [![Join the chat at https://gitter.im/prodicus/tnote](https://badges.gitter.im/prodicus/tnote.svg)](https://gitter.im/prodicus/tnote?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

```
                            _________ _        _______ _________ _______ 
                            \__   __/( (    /|(  ___  )\__   __/(  ____ \
                               ) (   |  \  ( || (   ) |   ) (   | (    \/
                               | |   |   \ | || |   | |   | |   | (__    
                               | |   | (\ \) || |   | |   | |   |  __)   
                               | |   | | \   || |   | |   | |   | (      
                               | |   | )  \  || (___) |   | |   | (____/\
                               )_(   |/    )_)(_______)   )_(   (_______/
```

A dead simple command line note taking app built for you!

## Index

- [Demo](#demo)
- [Features](#features)
- [Installation](#installation)
  - [Installing dependencies](#installing-dependencies)
  - [Clone it](#clone-it)
  - [Run it](#run-it)
- [Supported platforms](#supported-platforms)
- [Contributing](#contributing)
  - [To-do](#to-do)
  - [Contributers](#contributers)
- [Issues](#issues)
- [License](#license)
- [Donation](#donation)

## Demo
[:arrow_up: Back to top](#index)

Watch a live demo of it working here

[![asciicast](https://asciinema.org/a/35557.png)](https://asciinema.org/a/35557)

*Here's the [link to previous version](https://asciinema.org/a/35378) if you are interested!*

***

## Features
[:arrow_up: Back to top](#index)

- **Dead simple to use**: Even your granny would be able to use it. No seriously!
- **Feature rich** Add your precious note with it's _title_ , _content_ , _tags_
- **Secure**: Encrypts your database using standard **AES-256 in CBC mode**. So even if anybody gets hand of your database file. He cannot make any sense of it. [A little demo of what I am doing using it](https://github.com/tasdikrahman/tnote/wiki/So-you-say-it-is-encrypted-eh%3F)

**NOTE**
  _This feature is available/tested only on linux based systems. Support for other OS's coming soon!_

- **Text Highlighting is cross platform** - Supports Linux, Windows and Mac for the terminal based highlighting.
- **Searching for notes is hassle free** in `tnote`: It supports full text search for notes based on _content_, _tags_
    - The search query if found in the database will be highlighted if found. Looks pleasing to the eyes
- Ability to add and remove tags for each note.
- Adds timestamp for each note which has been added.
- Written in uncomplicated python.

Need I say more?

***

## Installation
[:arrow_up: Back to top](#index)

#### Installing dependencies

**NOTE** 

On **Linux**, install `libsqlcipher-dev` 

```sh
$ sudo apt-get install libsqlcipher-dev
```

On **Mac OS**, you can install it by 

```sh
$ brew install sqlcipher
```

#### Clone it


```sh
$ git clone https://github.com/tasdikrahman/tnote.git
$ cd tnote && pip install -r requirements.txt
```

*Add a symbolic link to it*

```sh
$ chmod +x tnote
$ cd ~/bin/ 
$ ln -s ~/some/path/to/tnote
```

Replace `~/some/path/to/tnote` by the path where you have cloned the repo. For example if you have cloned it to `~/Downloads/tnote` folder than your command should look something like

`$ ln -s ~/Downloads/tnote/tnote`

#### Run it

Fire it up! :volcano:

`$ tnote`

***

## Supported platforms
[:arrow_up: Back to top](#index)

| OS | Support status |
| --- | --- |
| Linux | :white_check_mark: Full support |
| Mac OS | :white_check_mark: Full support  |
| Windows | :ballot_box_with_check: encrytion of the Database for windows not yet supported |

***

## Contributing
[:arrow_up: Back to top](#index)

This app was created in a timespan of 2 hours while learning to use [peewee (ORM)](https://github.com/coleifer/peewee). So don't be shy to make some PR's here :smile:

#### To-do
    
- [ ] Add **unit tests**. Like real quick!
- [ ] Make it pip installable
- [ ] Ability to edit the content of a note
- [x] Add python2 support
- [x] Add tags support for notes
- [x] Remove tahs for notes
- [x] Add option to add title for notes
- [ ] Add option to remove title for notes
- [x] Add option to search for notes using content
- [x] Add option to search for notes using tags
- [ ] Add option to search for notes using title
- [ ] Add option to search for notes using timestamp
- [x] Encrypt the `.db` file using **Sqlcipher**
- [x] Add colorized text to the notes for improved UI
- [ ] Add better UI using **urwid**

#### Contributers

A big shout out to all the contributers, more specifically to these guys

- [@maxwellgerber](https://github.com/maxwellgerber)
- [@BrandtM](https://github.com/BrandtM)

## Motivation
[:arrow_up: Back to top](#index)

Why not! Cheers to a crazy weekend :smile:

***

## Issues
[:arrow_up: Back to top](#index)

You can report the bugs at the [issue tracker](https://github.com/tasdikrahman/tnote/issues)

**OR**

You can [tweet me](https://twitter.com/tasdikrahman) if you can't get it to work. In fact, you should tweet me anyway.

***

## License
[:arrow_up: Back to top](#index)

Built with ♥ and after a lot of pizzas by [Tasdik Rahman](http://tasdikrahman.me) under [MIT License](http://prodicus.mit-license.org)

You can find a copy of the License at http://prodicus.mit-license.org/

## Donation
[:arrow_up: Back to top](#index)

If you have found my little bits of software being of any use to you, do consider helping me pay my internet bills :)

| PayPal | <a href="https://paypal.me/tasdik" target="_blank"><img src="https://www.paypalobjects.com/webstatic/mktg/logo/AM_mc_vs_dc_ae.jpg" alt="Donate via PayPal!" title="Donate via PayPal!" /></a> |
|:-------------------------------------------:|:-------------------------------------------------------------:|
| Gratipay  | <a href="https://gratipay.com/tasdikrahman/" target="_blank"><img src="https://cdn.rawgit.com/gratipay/gratipay-badge/2.3.0/dist/gratipay.png" alt="Support via Gratipay" title="Support via Gratipay" /></a> |
| Patreon | <a href="https://www.patreon.com/tasdikrahman" target="_blank"><img src="http://i.imgur.com/ICWPFOs.png" alt="Support me on Patreon" title="Support me on Patreon" /></a> |
| £ (GBP) | <a href="https://transferwise.com/pay/d804d854-6862-4127-afdd-4687d64cbd28" target="_blank"><img src="http://i.imgur.com/ARJfowA.png" alt="Donate via TransferWise!" title="Donate via TransferWise!" /></a> |
| € Euros | <a href="https://transferwise.com/pay/64c586e3-ec99-4be8-af0b-59241f7b9b79" target="_blank"><img src="http://i.imgur.com/ARJfowA.png" alt="Donate via TransferWise!" title="Donate via TransferWise!" /></a> |
| ₹ (INR)  | <a href="https://www.instamojo.com/@tasdikrahman" target="_blank"><img src="https://www.soldermall.com/images/pic-online-payment.jpg" alt="Donate via instamojo" title="Donate via instamojo" /></a> |
