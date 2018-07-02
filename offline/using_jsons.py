import traceback
import json
import os

import pprint

def load_db():
    db = {}
    success = []
    fail = []

    jsons = os.listdir("{0}/db".format(os.getcwd()))

    for j in jsons:
        print("Processing {0}".format(j))
        json_data = {}
        with open("{0}/db/{1}".format(os.getcwd(), j)) as fin:
            try:
                json_data = json.load(fin)
            except Exception as error:
                print("Error loading {0}: {1}".format(j, traceback.format_exc()))
                fail.append(j)
                continue
        for item in json_data:
            target = item["Target"]
            if target in db:
                db[target][j] = item
            else:
                db[target] = {}
                db[target][j] = item
        success.append(j)

    print("Success fully loaded: {0}".format(success))
    print("Couldn't load: {0}".format(fail))

    return db

def ls(db):
    pprint.pprint(db)
    return

def h():
    print("""

            To use this tool, simply enter the name of the target you wish to search for in the database
            then hit 'Enter.'

            Some other useful commands are listed below.

            Commands:
            ls -> print database
            help -> print this dialogue
            quit, .q, q, exit -> Terminate program
    """)
    return

def main():
    # Load database from JSON's
    db = load_db()

    # Holds terms that allow user to exit program
    exit_terms = ("q", ".q", "exit", "quit")

    # Commands
    commands = ("ls", "help")

    # Main input loop
    while(True):
        h()
        usr_inp = raw_input(">> ")
        if usr_inp in exit_terms:
            return
        elif usr_inp in commands: 
            if usr_inp == "ls":
                ls(db)
            elif usr_inp == "help":
                h()
        else:
            if usr_inp in db:
                print("Here's what we have on {0}:".format(usr_inp))
                pprint.pprint(db[usr_inp])
            else:
                print("{0} not found.".format(usr_inp))

if __name__ == "__main__":
    main()
