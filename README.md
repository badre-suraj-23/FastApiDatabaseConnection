-----------------𝐇𝐨𝐰 𝐭𝐨 𝐂𝐨𝐧𝐧𝐞𝐜𝐭 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞 𝐢𝐧 𝐅𝐚𝐬𝐭𝐀𝐩𝐢------------------------------------
## Setup Instructions

### Prerequisites
Ensure you have Python installed (version 3.x recommended). Install dependencies using:

```bash
pip install sqlalchemy sqlite3
```

## Using SQLAlchemy with SQLite

𝐁𝐞𝐥𝐨𝐰 𝐢𝐬 𝐚𝐧 𝐞𝐱𝐚𝐦𝐩𝐥𝐞 𝐨𝐟 𝐡𝐨𝐰 𝐭𝐨 𝐞𝐬𝐭𝐚𝐛𝐥𝐢𝐬𝐡 𝐚 𝐜𝐨𝐧𝐧𝐞𝐜𝐭𝐢𝐨𝐧 𝐮𝐬𝐢𝐧𝐠 𝐒𝐐𝐋𝐀𝐥𝐜𝐡𝐞𝐦𝐲 𝐚𝐧𝐝 𝐒𝐐𝐋𝐢𝐭𝐞:
```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an SQLite database engine
DATABASE_URL = "sqlite:///database.db"
engine = create_engine(DATABASE_URL, echo=True)

# Define a Base class
Base = declarative_base()

# Define a sample model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

# Create tables
Base.metadata.create_all(engine)

# Create a session
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Insert sample data
new_user = User(name="John Doe")
session.add(new_user)
session.commit()

# Query data
users = session.query(User).all()
for user in users:
    print(user.id, user.name)
```

## Using SQLite with Raw SQL

------------------------------------------------------------------------------------------------------------------------------

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

### Running Python Code
Save the above Python code as `main.py` and execute:

```bash
python main.py
```

### Running SQL Commands
To execute the SQL script, you can use the SQLite command-line tool:

```bash
sqlite3 database.db < script.sql
```

This will create an SQLite database (`database.db`) and insert/query sample data.

## License
Specify the license for your project.

------------------------------------------------------------------------------------------------------------------------------
𝓣𝓱𝓪𝓷𝓴 𝓨𝓸𝓾 𝓕𝓸𝓻 𝓥𝓲𝓼𝓲𝓽𝓲𝓷𝓰 𝓜𝔂 𝓡𝓮𝓹𝓸.
