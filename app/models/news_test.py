import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''

        self.new_news = source('abc-news','ABC NEWS','Your trusted source for breaking news anylisis  exclusive interviews,headlines,videos at ABCNews.com','https://abcnews.go.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()