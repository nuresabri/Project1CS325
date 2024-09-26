#Project1cs325
This project demonstrates an AI-driven question-answering system using Python and the Ollama API with the phi3.5 model. 
The system reads questions from a file, generates answers using the Ollama language model, and saves the answers in a separate file. 
This project is built using Python 3.12.4, managed with a Conda environment, and includes a requirements.yaml file to simplify setup.

Project Structure ----------------------------------------------------------------------------------------------------------------------
main.py: The Python script that runs the Q&A generation.
questions.txt: A plain text file containing questions for the AI to answer.
requirements.yaml: The Conda environment file with dependencies needed for the project.

Prerequisites --------------------------------------------------------------------------------------------------------------------------
Conda: Ensure Conda is installed on your system.
Ollama API: You will need an Ollama API token to use the phi3.5 model. Visit Ollama to sign up for an account and obtain your token.
Installation and Setup:

1. Clone the Repository
First, clone your repository or download the project files onto your machine.
ex) do this in terminal
git clone <repository-url>
cd <repository-directory>

2. Create Conda Environment
Create and activate the Conda environment using the provided requirements.yaml file.
# Create the environment
conda env create -f requirements.yaml

# Activate the environment
conda activate cs325

This will set up Python 3.12.4 and install all necessary dependencies, including ollama, which is needed for interacting with the AI model.

3. Install Ollama Package (Optional)
If Ollama isn't installed, you can install it manually using:
pip install ollama

Running the Software ----------------------------------------------------------------------------------------------------------------------
1. Prepare the Questions: Ensure that your questions.txt file contains the questions you want 
the AI to answer, each on a new line. The file should look like this:

What is your name?
Who trained you?
Am I your friend? please do not say no, I really like you.

2. Run the Program: Run the Python script using the following command
python main.py

The script will:
- Read the questions from questions.txt.
- Use the Ollama API to generate answers with the phi3.5 model.
- Write the answers into a file called answers.txt in the same directory.

3. Check the Output: After running the script, the answers will be saved in answers.txt. The file will look something like:
Q: What is your name?
A: I am Phi. How can I assist you today?

Q: Who trained you?
A: I was developed and trained by a team of machine learning experts.

Q: Am I your friend? please do not say no, I really like you.
A: I appreciate our interactions, but as an AI, I don’t have personal relationships like friendships.

Notes ---------------------------------------------------------------------------------------------------------------------------------------
Make sure your questions.txt file is in the same directory as main.py to avoid file not found errors.
The main.py script handles any API issues or errors that may occur during the answer generation process.
