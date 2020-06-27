import requests

class Crawler:
    successful = False
    text = ""

    def crawl(self, url):
        self.successful = False
        self.text = ""
        result = requests.get(url)
        if result.status_code == 200:
            self.successful = True
            self.text = result.text

    def wasSuccessful(self):
        return self.successful

    def getText(self):
        return self.text