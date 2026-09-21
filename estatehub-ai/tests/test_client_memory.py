from app.property_database import init_db,SessionLocal
from app.client_memory import get_or_create_client
def test_memory():
    init_db(); db=SessionLocal()
    c=get_or_create_client(db,"Memory Estate Test")
    assert c.id is not None
    db.close()
