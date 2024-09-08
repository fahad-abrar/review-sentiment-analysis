# Sentiment Analysis API

This project is a sentiment analysis API that classifies user reviews as positive, negative, or neutral. The backend is built with Flask and RabbitMQ for message queuing. The API takes user input (a review) and returns the sentiment of that review.

## Features

- **Sentiment Analysis**: Classifies reviews into positive, negative, or neutral categories.
- **Flask Framework**: Provides a RESTful API for easy interaction.
- **RabbitMQ**: Manages the message queue to handle asynchronous processing.

## Prerequisites

This project meets the following requirements:

- Python 3.8+
- Flask
- RabbitMQ
- Pipenv or another virtual environment tool

Update the environment variables to match your setup. You can do this by creating a `.env` file in the root of your project:


