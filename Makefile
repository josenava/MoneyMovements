#!/bin/bash

run-server:
	docker exec -it money_transactions_api python manage.py runserver 0.0.0.0:8000

ssh-api:
	docker exec -it money_transactions_api bash
