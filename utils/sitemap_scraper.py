import httpx
from parsel import Selector
from typing import List, Optional


def get_sitemap_links(sitemap_url: str) -> Optional[List[str]]:
    try:
        response = httpx.get(sitemap_url)
        response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404, 500)
        selector = Selector(response.text)

        links = []
        for url in selector.xpath('//url'):
            link = url.xpath('loc/text()').get()
            if link is not None:
                links.append(link)

        return links if links else None
    except httpx.HTTPError as e:
        print(f"HTTP Error occurred while fetching sitemap: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Example usage:
if __name__ == "__main__":
    # Update if outdated
    sitemap_url = 'https://123wrestling.com/post-sitemap.xml'
    sitemap_links = get_sitemap_links(sitemap_url)
    if sitemap_links is not None:
        print("Sitemap links:")
        for link in sitemap_links:
            print(link)
    else:
        print("No links found in the sitemap.")
