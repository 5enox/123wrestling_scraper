from utils.sitemap_scraper import get_sitemap_links
from utils.website_scraper import run_playwright
from sites.site_scraper import LinksProcessor
from utils.database import DatabaseHandler

# Importing Necessary Libs
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the value of the environment variable 'POSTS_SITEMAP'
SITEMAP = a if (a := os.getenv('POSTS_SITEMAP')) is not None else ''


def main():
    """
    This is the main function of the program.
    It serves as the entry point for the script execution.
    """
    try:
        # Get links from sitemap
        links = get_sitemap_links(SITEMAP)

        if links:
            # Initialize database handler
            db_handler = DatabaseHandler()

            # Initialize links processor
            links_processor = LinksProcessor(links)

            # for link in links_processor:
            #     # Process each link
            #     processed_links = links_processor.process(link)

            #     if processed_links:
            #         # Start playwright scraper for each processed link
            #         for processed_link in processed_links:
            #             try:
            #                 run_playwright(processed_link)
            #             except Exception as e:
            #                 print(f"Error occurred while scraping link {
            #                       processed_link}: {e}")

            #                 # Log the error or handle it as needed
            #     else:
            #         print(f"No processed links found for {link}")
        else:
            print("No links found in the sitemap.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
