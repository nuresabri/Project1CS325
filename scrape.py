import requests                            # import the requests library to handle http requests
from bs4 import BeautifulSoup              # import beautifulsoup for parsing html
import os                                  # import os to interact with the operating system

def scrape_review(url):                    # function to scrape reviews from a given url
    try:
        response = requests.get(url)       # send a get request to the provided url
        response.raise_for_status()        # raise an error if the request was unsuccessful (4xx or 5xx status codes)

        soup = BeautifulSoup(response.content, 'html.parser')       # parse the html content of the response
        reviews = soup.find_all('app-review-row')                   # find all review elements on the page

        os.makedirs('reviews', exist_ok=True)           # create the directory for review text files

        all_reviews_text = []                       # initialize a list to hold the text of all reviews

        for i, review in enumerate(reviews):     # loop through each review found on the page
            
        # extract review details, handling missing information
            author = review.find('a', class_='deco-none')
            outlet = review.find('span', class_='outlet-name')
            score = review.find('span', class_='score-number-bold')
            date = review.find('div', class_='text-right date-block')
            summary = review.find('p', class_='mb-0 wspw')
            review_link = review.find('a', target='_blank')

         # safely extract text or assign default messages
            author_text = author.text.strip() if author else 'no author'
            outlet_text = outlet.text.strip() if outlet else 'no outlet'
            score_text = score.text.strip() if score else 'no score'
            date_text = date.text.strip() if date else 'no date'
            summary_text = summary.text.strip() if summary else 'no summary'
            review_link_text = review_link['href'] if review_link else 'no link'

        # format the extracted review information into a structured text format
            review_text = (f"review {i + 1}:\n"
                           f"author: {author_text}\n"
                           f"outlet: {outlet_text}\n"
                           f"score: {score_text}\n"
                           f"date: {date_text}\n"
                           f"summary: {summary_text}\n"
                           f"review link: {review_link_text}\n\n")

            all_reviews_text.append(review_text)                # append the formatted review text to the list

        filename = f'reviews/reviews_{url.split("/")[-2]}.txt'  # construct the filename for the output text file
        with open(filename, 'w', encoding='utf-8') as file:     # open the file in write mode with utf-8 encoding
            file.write(''.join(all_reviews_text))               # write all collected review texts into the file

        print(f'saved all reviews to {filename}')       # print a message indicating that the reviews have been saved
    except Exception as e:
        print(f'error scraping {url}: {e}')         # print an error message if something goes wrong

def main():  # main function that reads urls from a file and initiates the scraping process
    with open('urls.txt', 'r') as file:         # open the 'urls.txt' file in read mode
        urls = file.read().splitlines()         # read all lines from the file and store them as a list of urls

    for url in urls:                            # loop through each url in the list
        scrape_review(url)                      # call the scrape_review function to scrape reviews for each url

                                                # entry point of the script
if __name__ == "__main__":
    main()                                      # execute the main function
