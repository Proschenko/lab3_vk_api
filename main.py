import requests
import json

ACCESS_TOKEN = 'Ваш токен'

API_VERSION = '5.131'


def get_user_info(user_id):
    url = f"https://api.vk.com/method/users.get?user_ids={user_id}&fields=city,domain&access_token={ACCESS_TOKEN}&v={API_VERSION}"
    response = requests.get(url)
    return response.json()


def get_friends(user_id):
    url = f"https://api.vk.com/method/friends.get?user_id={user_id}&fields=city,domain&access_token={ACCESS_TOKEN}&v={API_VERSION}"
    response = requests.get(url)
    return response.json()


def get_followers(user_id):
    url = f"https://api.vk.com/method/users.getFollowers?user_id={user_id}&fields=city,domain&access_token={ACCESS_TOKEN}&v={API_VERSION}"
    response = requests.get(url)
    return response.json()


def get_subscriptions(user_id):
    url = f"https://api.vk.com/method/users.getSubscriptions?user_id={user_id}&extended=1&access_token={ACCESS_TOKEN}&v={API_VERSION}"
    response = requests.get(url)
    return response.json()


def save_to_json(data, filename="vk_data.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    user_id = '231805785' # Моя страница

    # Получение основной информации о пользователе
    user_info = get_user_info(user_id)

    # Получение информации о подписчиках
    followers = get_followers(user_id)

    # Получение информации о друзьях
    friends = get_friends(user_id)

    # Получение информации о группах, на которые подписан пользователь
    subscriptions = get_subscriptions(user_id)

    # Сбор всех данных в одну структуру
    data = {
        "user_info": user_info,
        "followers": followers.get("response", {}).get("items", []),  # Детали о подписчиках
        "friends": friends.get("response", {}).get("items", []),  # Детали о друзьях
        "subscriptions": subscriptions.get("response", {}).get("items", [])  # Названия групп
    }

    # Сохранение данных в JSON-файл
    save_to_json(data, f"vk_data_{user_id}.json")
