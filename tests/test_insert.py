from api.DatabaseManager import DatabaseManager  # Replace with your actual import

def test_insert_ram_data():
    db_manager = DatabaseManager('test_ram_info.db')
    db_manager.insert_ram_data([1000, 500, 500])  # Example data
    data = db_manager.get_last_n_entries(1)
    assert data[0][1] == 1000  # Assuming 1st column is 'total'