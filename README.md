# AIML Discord chatter bot

> An intelligent chatbot built using AIML module and Intent datasets.

## Installation and Usage
### Creating the bot on Discord

1. Create bot on Discord's [bot portal](https://discord.com/developers/applications/)
2. Make a **New Application**
3. Go to **Bot** settings and click on **Add Bot**
4. Give **Administrator** permission to bot
5. You will find your bot **TOKEN** there, it is important that you save it
6. Go to **OAuth2** and click bot, than add **Administrator** permissions
7. You can follow the link that will appear to add the bot to your discord server

## Installation

This is a guide to help you self host the bot, and use it on your own which simplifies the work, and allows you to have
a bot for yourself.

## Docker

**NOTE**: The docker is being tested and being made to worked properly. It hasn't been working perfectly yet. I advise
to use non docker steps until the docker works perfectly when deploying / running. Sorry for this inconvenience.

Docker is an easy way of containerizing and delivering your applications quickly and easily, in an 
convenient way. It's really simple to get started with this, with docker handling all the installation
and other tasks.Configure the environmental variables by renaming the `.env.example` file to `.env` with the respective 
values. Then, run `docker-compose --env-file .env up` after getting the project and config ready.

**Docker mini guide:**

- Running the bot: `docker-compose --env-file .env up`
- Stopping the bot: `docker-compose down`
- Rebuilding the bot: `docker-compose build`

### Self hosting without docker

This is a clean and neat way of hosting without using docker. You can follow this if docker doesn't work
well on your system, or it doesn't support it. Containers are resource intensive, and your PC might not
be able to do it, this is the perfect method to get started with the self-hosting.

- Clone or fork the repository, whichever suits you better.
- Install `pipenv`, a virtual env for python. Command: **`pip install pipenv`**
- Create the virtual environment and prepare it for usage using `pipenv update`
- Configure the environmental variables by renaming the `.env.example` file to `.env` with the respective 
  values for it. If you're using heroku or other platforms that have option for external environmental
  variables, use that instead of `.env`
- Configure the options and settings available in `config.py` inside the Bot module, according to your
  preferences.
- Run the server using `pipenv run start`

### Usage

Go to any channel in discord of any server where this bot is invited, Make a channel with the same exact name as 
specified in `.env` and Send a message there. The bot should respond to the message sent.

## 🤝 Contributing

Contributions, issues and feature requests are welcome. After cloning & setting up project locally, you can just submit 
a PR to this repo and it will be deployed once it's accepted.

⚠️ It’s good to have descriptive commit messages, or PR titles so that other contributors can understand about your 
commit or the PR Created. Read [conventional commits](https://www.conventionalcommits.org/en/v1.0.0-beta.3/) before 
making the commit message.

## 💬 Get in touch

If you have various suggestions, questions or want to discuss things with our community, Join our discord server!

[![Discord](https://discordapp.com/api/guilds/835940276869791816/widget.png?style=shield)](https://discord.gg/MKC4qna4Gz)

## Show your support

We love people's support in growing and improving. Be sure to leave a ⭐️ if you like the project and 
also be sure to contribute, if you're interested!

## License

- [GPL V3](https://github.com/janaSunrise/AIML-discord-chatter-bot/blob/main/LICENSE)

<div align="center">
  Made by Sunrit Jana with ❤️
</div>
