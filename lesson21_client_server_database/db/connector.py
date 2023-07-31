import sqlalchemy.exc
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import select, delete
from asyncpg.exceptions import UniqueViolationError

from lesson21_client_server_database.db.models import User, Post, Comment, Like
from lesson21_client_server_database.structures import OperationStatus


class DatabaseConnector:

    def __init__(self, db_url):
        self._url = db_url
        self._engine = create_async_engine(self._url, echo=True)
        # *async_sessionmaker* call returns AsyncSession class object
        self._session = async_sessionmaker(self._engine)

    @staticmethod
    async def _get_user(
        session: AsyncSession,
        user_name: str,
        user_age: int
    ) -> User | None:
        return (
            await session.execute(
                select(User)
                .where(
                    User.name == user_name,
                    User.age == user_age
                )
            )
        ).unique().scalar_one_or_none()

    @staticmethod
    async def _get_post(
        session: AsyncSession,
        user_name: str,
        user_age: int,
        post_title: str,
        post_description: str
    ) -> Post | None:

        return (
            await session.execute(
                select(Post)
                .join(User)
                .where(
                    User.name == user_name,
                    User.age == user_age,
                    Post.title == post_title,
                    Post.description == post_description
                )
            )
        ).unique().scalar_one_or_none()
    @staticmethod
    async def _get_comment(
        session: AsyncSession,
        user_name: str,
        user_age: int,
        post_title: str,
        post_description: str,
        comment_title: str
    ) -> Comment | None:

        return (
            await session.execute(
                select(Comment)
                .join(Post)
                .join(User)
                .where(
                    User.name == user_name,
                    User.age == user_age,
                    Post.title == post_title,
                    Post.description == post_description,
                    Comment.title == comment_title
                )
            )
        ).unique().scalar_one_or_none()

    @staticmethod
    async def _get_like(
        session: AsyncSession,
        user_name: str,
        user_age: int,
        post_title: str,
        post_description: str,
    ) -> Like | None:
        return (
            await session.execute(
                select(Like)
                .join(Post)
                .join(User)
                .where(
                    User.name == user_name,
                    User.age == user_age,
                    Post.title == post_title,
                    Post.description == post_description,
                )
            )
        ).unique().scalar_one_or_none()

    @staticmethod
    async def _add_post_avoid_conflict(
        session: AsyncSession,
        user: User,
        post: Post,
    ) -> OperationStatus:
        try:
            async with session.begin_nested():
                user.posts.append(post)
                return OperationStatus.SUCCESS
        except sqlalchemy.exc.IntegrityError as exc:
            match exc.orig and exc.orig.__cause__:
                case UniqueViolationError() as exc:
                    print(repr(exc))
                    return OperationStatus.NOT_UNIQUE
                case _:
                    raise exc
    @staticmethod
    async def _edit_post(
        session: AsyncSession,
        post,
        new_post
    ) -> OperationStatus:
        try:
            async with session.begin_nested():
                post.title = new_post.title
                post.description = new_post.description
                return OperationStatus.SUCCESS
        except sqlalchemy.exc.IntegrityError as exc:
            match exc.orig and exc.orig.__cause__:
                case _:
                    raise exc
    async def add_post(
        self,
        user_name: str,
        user_age: int,
        post_title: str,
        post_description: str
    ) -> OperationStatus:

        # here (and in all methods bellow) we use *async with self._session()*
        # instead of *async with self._session*
        # because *self._session* stores the reference to
        # the AsyncSession class, NOT AsyncSession class Instance!
        async with self._session() as session:
            async with session.begin():
                user = await self._get_user(
                    session, user_name, user_age
                )
                if not user:
                    return OperationStatus.NOT_EXIST

                post = Post(title=post_title, description=post_description)
                return await self._add_post_avoid_conflict(session, user, post)

    async def add_comment(
        self,
        user_name: str,
        user_age: int,
        post_title: str,
        post_description: str,
        comment_title: str
    ) -> OperationStatus:

        async with self._session() as session:
            async with session.begin():
                post = await self._get_post(
                    session,
                    user_name, user_age,
                    post_title, post_description
                )
                if not post:
                    return OperationStatus.NOT_EXIST

                post.comments.append(
                    Comment(
                        title=comment_title,
                        user_id=post.user_id  # required
                    )
                )
                return OperationStatus.SUCCESS

    async def add_like(
        self,
        user_name: str,
        user_age: int,
        post_title: str,
        post_description: str,
    ) -> OperationStatus:

        async with self._session() as session:
            async with session.begin():
                post = await self._get_post(
                    session,
                    user_name, user_age,
                    post_title, post_description
                )
                if not post:
                    return OperationStatus.NOT_EXIST

                post.likes.append(
                    Like(
                        user_id=post.user_id  # required
                    )
                )
                return OperationStatus.SUCCESS

    # TODO: Implement methods bellow as Homework

    async def edit_post(
        self,
        user_name: str,            # for Select!
        user_age: int,             # for Select!
        post_title: str,           # for Select!
        post_description: str,     # for Select!
        new_post_title: str,       # for UPDATE!
        new_post_description: str  # for UPDATE!
    ):
        async with self._session() as session:
            async with session.begin():
                post = await self._get_post(
                    session, user_name, user_age, post_title, post_description
                )
                if not post:
                    return OperationStatus.NOT_EXIST

                post.title = new_post_title
                post.description = new_post_description
                return OperationStatus.SUCCESS

    async def edit_comment(
        self,
        user_name: str,         # for Select!
        user_age: int,          # for Select!
        post_title: str,        # for Select!
        post_description: str,  # for Select!
        comment_title: str,     # for Select!
        new_comment_title: str  # for UPDATE!
    ):
        async with self._session() as session:
            async with session.begin():
                comment = await self._get_comment(
                    session, user_name, user_age, post_title, post_description, comment_title
                )

                if not comment:
                    return OperationStatus.NOT_EXIST

                comment.title = new_comment_title
                return OperationStatus.SUCCESS

    async def delete_post(
        self,
        user_name: str,
        user_age: int,
        post_title: str,
        post_description: str,
    ):
        async with self._session() as session:
            async with session.begin():
                post = await self._get_post(
                    session, user_name, user_age, post_title, post_description
                )
                if not post:
                    return OperationStatus.NOT_EXIST

                await session.delete(post)
                return OperationStatus.SUCCESS

    async def delete_comment(
        self,
        user_name: str,
        user_age: int,
        post_title: str,
        post_description: str,
        comment_title: str
    ):
        async with self._session() as session:
            async with session.begin():
                comment = await self._get_comment(
                    session, user_name, user_age, post_title, post_description, comment_title
                )

                if not comment:
                    return OperationStatus.NOT_EXIST

                await session.delete(comment)
                return OperationStatus.SUCCESS

    async def delete_like(
        self,
        user_name: str,
        user_age: int,
        post_title: str,
        post_description: str,
    ):
        async with self._session() as session:
            async with session.begin():
                like = await self._get_like(
                    session, user_name, user_age, post_title, post_description
                )

                if not like:
                    return OperationStatus.NOT_EXIST

                await session.delete(like)
                return OperationStatus.SUCCESS

