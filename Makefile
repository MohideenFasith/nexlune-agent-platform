install:
	python -m pip install -e .[dev]

test:
	pytest -q

run:
	uvicorn nexlune_agent.main:app --reload

check:
	python -m compileall -q src tests
	pytest -q
