from urllib import request


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        # 打开新的 URL 设置超市时间
        response = request.urlopen(url,None,5)

        # 判断返回值
        if response.getcode() != 200:
            return None

        # 返回内容
        return response.read()