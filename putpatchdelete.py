import requests



get_url = "https://jsonplaceholder.typicode.com/todos/15"



#get_response = requests.get(get_url)
#print(get_response.json())


#PUT
to_do_item_15 = {"userId" : 16 , "title":"demo baba","completed":False}
#put_response = requests.put(get_url, json=to_do_item_15)
#print(put_response.json())


#PATCH
to_do_item_patch_15 = {"title": "malamine"}
#atch_response = requests.patch(get_url, json=to_do_item_patch_15)
#print(patch_response.json())


#DELETE
delete_response = requests.delete(get_url)
print(delete_response.json())
print(delete_response.status_code)