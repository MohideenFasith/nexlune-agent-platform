# Nexlune Agent Platform

A runnable foundation for a production AI-agent control plane. It supports bounded planning, tool execution, memory, run lifecycle management and deterministic evaluation. No model API key is required for the reference implementation.

## Run
```bash
python -m pip install -e .[dev]
uvicorn nexlune_agent.main:app --reload
```

## API
- `POST /runs` create a run from a goal
- `POST /runs/{id}/execute` execute the plan
- `GET /runs/{id}` inspect state and trace
- `GET /runs/{id}/score` evaluate outcome
- `GET /health` liveness
