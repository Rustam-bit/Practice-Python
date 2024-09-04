from typing import List


class Twitter:

   def __init__(self):
       # YOUR CODE HERE

   def post_tweet(self, user_id, tweet_id):
       # YOUR CODE HERE

   def get_news_feed(self, user_id) -> List[int]:
       # YOUR CODE HERE

   def follow(self, follower_id, followee_id):
       # YOUR CODE HERE

   def unfollow(self, follower_id, followee_id):
       # YOUR CODE HERE

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)