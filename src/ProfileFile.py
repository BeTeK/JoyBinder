import json



class ProfileFile:
    def __init__(self):
        self.loaded = False
        self.type = "expert"
        self.code = ""
        self.joyMappings = {}

    def load(self, filename):
        with open(filename, "rb") as f:
            contents = json.loads(f.read().decode("utf-8"))
            self.type = contents["type"]
            self.code = contents["code"]
            self.joyMappings = contents["joyMappings"]

    def save(self, filename):
        contents = {
            "version" : "1.0",
            "type" : self.type,
            "code" : self.code,
            "joyMappings" : self.joyMappings
        }
        with open(filename, "wb") as f:
            f.write(json.dumps(contents).encode("utf-8"))


    def setCode(self, txt):
        self.type = "expert"
        self.code = txt

    def isExpert(self):
        return self.type == "expert"

    def getCode(self):
        return self.code

    def setJoyName(self, joyGuid, name):
        self.joyMappings[joyGuid] = name

    def getJoyMappings(self):
        return self.joyMappings

