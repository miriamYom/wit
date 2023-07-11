import file_handler
class Wit:

    @staticmethod
    def validate_is_wit_repo():
        return file_handler.find_base_path()


    @staticmethod
    def init():
        # TODO: Handle error
        if Wit.validate_is_wit_repo():
            raise Exception("Project already Initialized")

        else:
            file_handler.create_dir(".wit")
            file_handler.create_dir(".wit/images")
            file_handler.create_dir(".wit/staging_area")


    @staticmethod
    def move_to_staging(full_path):
        target_path = os.path.join(file_handler.base_path, "staging_area")
        file_handler.copy_item(full_path, target_path)

    @staticmethod
    def add(args):
        full_path = file_handler.validate_path(args[0])
        Wit.move_to_staging(full_path)

    @staticmethod
    def commit():
        pass