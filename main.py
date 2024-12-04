# import the OpinionProcesser class from the reviewAnalyzer module
from reviewAnalyzer import OpinionProcesser

# define the main function to initialize the processor and process the files
def main():
    # create an instance of OpinionProcesser, specify input and output directories
    processor = OpinionProcesser(inputDir="reviews", outputDir="opinions")
    
    # call the processFiles method to process the reviews
    processor.processFiles()

# check if the script is being run directly (not imported)
if __name__ == "__main__":
    # call the main function
    main()
