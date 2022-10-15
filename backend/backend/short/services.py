import uuid
from urllib.parse import urlparse

UUID_MAX_LENGTH = 8


class UuidService():
    def short_uuid():
        id = str(uuid.uuid4())
        return id[:UUID_MAX_LENGTH]


class UrlService():
    def is_absolute(url):
        return bool(urlparse(url).netloc)
