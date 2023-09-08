# creo gerarchia di eccezioni
class UndergroundException(Exception):
    pass


class StationAlreadyPresent(UndergroundException):
    pass


class ConnectionAlreadyPresent(UndergroundException):
    pass


# classe per rappresentare connessioni tra stazioni ("peso" dei rami del grafo)
class Connection:
    def __init__(self, line: str, time: int) -> None:
        self._line = line
        self._time = time
    
    @property
    def time(self) -> int:
        return self._time
    
    @property
    def line(self) -> str:
        return self._line
    
    def __str__(self) -> str:
        return "{}, {} min".format(self._line, self._time)
    

class Underground:
    def __init__(self) -> None:
        self._stations = {}

    def add_station(self, station: str) -> None:
        if station in self._stations:
            raise StationAlreadyPresent("Adding duplicate station: {}".format(station))
        self._stations[station] = {}
    
    def has_station(self, station: str) -> bool:
        return station in self._stations

    def add_connection(self, station1, station2, conn) -> None:
        if station2 in self._stations[station1]:
            raise ConnectionAlreadyPresent("Adding duplicate connection from {} to {}: {}".format(station1, station1, str(conn)))
        self._stations[station1][station2] = conn
        self._stations[station2][station1] = conn

    def get_connection(self, station1, station2) -> Connection | None:
        if station2 not in self._stations[station1]:
            return None
        return self._stations[station1][station2]
    
    @staticmethod
    def _parse_row(row: str) -> tuple[str, str, str, int]:
        row = row.strip().split(";")
        s1 = row[0]
        s2 = row[1]
        line = row[2]
        time = int(row[3])
        return s1, s2, line, time
    
    @classmethod
    def from_file(cls, fname: str, verbose=False) -> "Underground":
        und = cls()
        with open(fname) as f:
            for row in f:            
                s1, s2, line, time = cls._parse_row(row)
                # metodo 1
                # - controllo se stazioni ci sono già prima di aggiungerle
                # - codice meno chiaro se molto controlli, ma più veloce
                if not und.has_station(s1):
                    und.add_station(s1)
                if not und.has_station(s2):
                    und.add_station(s2)
                conn = Connection(line, time)
                # metodo 2
                # - provo ad aggiungere connessione, se già presente gestisco eccezione
                # - codice più chiaro per controlli complessi, ma più lento
                try:
                    und.add_connection(s1, s2, conn)
                except ConnectionAlreadyPresent as e:
                    if verbose:
                        print(str(e))
        return und
    

def main():
    # creo grafico da file
    und = Underground.from_file("data/london.csv", verbose=True)

    # provo ottenere una delle connessioni salvate e controllo se è simmetrica (grafo diretto)
    print(und.get_connection("Goodge Street", "Tottenham Court Road"))
    print(und.get_connection("Tottenham Court Road", "Goodge Street"))


if __name__ == "__main__":
    main()
