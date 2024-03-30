class LinksProcessor:
    def __init__(self, site_name):
        self.site_name = site_name
        # Add any common attributes or initialization logic here

    def process_links(self, links):
        processed_links = []
        if self.site_name == 'dailymotion':
            processed_links = self.dailymotion(links)
        elif self.site_name == 'fembed':
            processed_links = self.fembed(links)
        elif self.site_name == 'netu':
            processed_links = self.netu(links)
        elif self.site_name == 'fastvideo':
            processed_links = self.fastvideo(links)
        # Add more elif conditions for additional sites
        return processed_links

    def dailymotion(self, links):
        processed_links = []
        # Process the links using the dailymotion logic
        # ...
        return processed_links

    def fembed(self, links):
        processed_links = []
        # Process the links using the fembed logic
        # ...
        return processed_links

    def netu(self, links):
        processed_links = []
        # Process the links using the netu logic
        # ...
        return processed_links

    def fastvideo(self, links):
        processed_links = []
        # Process the links using the fastvideo logic
        # ...
        return processed_links
