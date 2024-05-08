car_sql_script_create_table = """
    CREATE TABLE IF NOT EXISTS Car (
        id INTEGER PRIMARY KEY,
        model TEXT NOT NULL,
        price INTEGER NOT NULL,
        mileage INTEGER NOT NULL
    )
"""

car_sql_script_insert = """
    INSERT INTO Car (model, price, mileage) VALUES (?, ?, ?)
"""

car_sql_script_select_all = """
    SELECT * FROM Car
"""

car_sql_script_delete_all = """
    DELETE FROM Car
"""

car_sql_script_delete_by_id = """
    DELETE FROM Car WHERE id = ? 
"""



