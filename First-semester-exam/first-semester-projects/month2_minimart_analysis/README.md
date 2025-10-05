## Setup Instructions

1. **Create virtual environment**
2. **Install dependencies** `pip install -r requirements.txt`
3. **Set up postreSQL database**
    ```
    psql -U postgres
    CREATE DATABASE minimart_db;
    \c minimart_db
    \i sql/create_tables.sql
    \i sql/insert_data.sql
    exit
    ```
4. **Edit utils.py to your credentials**
5. **Run the program**
    ```
    cd python
    python main.py
    ```

