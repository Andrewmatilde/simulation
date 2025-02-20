import csv
import mysql.connector

# 读取CSV文件中的所有ID
def read_ids_from_csv(file_path):
    ids = []
    with open(file_path, mode='r', encoding='utf-8-sig') as file:  # 使用 utf-8-sig 去除 BOM
        reader = csv.reader(file)
        for row in reader:
            if not row:  # 跳过空行
                continue
            id_str = row[0].strip()  # 去除首尾空白字符
            try:
                ids.append(int(id_str))
            except ValueError:
                print(f"无法将 {id_str} 转换为整数，已跳过。")
    return ids

# 查询MySQL
def query_mysql(ids):
    # 建立MySQL连接
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=20036,
        user='root',
        password='znUiFjxfpuMFMPgK*-iiK5S9w2HBjLlL',
        database='registry'
    )
    cursor = connection.cursor()

    # 构建查询SQL
    query = f"SELECT * FROM u_project WHERE top_org_id IN ({','.join(map(str, ids))})"
    print(query)
    cursor.execute(query)

    # 获取查询结果
    results = cursor.fetchall()

    # 关闭连接
    cursor.close()
    connection.close()

    return results

# 主程序
if __name__ == '__main__':
    file_path = 'company.csv'
    ids = read_ids_from_csv(file_path)
    results = query_mysql(ids)
    for row in results:
        print(row)
