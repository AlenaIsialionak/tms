import asyncio
import string
from multiprocessing import Process
from datetime import datetime
from sqlalchemy import select

from lesson18_19_sqlalchemy import config
from lesson18_19_sqlalchemy.models import Post, User, Comment, Like
from lesson18_19_sqlalchemy.db_worker import DatabaseWorker
from lesson18_19_sqlalchemy.queries import joins
from lesson18_19_sqlalchemy.queries import groupings
import traceback

# Homework

async def get_update_comments_title_and_check_updates(db_worker: DatabaseWorker, post_id: int):
    update_result = await db_worker.update_comment_by_post_id(post_id=post_id, title='')
    real_post_comment = await db_worker.get_post_by_id(post_id=post_id)
    print(50 *'*')
    print(real_post_comment)
    print(50 * '*')

    await database_worker.check_db()
    time_now = datetime.now()
    current_time = 'Update time:'+time_now.strftime("%H:%M:%S")
    update_result = await db_worker.update_comment_by_post_id(post_id=post_id, title=current_time)
    assert update_result.lower() == 'ok'
    real_user = await db_worker.get_comment_by_post_id(post_id=post_id)
    print(50 * '*')
    print(real_user)
    print(50 * '*')
    assert real_user.title == 'Wow, It is great!' + ' ' + current_time
    real_post_comment = await db_worker.get_post_by_id(post_id=post_id)
    print(50 *'*')
    print(real_post_comment)
    print(50 *'*')


async def count_like(db_worker: DatabaseWorker):
    count_result = await db_worker.get_likes_count_by_posts_and_users()
    print(50 *'*')
    a = list(count_result)
    result = [{'post_id':(a[j])[0], 'user_id':(a[j])[2]} for j in range(3) if (a[j])[1] != None]
    print(result)
    return result


# def create_likes_concurrently(db_worker: DatabaseWorker, id_post):
#     new_like = []
#     for i in id_post:
#         new_like.append(Like(
#             user_id=i['user_id'],
#             post_id=i['post_id']))
#     def _run_in_event_loop(like_):
#
#         asyncio.run(
#             db_worker.add_new_like( like=like_
#             )
#         )
#
#     running_procs = []
#     for like in new_like:
#         proc = Process(target=_run_in_event_loop, args=(like,))
#         proc.start()
#         running_procs.append(proc)
#
#     for p in running_procs:
#         p.join()



# def create_likes_concurrently(db_worker: DatabaseWorker, id_post):
#     new_like = []
#     for i in id_post:
#         new_like.append(Like(
#             user_id=i['user_id'],
#             post_id=i['post_id']))
#
#     for like in new_like:
#         asyncio.run(
#             db_worker.add_new_like(like=like)
#         )


if __name__ == '__main__':
    database_worker = DatabaseWorker(config.DB_URL)
    database_worker.connect()
    asyncio.run(
        get_update_comments_title_and_check_updates(database_worker, post_id=2)
    )
    # asyncio.run(
    #     count_like(database_worker)
    # )
    # id_post = asyncio.run(
    #     count_like(database_worker)
    # )
    # create_likes_concurrently(database_worker, id_post=id_post)






