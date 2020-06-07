from requests import get
from bs4 import BeautifulSoup
import webbrowser

print(" ___ _   ___     _____ ____ ___ ___   ____ _     ___ ")
print("|_ _| \ | \ \   / /_ _|  _ \_ _/ _ \ / ___| |   |_ _|")
print(" | ||  \| |\ \ / / | || | | | | | | | |   | |    | |")
print(" | || |\  | \ V /  | || |_| | | |_| | |___| |___ | | ")
print("|___|_| \_|  \_/  |___|____/___\___(_)____|_____|___|")

print("""
Select an instance:
1) invidio.us
2) invidious.snopyta.org
3) yewtu.be

""")
instance = input("Select an instance: ")
if instance == "1":
    instance = "https://invidio.us"
elif instance == "2":
    instance = "https://invidious.snopyta.org"
elif instance == "3":
    instance = "https://yewtu.be"

search_query = input("Search something > ")

url = instance+"/search?q="+search_query

results_list = []

page = BeautifulSoup(get(url).text, features="html5lib")

i=1
for link in page.find_all('a'):
    if link.get("href")[0:6] == "/watch":
        if link.string != None:
            print(f"[{i}]=========================================================================================================")
            print(link.string)
            video_link = instance+link.get("href")
            print(video_link)
            results_list.append(video_link)
            i+=1
print("=========================================================================================================")

selected_video = None
selected_video = int(input("Insert the number of the video you want to watch: "))
while selected_video == None or selected_video < 1 or selected_video >= len(results_list):
    selected_video = int(input("[UNVALID DATA] Insert the number of the video you want to watch: "))
webbrowser.open(results_list[selected_video-1], new=2)
