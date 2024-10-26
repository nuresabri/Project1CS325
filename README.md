# Game Review Scraper

## Overview
This Python script scrapes user reviews from game review pages listed in `urls.txt`, extracting details like author, outlet, score, date, summary, and review link. Each review page’s reviews are saved in individual text files within the `reviews` directory.
It is designed to work with the website "opencritic.com" and its reviews section. 

## Purpose
- Collect and organize game reviews for analysis.
- Demonstrate web scraping with Python’s `requests` and `BeautifulSoup`.
  
## Requirements
The script requires:
- `requests`
- `beautifulsoup4`

These dependencies are managed with Conda and listed in `requirements.yaml`.

## Setup and Installation

### Step 1: Clone the Repository
Clone the repository and navigate to its directory:
git clone <repository-url>
cd <repository-directory>

### Step 2: Create and Activate Conda Environment
Create and activate the environment using the provided YAML file:

bash
conda env create -f requirements.yaml
conda activate reviews_scraper

### Step 3: Prepare urls.txt
In the project root, create a urls.txt file and list each game review URL on a new line.

Running the Script
Run the following command to start scraping:
python scrape.py

Each URL’s reviews will be saved in the reviews directory, formatted by page.

Code Breakdown
scrape_review(url)
Fetches Page: Sends a GET request and raises an error if the request fails.
Parses Reviews: Finds all reviews and extracts details like author, outlet, score, date, summary, and link.
Formats & Saves: Creates a reviews directory (if it doesn’t exist), formats each review, and saves them in a structured text file for each URL.
main()
Reads URLs from urls.txt.
Calls scrape_review(url) on each URL in the list.
Error Handling
The script handles HTTP and general exceptions, printing an error message if scraping fails.

File Structure
/project-directory
├── scrape.py          # main script
├── urls.txt           # list of URLs to scrape
├── requirements.yaml  # Conda environment file
└── reviews/           # folder where reviews files are saved
