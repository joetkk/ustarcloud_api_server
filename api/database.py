#    Author details for techsupport:
#        - Name: joe
#        - Email: joetkk@outlook.my
#        - Contact: 016-2010402
#        - Date: 2024-03-06
import mysql.connector
import logging
from api.errorhandler import handle_error
from api.errorlog import write_errorlog
from typing import Tuple, List, Dict


def write_db(db_data: Tuple):
    try:
        # Establish the connection
        cnx = mysql.connector.connect(
            host="127.0.0.1",
            port=5525,
            user="root",
            password="root",
            database="ustarcloud"
        )

        cursor = cnx.cursor()

        # Check that the number of values in db_data matches the number of columns in the query
        if len(db_data) != 21:
            print("Unexpected number of values in db_data tuple")

        # Check that the order of the values in db_data matches the order of the columns in the query
        if db_data[0] is not None and not isinstance(db_data[0], str):
            print("Unexpected value for column 'alive_type'")
        if db_data[1] is not None and not isinstance(db_data[1], str):
            print("Unexpected value for column 'dep_name_concat'")
        if db_data[2] is not None and not isinstance(db_data[2], str):
            print("Unexpected value for column 'device_key'")
        if db_data[3] is not None and not isinstance(db_data[3], str):
            print("Unexpected value for column 'device_name'")
        if db_data[4] is not None and not isinstance(db_data[4], str):
            print("Unexpected value for column 'emp_no'")
        if db_data[5] is not None and not isinstance(db_data[5], str):
            print("Unexpected value for column 'id_'")
        if db_data[6] is not None and not isinstance(db_data[6], str):
            print("Unexpected value for column 'name'")
        if db_data[7] is not None and not isinstance(db_data[7], str):
            print("Unexpected value for column 'org_id'")
        if db_data[8] is not None and not isinstance(db_data[8], (str)):
            print("Unexpected value for column 'pass_time_type'")
        if db_data[9] is not None and not isinstance(db_data[9], (str)):
            print("Unexpected value for column 'permission_time_type'")        
        if db_data[10] is not None and not isinstance(db_data[10], str):
            print("Unexpected value for column 'person_id'")
        if db_data[11] is not None and not isinstance(db_data[11], str):
            print("Unexpected value for column 'person_type'")
        if db_data[12] is not None and not isinstance(db_data[12], str):
            print("Unexpected value for column 'photo_url'")
        if db_data[13] is not None and not isinstance(db_data[13], str):
            print("Unexpected value for column 'rec_mode'")
        if db_data[14] is not None and not isinstance(db_data[14], str):
            print("Unexpected value for column 'rec_status'")
        if db_data[15] is not None and not isinstance(db_data[15], str):
            print("Unexpected value for column 'rec_type'")
        if db_data[16] is not None and not isinstance(db_data[16], str):
            print("Unexpected value for column 'result_time_GMT8'")
        if db_data[17] is not None and not isinstance(db_data[17], str):
            print("Unexpected value for column 'temperature'")
        if db_data[18] is not None and not isinstance(db_data[18], (str)):
            print("Unexpected value for column 'temperature_state'")
        if db_data[19] is not None and not isinstance(db_data[19], str):
            print("Unexpected value for column 'temperature_unit'")
        if db_data[20] is not None and not isinstance(db_data[20], str):
            print("Unexpected value for column 'type_'")            


        # SQL query string
        query = """
            INSERT INTO ustarcloud.tbl_ustarcloud (alive_type, dep_name_concat, device_key, device_name, emp_no, id_, name, org_id, pass_time_type, permission_time_type, person_id, person_type, photo_url, rec_mode, rec_status, rec_type, show_time, temperature, temperature_state, temperature_unit, type_)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Execute the query using execute() method
        try:
            cursor.execute(query, db_data)
        except mysql.connector.Error as message:
            print("Error:", message)
            handle_error(str(message))
        # Commit the transaction
        cnx.commit()

    except mysql.connector.Error as message:
        logging.error(f"Error: {message}")
        handle_error(str(message))
    finally:
        if cnx.is_connected():
            cursor.close()
            cnx.close()
    print("successfully logged to mysql database")