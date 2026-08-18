from collections import defaultdict

class MemoryStore:
    def __init__(self): self._data=defaultdict(list)
    def add(self, namespace:str, value:str)->None:
        if value and value not in self._data[namespace]: self._data[namespace].append(value)
    def search(self, namespace:str, query:str)->list[str]:
        terms={t.lower() for t in query.split()}
        scored=[]
        for item in self._data[namespace]:
            score=len(terms & {t.lower().strip(".,") for t in item.split()})
            if score: scored.append((score,item))
        return [x for _,x in sorted(scored, reverse=True)]
