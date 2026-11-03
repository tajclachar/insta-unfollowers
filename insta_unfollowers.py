"""Instagram Follower / Unfollower Check
Taj Clachar
November 2nd, 2026"""

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


def parse_following(parsed_file: BeautifulSoup) -> set[str]:
    """Parse through an html file and return the set of usernames that are being 
    followed"""

    following_list = []

    for name in parsed_file.find_all('h2', class_='_3-95 _2pim _a6-h _a6-i'):
        following_list.append(name.get_text())

    return set(following_list)


def parse_followers(parsed_file: BeautifulSoup) -> set[str]:
    """Parse an html file to return a set containing all of the follower's 
    usernames"""

    followers_list = []

    for name in parsed_file.find_all('a', target='_blank'):
        followers_list.append(name.get_text())

    return set(followers_list)


def save_result(usernames: list[str], export_path: Path) -> None:
    """Write the usernames to a file"""

    with open(file=export_path, mode='w', encoding='utf-8') as f:
        for username in usernames:
            f.write(username + '\n')


def not_following_back(following_set: set[str], followers_set: set[str]) -> list[str]:
    """Return a sorted list of accounts that don't follow you back."""
    return sorted(following_set.difference(followers_set))


def main() -> None:
    """Prompt an export folder, discover who isn't following back and save the list down"""

    folder = input("Path to your Instagram export folder: ").strip().strip("'\"")
    connection_directory = get_directory(Path(folder).expanduser())

    # Get the following file
    following = parse_following(read_soup(connection_directory / "following.html"))

    # Get followers file
    followers = set()
    for file in connection_directory.glob("followers_*.html"):
        followers |= parse_followers(read_soup(file))

    # Calculate the difference between the followers and following
    result = not_following_back(following, followers)

    for username in result:
        print(username)
    print(f"\n{len(result)} accounts aren't following you back :(")

    # Saving the results as a text file
    save_result(result, Path("not_following_back.txt"))
    print("Full list saved to not_following_back.txt")


if __name__ == "__main__":
    main()