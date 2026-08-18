from .models import Run, RunState

def score_run(run:Run)->dict[str,float]:
    completion=1.0 if run.state==RunState.completed else 0.0
    coverage=(len(run.trace)/len(run.plan)) if run.plan else 0.0
    no_errors=1.0 if run.error is None else 0.0
    total=round(0.5*completion+0.4*coverage+0.1*no_errors,4)
    return {"completion":completion,"coverage":round(coverage,4),"no_errors":no_errors,"score":total}
