from wit_manager import Wit

class WitInterface:
    @staticmethod
    def handle_commands(command, args):
        if command == "init":
            Wit.init()




