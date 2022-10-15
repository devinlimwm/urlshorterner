import uuid
from urllib.parse import urlparse


class UuidService():
    def short_uuid():
        id = str(uuid.uuid4())
        return id[:8]


class UrlService():
    def is_absolute(url):
        return bool(urlparse(url).netloc)
