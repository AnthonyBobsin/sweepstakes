
class SweepProcessor:
    def process_status(self, status):
        # TODO: Check if it is the original tweet
        if status.retweeted:
            return None

        # TODO: Filter tweet and find out if I should follow
        # tweet = status.text
        return {
            'tweet': status.text,
            'user': status.user.name,
            'id': status.id
        }