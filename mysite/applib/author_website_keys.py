class AuthorWebsiteKeys(object):
    #integer keys for apps
    GLOBAL = 0
    HOME = 1
    ARTICLES = 2

    #integer keys for file types
    HTML = 0
    CSS = 1
    JS = 2
    JPG = 3

    #id keys for request of file path as STATICROOT or as STATICURL
    STATICROOT = 0
    STATICURL = 1

    #website content or frontend (HTML, CSS, JS) pages
    CONTENT = 0
    FRONTEND = 1

    def __init__(self):
        pass