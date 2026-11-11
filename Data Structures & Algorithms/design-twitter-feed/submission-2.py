
import time
class Twitter:

    def __init__(self):
        self.users = {}

    def createUser(self, userId):
        self.users[userId] = {
            "tweets": [],
            "follows": set()
        }


    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.createUser(userId)

        self.users[userId]["tweets"].append((time.time(), tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        if userId not in self.users:
            self.createUser(userId)
        
        res = heapq.heapify(self.users[userId]["tweets"][-10:])

        for followeeId in self.users[userId]["follows"]:
            tweets = self.users[followeeId]["tweets"][-10:]
            for tweet in tweets:
                heapq.heappush(res, tweet)
                if len(res) > 10:
                    heapq.heappop(res)
        
        res.sort(reverse=True)

        return [tup[1] for tup in res[:10]]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.createUser(followerId)
        if followeeId not in self.users:
            self.createUser(followeeId)
        if followeeId not in self.users[followerId]["follows"]:
            self.users[followerId]["follows"].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.createUser(followerId)
        if followeeId not in self.users:
            self.createUser(followeeId)
        if followeeId in self.users[followerId]["follows"]:
            self.users[followerId]["follows"].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)