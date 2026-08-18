from .models import Step

class Planner:
    def plan(self, goal: str) -> list[Step]:
        cleaned=" ".join(goal.split())
        parts=[p.strip() for p in cleaned.replace(";", ".").split(".") if p.strip()]
        parts=parts[:6] or [cleaned]
        steps=[]
        for i,p in enumerate(parts,1):
            tool="calculator" if any(ch.isdigit() for ch in p) and any(op in p for op in "+-*/") else "echo"
            steps.append(Step(id=i,instruction=p,tool=tool,argument=p))
        return steps
