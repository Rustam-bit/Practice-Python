import heapq
from typing import List


class Twitter:

    def __init__(self):
        self.tweets = {}
        self.follows = {}
        self.time = 0

    def post_tweet(self, user_id, tweet_id):
        if user_id not in self.tweets:
            self.tweets[user_id] = []
        self.tweets[user_id].append((self.time, tweet_id))
        self.time += 1

    def get_news_feed(self, user_id) -> List[int]:
        twet = []
        if user_id in self.tweets:
            twet.extend(self.tweets[user_id])
        if user_id in self.follows:
            for foloewee in self.follows[user_id]:
                if foloewee in self.tweets:
                    twet.extend(self.tweets.get(foloewee, []))
        return [x for _, x in heapq.nlargest(10, twet)]

    def follow(self, follower_id, followee_id):
        if follower_id not in self.follows:
            self.follows[follower_id] = set()
        self.follows[follower_id].add(followee_id)

    def unfollow(self, follower_id, followee_id):
        if follower_id in self.follows:
            if followee_id in self.follows[follower_id]:
                self.follows[follower_id].remove(followee_id)


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
