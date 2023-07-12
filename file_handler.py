import os
class FileHandler:

    base_path = None
    working_directory = None

    @classmethod
    def create_dir(cls, path):
        current_path = os.path.join(cls.base_path, path)
        if os.path.exists(current_path):
            raise Exception("directory is already exist")
        os.makedirs(path)

    @classmethod
    def find_base_path(cls):
        current_directory = os.getcwd()
        while current_directory != '/':
            cls.base_path = os.path.join(current_directory, '.wit')
            if os.path.isdir(cls.base_path):
                return cls.base_path
            current_directory = os.path.dirname(current_directory)
        raise FileNotFoundError(".wit directory not found.")

    # @classmethod
    # def find_base_path(cls):
    #     if cls.base_path:
    #         return cls.base_path
    #     # TODO: find first dir's path with .wit in it
    #     found = False
    #     # TODO: handle not wit repo
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

