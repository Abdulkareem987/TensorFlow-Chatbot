# TensorFlow-Chatbot

## Task 9 for AI path in SM 2021 summer training
 
This is a simple arabic evaluation chatbot, built using Python, NLTK, and TensorFlow.

The chatbot runs on terminal, or any alternatives you might have, and allow the user to chat with the bot and evaluate using simple commands.

The chatbot command, which are in the JSON file, were processed using NLTK and trained using TensorFlow.

## List of main files:

1- intents.json: This file contains the chatbot patterns and responses, that allow the the chat bot to understands what the user is trying to say and write an appropriate response.

2- training.py: this is a python file that contains the code to load the intents.json file and build neural networks to train the chatbot using the data in .json file. The data extracted from json file are saved into binary .pkl files to allow the chatbot to handel them.

3- chatbot.py: this python code builds that chatbot, and loads the .json file and .pkl files into it to allow it to correctly understand the user and respond.

## Notes:

1- Run training.py first to train the chatbot model.

2- Since the chatbot is in arabic, windows default terminal and powershell might not show the words correctly. It worked fine on MAC device and on CMDR terminal.