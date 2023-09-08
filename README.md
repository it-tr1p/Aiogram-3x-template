# Aiogram-3x-template

## Installation  
1. Clone the repository:\
`git clone https://github.com/it-tr1p/Short-links.git`
2. Create venv & install the dependencies:\
`poetry shell & poetry install`
3. Change the name of `.env.dist` to `.env` and set all environment variables as you need \
4. Change project name and other information in `pyproject.toml`

## Migrations
Generate alembic revision for migration with given name \
`make generate NAME=<name>` \
Apply migrations to the target database \
`make migrate`