class Index:
    def __init__(self, url:str, tag:str):
        self.url = url
        self.tag = tag

    def toJson(self):
        return {"url":self.url, "tag":self.tag}