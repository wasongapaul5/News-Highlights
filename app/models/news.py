class Source:
    '''
    News class to define News objects
    '''

    def __init__(self,id,name,title,description,urlToImage,author):
        self.id = id
        self.name = name
        self.title = title
        self.description = description
        self.author = author
        self.urlToImage=urlToImage


class Articles:
    '''
    Defines the articles objects
    '''

    def __init__(self,id,name,author,title,description,url,urlToImage,publishedAt):
        self.id = id
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
