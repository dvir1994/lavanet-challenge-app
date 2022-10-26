# Lavanet

## ISBN REST API

This application allows you to query ISBNs and obtain a detailed JSON. Additionally, we've added a feature to get covers from the queries.

_Requirements_

- Docker `v20.10`
- docker-compose `v2.12`

### ✨Nice features✨

- WSGI implementation
- Error logging
- Pipeline with CircleCI
- Clean code
- Helper functions

## Getting started

Run the application with docker-compose:

    docker-compose up

Visit http://localhost

_Note: The home page will dynamically change between servers when deployed in the cloud with Kubernetes._

## Routes

`/`

Home page.

`book/<ISBN>`

Query the ISBN and return detailed JSON.

`cover_image/<ISBN>`

Query the ISBN and return an HTML with a medium-size cover image and JSON.

## Contributors

- Luis Lopez
