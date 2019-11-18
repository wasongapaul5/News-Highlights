import unittest
from models import news
News = news.News
class NewsTest(unittest.Testcase):
    '''
    Test class to test the behaviour of the news class
    '''
    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_source = Source('abc-news','ABC News','Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.','https://abcnews.go.com','general','en','us')
        def test_instance(self):
            self.assertTrue(isinstance(self.new_news,News))
if __name__=='__main__':
    unittest.main()