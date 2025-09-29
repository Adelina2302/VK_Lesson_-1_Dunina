import requests
import urllib.parse
import os
import argparse
from dotenv import load_dotenv


def is_shorten_link(token, url):
    url_parts = urllib.parse.urlparse(url)
    if url_parts.netloc != "vk.cc":
        return False
    link_key = url_parts.path.lstrip("/")
    api_url = "https://api.vk.com/method/utils.getLinkStats"
    params = {
        "access_token": token,
        "key": link_key,
        "interval": "forever",
        "v": "5.199"
    }
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    stats_response = response.json()
    return "error" not in stats_response


def shorten_link(token, url):
    api_url = "https://api.vk.com/method/utils.getShortLink"
    params = {"access_token": token, "url": url, "v": "5.199"}
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    api_response = response.json()
    if "error" in api_response:
        raise Exception(api_response["error"]["error_msg"])
    return api_response["response"]["short_url"]


def count_clicks(token, link):
    url_parts = urllib.parse.urlparse(link)
    if url_parts.netloc == "vk.cc":
        link_key = url_parts.path.lstrip("/")
    else:
        link_key = link.replace("https://vk.cc/", "").replace("vk.cc/", "")
    api_url = "https://api.vk.com/method/utils.getLinkStats"
    params = {"access_token": token, "key": link_key, "interval": "forever", "v": "5.199"}
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    stats_response = response.json()
    if "error" in stats_response:
        raise Exception(stats_response["error"]["error_msg"])
    stats_list = stats_response["response"]["stats"]
    clicks_count = sum(day.get("views", 0) for day in stats_list)
    return clicks_count


def main():
    load_dotenv()
    vk_token = os.environ['VK_TOKEN']

    parser = argparse.ArgumentParser(description="VK link shortener and stats")
    parser.add_argument("url", help="Введите ссылку для сокращения или анализа")
    args = parser.parse_args()

    user_url = args.url.strip()

    try:
        if is_shorten_link(vk_token, user_url):
            clicks_count = count_clicks(vk_token, user_url)
            print("Количество переходов по короткой ссылке:", clicks_count)
        else:
            if user_url.startswith("http://") or user_url.startswith("https://"):
                short_link = shorten_link(vk_token, user_url)
                print("Сокращённая ссылка:", short_link)
            else:
                print("Ошибка: ссылка должна начинаться с http:// или https://")
    except requests.RequestException as req_exc:
        print("Ошибка сети или HTTP-запроса:", req_exc)
    except Exception as api_exc:
        print("Ошибка API:", api_exc)


if __name__ == "__main__":
    main()
