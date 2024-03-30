# utils/sitemap_scraper.py
import requests
import xml.etree.ElementTree as ET


def scrape_sitemap(sitemap_url):
    try:
        response = requests.get(sitemap_url)
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            links = []
            for child in root:
                for url in child:
                    loc = url.find(
                        '{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
                    if loc is not None:
                        links.append(loc.text)
            return links
        else:
            print("Failed to fetch sitemap:", response.status_code)
            return []
    except Exception as e:
        print("Error occurred while scraping sitemap:", e)
        return []


# Example usage:
if __name__ == "__main__":
    sitemap_url = "https://123wrestling.com/post-sitemap.xml"
    post_links = scrape_sitemap(sitemap_url)
    print("Post links extracted from sitemap:")
    for link in post_links:
        print(link)
