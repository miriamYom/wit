import wit_manager
class WitInterface:
    @staticmethod
    def handle_commands(command, args):
        wit_manager.Wit.init()