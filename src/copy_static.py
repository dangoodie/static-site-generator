import os, shutil


def get_project_root():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    return project_root


def check_dest(dest):
    if not os.path.exists(dest):
        os.mkdir(dest)


def delete_from_dest(dest):
    contents = os.listdir(dest)

    for item in contents:
        item_path = os.path.join(dest, item)

        # file
        if os.path.isfile(item_path):
            os.remove(item_path)
        else:
            # directory
            delete_from_dest(item_path)
            os.rmdir(item_path)


def copy_source_to_dest(source, dest):
    if os.path.exists(source):
        contents = os.listdir(source)

        for item in contents:
            item_path = os.path.join(source, item)

            # file
            if os.path.isfile(item_path):
                shutil.copy(item_path, dest)
            else:
                # directory
                dir_path = os.path.join(dest, item)
                os.mkdir(dir_path)
                copy_source_to_dest(item_path, dir_path)
