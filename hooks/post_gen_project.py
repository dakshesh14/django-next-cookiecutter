import os
import shutil

BASE_DIR = "{{ cookiecutter.project_slug}}"


def remove_app_directory_from_next():
    """
    This function removes the 'apps' directory from the next project.
    """
    next_app_dir = os.path.join("apps", "web", "app")
    if os.path.exists(next_app_dir):
        shutil.rmtree(next_app_dir)


def remove_pages_directory_from_next():
    """
    This function removes the 'pages' directory from the next project.
    """
    next_pages_dir = os.path.join("apps", "web", "pages")
    if os.path.exists(next_pages_dir):
        shutil.rmtree(next_pages_dir)


def main():
    """
    This function is the main function that runs the other functions.
    """
    use_app_directory = "{{ cookiecutter.directory_structure_in_next }}" == "app"

    if use_app_directory:
        remove_pages_directory_from_next()
    else:
        remove_app_directory_from_next()


if __name__ == "__main__":
    main()
