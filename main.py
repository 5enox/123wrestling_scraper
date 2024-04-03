from py import process
from utils.sitemap_scraper import get_sitemap_links  # Done
from utils.website_scraper import run_playwright  # Currently Working on
from utils.downloader import download_videos  # Done
from sites.links_handler import LinksProcessor  # Under Progress 2/6
from utils.database import DatabaseHandler  # Done

# Importing Necessary Libraries
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the value of the environment variable 'POSTS_SITEMAP'
SITEMAP = os.getenv('POSTS_SITEMAP', '')


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
            db_handler.create_table()

            # Initialize links processor
            links_processor = LinksProcessor()
            # Start playwright scraper for each processed link
            try:
                processed_links = run_playwright(links)
                download_links = links_processor.dailymotion(
                    links=processed_links)
                # Still working on fixing this
                data = download_videos(download_links)
                db_handler.save_video(data)

            except Exception as e:
                print(
                    f"Error occurred while scraping link {processed_link}: {e}")

                # Log the error or handle it as needed
        else:
            print("No links found in the sitemap.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
