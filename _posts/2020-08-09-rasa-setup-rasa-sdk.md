---
layout: post
title:  Setup Rasa SDK on local machine
comments: true
categories: [ChatBOT, Python, Rasa]
excerpt: Python SDK for the development of custom actions for Rasa. Actions are the things your bot runs in response to user input
---

## About RASA

Building contextual assistants & chatbots that really help customers is hard. Rasa provides infrastructure & tools necessary for high-performing, resilient, proprietary contextual assistants that work. With Rasa, all developers can create better text- and voice-based assistants.

## Actions

Actions are the things your bot runs in response to user input. There are four kinds of actions in Rasa:
- **Utterance Actions**: start with *utter_* and send a specific message to the user.
- **Retrieval Actions**: start with *respond_* and send a message selected by a retrieval model.
- **Custom Actions**: run arbitrary code and send any number of messages (or none).
- **Default Actions**: e.g. action_listen, action_restart, action_default_fallback.

## Setup

- Create new conda environment. Mine is 'rasasdksrc'
- Go do *e:\git\rasahq* folder on command prompt
- Get latest source code from `git clone https://github.com/RasaHQ/rasa-sdk.git`
- Install *poetry* using command 
  `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python`
  
  If you run into any issue with above command then work-around is
  - Get content of the file `https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py` and save it in a file *get_poetry.py* on your machine.
  - Run `python get_poetry.py`
- Run `poetry install` to install dependencies needed for *rasa-sdk*

## Debugging

- Switch to conda environment for rasa. Mine is `rasasrc`. 
- On command prompt, go to the folder where you want to create new rasa project.
- Run command `rasa init` and then follow instructions to create new project.
- Switch back to conda environment corresponding to *rasa-sdk*. 
- Run commnad `python -m rasa_sdk --actions actions`
- You are all set.
