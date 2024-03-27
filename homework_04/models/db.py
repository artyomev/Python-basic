from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
import os


#PG_CONN_URI =  "postgresql+asyncpg://postgres:admin@localhost:5432/postgres" # локальная бд для тестирования
PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"

engine = create_async_engine(PG_CONN_URI)

Session = async_sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False
)