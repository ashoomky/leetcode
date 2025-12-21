class Twitter(object):

    def __init__(self):
        self.follow_map = defaultdict(set) # stores user ids and followees
        self.tweet_map = defaultdict(list) # stores user ids and their tweet as a list of (count, tweet ids) pairs
        self.count = 0 # tracks number of tweets

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.tweet_map[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        result = [] # ordered starting from most recent
        min_heap = []

        #since a user can technically follow themselves, add them to the followset 
        self.follow_map[userId].add(userId)
        for followeeId in self.follow_map[userId]:
            if followeeId in self.tweet_map:
                index = len(self.tweet_map[followeeId]) - 1 # index of the most recent tweet of who user follows 
                count, tweetId = self.tweet_map[followeeId][index] # count and tweet id of who user follows most recent tweet
                min_heap.append([count, tweetId, followeeId, index - 1]) # keep track of followee id because we need it to get the next most recent tweet, and index - 1 to access the previous tweet (next most recent)
        heapq.heapify(min_heap)

        while min_heap and len(result) < 10:
            count, tweetId, followeeId, index = heapq.heappop(min_heap)
            result.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweet_map[followeeId][index] # tells us the next tweet to add to our heap
                heapq.heappush(min_heap, [count, tweetId, followeeId, index - 1])
        return result


    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)





# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)