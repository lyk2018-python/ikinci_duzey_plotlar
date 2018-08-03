from collections import Counter
import requests
import bs4
import matplotlib.pyplot as plt
from datetime import datetime
import statistics

def get_time(line):
    date = line.split(" -")[0]  # 8/26/17, 5:13 PM
    return datetime.strptime(date, "%m/%d/%y, %I:%M %p")

def count_the_messages_by_word():
    with open("chat.txt",encoding="utf8") as f:
        text = f.readlines()
    response = requests.get(
        "http://www.turkceogretimi.com/tavsiyeler/en-%C3%A7ok-kullan%C4%B1lan-1000-t%C3%BCrk%C3%A7e-kelime")
    soup = bs4.BeautifulSoup(response.text, "lxml")
    table = soup.find("table")
    common_words = list()
    for row in table.find_all("tr")[2:50]:
        word = row.find_all("td")[1].text.strip()
        common_words.append(word)

    special_messages = ["<Media omitted>", "(file attached)", "This message was deleted", 'You deleted this message']
    n = ""
    for line in text:
        message = line.split(": ", 1)[-1]
        if all([i not in message for i in special_messages]) and all(
                [i.lower() not in message.lower().split() for i in common_words]) and message:
            n += message + " "

    message_counts = Counter([word for word in n.split() if not word.isdecimal()])
    message_counts = message_counts.most_common(25)
    data, labels = list(zip(*message_counts))
    plt.pie(data, labels=labels)
    plt.title("Most common 25 words")
    plt.show()

def count_the_messages_by_time():
    with open("chat.txt",encoding="utf8") as f:
        text = f.readlines()

    time_intervals = [[0 for i in range(6)] for j in range(24)]

    for line in text:
        date = get_time(line)
        time = date.time()
        hour, minute = time.hour, time.minute // 10
        time_intervals[hour][minute] += 1

    ticks = [i for i in range(len(time_intervals))]
    tints = list(zip(*time_intervals))

    avg_intervals = []
    for i in time_intervals:
        avg_intervals.append(statistics.mean(i))

    fig, ax = plt.subplots()
    for i in range(6):
        ax.bar([t + 0.15*i for t in ticks], tints[i], 0.2)
    ax.plot([t + 0.45 for t in ticks], avg_intervals)
    ax.set_xticks([t / 2 for t in [i for i in range(len(time_intervals) * 2)]])
    plt.title("24 hour group activity")
    plt.show()


if __name__ == '__main__':
    count_the_messages_by_word()
    count_the_messages_by_time()