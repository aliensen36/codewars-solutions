class IPv4Address:
    _cache = {}

    def __new__(cls, parts):
        key = tuple(parts)
        if key in cls._cache:
            return cls._cache[key]
        obj = super().__new__(cls)
        cls._cache[key] = obj
        return obj

    def __init__(self, parts):
        if len(parts) != 4:
            raise ValueError("IPv4Address must have exactly 4 parts")
        if parts[0] == 0:
            raise ValueError("The first part of IPv4Address cannot be zero.")
        for part in parts:
            if not isinstance(part, int):
                raise ValueError("The part of IPv4Address must be an integer.")
            if part < 0 or part > 255:
                raise ValueError("The part of IPv4Address must be between 0 and 255.")
        self._parts = tuple(parts)

    def __str__(self):
        return ".".join(str(part) for part in self.parts)

    def __eq__(self, other):
        if not isinstance(other, IPv4Address):
            raise ValueError("Can only compare IPv4Address with IPv4Address")
        return tuple(self.parts) == tuple(other.parts)

    def __hash__(self):
        return hash(tuple(self.parts))

    @classmethod
    def from_string(cls, string):
        return cls(list(map(int, string.split("."))))

    def __lt__(self, other):
        if not isinstance(other, IPv4Address):
            raise ValueError("...")
        return tuple(self.parts) < tuple(other.parts)

    def __gt__(self, other):
        if not isinstance(other, IPv4Address):
            raise ValueError("...")
        return tuple(self.parts) > tuple(other.parts)

    def __le__(self, other):
        if not isinstance(other, IPv4Address):
            raise ValueError("...")
        return tuple(self.parts) <= tuple(other.parts)

    def __ge__(self, other):
        if not isinstance(other, IPv4Address):
            raise ValueError("...")
        return tuple(self.parts) >= tuple(other.parts)

    @property
    def parts(self):
        return self._parts


a = IPv4Address([1,2,3,4])
print(a.parts)          # (1, 2, 3, 4) — кортеж
print(str(a))           # 1.2.3.4 — __str__ всё ещё работает

try:
    a.parts = [4,3,2,1]
except AttributeError as e:
    print("AttributeError:", e)

try:
    a.parts[0] = 4
except TypeError as e:
    print("TypeError:", e)
