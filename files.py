import os


def get_project_dir():
    return os.getcwd()


def get_news_dir():
    project_dir = get_project_dir()
    return os.path.join(project_dir, "30News")


def list_files_on_dir(dirname):
    return os.listdir(dirname)


def get_news_name_list():
    news_dir = get_news_dir()
    news_list = list_files_on_dir(news_dir)
    return news_list


def stringfy_file(path: str):
    try:
        with open(path, "rt", encoding="utf-8") as f:
            text = f.read()
            return text
    except Exception as e:
        print(e)


def get_new_at_index(idx: int):
    news_list = get_news_name_list()
    news_dir = get_news_dir()

    try:
        chosen_new = news_list[idx]
    except:
        print("Index out of bounds")

    new_path = os.path.join(news_dir, chosen_new)

    return stringfy_file(new_path)
