-----------------𝐇𝐨𝐰 𝐭𝐨 𝐂𝐨𝐧𝐧𝐞𝐜𝐭 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞 𝐢𝐧 𝐅𝐚𝐬𝐭𝐀𝐩𝐢------------------------------------
𝐀 𝐠𝐮𝐢𝐝𝐞 𝐨𝐧 𝐡𝐨𝐰 𝐭𝐨 𝐜𝐨𝐧𝐧𝐞𝐜𝐭 𝐚 𝐒𝐐𝐋𝐢𝐭𝐞 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞 𝐮𝐬𝐢𝐧𝐠 𝐒𝐐𝐋𝐀𝐥𝐜𝐡𝐞𝐦𝐲 𝐢𝐧 𝐅𝐚𝐬𝐭𝐀𝐏𝐈.

## Setup Instructions

### Prerequisites
Ensure you have Python installed (version 3.x recommended). Install dependencies using:

```bash
pip install fastapi[all] sqlalchemy uvicorn
```

## Using FastAPI with SQLAlchemy and SQLite

𝐁𝐞𝐥𝐨𝐰 𝐢𝐬 𝐚𝐧 𝐞𝐱𝐚𝐦𝐩𝐥𝐞 𝐨𝐟 𝐡𝐨𝐰 𝐭𝐨 𝐞𝐬𝐭𝐚𝐛𝐥𝐢𝐬𝐡 𝐚 𝐜𝐨𝐧𝐧𝐞𝐜𝐭𝐢𝐨𝐧 𝐮𝐬𝐢𝐧𝐠 𝐅𝐚𝐬𝐭𝐀𝐏𝐈, 𝐒𝐐𝐋𝐀𝐥𝐜𝐡𝐞𝐦𝐲, 𝐚𝐧𝐝 𝐒𝐐𝐋𝐢𝐭𝐞:

```python
from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

app = FastAPI()

# Database configuration
DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define a sample model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/")
def create_user(name: str, db: Session = Depends(get_db)):
    new_user = User(name=name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    return db.query(User).all()
```

## Using SQLite with Raw SQL

𝐁𝐞𝐥𝐨𝐰 𝐢𝐬 𝐚𝐧 𝐞𝐱𝐚𝐦𝐩𝐥𝐞 𝐨𝐟 𝐡𝐨𝐰 𝐭𝐨 𝐜𝐫𝐞𝐚𝐭𝐞 𝐚 𝐭𝐚𝐛𝐥𝐞 𝐚𝐧𝐝 𝐢𝐧𝐬𝐞𝐫𝐭/𝐪𝐮𝐞𝐫𝐲 𝐝𝐚𝐭𝐚 𝐮𝐬𝐢𝐧𝐠 𝐫𝐚𝐰 𝐒𝐐𝐋 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬:

```sql
-- Create a table
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

-- Insert sample data
INSERT INTO users (name) VALUES ('John Doe');

-- Query data
SELECT * FROM users;
```

## Running the Code

### Running FastAPI Server
Save the above Python code as `main.py` and execute:

```bash
uvicorn main:app --reload
```

This will start a FastAPI server on `http://127.0.0.1:8000`. You can visit `http://127.0.0.1:8000/docs` to access the API documentation.

### Running SQL Commands
To execute the SQL script, you can use the SQLite command-line tool:

```bash
sqlite3 database.db < script.sql
```

This will create an SQLite database (`database.db`) and insert/query sample data.

## License
Specify the license for your project.

---

𝓣𝓱𝓪𝓷𝓴 𝓨𝓸𝓾 𝓕𝓸𝓻 𝓥𝓲𝓼𝓲𝓽𝓲𝓷𝓰 𝓜𝔂 𝓡𝓮𝓹𝓸.

