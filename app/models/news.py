class Source:
    '''
    Source class to define  objects
    '''

    def __init__(self,id,name,title,urlToImage,author):
        self.id = id
        self.name = name
        self.title = title
        self.description = description
        self.urlToImage=urlToImage
        self.author = author


class Articles:
    '''
    Defines the articles objects
    '''

    def __init__(self,id,name,author,title,url,urlToImage):
        self.id = id
        self.name = name
        self.author = author
        self.title = title
        self.url = url
        self.urlToImage = urlToImage
