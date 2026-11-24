# Creating a class for Instagram followers.

class InstaAnalysis():
    def __init__(self, followers: set, following: set) -> None:

        # Type Check
        if type(followers) != set:
            raise TypeError("Please only insert a set here!")
        if type(following) != set:
            raise TypeError("Please only insert a set here!")

        # Value Check

        # Other check that Im forgetting

        # Initialize
        self.followers = followers
        self.following = following

    def following_and_followers(self) -> set[str]:
        """Returns a set of every unique username thats in the follower and following list"""
        return self.following.union(self.followers)


    def not_following_you_back(self) -> set[str]:
        """Return a set of accounts that don't follow you back."""
        return self.following.difference(self.followers)


    def accounts_you_dont_follow_back(self) -> set[str]:
        """Return a set of accounts that you don't follow back."""
        return self.followers.difference(self.following)


    def mutuals(self) -> set[str]:
        """Returns a set of elements that are in both of the sets. """
        return self.following.intersection(self.followers)

    def cartesian_product(self) -> list[tuple]:
        """returns a list of 2-element tuples which contain a follower and following"""
        every_pair = []

        for follower in self.followers:
            for following in self.following:
                pair = (follower, following)
                every_pair.append(pair)
        return every_pair



    def cartesian_mutual_count(self) -> list[tuple]:
        """returns a list of 2-element tuples which contain a follower and following"""
        every_pair = []

        for follower in self.followers:
            for following in self.following:
                if follower == following:
                    pair = (follower, following)
                    every_pair.append(pair)
        return every_pair



if __name__ == "__main__":
    t = InstaAnalysis({'a', '1', 'b'}, {'a', 'drake', '2'})
    print(t.following_and_followers())
    print(t.not_following_you_back())
    print(t.accounts_you_dont_follow_back()) 
    print(t.mutuals()) 



