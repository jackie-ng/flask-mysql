import mysql.connector
from flask import jsonify

# Configuration

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "todo_flask"
}

def get_data():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)  # Use dictionary cursor to return rows as dictionaries
    try:
        get_data_query = 'SELECT * from todolist'

        cursor.execute(get_data_query)
        data = cursor.fetchall()

        result = {
            "header": {"status": "success", "message": "Data retrieved successfully"},
            "data": data
        }

        return result["data"]

    except mysql.connector.Error as err:
        error_result = {
            "header": {"status": "error", "message": f"Error: {err}"},
            "data": None
        }
        return jsonify(error_result)

    finally:
        cursor.close()
        connection.close()

def insert_data(data):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    try:
        insert_data_query = "INSERT INTO todolist (task_name, completed) VALUES (%s, %s)"
        users_data = (data['task_name'], data['completed'])

        cursor.execute(insert_data_query, users_data)

        connection.commit()

        print('+++++++++ Data added successfully ++++++++++')

        # EXTRA _ REMOVE IN CASE OF ANY ERRORS
        last_inserted_id = cursor.lastrowid

        return last_inserted_id


    except mysql.connector.Error as err:
        print('f"Error:', err)

    finally:
        cursor.close()
        connection.close()



def delete_data(task_id):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    delete_task_query = 'DELETE FROM todolist WHERE id = %s'

    cursor.execute(delete_task_query, (task_id,))
    connection.commit()
    print('--------- Data has been cleared successfully -------')

def toggle_data(data, task_id):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    completed = data["completed"]
    modify_task_query = 'UPDATE todolist SET completed = %s WHERE id = %s'
    cursor.execute(modify_task_query, (completed, task_id))
    connection.commit()
    print('--------- Data has been updated successfully -------')


