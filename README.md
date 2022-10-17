# URL Shorterner

## How to run:

1. Navigate to root folder of repository
2. Ensure that Docker is up and running
3. Run following command to start `docker-compose up`
4. Load up `localhost:3000` or whichever port defined in `docker-compose.yml`

# Testing:

As I'm not entirely familiar with the testing framework, I have done a minimal version to test the views. For production settings, I would opt to test the models and routings, as well as integration tests.

# CSRF Exemption:

As this is a MVP version and I have not setup the User modelling which is required to get the csrftoken after logging in based on what I've read on stackoverflow. I have chose to exempt CSRF for the POST request.

# Branching:

For this MVP version, as I am working alone with no production environment, I have chose not to use the pull request and merge method to staging branch and then to main.
