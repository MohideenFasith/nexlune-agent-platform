from fastapi import FastAPI, HTTPException
from .models import CreateRun
from .service import AgentService
from .evals import score_run

app=FastAPI(title="Nexlune Agent Platform",version="0.1.0")
service=AgentService()
@app.get("/health")
def health(): return {"status":"ok"}
@app.post("/runs",status_code=201)
def create_run(body:CreateRun): return service.create(body.goal)
@app.get("/runs/{run_id}")
def get_run(run_id:str):
    try:return service.get(run_id)
    except KeyError: raise HTTPException(404,"run not found")
@app.post("/runs/{run_id}/execute")
def execute(run_id:str):
    try:return service.execute(run_id)
    except KeyError: raise HTTPException(404,"run not found")
@app.get("/runs/{run_id}/score")
def score(run_id:str):
    try:return score_run(service.get(run_id))
    except KeyError: raise HTTPException(404,"run not found")
