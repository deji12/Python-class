import requests

base_url = "https://03a4-102-68-110-193.ngrok-free.app"

new_blog = {
    "name": "Sunday",
    "content": "Today is a blissful Sunday"
}

delete_blog = requests.delete(f"{base_url}/delete-blog/{3}")
print(delete_blog.json())

# create_new_blog = requests.post(f"{base_url}/create-blog/", data=new_blog)

# response = requests.get(f"{base_url}/get-blogs/")

# data = response.json()

# print(data)


# updae_existing_blog = requests.put(f"{base_url}/update-blog/3", data=new_blog)