import pymysql
def get_data(sql):
    conn = pymysql.connect(host='47.94.243.187', user='root', password='Ab103827', port=3306, db='quanyu')
    cur = conn.cursor()
    try:
        cur.execute(sql)
        #获取表的所有字段名称
        coloumns = [row[0] for row in cur.description]
        result = [[str(item) for item in row] for row in cur.fetchall()]
        return [dict(zip(coloumns, row)) for row in result]
    except Exception:
        conn.rollback()
    finally:
        conn.close()


