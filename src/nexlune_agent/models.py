from enum import Enum
from pydantic import BaseModel, Field

class RunState(str, Enum):
    queued="queued"; running="running"; completed="completed"; failed="failed"

class Step(BaseModel):
    id: int
    instruction: str
    tool: str
    argument: str

class TraceEvent(BaseModel):
    step_id: int
    tool: str
    input: str
    output: str

class Run(BaseModel):
    id: str
    goal: str
    state: RunState = RunState.queued
    plan: list[Step] = Field(default_factory=list)
    trace: list[TraceEvent] = Field(default_factory=list)
    error: str | None = None

class CreateRun(BaseModel):
    goal: str = Field(min_length=3, max_length=2000)
