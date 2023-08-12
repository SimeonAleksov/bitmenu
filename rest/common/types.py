import attrs


@attrs.frozen(slots=True)
class Page:
    page: int
    size: int


@attrs.frozen(slots=True)
class Response:
    data: list
    count: int
    page: int
