from .database import DatabaseHandler

# Example usage
db_handler = DatabaseHandler()
db_handler.create_table()

# Assuming you have the details of the video to save
site = 'example_site'
title = 'Example Video Title'
url = 'http://example.com/video'
# Other details as a dictionary
other_details = {'duration': '10 mins', 'resolution': '720p'}

# Save the video details to the database
db_handler.save_video(site, title, url, other_details)

# Close the database connection when done
db_handler.close_connection()
