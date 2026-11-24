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

def num_cartesian_pairs(cartesian_product_list = list[tuple]) -> int:
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

def num_cartsian_mutuals_pairs(cartesian_mutual_list: list) -> int:
    return len(cartesian_mutual_list)


def unique_accounts(account: InstaAnalysis) -> int:
    return (len(account.followers) + len(account.following) - len(account.mutuals()))

def chance_follows_you_back(account: InstaAnalysis) -> float:
    return len(account.mutuals()) / len(account.following)


def chance_you_follow_back(account: InstaAnalysis) -> float:
    return len(account.mutuals()) / len(account.followers)



def summary(account: InstaAnalysis) -> dict:
    pass
