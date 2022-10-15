import uuid


class UuidService():
    def shortUuid():
        id = str(uuid.uuid4())
        return id[:8]
