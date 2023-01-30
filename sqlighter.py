import re
import sqlite3


async def add(item):
    connect = sqlite3.connect('db.db')
    cursor = connect.cursor()
    m = []
    m.append(item)
    cursor.execute('INSERT INTO shop VALUES(?)', m)
    connect.commit()
    cursor.close()


async def algebra():
    connect = sqlite3.connect('db.db')
    cursor = connect.cursor()
    query = 'SELECT Алгебра FROM Предметы'
    cursor.execute(query)
    data = cursor.fetchall()
    m1 = []

    for i in data:
        m1.append(i)

    l1 = len(data)
    g1 = []

    for i in range(l1):
        a1 = re.sub('|\(|\'|\,|\)', '', str(m1[i]))
        g1.append(a1)
    c1 = []

    for i in g1:
        q1 = i + '\n'
        c1.append(q1)

    v1 = '\n'.join(c1)

    return 'Алгебра: ' + v1


async def geometry():
    connect = sqlite3.connect('db.db')
    cursor = connect.cursor()
    query = 'SELECT Геометрия FROM Предметы'
    cursor.execute(query)
    data = cursor.fetchall()
    m2 = []

    for i in data:
        m2.append(i)

    l2 = len(data)
    g2 = []

    for i in range(l2):
        a2 = re.sub('|\(|\'|\,|\)', '', str(m2[i]))
        g2.append(a2)
    c2 = []

    for i in g2:
        q2 = i + '\n'
        c2.append(q2)

    v2 = '\n'.join(c2)

    return 'Геометрия: ' + v2


async def russian():
    connect = sqlite3.connect('db.db')
    cursor = connect.cursor()
    query = 'SELECT Русский FROM Предметы'
    cursor.execute(query)
    data = cursor.fetchall()
    m3 = []

    for i in data:
        m3.append(i)

    l3 = len(data)
    g3 = []

    for i in range(l3):
        a3 = re.sub('|\(|\'|\,|\)', '', str(m3[i]))
        g3.append(a3)
    c3 = []

    for i in g3:
        q3 = i + '\n'
        c3.append(q3)

    v3 = '\n'.join(c3)

    return 'Русский: ' + v3


async def litricher():
    connect = sqlite3.connect('db.db')
    cursor = connect.cursor()
    query = 'SELECT Алгебра FROM Предметы'
    cursor.execute(query)
    data = cursor.fetchall()
    m4 = []

    for i in data:
        m4.append(i)

    l4 = len(data)
    g4 = []

    for i in range(l4):
        a4 = re.sub('|\(|\'|\,|\)', '', str(m4[i]))
        g4.append(a4)
    c4 = []

    for i in g4:
        q4 = i + '\n'
        c4.append(q4)

    v4 = '\n'.join(c4)

    return 'Литература: ' + v4


async def biology():
    connect = sqlite3.connect('db.db')
    cursor = connect.cursor()
    query = 'SELECT Биология FROM Предметы'
    cursor.execute(query)
    data = cursor.fetchall()
    m5 = []

    for i in data:
        m5.append(i)

    l5 = len(data)
    g5 = []

    for i in range(l5):
        a5 = re.sub('|\(|\'|\,|\)', '', str(m5[i]))
        g5.append(a5)
    c5 = []

    for i in g5:
        q5 = i + '\n'
        c5.append(q5)

    v5 = '\n'.join(c5)

    return 'Биология: ' + v5


async def geography():
    connect = sqlite3.connect('db.db')
    cursor = connect.cursor()
    query = 'SELECT География FROM Предметы'
    cursor.execute(query)
    data = cursor.fetchall()
    m6 = []

    for i in data:
        m6.append(i)

    l6 = len(data)
    g6 = []

    for i in range(l6):
        a6 = re.sub('|\(|\'|\,|\)', '', str(m6[i]))
        g6.append(a6)
    c6 = []

    for i in g6:
        q6 = i + '\n'
        c6.append(q6)

    v6 = '\n'.join(c6)

    return 'География: ' + v6


async def history():
    connect = sqlite3.connect('db.db')
    cursor = connect.cursor()
    query = 'SELECT История FROM Предметы'
    cursor.execute(query)
    data = cursor.fetchall()
    m7 = []

    for i in data:
        m7.append(i)

    l7 = len(data)
    g7 = []

    for i in range(l7):
        a7 = re.sub('|\(|\'|\,|\)', '', str(m7[i]))
        g7.append(a7)
    c7 = []

    for i in g7:
        q7 = i + '\n'
        c7.append(q7)

    v7 = '\n'.join(c7)

    return 'История: ' + v7


