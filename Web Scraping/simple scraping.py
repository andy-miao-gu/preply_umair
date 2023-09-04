import requests
data = requests.get("https://www3.nhk.or.jp/nhkworld/en/news/20230731_10/")
dt=data.text.split("/p")
for each in dt:
    if "<p>"  in each:
        print(each)