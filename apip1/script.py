
import requests


endpoint = "http://127.0.0.1:8000/apip/Book/?limit=2"
# dict1 = {}
# lst1 = []
# while(True):
#     resp = requests.get(endpoint)
#     [lst1.append(obj) for obj in resp.json()['results']]
#     next_url = resp.json()['next']
#     if not next_url:
#         break
#     endpoint = next_url

# print(lst1)

resp = requests.get(endpoint);
print(resp)
a = resp.json()
print(a['count'])
print(a['results'])










# print()
# print()
# # print(type(r))
# # print(r.url)

# # print(type(r.content))
# # print(r.content['count'])
# # print(vars(r))

# a = r.content



# print()
# print(r.json())
# print(r.json()['results'])
# for u in r.json()['results']:
#     print("u = ", u)
#     print(u['id'])

# print()

