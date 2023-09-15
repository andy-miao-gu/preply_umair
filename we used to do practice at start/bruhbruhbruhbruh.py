import requests as rq
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = rq.get(url)
print("Status code:", r.status_code)
text = r.text
json_f = r.json()
