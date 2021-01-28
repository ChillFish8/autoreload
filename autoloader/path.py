import pathlib

from typing import Optional


class RenderPath:
    def __init__(self, url=None, fp=None):
        self.url: Optional[str] = url
        self.fp: Optional[pathlib.Path] = fp

    @classmethod
    def from_str(cls, path: str) -> "RenderPath":
        if path.startswith(("http", "https")):
            return cls(url=path)
        else:
            p = pathlib.Path(path)
            return cls(fp=p)

    def to_url(self) -> str:
        if self.url is not None:
            return self.url

        return str(self.fp.resolve())
