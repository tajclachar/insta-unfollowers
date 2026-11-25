# Main: Where the function runs

# from insta_unfollowers
from pathlib import Path
from parsing import get_directory, parse_followers, parse_following, save_result
from insta_unfollowers import InstaAnalysis
from stats import summary

def main() -> None:
    """Prompt an export folder, discover who isn't following back and save the list down"""

    # Grab user folder path
    folder = input("Path to your Instagram export folder: ").strip().strip("'\"")

    save_decision = input("Would you like to save the list of people not following you back to a text file? (y/n): ")
    save_decision = save_decision.strip().lower()

    # get_directory, creates the path to the exist folder within the users download. 
    connection_directory = get_directory(Path(folder).expanduser())

    # Create sets for the user's followers and following
    followers = parse_followers(connection_directory)
    following = parse_following(connection_directory)

    # Create Analysis object
    account = InstaAnalysis(followers, following)

    # Print the stats
    for key, value in summary(account).items():
        print(f"{key}: {value}")

    # Sorted list of accounts not following the user back
    not_following_back = sorted(account.not_following_you_back())

    # Print a list of those who aren't following you back
    for name in not_following_back:
        print(name)
    
    # Save the Results
    if save_decision == "y":
        save_result(not_following_back, Path("not_following_back.txt"))
        print("Saved to not_following_you_back.txt")


if __name__ == "__main__":
    main()
