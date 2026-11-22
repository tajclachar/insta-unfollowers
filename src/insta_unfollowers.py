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
        pass

    def not_following_you_back(self):
        pass

    def not_following__you_back(self) -> list[str]:
        """Return a sorted list of accounts that don't follow you back."""
        return sorted(self.following.difference(self.followers))


    def accounts_you_dont_follow_back(self):
        pass

    def mutuals(self):
        pass





