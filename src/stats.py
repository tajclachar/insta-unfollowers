# stats.py: A summary of findings from an accounts following and follower data
from insta_unfollowers import InstaAnalysis


def cartesian_product(account: InstaAnalysis) -> list[tuple]:
    """returns a list of 2-element tuples which contain a follower and following"""
    every_pair = []

    for follower in account.followers:
        for following in account.following:
            pair = (follower, following)
            every_pair.append(pair)
    return every_pair

def num_cartesian_pairs(cartesian_product_list: list[tuple]) -> int:
    
    return len(cartesian_product_list)

def cartesian_mutual_pairs(account: InstaAnalysis) -> list[tuple]:
    """returns a list of 2-element tuples which contain a follower and following"""
    every_pair = []

    for follower in account.followers:
        for following in account.following:
            if follower == following:
                pair = (follower, following)
                every_pair.append(pair)
    return every_pair

def num_cartesian_mutuals_pairs(cartesian_mutual_list: list) -> int:
    return len(cartesian_mutual_list)


def unique_accounts(account: InstaAnalysis) -> int:
    return (len(account.followers) + len(account.following) - len(account.mutuals()))


def chance_you_follow_back(account: InstaAnalysis) -> float:
    return len(account.mutuals()) / len(account.followers)


def chance_follows_you_back(account: InstaAnalysis) -> float:
    return len(account.mutuals()) / len(account.following)


def summary(account: InstaAnalysis) -> dict:

    number_of_followers = len(account.followers)
    number_of_following = len(account.following)
    number_of_mutuals = len(account.mutuals())
    probability_you_follow_them = chance_you_follow_back(account)
    probability_they_follow_you_back = chance_follows_you_back(account)

    summary_dict = {"Number of Followers":number_of_followers,
                    "Number of Following":number_of_following,
                    "Number of Friends (Mutuals)":number_of_mutuals,
                    "Probability you follow someone back":probability_you_follow_them,
                    "Probability someone follows you back":probability_they_follow_you_back}

    return summary_dict