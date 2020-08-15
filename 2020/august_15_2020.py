# import requests
# url = 'http://news.163.com/rank/'
# res = requests.get(url).text
# content = requests.get(url).content
# print(content.decode('gbk'))



'''
查询mysql表
'''
# import pymysql
#
# def mysql_conn():
#     # 新建连接
#     con = pymysql.connect(host='localhost',user='root',password='test',port=3306,database='library')
#     # 定义游标
#     cursor = con.cursor()
#     # 定义mysql查询表的语句
#     sql = 'select * from mytest2'
#     try:
#         # 执行sql语句
#         cursor.execute(sql)
#         result = cursor.fetchall()
#         for data in result:
#             print(data)
#     except Exception:
#         print('查询失败！')
#     finally:
#         # 关闭数据库连接
#         con.close()
#         # 关闭游标
#         cursor.close()
# mysql_conn()


'''
创建mysql表
'''
# import pymysql
#
# def mysql_conn():
#     # 新建连接
#     con = pymysql.connect(host='localhost',user='root',password='test',port=3306,database='library')
#     # 定义游标
#     cursor = con.cursor()
#     # 创建mysql表的语句
#     sql = 'create table mytest2(' \
#           'sno int primary key auto_increment,' \
#           'sname varchar(30) not null,' \
#           'age int(3))'
#     try:
#         # 执行sql语句
#         cursor.execute(sql)
#         print('创建成功')
#     except Exception:
#         print('创建失败！')
#     finally:
#         # 关闭数据库连接
#         con.close()
#         # 关闭游标
#         cursor.close()
# mysql_conn()


'''
mysql表插入单条数据
'''
# import pymysql
#
# def mysql_conn():
#     # 新建连接
#     con = pymysql.connect(host='localhost',user='root',password='test',port=3306,database='library')
#     # 定义游标
#     cursor = con.cursor()
#     # 定义mysql语句，查询表名为mytest的内容p
#     sql = 'insert into mytest2 (sname,age)  values (%s,%s)'
#     try:
#         # 执行sql语句
#         cursor.execute(sql,('康',18))
#         # 提交
#         con.commit()
#         print('插入成功')
#     except Exception:
#         print('插入失败！')
#     finally:
#         # 关闭数据库连接
#         con.close()
#         # 关闭游标
#         cursor.close()
# mysql_conn()

'''
mysql表插入多条数据
'''
# import pymysql
#
# def mysql_conn():
#     # 新建连接
#     con = pymysql.connect(host='localhost',user='root',password='test',port=3306,database='library')
#     # 定义游标
#     cursor = con.cursor()
#     # 定义mysql语句，查询表名为mytest的内容p
#     sql = 'insert into mytest2 (sname,age)  values (%s,%s)'
#     try:
#         # 执行sql语句
#         cursor.executemany(sql,[('康',20),('陈',19),('祝',20)])
#         # 提交
#         con.commit()
#         print('插入成功')
#     except Exception as e:
#         print(e)
#         # 回滚
#         con.rollback()
#         print('插入失败！')
#     finally:
#         # 关闭数据库连接
#         con.close()
#         # 关闭游标
#         cursor.close()
# mysql_conn()

'''
mysql表删除单条数据
'''
# import pymysql
#
# def mysql_conn():
#     # 新建连接
#     con = pymysql.connect(host='localhost',user='root',password='test',port=3306,database='library')
#     # 定义游标
#     cursor = con.cursor()
#     # 定义mysql语句，查询表名为mytest的内容p
#     sql = 'delete from mytest2 where sname=%s'
#     try:
#         # 执行sql语句
#         cursor.execute(sql,('陈'))
#         # 提交
#         con.commit()
#         print('删除成功')
#     except Exception as e:
#         print(e)
#         con.rollback()
#         print('删除失败！')
#     finally:
#         # 关闭数据库连接
#         con.close()
#         # 关闭游标
#         cursor.close()
# mysql_conn()








