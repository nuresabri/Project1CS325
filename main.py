import os
import ollama

def main():
    cwd = os.getcwd()  # identifies current working directory and saves it
    print(f"Current working directory: {cwd}") #prints out cwd, was using for debugging

    questionsFile = "questions.txt" #sets questionsFile to the questions.txt, file w questions
    answersFile = os.path.join(cwd, "answers.txt")  # saves answers.txt in cwd

    # reads the questions from questions.txt
    try:
        with open(questionsFile, "r") as file:
            questions = file.readlines()            # reads the questions from questions.txt

        questions = [question.strip() for question in questions if question.strip()]    # organizes the read questions into list
        print(f"Questions read successfully: {questions}")  # outputs if questions were read correctly, was using for debugging
    
    except FileNotFoundError:
        print(f"Error: File {questionsFile} not found.") # throws error message if questionsFile was not found
        questions = []                                   # returns empty list if error occured
    except Exception as e:
        print(f"Error reading questions: {e}")           # same thing but if questionsFile could not be read
        questions = []

    if questions:
        answers = []                                     # setting answers to an empty list (for now)
        for question in questions:
            try:
                prompt = f"Q: {question}\nA:" #sets individual question to prompt variable

                response = ollama.chat(model="phi3.5",                                      # calls the ollama api with correct phi model, message paramter,
                                       messages=[{'role': 'user', 'content': prompt}],      # setting role to users and content to the prompts, and streaming enabled
                                       stream=True)

                full_answer = ""                                    # iterates over the streamed response
                for chunk in response:                              # streamed chunks of the response
                    # accessesthe 'content' within 'message'
                    if 'message' in chunk and 'content' in chunk['message']:
                        full_answer += chunk['message']['content']

                full_answer = full_answer.strip()  # cleans up the generated response
                answers.append(full_answer)

                print(f"Generated answer for question: '{question}' -> {full_answer}") # outputs the response generated, mainly for debugging
            
            except Exception as e:
                print(f"Error generating answer for question '{question}': {e}")       # throws error if answer couldnt be made and return empty string
                answers.append("")

        try:
            # writes questions and answers to the answers.txt file
            with open(answersFile, "w") as file:
                for question, answer in zip(questions, answers):
                    file.write(f"Q: {question}\nA: {answer}\n\n")
            print(f"Answers successfully written to {answersFile}")
        
        except Exception as e:
            print(f"Error writing answers to file: {e}")
    else:
        print("No questions found")

if __name__ == "__main__":
    main()
