import requests
from bs4 import BeautifulSoup
import pandas

urls = "https://www.oyorooms.com/hotels-in-bangalore/"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}

page = requests.get(urls)
content = page.content

soup = BeautifulSoup(content, "html.parser")

all_hotels = soup.find_all("div", {"class": "hotelCardListing"})
scraped_info_list=[]

for hotel in all_hotels:
    hotel_dict={}
    hotel_dict["name"] = hotel.find("h3", {"class": "listingHotelDescription__hotelName"}).text
    hotel_dict["address"] = hotel.find("span", {"itemprop": "streetAddress"}).text
    hotel_dict["price"] = hotel.find("span", {"class": "listingPrice__finalPrice"}).text
    #try .... except
    try :
        hotel_dict["rating"] = hotel.find("span", {"class": "hotelRating__ratingSummary"}).text
    except AttributeError:
        pass

    parent_amenities_element = hotel.find("div", {"class": "amenityWrapper"})

    amenities_list = []
    for amenity in parent_amenities_element.find_all("div", {"class": "amenityWrapper__amenity"}):
        (amenities_list.append(amenity.find("span", {"class": "d-body-sm"}).text.strip()))

    hotel_dict["amenities"] = ', '.join(amenities_list[:-1])

    scraped_info_list.append(hotel_dict)

    #print(hotel_name, hotel_address, hotel_price, hotel_rating, amenities_list)

dataframe = pandas.DataFrame(scraped_info_list)
dataframe.to_csv("Oyo.csv")