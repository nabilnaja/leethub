class Twitter:
    
    def __init__(self):
        """
        Time complexity: O(1) 
        """
        self.follows = defaultdict(set)
        self.tweets = defaultdict(list)
        self.timestamp = 0
        self.feed_limit = 10
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Time complexity: O(1) 
        """
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        K is the number of followees
        k * 10 is the number of tweet we fetch
        Time complexity: O(KlogK)
        Space complexity - O (k)
        """
        users = self.follows[userId]    
        users.add(userId)
        tweets = []
        res = []
        for user in users:
            if len(self.tweets[user]) > 0:
                tweets.extend(self.tweets[user][-self.feed_limit:])
        return [tweet[1] for tweet in heapq.nlargest(self.feed_limit, tweets)]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Time complexity: O(1) 
        """
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Time complexity: O(1) 
        """
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)