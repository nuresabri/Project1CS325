# import necessary modules
import os
import ollama
import logging
import matplotlib.pyplot as plot
import time  # for timestamping the graph file

# set up logging for debugging
logging.basicConfig(level=logging.DEBUG)

class OpinionAnalyzer:
    def __init__(self, model="phi3.5"):
        # initialize with a model, default is "phi3.5"
        self.model = model

    def AnalyzeOpinion(self, review):
        try:
            # log the review being processed
            logging.debug(f"Sending request for review: {review}")
            # define the prompt for sentiment analysis
            prompt = (
                "Classify the following review as positive, negative, or neutral. "
                "Respond with **only one word** (positive, negative, or neutral) and nothing else. "
                "Do not provide any additional text or explanation.\n\n"
                f"Review: {review}"
            )

            # send the request to the Ollama model
            response = ollama.chat(
                model=self.model,
                messages=[{'role': 'user', 'content': prompt}],
                stream=True
            )

            opinion = ""
            max_length = 50  # limit response length to avoid overly long responses

            for chunk in response:
                if 'message' in chunk and 'content' in chunk['message']:
                    # log each chunk of the response from Ollama
                    logging.debug(f"API Response Chunk: {chunk['message']['content']}")
                    opinion += chunk['message']['content']
                    
                    # check if a valid response is complete
                    opinion = opinion.strip().lower()
                    valid_responses = ["positive", "negative", "neutral"]
                    if opinion in valid_responses:
                        return opinion
                    
                    # safeguard if the response exceeds the max length
                    if len(opinion) > max_length:
                        logging.warning(f"Response exceeded max length: {opinion}. Defaulting to 'neutral'.")
                        return "neutral"

            # handle unexpected responses
            logging.warning(f"Unexpected response: {opinion}. Defaulting to 'neutral'.")
            return "neutral"

        except Exception as e:
            # log any errors that occur during the API call
            logging.error(f"Error during API call: {e}")
            return "neutral"

    def processFile(self, inputFile, outputFile):
        # read the input file containing reviews
        with open(inputFile, 'r', encoding='utf-8') as file:
            comments = file.readlines()

        # if the input file is empty, skip processing
        if not comments:
            logging.warning(f"Empty review file: {inputFile}")
            return

        opinions = []
        for comment in comments:
            if "summary:" in comment.lower():
                # extract the review summary
                review_summary = comment.replace("summary:", "").strip()
                logging.debug(f"Processing summary: {review_summary}")
                # analyze the sentiment of the review
                opinion = self.AnalyzeOpinion(review_summary)
                opinions.append((review_summary, opinion))

        # write the opinions to the output file
        with open(outputFile, 'w', encoding='utf-8') as file:
            for review, opinion in opinions:
                file.write(f"Review: {review}\nOpinion: {opinion}\n\n")


class OpinionProcesser:
    def __init__(self, inputDir="reviews", outputDir="opinions"):
        # initialize with directories for input and output files
        self.inputDir = inputDir
        self.outputDir = outputDir
        os.makedirs(self.outputDir, exist_ok=True)  # create output directory if it doesn't exist
        self.makeOp = OpinionAnalyzer()  # create an instance of OpinionAnalyzer

    def processFiles(self):
        opinionCount = []  # list to store sentiment counts for each product
        productNames = []  # list to store product names

        # loop through each file in the input directory
        for inputFile in os.listdir(self.inputDir):
            if inputFile.endswith(".txt"):
                # extract product name from file name
                product = inputFile.split("_")[-1].replace(".txt", "")
                productNames.append(product)

                # create paths for input and output files
                inputPath = os.path.join(self.inputDir, inputFile)
                outputPath = os.path.join(self.outputDir, f"opinions_{inputFile}")
                # process the reviews in the file
                self.makeOp.processFile(inputPath, outputPath)

                # read the opinions from the output file
                with open(outputPath, 'r', encoding='utf-8') as file:
                    opinions = [line.split(": ")[1].strip() for line in file if line.startswith("Opinion:")]
                    # count the occurrences of each sentiment type
                    counts = {
                        "positive": opinions.count("positive"),
                        "negative": opinions.count("negative"),
                        "neutral": opinions.count("neutral"),
                    }
                    opinionCount.append(counts)

        # plot the sentiment counts
        self.plotOpinionCount(opinionCount, productNames)

    @staticmethod
    def plotOpinionCount(opinionCount, productNames):
        # define sentiment types
        reviewTypes = ["positive", "negative", "neutral"]
        data = {reviewType: [] for reviewType in reviewTypes}

        # aggregate the sentiment counts for each product
        for counts in opinionCount:
            for reviewType in reviewTypes:
                data[reviewType].append(counts.get(reviewType, 0))

        # check if there is any data to plot
        if all(sum(data[reviewType]) == 0 for reviewType in reviewTypes):
            logging.warning("No data to plot! All sentiment counts are zero.")
            return

        # create x-axis positions for the bar graph
        x = range(len(productNames))
        width = 0.25  # width of each bar

        # plot the bar graph for each sentiment type
        for i, reviewType in enumerate(reviewTypes):
            plot.bar(
                [p + i * width for p in x],
                data[reviewType],
                width=width,
                label=reviewType,
                color=["green", "red", "gray"][i]
            )

        # label the axes and set the title
        plot.xticks([p + width for p in x], productNames, rotation=45)
        plot.xlabel("Products")
        plot.ylabel("Opinion Count")
        plot.title("Opinion Analysis of Reviews")
        plot.legend()
        plot.tight_layout()

        # create a unique filename for the graph using the current timestamp
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        graph_filename = f"analysis_graph_{timestamp}.png"
        plot.savefig(graph_filename)  # save the graph
        plot.show()  # display the graph
