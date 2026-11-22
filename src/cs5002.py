# CS5002 Discrete Structures and Theory Deliverables

# Imports
from pathlib import Path
from parsing import get_directory, parse_followers, parse_following, read_soup
from insta_unfollowers import InstaAnalysis


def main():
    connection_directory = get_directory(Path('/Users/tajclachar/Documents/Computer Science/Projects/01 Instagram Followers/example_export').expanduser())

    # Create sets for the user's followers and following
    followers = parse_followers(connection_directory)
    following = parse_following(connection_directory)

    # Create Analysis object
    account = InstaAnalysis(followers, following)
    
    # print(len(account.followers))
    # print(len(account.following))

    universal_set = account.following_and_followers()
    fan_of = account.not_following_you_back()
    fans = account.accounts_you_dont_follow_back()
    mutuals = account.mutuals()

    # print(universal_set)
    # print(fan_of)
    # print(fans)
    # print(mutuals)

    # print(fan_of in universal_set)
    print(mutuals.issubset(account.following))
    print(mutuals.issubset(account.followers))

    # Module 2 (Logic and De Morgan's)

    # Let F = Followers, G = Following, U = all the followers and following, the universal set
    # Is x ∈ F ∩ G equivalent to (x ∈ F) AND (x ∈ G)?
    # mutuals we already have
    # { x ∈ F ∩ G | (x ∈ F) ∧ (x ∈ G) }
    # print(mutuals == {val for val in account.following if val in account.followers and account.following})
    

if __name__ == "__main__":
    main()