"""Instagram Follower / Unfollower Check
Taj Clachar
November 2nd, 2026"""

from pathlib import Path
import parsing
from bs4 import BeautifulSoup




def not_following_back(following_set: set[str], followers_set: set[str]) -> list[str]:
    """Return a sorted list of accounts that don't follow you back."""
    return sorted(following_set.difference(followers_set))


if __name__ == "__main__":
    main()