class Twitter:
    """
    Time complexity: 
    Space complexity:    
    """
    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = defaultdict(list)
        self.timestamp = 0
        self.feed_limit = 10
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.follows[userId]    
        users.add(userId)
        tweets = []
        res = []
        for user in users:
            if len(self.tweets[user]) > 0:
                tweets.extend(self.tweets[user][-self.feed_limit:])
        return [tweet[1] for tweet in heapq.nlargest(self.feed_limit, tweets)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)