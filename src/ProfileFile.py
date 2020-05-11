import json
import base64


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
            self.joyMappings = {}
            for index, guid in contents["joyMappings"].items():
                self.joyMappings[int(index)] = base64.b64decode(guid.encode("utf-8"))

    def save(self, filename):
        encodedMappings = {}
        for index, guid in self.joyMappings.items():
            encodedMappings[index] = base64.b64encode(guid).decode("utf-8")

        contents = {
            "version" : "1.0",
            "type" : self.type,
            "code" : self.code,
            "joyMappings" : encodedMappings
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

    def getJoyMappings(self):
        return self.joyMappings

    def setMappings(self, mappings):
        self.joyMappings = mappings

