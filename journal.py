#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: tasdik
# @Date:   2016-01-29
# @Email:  prodicus@outlook.com  Github username: @prodicus
# @Last Modified by:   tasdik
# @Last Modified time: 2016-02-02
# MIT License. You can find a copy of the License
# @http://prodicus.mit-license.org

# Follows a CRUD approach

from __future__ import print_function
from collections import OrderedDict
import sys
import datetime
import os

from peewee import *


try:
    input = raw_input   # for python2 compatibility
except NameError:
    pass

path = os.getenv('HOME', os.path.expanduser('~')) + '/.tnote'
db = SqliteDatabase(path + '/diary.db')

class DiaryEntry(Model):

    """The main Diray Model"""
    title = CharField()
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)
    tags = CharField()

    class Meta:
        database = db


def initialize():
    """Create the table and the database if they don't exist till now"""
    # os.makedirs(path, exist_ok=True)
    ## ^^ exist_ok is not there in python2 
    ## ref: http://stackoverflow.com/a/5032238/3834059

    if not os.path.exists(path):
       os.makedirs(path)
    db.connect()
    db.create_tables([DiaryEntry], safe=True)


def menu_loop():
    """To display the diary menu"""

    choice = None
    while choice != 'q':
        clear()
        print('*'*20)
        print("\nEnter 'q' to quit")
        for key, value in menu.items():
            print('{}) {} : '.format(key, value.__doc__))
        choice = input('Action : ').lower().strip()

        if choice in menu:
            clear()
            menu[choice]()


def clear():
    """for removing the clutter from the screen when necessary"""
    os.system('cls' if os.name=='nt' else 'clear')


def add_entry():
    """Adds an entry to the diary"""
    finish_key = "ctrl+Z" if os.name=='nt' else "ctrl+D"
    title_string = "Title (press %s when finished)" % finish_key
    print(title_string)
    print("="*len(title_string))
    title = sys.stdin.read().strip()
    if title:
        entry_string = "\nEnter your entry: (press %s when finished)" % finish_key
        print(entry_string)
        print("="*len(entry_string))
        data = sys.stdin.read().strip()  # reads all the data entered from the user
        if data:    # if something was actually entered
            print ("KEY", finish_key)
            print("\nEnter comma separated tags(if any!): (press %s when finished)" % finish_key)
            print("Tags: ", end="")
            tags = sys.stdin.read().strip()
            print("="*len(entry_string))
            if input("\nSave entry (y/n) : ").lower() != 'n':  # anything other than 'n'
                DiaryEntry.create(content=data, tags=tags, title=title)
                print("Saved successfully")
    else:
        print("No title entered! Press Enter to return to main menu")
        input()
        clear()
        return

def view_entry(search_query=None, search_content=True):
    """Views a diary entry"""
    entries = DiaryEntry.select().order_by(DiaryEntry.timestamp.desc())

    if search_query and search_content:
        results = list(entries.where(DiaryEntry.content.contains(search_query)))
    elif search_query and not search_content:
        results = list(entries.where(DiaryEntry.title.contains(search_query))) + list(entries.where(DiaryEntry.tags.contains(search_query)))
    else:
    	results = list(entries)

    if len(results) == 0:
        print("\nYour search had no results. Press enter to return to the main menu!")
        input()
        clear()
        return

    index = 0
    size = len(results)-1
    while 1:
        entry = results[index]
        timestamp = entry.timestamp.strftime("%A %B %d, %Y %I:%M%p ")
        clear()
        """A: weekeday name
        B: month name
        D: day number
        Y: year
        I: hour(12hr clock)
        M: minute
        p: am or pm
        """
        head = "{title} @ \"{timestamp}\"".format(title=entry.title, timestamp=entry.timestamp)
        print(head)
        print('='*len(head))
        print(entry.content)
        print(('\nTags:' + entry.tags) if entry.tags else '\nNo tags supplied')
        print('\n\n'+'='*len(head))
        print('n) next entry')
        print('p) previous entry')
        print('d) delete entry')
        print('q) to return to main menu')

        next_action = input('Action: [n/p/q/d] : ').lower().strip()
        if next_action == 'q':
            break
        elif next_action == 'd':
            delete_entry(entry)
            size -= 1
        elif next_action == 'n':
            index += 1
            if(index > size):
                index = size
        elif next_action == 'p':
            index -= 1
            if(index < 0):
                index = 0


def search_entries():
    """Let's us search through the diary entries"""
    while 1:
        clear()
        print("What do you want to search for?")
        print("c) Content")
        print("t) Title and Tags")
        print("q) Return to the main menu")
        print("===============================")
        print("Action [c/t/q] : ", end="")
        query_selector = input("").lower()
        if query_selector == "t":
            view_entry(input("Enter a search Query: "), search_content=False)
            break
        elif query_selector == "c":
            view_entry(input("Enter a search Query: "), search_content=True)
            break
        elif query_selector == "q":
            break
        else:
            print("Your input was not recognized, please try again!\n")
            input('')


def delete_entry(entry):
    """deletes a diary entry"""
    # It makes the most sense to me to delete the entry while I am
    # reading it in from the 'view_entry' method so here it is
    if input("Are you sure (y/n) : ", end="").lower().strip() == 'y':
        entry.delete_instance()
        print("Entry was deleted!")


menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entry),
    ('s', search_entries)
])

if __name__ == "__main__":
    initialize()
    menu_loop()
