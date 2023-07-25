import sqlalchemy.exc
from sqlalchemy import text, desc, func, select
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
import asyncio
from sqlalchemy import select, delete
from asyncpg.exceptions import UniqueViolationError
from sqlalchemy.orm import joinedload
from lesson18_19_sqlalchemy import config
import datetime
from lesson18_19_sqlalchemy.models import User, Post, Comment, Like
users = User
posts = Post
comments = Comment
likes = Like


class DatabaseWorker:

    def __init__(self, db_url):
        self._url = db_url
        self._engine = None
        self._session = None

    def connect(self):
        self._engine = create_async_engine(self._url, echo=True)
        self._session = AsyncSession(self._engine)

    async def check_db(self):
        async with self._session as s:
            await s.execute(text("SELECT 1"))



    @staticmethod
    async def _get_comment_by_post_id_from_session(session: AsyncSession, post_id: int):

        query = select(Comment).where(Comment.post_id == post_id)

        result = await session.execute(query)
        result = result.unique().scalar_one_or_none()
        return result

    @staticmethod
    async def _get_post_by_id_from_session(session: AsyncSession, post_id: int):

        query = select(Post).where(Post.id == post_id)
        result = await session.execute(query)
        result = result.unique().scalar_one_or_none()
        return result

    async def get_comment_by_post_id(self, post_id: int):
        async with self._session as s:
            return await self._get_comment_by_post_id_from_session(s, post_id)

    async def get_post_by_id(self, post_id: int):
        async with self._session as s:
            return await self._get_post_by_id_from_session(s, post_id)

    async def update_comment_by_post_id(self, post_id: int, **data):
        if not data:
            print(f"No data to update user with Id {post_id}")
            return
        async with self._session as s:
            async with s.begin():
                comment = await self._get_comment_by_post_id_from_session(s, post_id=post_id)
                if comment is None:
                    print(f"No user with Id: {post_id}")
                    return

                if (title := data.get("title")) is not None:
                    now = 'Wow, It is great!'
                    comment.title = now +' '+ title


                if (new_post := data.get("new_post")) is not None:
                    comment.posts.append(new_post)


                return "Ok"


    @staticmethod
    async def _get_likes_count_by_posts_and_users(session: AsyncSession):
        query = (
            select(posts.id, posts.title, posts.user_id, likes.post_id)
            .join_from(users, posts, isouter=True)
            .join_from(posts, likes, isouter=True)
            .where(likes.post_id == None))

        result =await session.execute(query)
        return result
    async def get_likes_count_by_posts_and_users(self):
        async with self._session as s:
            return await self._get_likes_count_by_posts_and_users(s)

    @staticmethod
    async def _add_like(session: AsyncSession, like: Like):
        try:

            async with session.begin_nested():
                session.add(like)
                return "Ok"

        except sqlalchemy.exc.IntegrityError as exc:

            match exc.orig and exc.orig.__cause__:
                case UniqueViolationError() as exc:

                    print(repr(exc))
                case _:
                    raise exc

    async def add_new_like(self, like: Like):
        async with self._session as s:
            async with s.begin():
                result = await self._add_like(s, like=like)

                return result





























    async def delete_post_by_id(self, post_id: int):
        """
        Deletes row from "posts" table
        """
        async with self._session as s:
            """
            Using *session.begin()* context manager
            you don't need to call *session.commit()* OR *session.rollback()*
            at the end of *async with self._session as s* block
            """
            async with s.begin():
                query = delete(Post).where(Post.id == post_id)
                return await s.execute(query)

    async def update_user_by_id(self, user_id: int, **data):
        if not data:
            print(f"No data to update user with Id {user_id}")
            return

        async with self._session as s:
            """
            starting the new Transaction using 'begin()' context manager
            to avoid making 'commit / rollback' directly later
            """
            async with s.begin():
                user = await self._get_user_by_id_from_session(s, user_id=user_id)
                """
                NOTE: if we would use *self.get_user_by_id(user_id=user_id)* here,
                the updates we will make bellow will not be applied to real Database state!
                Because in this case the User object was got within the another Session
                """
                if user is None:
                    print(f"No user with Id: {user_id}")
                    return

                if (name := data.get("name")) is not None:
                    user.name = name  # update user's name
                if (age := data.get("age")) is not None:
                    user.age = age  # update user's age
                if (gender := data.get("gender")) is not None:
                    user.gender = gender  # update user's gender
                if (nationality := data.get("nationality")) is not None:
                    user.nationality = nationality  # update user's nationality

                """
                add new post to User: this requires to use
                *lazy="joined"* on "posts" attribute in User class.
                This makes automatic JOIN of "users" and "posts" tables
                when you just SELECT a User, and also it binds the "posts"
                to the User object within the Session
                """
                if (new_post := data.get("new_post")) is not None:
                    user.posts.append(new_post)

                """
                At the end of context manager body the updates we made above
                are applied to the Database
                """

                return "Ok"




























    async def add_new_user(self, user: User):
        async with self._session as s:
            async with s.begin():
                result = await self._add_user(s, user=user)

                return result

    @staticmethod
    async def _add_user(session: AsyncSession, user: User):
        try:
            """
            create SAVEPOINT for started Transaction
            """
            async with session.begin_nested():
                session.add(user)  # attach User object to the session
                return "Ok"

        except sqlalchemy.exc.IntegrityError as exc:
            """
            Here we check that underlying Exception is
            the UniqueViolationError which occurs when
            the UNIQUE constraint was Violated: in this specific case,
            it may occur upon adding the 2 SAME Users
            """
            match exc.orig and exc.orig.__cause__:
                case UniqueViolationError() as exc:
                    """
                    Please NOTE that here we only print the 
                    Exception's traceback without raising 
                    the Exception itself!
                    """
                    print(repr(exc))
                case _:
                    raise exc

            # Transaction state will be RELEASED OR ROLLED BACK to the SAVEPOINT



