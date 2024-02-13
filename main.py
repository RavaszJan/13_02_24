# abstraktne triedy
from abc import ABC, abstractmethod
class Zviera(ABC):
    @abstractmethod
    def zvuk(self):
        pass

class Pes(Zviera):
    def zvuk(self):
        return "Haf"

class Macka(Zviera):
    def zvuk(self):
        return "Mnau"

# moje_zviera=Zviera()

moj_pes=Pes()
print(moj_pes.zvuk())

moja_macka=Macka()
print(moja_macka.zvuk())

