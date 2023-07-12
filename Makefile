install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pipx install --force dist/*.whl

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

make lint:
	poetry run flake8 brain_games