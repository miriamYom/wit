from wit_manager import Wit

class WitInterface:
    @staticmethod
    def handle_commands(command, args):
        try:
            if command == "init":
                Wit.init()
        # except:





