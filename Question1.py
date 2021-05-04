 # python 3.6

# Challenge no 1:
#
# Find the top 10 trending hashtags in twitter. You can write a standalone Python class(es) / interfaces as deemed to be fit. 
#
# Assumptions & notes :
#
# 1) A tweet is a text being input by tweeters.
#
# 2) A main method in a Python class to be implemented which takes the tweet as an input.
#
# 3) You need to extract hashtag from a tweet text (Ex:sachin is hashtag in the tweet -> "Worlds best cricketer is #sachin")
#
# 4) Maintain a data structure that keeps tracking of the count of each hashtag that is coming to your main method
#
# 5) Print the list of top 10 hashtags at the end of main method execution


import collections


class Tweeter:
    def __init__(self):
        self.hash_tag = {}

    def tweet(self, value):
        """"
        """
        string_list = value.split(' ')
        for string in string_list:
            if string.startswith('#'):
                if self.hash_tag.get(string[1:]):
                    count = self.hash_tag.get(string[1:])
                    count = count + 1
                    self.hash_tag[string[1:]] = count
                else:
                    self.hash_tag[string[1:]] = 1

    def print_top_hashtag(self):
        count = 1
        data = collections.OrderedDict(sorted(self.hash_tag.items(), key=lambda item: item[1], reverse=True))
        print('\nTop Trending Tweet"s and Their Count ')
        for keys, value in data.items():
            print(keys+' : '+str(value))
            count = count + 1
            if count == 10:
                break


if __name__ == '__main__':
    obj = Tweeter()
    tweet_continue = True
    while tweet_continue:
        message = input('enter tweet :\n')
        obj.tweet(value=message)
        wrong_input =True
        while wrong_input:
            try:
                tweet_continue_input = input('want to continue tweet Y/N :\n')
                if tweet_continue_input.lower() == 'n':
                    tweet_continue = False
                wrong_input = False
            except Exception as e:
                print(' Enter Correct Input')
    obj.print_top_hashtag()



