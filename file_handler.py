import os
class FileHandler:

    base_path = os.getcwd()
    working_directory = None

    @staticmethod
    def create_dir(path):
        current_path = os.path.join(base_path, path)
        if os.path.exists(current_path):
            raise Exception("directory is already exist")
        os.makedirs(path)

    @classmethod
    def find_base_path(cls):
        if cls.base_path:
            return cls.base_path
        # TODO: find first dir's path with .wit in it
        found = False
        # TODO: handle not wit repo
        # raise Exception("Not a wit repository")

    @classmethod
    def validate_path(cls, path):
        full_path = os.path.join(cls.working_directory, path)
        if not os.path.exists(full_path):
            pass
            # TODO: handle file doesn't exist

    @classmethod
    def copy_item(cls, origin, target):
        pass

