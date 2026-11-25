# Main: Where the function runs

# from insta_unfollowers
from pathlib import Path
from parsing import get_directory, parse_followers, parse_following
from insta_unfollowers import InstaAnalysis
from stats import summary

def main() -> None:
    """Prompt an export folder, discover who isn't following back and save the list down"""

    # Grab user folder path
    folder = input("Path to your Instagram export folder: ").strip().strip("'\"")

    # get_directory, creates the path to the exist folder within the users download. 
    connection_directory = get_directory(Path(folder).expanduser())

    # Create sets for the user's followers and following
    followers = parse_followers(connection_directory)
    following = parse_following(connection_directory)

    # Create Analysis object
    account = InstaAnalysis(followers, following)

    
    for key, value in summary(account).items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
