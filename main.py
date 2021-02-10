import json
import requests

from http.cookies import SimpleCookie
from datetime     import datetime, timedelta

from config       import USER_ID, TOKEN, HTTP_REQUEST


def get_cookie(token, url):
    cookie     = SimpleCookie(f'token_v2 = "{token}"; Path=/; Domain=.www.notion.so')
    cookie_jar = requests.get(url).cookies
    cookie_jar.update(cookie)

    return cookie_jar

def get_notion_response(url, headers, body, cookies):
    response = requests.post(
        url,
        headers = headers,
        data    = json.dumps(body),
        cookies = cookies
    ).json()

    return response


def get_notion_value(url, headers, body, cookies, user_id):
    response        = get_notion_response(url, headers, body, cookies)
    recent_block_id = response["result"]["blockIds"][-1]
    recent_block    = response["recordMap"]["block"][recent_block_id]

    title        = str(recent_block["value"]["properties"]["title"][0][0])
    created_time = recent_block["value"]["created_time"]
    date         = datetime.utcfromtimestamp(created_time / 1000) + timedelta(hours = 9)
    date         = date.strftime("%Y-%m-%d")
    url          = f"https://notion.so/{user_id}/" + recent_block_id.replace('-', '')

    message      = f"제목: {title}\n작성 일자: {date}\nURL: {url}"

    return message


def lambda_handler(event, context):
    url     = HTTP_REQUEST["URL"]
    headers = HTTP_REQUEST["HEADERS"]
    body    = HTTP_REQUEST["BODY"]
    cookies = get_cookie(TOKEN, url = url)

    message = get_notion_value(url, headers, body, cookies, USER_ID)

    return message