# Main: Where the function runs

# from insta_unfollowers
from pathlib import Path
from parsing import get_directory, parse_followers, parse_following, read_soup
from insta_unfollowers import InstaAnalysis

def main() -> None:
    """Prompt an export folder, discover who isn't following back and save the list down"""

    folder = input("Path to your Instagram export folder: ").strip().strip("'\"")
    connection_directory = get_directory(Path(folder).expanduser())
    parsed_html = read_soup(connection_directory)
    followers = parse_followers(parsed_html)
    following = parse_following(parsed_html)

    # Create Analysis object
    account_object = InstaAnalysis(followers, following)
    account_object.not_following__you_back()



if __name__ == "__main__":
    main()
