from dataclasses import dataclass
@dataclass
class Anno:
    anno_partecipazione : int
    def __eq__(self, other):
        return isinstance(other, Anno) and self.anno_partecipazione == other.anno_partecipazione
    def __hash__(self):
        return hash(self.anno_partecipazione)

    def __str__(self):
        return f"{self.anno_partecipazione}"

    def __repr__(self):
        return f"{self.anno_partecipazione}"