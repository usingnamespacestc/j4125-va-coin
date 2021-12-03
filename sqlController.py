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
    output = []
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
            output = cursor.fetchall()
    except pymysql.Error as e:
        # 输出异常信息
        print(e.args)
        # 发生错误时回滚
        db.rollback()

    # 关闭数据库连接
    db.close()

    return output


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
        quote = coin_data[single_coin_data]['quote']
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
        for single_quote in quote:
            find_sql = []
            crypto_id = id
            price = str(quote[single_quote]["price"])
            volume_24h = str(quote[single_quote]["volume_24h"])
            volume_change_24h = str(quote[single_quote]["volume_change_24h"])
            percent_change_1h = str(quote[single_quote]["percent_change_1h"])
            percent_change_24h = str(quote[single_quote]["percent_change_24h"])
            percent_change_7d = str(quote[single_quote]["percent_change_7d"])
            percent_change_30d = str(quote[single_quote]["percent_change_30d"])
            percent_change_60d = str(quote[single_quote]["percent_change_60d"])
            percent_change_90d = str(quote[single_quote]["percent_change_90d"])
            market_cap = str(quote[single_quote]["market_cap"])
            market_cap_dominance = str(quote[single_quote]["market_cap_dominance"])
            fully_diluted_market_cap = str(quote[single_quote]["fully_diluted_market_cap"])
            quote_last_updated = str(parse(quote[single_quote]["last_updated"]).timestamp())
            sql_string = "SELECT * FROM quote WHERE _crypto_id = "+crypto_id + " and _last_updated = "+quote_last_updated
            find_sql.append(sql_string)
            if(len(execute_sql(find_sql)) != 0):
                print("exists")
            else:
                print("not exists")
                sql_list.append("INSERT INTO quote(" +
                           "_crypto_id," +
                           "_price," +
                           "_volume_24h," +
                           "_volume_change_24h," +
                           "_percent_change_1h," +
                           "_percent_change_24h," +
                           "_percent_change_7d," +
                           "_percent_change_30d," +
                           "_percent_change_60d," +
                           "_percent_change_90d," +
                           "_market_cap," +
                           "_market_cap_dominance," +
                           "_fully_diluted_market_cap," +
                           "_last_updated" +
                           ") " +
                           "VALUES(" +
                           crypto_id + "," +
                           price + "," +
                           volume_24h + "," +
                           volume_change_24h + "," +
                           percent_change_1h + "," +
                           percent_change_24h + "," +
                           percent_change_7d + "," +
                           percent_change_30d + "," +
                           percent_change_60d + "," +
                           percent_change_90d + "," +
                           market_cap + "," +
                           market_cap_dominance + "," +
                           fully_diluted_market_cap + "," +
                           quote_last_updated + ")")
    execute_sql(sql_list)


def get_crypto_list():
    sql = 'select _name, _symbol from crypto order by _name'
    return execute_sql([sql])


def get_latest_price(symbol):
    sql = 'select _last_updated, _price from quote ' \
          'where _crypto_id = (select _id from crypto ' \
          'where _symbol = "' + symbol + '") ' \
          'order by _last_updated desc limit 1'
    return execute_sql([sql])[0]


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

    test_sql = ["select * from quote"]
    print(len(execute_sql(test_sql)))
    for one in execute_sql(test_sql):
        print(one)


