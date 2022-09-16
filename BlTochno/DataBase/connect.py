from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from secret import CONNECT_TO_DB

engine = create_engine(CONNECT_TO_DB)
