#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: tasdik
# @Date:   2016-01-29
# @Email:  prodicus@outlook.com  Github username: @prodicus
# @Last Modified by:   maxwellgerber
# @Last Modified time: 2016-02-01
# MIT License. You can find a copy of the License
# @http://prodicus.mit-license.org

# Follows a CRUD approach
from __future__ import print_function
from builtins import input
from collections import OrderedDict
import sys
import datetime
import os

from peewee import *

path = os.getenv('HOME', os.path.expanduser('~')) + '/.tnote'
db = SqliteDatabase(path + '/diary.db')

class DiaryEntry(Model):

    """The main Diray Model"""
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


def initialize():
    """Create the table and the database if they don't exist till now"""
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
    if os.name=='nt':
        print("Enter your entry: (press ctrl+Z <Return> when finished)")
    else:
        print("Enter your entry: (press ctrl+D when finished)")
    data = sys.stdin.read().strip() # reads all the data entered from the user
    if data:    # if something was actually entered
        if input("\nSave entry (y/n)").lower() != 'n':  # anything other than 'n'
            DiaryEntry.create(content=data)
            print("Saved successfully")


def view_entry(search_query=None):
    """Views a diary entry"""
    entries = DiaryEntry.select().order_by(DiaryEntry.timestamp.desc())

    if search_query:
        entries = entries.where(DiaryEntry.content.contains(search_query))

    entries = list(entries)
    index = 0
    size = len(entries)-1
    while 1:
        if(len(entries) > 0):
            entry = entries[index]
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
            print(timestamp)
            print('='*len(timestamp))
            print(entry.content)
            print('\n\n'+'='*len(timestamp))
        else:
            no_notes = 'You have no notes.'
            print('='*len(no_notes))
            print(no_notes)
            print('\n\n'+'='*len(no_notes))
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
    view_entry(input("Enter a search Query: "))


def delete_entry(entry):
    """deletes a diary entry"""
    # It makes the most sense to me to delete the entry while I am
    # reading it in from the 'view_entry' method so here it is
    if input("Are you sure (y/n) : ").lower().strip() == 'y':
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
