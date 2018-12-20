class Claim:
    def __init__(self, claim_id, left, top, width, height):
        self.claim_id = claim_id
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return str.format('#{} @ {},{}:{}x{}', self.claim_id, self.left, self.top, self.width, self.height)

    def __repr__(self) -> str:
        return self.__str__()

