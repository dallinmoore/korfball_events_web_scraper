import requests
from bs4 import BeautifulSoup
import csv

def scrape_korfball_events(base_url, output_file):
    page_number = 1

    # Open the CSV file for writing
    with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
        # Create a CSV writer object
        csv_writer = csv.writer(csv_file)

        # Write header to the CSV file
        csv_writer.writerow(['Event Title', 'Country', 'City', 'Address', 'Start Date', 'End Date','Link'])

        while True:
            # Construct the URL for the current page
            if page_number == 1:
                url = f'{base_url}/?tribe-bar-date=2015-01-01'
            else:
                url = f'{base_url}/page/{page_number}/?tribe-bar-date=2015-01-01'

            print(f"Fetching page: {url}")

            # Make an HTTP GET request to the URL
            response = requests.get(url)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the HTML content of the page using BeautifulSoup
                soup = BeautifulSoup(response.text, 'html.parser')

                # Check if there are no upcoming events message
                no_events_message = soup.find('li', class_='tribe-events-c-messages__message-list-item')
                if no_events_message and "There were no results found." in no_events_message.text:
                    print("No upcoming events message found. Exiting.")
                    break

                # Find and write the titles, links, venue, start date, and end date of events to the CSV file
                events = soup.find_all('div', class_='tribe-events-calendar-list__event-details tribe-common-g-col')
                for event in events:
                    title_element = event.find_next('h3')
                    title = title_element.text.strip()
                    link = title_element.find('a')['href'] if event.find('a') else None

                    # Find the venue information 
                    location_element = event.find('address', class_='tribe-events-calendar-list__event-venue')
                    location_title_element = location_element.find('span', class_='tribe-events-calendar-list__event-venue-title') if location_element else None
                    location_address_element = location_element.find('span', class_='tribe-events-calendar-list__event-venue-address') if location_element else None

                    location_title = location_title_element.text.strip() if location_element else None
                    location_address = location_address_element.text.strip() if location_element else None
                    address = ", ".join([location_title.strip(",").strip(" "),location_address.strip(",").strip(" ")])  if location_element else None

                    # Combine title and address into location_list
                    location_list = location_title.split(', ') + location_address.split(', ') if location_title and location_address else None
                    country = location_list[-1].strip(", ") if location_list else None
                    city = location_list[-2] if location_list and len(location_list) > 1 else None


                    # Find the start date and end date
                    start_date_element = event.find_next('span', class_='tribe-event-date-start')
                    start_date = start_date_element.text.strip() if start_date_element else None

                    end_date_element = event.find_next('span', class_='tribe-event-date-end')
                    end_date = end_date_element.text.strip() if end_date_element else None

                    # Write the title, link, venue, start date, and end date to the CSV file on the same line
                    csv_writer.writerow([title, country, city, address, start_date, end_date,link])


                # Move to the next page
                page_number += 1
            else:
                print(f"Failed to fetch the page. Status code: {response.status_code}")
                break

# Example usage
base_url = 'https://korfball.sport/events/list'
output_file = 'korfball_events.csv'
scrape_korfball_events(base_url, output_file)
