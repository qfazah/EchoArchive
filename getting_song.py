import requests
from bs4 import BeautifulSoup


class GettingSong:
    def __init__(self):
        self.user_input = input("write the year of which songs do you need")
        # Set the target URL for the 2025 singles
        self.URL = f"https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_{self.user_input}"
        # Set the User-Agent so Wikipedia accepts our request
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }

    def scrapping_data(self):
        # 1. Send the request to the website
        response = requests.get(self.URL, headers=self.headers)

        # 2. Parse the raw HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # 3. Find the main wikitable holding the charts
        table = soup.find("table", class_="wikitable")

        if table:
            for row in table.find_all("tr")[1:]:

                columns = row.find_all("td")
                # 6. Check if we have columns to prevent indexing errors (some rows might be empty)
                if len(columns) >= 2 :
                    title_column = columns[1]
                    a_tag = title_column.find("a")
                    if a_tag:
                        song_name = a_tag.text

                        with open("song_names.txt" , mode = "a" , encoding="utf-8") as file :
                            file.write(song_name +"\n")


        else:
            print("Could not find the target table on the page.")


# This runs the class when you click play in PyCharm
if __name__ == "__main__":
    file = GettingSong()
    file.scrapping_data()