import glob
import json
import os

from Index import Index


class Indexer:
    def __init__(self):
            self.found = []
            self.indexed = []
            self.added = []
            self.loadCurrentlyIndexed()
            self.index()
    def loadCurrentlyIndexed(self):
            self.indexed = json.load(open('indexed.json', 'r'))
    def saveAdded(self):
            with open('new.json', 'w') as f:
                all = []
                for new in self.added:
                    jsonIndex = new.toJson()
                    all.append(jsonIndex)
                json.dump(all, f)
            with open("indexed.json", "w") as f:
                all = []
                for index in self.found:
                    jsonIndex = index.toJson()
                    all.append(jsonIndex)
                json.dump(all, f)

    def index(self):
        for r, d, f in os.walk("images"):
            for file in f:
                dir = str(r).replace("images/", "").replace("\\", "/")
                url = f"https://images.project-namiko.net/{dir}/{file}"
                tag = dir.split("/")[len(dir.split("/")) - 1]
                index = Index(url, tag)

                self.found.append(index)
        for i in self.found:
            alreadyIndexed = False
            for i2 in self.indexed:
                if i2["url"] == i.url:
                    alreadyIndexed = True
            if not alreadyIndexed:
                self.added.append(i)
                print(f"URL: {i.url}, TAG: {i.tag}")
        self.saveAdded()

