import sys, json
from psycopg2 import connect, Error

with open('postgres-records.json') as json_data:

    # use load() rather than loads() for JSON files
    record_list = json.load(json_data)

    for i in record_list:

        table_name = i
        sql_string = ''
        data_table = record_list[table_name]

        if type(data_table) == dict:
            fields = []
            data = ''
            for x, y in data_table.items():
                fields.append(x)
                data = data + "\'" + y + "\',"

            data = data[:-1]
            table_name = i
            sql_string = 'INSERT INTO {} ({}) VALUES ({}); '.format(table_name, ','.join(fields), data)

            try:
                # declare a new PostgreSQL connection object
                conn = connect(
                    dbname = "campers4",
                    user = "postgres",
                    host = "localhost",
                    password = "oSaka_2019",
                    # attempt to connect for 3 seconds then raise exception
                    connect_timeout = 3)

                cur = conn.cursor()
                print("\ncreated cursor object:", cur)

            except (Exception, Error) as err:
                print("\npsycopg2 connect error:", err)
                conn = None
                cur = None

            if cur != None:
               try:
                   cur.execute(sql_string)
                   conn.commit()

                   print('\nfinished INSERT INTO execution')

               except (Exception, Error) as error:
                    print("\nexecute_sql() error:", error)
                    conn.rollback()

                    # close the cursor and connection
            cur.close()
            conn.close()
        else:
            for r in data_table:
                print(type(r))
                fields = []
                data = ''
                for x, y in r.items():
                    fields.append(x)
                    data = data + "\'" + y + "\',"

                data = data[:-1]
                table_name = i
                sql_string = 'INSERT INTO {} ({}) VALUES ({}); '.format(table_name, ','.join(fields), data)

                try:
                    # declare a new PostgreSQL connection object
                    conn = connect(
                        dbname="campers4",
                        user="postgres",
                        host="localhost",
                        password="oSaka_2019",
                        # attempt to connect for 3 seconds then raise exception
                        connect_timeout=3)

                    cur = conn.cursor()
                    print("\ncreated cursor object:", cur)

                except (Exception, Error) as err:
                    print("\npsycopg2 connect error:", err)
                    conn = None
                    cur = None

                if cur != None:

                    try:
                        cur.execute(sql_string)
                        conn.commit()

                        print('\nfinished INSERT INTO execution')

                    except (Exception, Error) as error:
                        print("\nexecute_sql() error:", error)
                        conn.rollback()

                        # close the cursor and connection
                cur.close()
                conn.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
