from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./leave.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


class LeaveRequest(Base):
    __tablename__ = "leave_requests"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(String)
    employee_name = Column(String)

    start_date = Column(Date)
    end_date = Column(Date)

    leave_days = Column(Integer)

    status = Column(String, default="Pending")


Base.metadata.create_all(bind=engine)