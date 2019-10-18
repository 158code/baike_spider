class UrlManager(object):
    
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    # 添加 url
    def add_new_url(self, url):
        if url is None:
            return

        if url not in self.new_urls or url not in self.old_urls:
            self.new_urls.add(url)

    # 添加新的 url
    def add_new_urls(self, urls):
        if urls is None:
            return

        for url in urls:
            self.new_urls.add(url)

    # 判断是否存在新的 url
    def has_new_url(self):
        return len(self.new_urls) != 0

    # 获取新的 url
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url