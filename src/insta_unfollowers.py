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

    def following_and_followers(self):
        """Returns a list of every unique username thats in the follower and following list"""
        return sorted(self.following.union(self.followers))


    def not_following_you_back(self) -> list[str]:
        """Return a sorted list of accounts that don't follow you back."""
        return sorted(self.following.difference(self.followers))


    def accounts_you_dont_follow_back(self):
        """Return a list of accounts that you follow, but don't follow back."""
        return sorted(self.followers.difference(self.following))


    def mutuals(self):
        """Returns a list of elements that are in both of the sets. """
        return sorted(self.following.intersection(self.followers))


if __name__ == "__main__":
    t = InstaAnalysis({'a', '1', 'b'}, {'a', 'drake', '2'})
    print(t.following_and_followers())
    print(t.not_following_you_back())
    print(t.accounts_you_dont_follow_back()) 
    print(t.mutuals()) 



