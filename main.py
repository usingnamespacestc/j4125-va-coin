import dataGrabber
import sqlController

if __name__ == '__main__':
    coin_data = dataGrabber.grab_data()
    sql_list = sqlController.update_data(coin_data)
    #sqlController.execute_sql(sql_list)
