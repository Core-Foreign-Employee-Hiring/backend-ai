from collections.abc import Generator

from sqlmodel import Session, SQLModel, create_engine

from app.core.config import settings

# SQLite 연결 설정
connect_args = {"check_same_thread": False}
engine = create_engine(settings.database_url, connect_args=connect_args, echo=False)


def create_db_and_tables():
    """데이터베이스 테이블 생성"""
    SQLModel.metadata.create_all(engine)


def get_db() -> Generator[Session, None, None]:
    """데이터베이스 세션 의존성"""
    with Session(engine) as session:
        yield session

