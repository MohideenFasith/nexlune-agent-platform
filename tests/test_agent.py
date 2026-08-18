from nexlune_agent.service import AgentService
from nexlune_agent.evals import score_run

def test_run_lifecycle():
    s=AgentService(); r=s.create("summarize this request")
    assert r.plan
    done=s.execute(r.id)
    assert done.state.value=="completed"
    assert score_run(done)["score"]==1.0

def test_calculator_failure_is_contained():
    s=AgentService(); r=s.create("2+2")
    done=s.execute(r.id)
    assert done.state.value=="completed"
    assert done.trace[0].output=="4.0"
