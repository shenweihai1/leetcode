
class Codec:
    def __init__(self):
        self.kv = {}
    
    def encode(self, longUrl):
        import hashlib
        m = hashlib.md5()
        m.update(longUrl)
        eUrl = m.hexdigest()
        self.kv[eUrl] = longUrl
        return eUrl
    
    def decode(self, shortUrl):
        return self.kv[shortUrl]