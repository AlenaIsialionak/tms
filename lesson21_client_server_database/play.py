import asyncio

from lesson21_client_server_database.client_and_server.client import Client
from lesson21_client_server_database.structures import User
from lesson21_client_server_database.client_and_server.config import SERVER_PORT
from datetime import datetime

SERVER_HOST = f"http://0.0.0.0"
SERVER_URL = f"{SERVER_HOST}:{SERVER_PORT}"


async def main():
    user = User(
        name="Ann",
        age=32,
    )

    post_tile, post_description = f"Ann new post", f"I don't figure out!"
    client = Client(server_url=SERVER_URL)
    add_post_result = await client.add_post(user, post_tile, post_description)
    print(add_post_result)

    add_comment_result = await client.add_comment(user, post_tile, post_description, comment_title="It's not good!")
    print(add_comment_result)

    add_like_result = await client.add_like(user, post_tile, post_description)
    print(add_like_result)

    new_post_title, new_post_description = f"Ann edited post", f"Everything will be good!"
    # edit_post_result = await client.edit_post(user, post_tile, post_description, new_post_title, new_post_description)
    # print(edit_post_result)

    post_tile, post_description = new_post_title, new_post_description
    comment_title = "It's not good!"
    new_comment_title = 'update'

    # edit_comment_result = await client.edit_comment(user, post_tile, post_description, comment_title, new_comment_title)
    # print(edit_comment_result)

    comment_title = new_comment_title

    # delete_comment_result = await client.delete_comment(user, post_tile, post_description, comment_title)
    # print(delete_comment_result)


    # delete_like_result = await client.delete_like(user, post_tile, post_description)
    # print(delete_like_result)


    # delete_post_result = await client.delete_post(user, post_tile, post_description)
    # print(delete_post_result)




if __name__ == '__main__':
    asyncio.run(main())
