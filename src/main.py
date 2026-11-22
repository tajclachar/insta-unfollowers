# Main: Where the function runs

from insta_unfollowers import 
from pathlib import Path
from bs4 import BeautifulSoup
from parsing import get_directory, parse_followers, parse_following

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



    # Saving the results as a text file
    save_result(result, Path("not_following_back.txt"))
    print("Full list saved to not_following_back.txt")

if __name__ == "__main__":
    main()