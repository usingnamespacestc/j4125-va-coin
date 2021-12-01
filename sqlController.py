import pymysql
from dateutil.parser import parse

host = 'localhost'
user = 'coin'
password = 'NAjCKHBMFGTKJjEy'
database = 'coin'


def test_connection():
    # 打开数据库连接
    db = pymysql.connect(host=host,
                         user=user,
                         password=password,
                         database=database)

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT VERSION()")

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()

    print("Database version : %s " % data)

    # 关闭数据库连接
    db.close()


def execute_sql(sql_list):
    # 打开数据库连接
    db = pymysql.connect(host=host,
                         user=user,
                         password=password,
                         database=database)

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    try:
        for sql in sql_list:
            # 执行sql语句
            sql = sql.replace("None", "NULL")
            cursor.execute(sql)
            db.commit()
    except pymysql.Error as e:
        # 输出异常信息
        print(e.args)
        # 发生错误时回滚
        db.rollback()

    # 关闭数据库连接
    db.close()


def update_data(coin_data):
    # print(coin_data)
    sql_list = []
    for single_coin_data in coin_data:
        id = str(coin_data[single_coin_data]['id'])
        name = coin_data[single_coin_data]['name']
        symbol = coin_data[single_coin_data]['symbol']
        num_market_pairs = str(coin_data[single_coin_data]['num_market_pairs'])
        date_added = str(parse(coin_data[single_coin_data]['date_added']).timestamp())
        max_supply = str(coin_data[single_coin_data]['max_supply'])
        circulating_supply = str(coin_data[single_coin_data]['circulating_supply'])
        total_supply = str(coin_data[single_coin_data]['total_supply'])
        last_updated = str(parse(coin_data[single_coin_data]['last_updated']).timestamp())
        sql_list.append("INSERT INTO crypto(" +
                        "_id," +
                        "_name," +
                        "_symbol," +
                        "_num_market_pairs," +
                        "_date_added," +
                        "_max_supply," +
                        "_circulating_supply," +
                        "_total_supply," +
                        "_last_updated" +
                        ") " +
                        "VALUES(" +
                        id + "," +
                        "'" + name + "'" + "," +
                        "'" + symbol + "'" + "," +
                        num_market_pairs + "," +
                        date_added + "," +
                        max_supply + "," +
                        circulating_supply + "," +
                        total_supply + "," +
                        last_updated +
                        ") " +
                        "ON DUPLICATE KEY UPDATE " +
                        "_name=" + "'" + name + "'" + "," +
                        "_symbol=" + "'" + symbol + "'" + "," +
                        "_num_market_pairs=" + num_market_pairs + "," +
                        "_date_added=" + date_added + "," +
                        "_max_supply=" + max_supply + "," +
                        "_circulating_supply=" + circulating_supply + "," +
                        "_total_supply=" + total_supply + "," +
                        "_last_updated=" + last_updated +
                        ";"
        )
        quote = coin_data[single_coin_data]['quote']
        # print(quote)
    execute_sql(sql_list)


if __name__ == '__main__':
    # test_connection()
    # test_sql = ["INSERT INTO test VALUES(1, "
    #             "2, "
    #             "3, "
    #             "4) "
    #             "ON DUPLICATE KEY UPDATE "
    #             "_int = 67, "
    #             "_bigint = 35234143151, "
    #             "_timestamp = 1367107200.0;"]
    # test_ql = "drop table test"
    # test_sql = [
    #     "INSERT INTO crypto(_id,_name,_symbol,_num_market_pairs,_date_added,_max_supply,_circulating_supply,_total_supply,_last_updated) VALUES(1027,'Ethereum','ETH',4671,1438905600.0,None,118554060.3115,118554060.3115,1638308468.0) ON DUPLICATE KEY UPDATE _name='Ethereum',_symbol='ETH',_num_market_pairs=4671,_date_added=1438905600.0,_max_supply=None,_circulating_supply=118554060.3115,_total_supply=118554060.3115,_last_updated=1638308468.0;"]
    execute_sql(test_sql)
