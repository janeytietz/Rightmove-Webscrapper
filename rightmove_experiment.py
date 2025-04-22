from bs4 import BeautifulSoup
import requests
import csv

# Insert link to fetch request
page_to_scrape = requests.get("Insert URL here")

# Parse the page using BeautifulSoup
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

# Debugging: Print the first 1000 characters of the parsed HTML
print(soup.prettify()[:1000])  # This will give you a glimpse of the structure

# Extract property data
ppm = soup.findAll("div", attrs={"class": "PropertyPrice_price__VL65t"})
nbr = soup.findAll("span", attrs={"class": "PropertyInformation_bedroomsCount___2b5R"})
address = soup.findAll("address", attrs={"class": "PropertyAddress_address__LYRPq"})
property_style = soup.findAll("span", attrs={"class": "PropertyInformation_propertyType__u8e76"})
agent = soup.findAll("span", attrs={"class": "MarketedBy_joinedText__HTONp"})

# Check if the elements were found
print(f"Found {len(ppm)} price elements")
print(f"Found {len(nbr)} bedroom count elements")
print(f"Found {len(address)} address elements")
print(f"Found {len(property_style)} property type elements")
print(f"Found {len(agent)} agent elements")

# Open the CSV file to write the data
with open("rightmove_experiment.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    # Write headers
    writer.writerow(["Price", "Bedrooms", "Address", "Property Style", "Agent"])

    # Loop through each listing and extract the relevant data
    for price, bedrooms, addr, style, agent_name in zip(ppm, nbr, address, property_style, agent):
        # Extract the text content from each element
        price_text = price.get_text(strip=True) if price else "N/A"
        bedrooms_text = bedrooms.get_text(strip=True) if bedrooms else "N/A"
        addr_text = addr.get_text(strip=True) if addr else "N/A"
        style_text = style.get_text(strip=True) if style else "N/A"
        agent_text = agent_name.get_text(strip=True) if agent_name else "N/A"

        # Print to console for verification
        print(f"{price_text} | {bedrooms_text} | {addr_text} | {style_text} | {agent_text}")

        # Write data to CSV file
        writer.writerow([price_text, bedrooms_text, addr_text, style_text, agent_text])

print("Data saved to 'rightmove_experiment.csv'")

