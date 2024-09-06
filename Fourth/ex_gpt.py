from typing import List, Dict, Set
import heapq


class Twitter:
    def __init__(self):
        # Хранение твитов: ключ — user_id, значение — список твитов (кортеж (счетчик, tweet_id))
        self.tweets = {}
        # Хранение подписок: ключ — follower_id, значение — множество followee_id
        self.following = {}
        # Счетчик для твитов, чтобы упорядочивать их по времени
        self.time = 0

    def post_tweet(self, user_id: int, tweet_id: int):
        # Если это первый твит пользователя, инициализируем его список твитов
        if user_id not in self.tweets:
            self.tweets[user_id] = []
        # Добавляем новый твит с временной меткой (счетчиком)
        self.tweets[user_id].append((self.time, tweet_id))
        self.time += 1

    def get_news_feed(self, user_id: int) -> List[int]:
        # Собираем твиты самого пользователя
        tweets_to_show = self.tweets.get(user_id, [])
        # Собираем твиты пользователей, на которых он подписан
        if user_id in self.following:
            for followee_id in self.following[user_id]:
                tweets_to_show.extend(self.tweets.get(followee_id, []))

        # Отбираем 10 последних твитов с помощью кучи (приоритетной очереди)
        return [tweet_id for _, tweet_id in heapq.nlargest(10, tweets_to_show)]

    def follow(self, follower_id: int, followee_id: int):
        # Если пользователь не подписывался раньше, инициализируем его подписки
        if follower_id not in self.following:
            self.following[follower_id] = set()
        # Подписываем пользователя на другого
        self.following[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int):
        # Если пользователь подписан на кого-то, отписываем его
        if follower_id in self.following and followee_id in self.following[follower_id]:
            self.following[follower_id].remove(followee_id)


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
