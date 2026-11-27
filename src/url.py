import validators
import urllib.parse
import rpa
class Url:
    def __init__(self, url) -> None:
        if not validators.url(url):
            raise ValueError("String should be a url")
        self._validated_url = url
        self._metadata = urllib.parse.urlparse(url)
      

    @property
    def metadata(self) -> urllib.parse.ParseResult:
        print(self._metadata)
        return self._metadata
    
    @property
    def get_url(self):
        return self._validated_url
    