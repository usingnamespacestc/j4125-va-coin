import dataGrabber
import sqlController
from fastapi import FastAPI
# from fastapi.responses import JSONResponse
# from fastapi.encoders import jsonable_encoder

app = FastAPI()


@app.get("/get_crypto_list/")
async def get_crypto_list():
    return sqlController.get_crypto_list()


@app.get("/get_latest_price/{symbol}")
async def get_latest_price(symbol=str):
    res = sqlController.get_latest_price(symbol)
    return {"last_updated": res[0], "price": res[1]}


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == '__main__':
    coin_data = dataGrabber.grab_data()
    sql_list = sqlController.update_data(coin_data)
    # sqlController.execute_sql(sql_list)
