from uuid import uuid4
from .models import Run, RunState, TraceEvent
from .planner import Planner
from .tools import ToolRegistry
from .memory import MemoryStore

class AgentService:
    def __init__(self):
        self.runs:dict[str,Run]={}; self.planner=Planner(); self.tools=ToolRegistry(); self.memory=MemoryStore()
    def create(self,goal:str)->Run:
        run=Run(id=str(uuid4()),goal=goal,plan=self.planner.plan(goal)); self.runs[run.id]=run; return run
    def get(self,run_id:str)->Run:
        if run_id not in self.runs: raise KeyError(run_id)
        return self.runs[run_id]
    def execute(self,run_id:str)->Run:
        run=self.get(run_id); run.state=RunState.running
        try:
            for step in run.plan:
                output=self.tools.execute(step.tool,step.argument)
                run.trace.append(TraceEvent(step_id=step.id,tool=step.tool,input=step.argument,output=output))
                self.memory.add(run.id,output)
            run.state=RunState.completed
        except Exception as exc:
            run.state=RunState.failed; run.error=f"{type(exc).__name__}: {exc}"
        return run
