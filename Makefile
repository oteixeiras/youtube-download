PYTHON=$(VENV)/bin/python3

# Dependencies Commands
install:
	$(PYTHON) install pytube3 
	$(PYTHON) install fastapi
	$(PYTHON) install uvicorn
	$(PYTHON) install youtube_dl
	$(PYTHON) install pytest

#run app locally
run:
	@uvicorn main:app --reload

test:  ## Run tests
	$(PYTHON) -m pytest
