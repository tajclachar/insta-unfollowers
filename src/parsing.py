# parsing.py - Creates a set of followers and following from a given path
from pathlib import Path
from bs4 import BeautifulSoup


def get_directory(directory: Path) -> Path:
    """Returns the file path to the folder that contains the followers and
    following file. If the path isn't valid, an error is returned"""

    connection_directory = directory / "connections" / "followers_and_following"

    if not connection_directory.exists():
        print("Couldn't find your followers/following files.")
        print("Make sure you gave the unzipped export folder, downloaded in HTML format!")
        raise SystemExit(1)
    return connection_directory


def read_soup(file_path: Path) -> BeautifulSoup:
    """Read in an html file and returns the parsed version"""
    with open(file_path, 'r', encoding='utf-8') as file:
        read_html = file.read()

    return BeautifulSoup(read_html, 'html.parser')


def parse_following(connection_directory: Path) -> set[str]:
    """Parse through an html file and return the set of usernames that are being 
    followed"""

    following_list = []
    parsed_file = read_soup(connection_directory / "following.html")
    for name in parsed_file.find_all('h2', class_='_3-95 _2pim _a6-h _a6-i'):
        following_list.append(name.get_text())

    return set(following_list)


def parse_followers(connection_directory: Path) -> set[str]:
    """Parse an html file to return a set containing all of the follower's 
    usernames"""

    followers_list = []
    for file in connection_directory.glob("followers_*.html"):
        parsed_file = read_soup(file)
        for name in parsed_file.find_all('a', target='_blank'):
            followers_list.append(name.get_text())

    return set(followers_list)


def save_result(usernames: list[str], export_path: Path) -> None:
    """Write the usernames to a file"""

    with open(file=export_path, mode='w', encoding='utf-8') as f:
        for username in usernames:
            f.write(username + '\n')
