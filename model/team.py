from dataclasses import dataclass
@dataclass
class Team:
    id :  int
    year : int
    team_code : str
    name :str
    def __eq__(self, other):
        return isinstance(other, Team) and self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return f"{self.team_code} ({self.name})"

    def __repr__(self):
        return f"{self.team_code} ({self.name})"

