SRC=.

format: ## Format codes
	poetry run autoflake --in-place --remove-unused-variables --remove-all-unused-imports --recursive ${SRC} ${TEST} && \
	poetry run isort ${SRC} ${TEST} && \
	poetry run black --line-length 119 ${SRC} ${TEST}