try:
    from bs4 import BeautifulSoup
    from urllib.request import urlopen
    import pandas as pd

except Exception as e:
    print("Some Modules are Missing {}".format(e))


class Stack(object):

    def __init__(self):
        self.data = []


class WebCrawler(object):

    def __init__(self, year):

        self.year = year
        self.base_url = "https://www.rottentomatoes.com/top/bestofrt/?year="+str(self.year)
        self.client = urlopen(self.base_url)
        self.stack = Stack()

    def scrapper(self):

        page_html=self.client.read()
        soup=BeautifulSoup(page_html, 'html.parser')
        self.client.close()
        containe = soup.find('table',  class_='table')

        movie_names = containe.find_all(class_='unstyled articleLink')
        movie_ratings=containe.find_all('span',class_='tMeterScore')

        name = []
        rating = []

        for i in range(0,100):
            name.append(movie_names[i].string.strip())
            Tem = movie_ratings[i].string
            rating.append(Tem)

        df = pd.DataFrame(data={
            "Movie":name,
            "Rating":rating
            })
        return df



class MovieRatings(object):

    def __init__(self, year):
        self.year = year
        self.webcrawler = WebCrawler(year=year)
        self.stack  = Stack()
        self.df = self.webcrawler.scrapper()

    def PrintData(self):
        print(self.df)

    def saveAsCsv(self):
        self.df.to_csv("Movies.csv")

    def saveAsJson(self):
        self.df.to_json("Movie.json")


if __name__ == "__main__":
    obj = MovieRatings(year=2019)
    obj.saveAsCsv()
    obj.saveAsJson()



