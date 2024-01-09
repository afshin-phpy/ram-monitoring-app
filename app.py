from fastapi import FastAPI
from api.RAMDataManager import RAMDataManager

app = FastAPI()

@app.get("/ram_info/{n}")
def get_ram_info(n: int):
    return RAMDataManager.get_ram_data(n)