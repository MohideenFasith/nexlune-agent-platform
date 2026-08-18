# Architecture

The service separates orchestration from execution. `Planner` converts a goal into bounded steps; `ToolRegistry` exposes deterministic tools; `MemoryStore` persists conversational facts in-process; `AgentService` owns runs and their lifecycle; `Evaluator` scores completed runs. The API is stateless with respect to transport and can later be backed by PostgreSQL/Redis without changing the orchestration contracts.

## Production extension points
- Replace in-memory stores with PostgreSQL and Redis.
- Add OAuth/OIDC authorization at the API edge.
- Run tool execution in isolated workers.
- Add vector retrieval and model-provider adapters behind interfaces.