async def obshyestvoznanie():
    connect = sqlite3.connect('db.db')
    cursor = connect.cursor()
    query = 'SELECT Обществознание FROM Предметы'
    cursor.execute(query)
    data = cursor.fetchall()
    m8 = []

    for i in data:
        m8.append(i)

    l8 = len(data)
    g8 = []

    for i in range(l8):
        a8 = re.sub('|\(|\'|\,|\)', '', str(m8[i]))
        g8.append(a8)
    c8 = []

    for i in g8:
        q8 = i + '\n'
        c8.append(q8)

    v8 = '\n'.join(c8)

    return 'Обществознание: ' + v8


async def informatic():
    connect = sqlite3.connect('db.db')
    cursor = connect.cursor()
    query = 'SELECT Информатика FROM Предметы'
    cursor.execute(query)
    data = cursor.fetchall()
    m9 = []

    for i in data:
        m9.append(i)

    l9 = len(data)
    g9 = []

    for i in range(l9):
        a9 = re.sub('|\(|\'|\,|\)', '', str(m9[i]))
        g9.append(a9)
    c9 = []

    for i in g9:
        q9 = i + '\n'
        c9.append(q9)

    v9 = '\n'.join(c9)

    return 'Информатика: ' + v9


async def english():
    connect = sqlite3.connect('db.db')
    cursor = connect.cursor()
    query = 'SELECT Английский FROM Предметы'
    cursor.execute(query)
    data = cursor.fetchall()
    m10 = []

    for i in data:
        m10.append(i)

    l10 = len(data)
    g10 = []

    for i in range(l10):
        a10 = re.sub('|\(|\'|\,|\)', '', str(m10[i]))
        g10.append(a10)
    c10 = []

    for i in g10:
        q10 = i + '\n'
        c10.append(q10)

    v10 = '\n'.join(c10)

    return 'Английский: ' + v10


async def fisics():
    connect = sqlite3.connect('db.db')
    cursor = connect.cursor()
    query = 'SELECT Физика FROM Предметы'
    cursor.execute(query)
    data = cursor.fetchall()
    m11 = []

    for i in data:
        m11.append(i)

    l11 = len(data)
    g11 = []

    for i in range(l11):
        a11 = re.sub('|\(|\'|\,|\)', '', str(m11[i]))
        g11.append(a11)
    c11 = []

    for i in g11:
        q11 = i + '\n'
        c11.append(q11)

    v11 = '\n'.join(c11)

    return 'Физика: ' + v11


async def chemistry():
    connect = sqlite3.connect('db.db')
    cursor = connect.cursor()
    query = 'SELECT Химия FROM Предметы'
    cursor.execute(query)
    data = cursor.fetchall()
    m12 = []

    for i in data:
        m12.append(i)

    l12 = len(data)
    g12 = []

    for i in range(l12):
        a12 = re.sub('|\(|\'|\,|\)', '', str(m12[i]))
        g12.append(a12)
    c12 = []

    for i in g12:
        q12 = i + '\n'
        c12.append(q12)

    v12 = '\n'.join(c12)

    return 'Химия: ' + v12


async def total():
    connect = sqlite3.connect('db.db')
    cursor = connect.cursor()
    cursor.fetchall()
    return 'Алгебра: ' + algebra.v1 + '\n' + 'Геометрия: ' + geometry.v2

# # async def db_start():
# #     global db, cur
# #
# #     db = sq.connect('new.db')
# #     cur = db.cursor()
# #
# #     cur.execute('CREATE TABLE IF NOT EXISTS profile(user_id TEXT PRIMARY KEY, photo, age, description, name)')
# #     db.commit()
# #
# # async def create_profile()
#
# class SQLighter:
#     def __init__(self, database_file):
#         """Подключаемся к БД и сохраняем курсор соединения"""
#         self.connection = sqlite3.connect(database='')
#         self.cursor = self.connection.cursor()
#
#     def get_subscriptions(self, status =True):
#         """Получаем всех активных подписчиков бота"""
#         with self.connection:
#             return self.cursor.execute("SELECT * FROM 'subscriptions' WHERE 'status' = ?", (status,)).fetchall()
#
#     def subscriber_exists(self, user_id):
#         """Проверяем есть ли уже юзер в базе"""
#         with self.connection:
#             result = self.cursor.execute("SELECT * FROM 'subscriptions' WHERE 'user_id' = ?", (user_id,)).fetchall()
#             return bool(len(result))
#
#     def add_subscriber(self, user_id, status=True):
#         """Добавлям нового подписчика"""
#         with self.connection:
#             return self.cursor.execute("INSERT INTO 'subscriptions' ('user_id', 'status') VALUES (?,?)",
#                                        (user_id, status))
#
#     def update_subscription(self, user_id, status):
#         """Обновляем статус подписки"""
#         return self.cursor.execute("UPDATE 'subscriptions' SET 'status' = ? WHERE 'user_id' = ?", (status, user_id))
#
#     def close(self):
#         """Закрываем соединение с БД"""
#         self.connection.close()
