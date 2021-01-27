
CREATE_VENV = python -m venv venv
START_VENV = source venv/bin/activate
STOP_VENV = deactivate

DEVELOPMENT_REQUIREMENTS = pip install -r requirements/development.txt
PRODUCTION_REQUIREMENTS = pip install -r requirements/production.txt

RUN_SERVER = uvicorn bluestorm_app.main:app --reload

DOCKER_TAG = bluestorm_challenge

install_development:
	$(CREATE_VENV) &&\
	$(START_VENV) &&\
	$(DEVELOPMENT_REQUIREMENTS) &&\
	$(STOP_VENV)

install_production:
	$(CREATE_VENV) &&\
	$(START_VENV) &&\
	$(PRODUCTION_REQUIREMENTS) &&\
	$(STOP_VENV)

run: venv bluestorm_app/main.py
	$(START_VENV) &&\
	$(RUN_SERVER) &&\
	$(STOP_VENV)

build-docker:
	docker build -t $(DOCKER_TAG) -f docker/Dockerfile .

run-docker:
	docker run -p 80:80 $(DOCKER_TAG)

run-tests:
	pytest