import db_conn

if __name__ == '__main__':
    print("School management System")
    print("*" * 100)

    database = "students.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS students (
                                       id integer PRIMARY KEY ,
                                       name text NOT NULL,
                                       age text,
                                       class_ text
                                   ); """

    # create a database connection
    conn = db_conn.create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        db_conn.create_table(conn, sql_create_projects_table)


    else:
        print("Error! cannot create the database connection.")

    id = 0
    while True:
        name = input("Enter name:")
        age = input("Enter age:")
        class_name = input("Enter class name:")
        id += 1
        inserted_data = (id, name, age, class_name)
        # insert data
        db_conn.insert_student_data(conn, inserted_data)

        if input("Do you want to add more data:").strip().lower() != "yes":
            conn.close()
            break
