from api.DatabaseManager import DatabaseManager
import psutil, os

class RAMDataManager:
    @staticmethod
    def ram_data():
        ram = psutil.virtual_memory()
        total_mb = ram.total / (1024 * 1024)
        free_mb = ram.free / (1024 * 1024)
        used_mb = ram.used / (1024 * 1024)
        return total_mb, free_mb, used_mb

    @staticmethod
    def insert_ram_info():
        try:
            script_dir = os.path.dirname(os.path.realpath(__file__))
            db = DatabaseManager(script_dir + '/../ram_info.db')
            ram_info = RAMDataManager.ram_data()
            db.insert_ram_data(ram_info)
        except Exception as e:
            return e
    @staticmethod
    def get_ram_data(n):
        db = DatabaseManager('ram_info.db')
        return db.get_last_n_entries(n)    