# Setup Guide

This guide provides a step-by-step process to set up the `nlp-search-engine` repository.

## Prerequisites

Before proceeding with the setup, ensure that you have the following:

- Python 3.x installed on your system
- Access to the internet

## Step 1: Clone the Repository

1. Open your terminal or command prompt.
2. Navigate to the directory where you want to clone the repository.
3. Run the following command to clone the repository:

    ```
    git clone git@github.com:felipebpl/nlp-search-engine.git
    ```

## Step 2: Create the `pg_env` Virtual Environment

1. Navigate to the cloned repository's directory:

    ```
    cd nlp-search-engine
    ```

2. Create a virtual environment named `pg_env` by running the following command:

    ```
    python3 -m venv pg_env
    ```

3. Activate the virtual environment:

    - For Windows:

      ```
      pg_env\Scripts\activate
      ```

    - For macOS/Linux:

      ```
      source pg_env/bin/activate
      ```

## Step 3: Install the Requirements

1. Ensure that you are in the `nlp-search-engine` directory and the `pg_env` virtual environment is activated.

2. Run the following command to install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

## Step 4: Run `pg.py` to Retrieve Essays

1. Make sure you are still in the `nlp-search-engine` directory and the `pg_env` virtual environment is activated.

2. Run the following command to execute the `pg.py` script:

    ```
    python pg.py
    ```

    This script will retrieve the essays and store them in a suitable format.

Congratulations! You have successfully set up the `nlp-search-engine` repository. You can now explore and utilize the essays as per your requirements.
