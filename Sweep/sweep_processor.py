import twitter

class SweepProcessor:
    def process_status(self, status):
        # TODO: Check if it is the original tweet
        if self.is_not_valid(status):
            return None

        tweet = status.text.lower()
        follow = True if "follow" in tweet else False
        return {
            'tweet': status.text,
            'user': status.user.name,
            'id': status.id,
            'follow': follow
        }

    def is_not_valid(self, status):
        return status.retweeted or status.in_reply_to_user_id or ("rt" not in status.text.lower())