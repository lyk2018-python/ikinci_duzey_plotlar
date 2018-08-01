import matplotlib
import requests
import bs4

matplotlib.use('Qt5Agg')
# matplotlib.rcParams['backend.qt5'] = 'PySide2'
import matplotlib.pyplot as plt


def get_html(base_url=""):
    return requests.get(base_url).text


def get_ufo_data():
    data = get_html("http://www.nuforc.org/webreports/ndxshape.html")

    soup = bs4.BeautifulSoup(data, "html.parser")

    tr_list = soup.find("tbody").find_all("tr")

    data_list = []
    for tr in tr_list:
        th_list = tr.find_all("td")
        data_list.append({
            "shape": th_list[0].string,
            "count": int(th_list[1].string)
        })

    return data_list


def show_graphics():
    ufo_data_list = get_ufo_data()
    shapes = [ufo["shape"] for ufo in ufo_data_list]
    counts = [ufo["count"] for ufo in ufo_data_list]

    plt.title("National UFO Reporting Center\nReport Index by Shape of Craft")
    plt.bar(shapes, counts)
    plt.xticks(rotation=45)
    plt.show()


if __name__ == "__main__":
    show_graphics()
