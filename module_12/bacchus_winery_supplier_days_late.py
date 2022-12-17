import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "root",
    "host": "127.0.0.1",
    "database": "bacchus",
    "raise_on_warnings": True
}
try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"],
                                                                                      config["database"]))
    input("\n\n Press any key to continue. . .")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("   The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("   The specified database does not exist")

    else:
        print(err)

cursor = db.cursor()


def show_sales(cursor, title):
    cursor.execute("""SELECT supplier_name,
SUM(-1 * datediff(expected_delivery_dt,actual_delivery_dt)) as 'Total Days Late',
count(*) as 'Number of Orders'
FROM inbound_orders a LEFT JOIN SUPPLIER b on a.supplier_id = b.supplier_id
GROUP BY supplier_name;""")

    deliveries = cursor.fetchall()

    print("\n      -- {} --".format(title))

    for delivery in deliveries:
        print("==============================================="
              + "\nSupplier Name:       {}\nTotal Days Late:     {}\n# of Orders:         {}".format(delivery[0],
                                                                                                 delivery[1],
                                                                                                 delivery[2],
                                                                                                 ))
    print("===============================================")


show_sales(cursor, " Displaying Delivery Report ")

db.close()
