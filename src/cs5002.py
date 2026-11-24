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
    
    # print(len(followers))
    # print(len(following))

    # Let F = Followers, G = Following, U = all the followers and following, the universal set

    # Module 3
    # F ∪ G = U = { x | x ∈ F ⋁ x ∈ G } 
    universal_set = account.following_and_followers()

    # G - F = { x ∈ U | x ∈ G ∧ x ∉ F}
    fan_of = account.not_following_you_back()

    # F - G = { x ∈ U | x ∈ F ∧ x ∉ G}
    fans = account.accounts_you_dont_follow_back()

    # F ∩ G = { x ∈ U | x ∈ F ∧ x ∈ G}
    mutuals = account.mutuals()

    # print(universal_set)
    # print(fan_of)
    # print(fans)
    # print(mutuals)

    # Checking if the mutuals set is a subset of followers and following subsets
    print(mutuals.issubset(following))
    print(mutuals.issubset(followers))

    # Module 2 (Logic and De Morgan's)

    # Let F = Followers, G = Following, U = all the followers and following, the universal set
    # Is x ∈ F ∩ G equivalent to (x ∈ F) AND (x ∈ G)?
    # mutuals we already have
    # { x ∈ F ∩ G | (x ∈ F) ∧ (x ∈ G) }
    print(mutuals == {val for val in universal_set if val in followers and val in following})   
    print(mutuals == (followers.intersection(following)))

    # complement(F ∩ G) = complement(F) ∪ complement(G)
    # 1. complement(F ∩ G) = U − (F ∩ G) - Everyone who isn't a mutual
    com_f_and_g = universal_set - (followers & following)
    # 2. complement(F) = U - F and complement(G) = U - G
    complement_f = universal_set - followers
    complement_g = universal_set - following

    # Both sets are empty and they equal each other.
    print(com_f_and_g == (complement_f | complement_g))

    # Inclusion Exclusion Principle
    # The union of two sets F and G
    num_followers = len(followers)
    num_following = len(following)

    total_accounts = num_following + num_followers
    total_unique_accounts = (num_followers + num_following - len(mutuals))
    print(f"The number of total accounts (including dupes) is {total_accounts}, but by using the inclusion exclusion principle, we can get the number of unique accounts which is {total_unique_accounts}!")
    print(f"Is the number of unique accounts equal to the number of accounts in the universal set? {total_unique_accounts == len(universal_set)}")


    # Module 3/4 Cartesian Products & Counting
    # Check if the length of the cartesian product is equal to the cardinality of 
    # the followers set multiplied by the cardinality of the following set
    cartesian_product = account.cartesian_product()
    print(f"Is the length of the cartesian product equal to the length of the product of the cardinalities of the following and followers set?: {len(cartesian_product) == (len(following) * len(followers))}")

    cartesian_mutuals = account.cartesian_mutual_count()
    print(f"Is the length of the cartesian product of the following and followers set equal to finding the mutuals using set operations? {(len(cartesian_mutuals) == len(mutuals))}")

    # Probability
    

if __name__ == "__main__":
    main()