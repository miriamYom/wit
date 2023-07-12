import sys
# this message will couse conflicts.... goodluck us!!!
import wit_interface

import wit_interface as WitInterface

if __name__ == "__main__":
    # TODO: handle edge cases
    command = sys.argv[1]
    args = sys.argv[2:]
    WitInterface.handle_commands(command, args)
    print("אני לא מצליחה להתרכז!!!")
