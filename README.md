# anonymous-telegram-bot

aiogram bot for anonymous messaging

## Tech Stack

- aiogram
- sqlalchemy
- postgres
- alembic

## Installation && Configuration

Installation is pretty **simple**, you'll need to clone this **repository** and have installed **docker** and *
*docker-compose** on your PC.

Clone project and change directory:

```shell
  git clone https://github.com/intezya/anonymous-telegram-bot

  cd anonymous-telegram-bot
```

Rename .env.example to .env and edit it. This file must looks like:

```env
BOT_TOKEN=<your bot token>

DB_USER=postgres
DB_PASS=postgres
DB_HOST=localhost
DB_PORT=5434
DB_NAME=postgres

POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres
```

Next, let's figure out how to run the bot.

<details>
<summary>1. Using docker and docker-compose</summary>

> The recommended way to use docker-compose.yaml is to build and run the services using Docker Compose. This approach
> simplifies the setup and ensures that all dependencies and configurations are correctly handled.
>
> ```sh
> docker-compose up --build
> ```
>
> This command will build the Docker images if they are not already built and start the services defined in the
> docker-compose.yaml file.
>
> Note that if you using this method, **you should name DB_HOST in .env the same as your postgres container named** (set
> DB_HOST=db if you dont change container name)
>
</details>

<details>
<summary>2. Without docker</summary>

> To run the bot without Docker, you need to set up the environment manually.
>
> ```sh
> poetry env use python3.12
> poetry update
> poetry run python src/bot.py
> ```
>
</details>

## Code style

[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

## License

[MIT](https://choosealicense.com/licenses/mit/) © [intezya](https://github.com/intezya)
