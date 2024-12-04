# Review Sentiment Analyzer with Ollama

This project is designed to analyze user reviews for products and generate sentiment analysis results using the Phi3.5 model from Ollama. The reviews are scraped from an eCommerce website as part of a previous web scraping project (Project 2). This project processes those reviews, assigns sentiment labels (positive, neutral, negative), and generates a bar graph visualizing the sentiment distribution.

## Example Directory Structure

- **reviews/**: This folder contains the scraped reviews from Project 2. Each review is stored as an individual `.txt` file.
- **scrape.py**: This is the script used in Project 2 to scrape reviews from an eCommerce website (not required to run sentiment analysis, but included for reference).
- **urls.txt**: Contains the URLs of the product pages used for scraping reviews.
- **test_funcs.py**: A file containing helper test functions for running unit tests on the sentiment analysis code.
- **reviewAnalyzer.py**: This is the main script that processes reviews, assigns sentiment labels using Ollama’s Phi3.5 model, and generates the sentiment distribution bar graph.
- **final.yaml**: A Conda environment configuration file with all the dependencies needed to run the project.

## Prerequisites

To run this project, you will need the following:

- **Ollama**: The Phi3.5 model from Ollama is required to perform sentiment analysis. You must install and run Ollama separately.
    - **Installation**: Follow the official Ollama [Installation Guide](https://ollama.com/docs) to install Ollama.
- **Python 3**: Ensure at least Python 3.13 is installed on your system.

## Installation Instructions

### Install Ollama and Start the Model

To use the Phi3.5 model, you need to have Ollama installed and running in the background.

1. Install Ollama using the instructions in the [Ollama Installation Guide](https://ollama.com/docs).

2. Once installed, open a separate terminal window and run the following command to start Ollama:

    ```bash
    ollama start
    ```

3. Leave this terminal window running in the background to allow the sentiment analysis code to access the model. **IMPORTANT**: Without having Ollama running, it will not process the reviews and will be stuck in a loop.

### Create the Conda Environment Using `final.yaml`

This project uses Conda to manage dependencies. You can create a new Conda environment from the provided `final.yaml` file:

1. Ensure you have Conda installed. If not, you can download it from [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

2. Run the following command to create the environment:

    ```bash
    conda env create -f final.yaml
    ```

3. After the environment is created, activate it using:

    ```bash
    conda activate review-sentiment-analyzer
    ```

This will install all the necessary dependencies to run the project.

## Running the Sentiment Analysis

1. **Ensure Ollama is running**: Make sure that Ollama is running in a separate terminal window by executing:

    ```bash
    ollama start
    ```

2. **Activate the Conda Environment**: In the terminal, activate the Conda environment where all dependencies are installed:

    ```bash
    conda activate review-sentiment-analyzer
    ```

3. **Run the Sentiment Analysis**: Once the environment is activated and Ollama is running, execute the main script (`reviewAnalyzer.py`) to process the reviews and generate the sentiment labels:

    ```bash
    python reviewAnalyzer.py
    ```

This will:

- Process each review file in the `reviews/` directory.
- Run sentiment analysis using the Phi3.5 model from Ollama.
- Assign sentiment labels (positive, neutral, negative) to each review.
- Save the sentiment-labeled reviews in the `reviews/` folder.
- Generate a bar graph visualizing the sentiment distribution (positive, neutral, negative) and save it as `sentiment_distribution.png` in the project directory.

## Running Tests

To ensure that your sentiment analysis code works correctly, you can run tests using `pytest`.

1. **Run pytest on test functions**: To run the tests in the `test_funcs.py` file, execute the following command in the terminal:

    ```bash
    pytest test_funcs.py
    ```

2. **Run pytest with output displayed**: You can also run pytest with the `-s` option to display the output directly in the terminal:

    ```bash
    pytest -s test_funcs.py
    ```

This will run all the tests defined in `test_funcs.py` and show you the results. Ensure all tests pass before proceeding.

## Output

The output of running `reviewAnalyzer.py` includes:

1. **Sentiment-Labeled Reviews**: Each review in the `reviews/` folder will have sentiment labels (positive, neutral, negative) appended to the text file. For example, a review file might look like:

    ```
    Review Text...
    Sentiment: Positive
    ```

2. **Bar Graph**: A bar graph showing the sentiment distribution (positive, neutral, negative) will be generated and saved as `sentiment_distribution.png` in the project directory.

## Example Folder Structure


## Dependencies

This project requires the following dependencies, which are listed in the `final.yaml` file:

- **Ollama**: To access and run the Phi3.5 model for sentiment analysis.
- **Matplotlib**: For generating the sentiment distribution bar graph.
- **Requests**: To interact with web scraping code. (really only needed for project 2)

These are the main ones, all of them are in the `final.yaml`.

To install these dependencies, create and activate the Conda environment using the `final.yaml` file:

```bash
conda env create -f final.yaml
conda activate review-sentiment-analyzer

Troubleshooting
Ollama not running: If Ollama is not running or unreachable, make sure to run ollama start in a separate terminal window. If you encounter issues, check the Ollama documentation for troubleshooting steps.

Missing Dependencies: If you receive errors related to missing dependencies, ensure you have activated the Conda environment and created it using the final.yaml file.

Test Failures: If any tests fail when running pytest, review the error messages to identify the issue. Ensure that all functions are implemented correctly and that the necessary dependencies are installed.
