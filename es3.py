from es2 import Underground, Connection


class UndergroundNavigator(Underground):

    def find_route(self, station1: str, station2: str, recursive: bool = True) -> tuple[list[tuple[str, str]], int]:
        if recursive:
            path = []
            visited = set()
            self._depth_first(station1, station2, visited, path)
        else:
            path = self._breadth_first(station1, station2)
        time = sum([c.time for _, c in path if c is not None])
        path = [(s, c.line if c is not None else "END") for s, c in path]
        return path, time

    def _depth_first(self, current: str, end: str, visited: set[str], path: list[tuple[str, Connection | None]]) -> bool:
        visited.add(current)
        if current == end:
            path.append((current, None))
            return True
        adjacent = {s for s in self._stations[current] if s not in visited}
        for s in adjacent:
            path.append((current, self._stations[current][s]))
            if self._depth_first(s, end, visited, path):
                return True
            path.pop()
        return False
    
    def _breadth_first(self, start: str, end: str) -> list[tuple[str, Connection | None]]:
        visited = set()
        if start == end:
            return [(start, None)]
        paths = [[(start, None)]]
        while paths:
            path = paths.pop(0)
            current = path[-1][0]
            connections = {(s, c) for s, c in self._stations[current].items() if s not in visited}
            for s, c in connections:
                if s == end:
                    path[-1] = (current, c)
                    return path + [(s, None)]
                visited.add(s)
                path[-1] = (current, c)
                paths.append(path + [(s, None)])
        return []
        

def main():
    # carico grafo
    und_nav = UndergroundNavigator.from_file("data/london.csv")

    # uso depth first
    route1 = und_nav.find_route("Picadilly Circus", "Covent Garden")
    route2 = und_nav.find_route("Covent Garden", "Picadilly Circus")
    print(*route1)
    print(*route2)

    # uso breadth first
    route1 = und_nav.find_route("Picadilly Circus", "Covent Garden", recursive=False)    
    route2 = und_nav.find_route("Covent Garden", "Picadilly Circus", recursive=False)
    print(*route1)
    print(*route2)


if __name__ == "__main__":
    main()