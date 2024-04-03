#    author details for techsupport:
#        - Name: joe
#        - Email: joetkk@outlook.my
#        - Contact: 016-2010402
#        - Date: 2024-03-06

import json
import datetime
import signal
import http
from datetime import timedelta
from typing import Tuple, List, Dict
from http.server import HTTPServer, BaseHTTPRequestHandler
from api.database import write_db
from api.errorhandler import handle_error
from api.writejson import write_json

class ValidRequestHandler(http.server.BaseHTTPRequestHandler):
    supported_methods = ('POST')

    def handle_one_request(self):
        try:
            self.raw_requestline = self.rfile.readline(65537)
            if not self.raw_requestline:
               return None
            if self.parse_request():
                self.do_POST()
        except ConnectionResetError:
            pass
        except Exception:
            # Handle any other unexpected exceptions
            self.send_response(500, "Internal Server Error")
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Error: Unexpected error occurred")
            handle_error(self, 500, "500 Internal Server Error")
        finally:
            # Close the connection
            self.close_connection = True
            self.wfile.flush()
            self.request.close()
        return None

    def do_POST(self):
        #print(self.headers)
        
        if self.request_version != 'HTTP/1.1':
            self.send_error(400, 'Unsupported HTTP version')
            handle_error(self, 400, '400 Unsupported HTTP version')
            return

        if self.command != 'POST':
            self.send_error(405, 'Method Not Allowed')
            handle_error(self, 405, '405 Method Not Allowed')
            return        
          
        try:
            req_datas = self.rfile.read(int(self.headers['content-length']))
            json_obj = json.loads(req_datas.decode())
            inner_json = json.loads(json_obj["content"])
            #using for loop with zip(), and range() functions
            for _, key in zip(range(1), json_obj):
                try:
                    if key == "content":
                        self.send_response(200) # Set the initial response code to 200
                        self.send_header('Content-type', 'application/json')
                        self.end_headers()
                        file_path = write_json(json_obj)
                        self.wfile.write(json.dumps({"file_path": file_path}).encode('utf-8'))

                        # Extract the required information
                        alive_type = inner_json["aliveType"]
                        dep_name_concat = inner_json["depNameConcat"]
                        device_key = inner_json["deviceKey"]
                        device_name = inner_json["deviceName"]
                        emp_no = inner_json["empNo"]
                        id_ = inner_json["id"]
                        name = inner_json["name"]
                        org_id = inner_json["orgId"]
                        pass_time_type = inner_json["passTimeType"]
                        permission_time_type = inner_json["permissionTimeType"]
                        person_id = inner_json["personId"]
                        person_type = inner_json["personType"]
                        photo_url = inner_json["photoUrl"]
                        rec_mode = inner_json["recMode"]
                        rec_status = inner_json["recStatus"]
                        rec_type = inner_json["recType"]
                        show_time = inner_json["showTime"]
                        temperature = inner_json["temperature"]
                        temperature_state = inner_json["temperatureState"]
                        temperature_unit = inner_json["temperatureUnit"]
                        type_ = inner_json["type"]

                        # Convert timezone from Amazon to GMT+8
                        time_GMT8 = datetime.datetime.strptime(show_time, '%Y-%m-%d %H:%M:%S') + timedelta(hours=8)
                        result_time_GMT8 = time_GMT8.strftime('%Y-%m-%d %H:%M:%S')

                        # Encap into database data connection
                        db_data = (str(alive_type), dep_name_concat, device_key, device_name, emp_no, str(id_), name, str(org_id), str(pass_time_type), str(permission_time_type), str(person_id), str(person_type), photo_url, str(rec_mode), str(rec_status), str(rec_type), result_time_GMT8, str(temperature), str(temperature_state), str(temperature_unit), str(type_))
                        write_db(db_data)
                        return True
                except ConnectionResetError:
                    pass
                except json.JSONDecodeError:
                    # Handle the case where the request data is not valid JSON
                    self.send_response(400, "Bad Request")
                    self.send_header("Content-type", "text/plain; charset=utf-8")
                    self.end_headers()
                    self.wfile.write(b"Error: Request data is not valid JSON")
                    handle_error(self, 400, "Bad Request - 400")
                except Exception:
                    # Handle any other unexpected exceptions
                    self.send_response(500, "Internal Server Error")
                    self.send_header("Content-type", "text/plain; charset=utf-8")
                    self.end_headers()
                    self.wfile.write(b"Error: Unexpected error occurred")
                    handle_error(self, 500, "Internal Server Error - 500")
        except ConnectionResetError:
            pass
        except json.JSONDecodeError:
            # Handle the case where the request data is not valid JSON
            self.send_response(400, "Bad Request")
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Error: Request data is not valid JSON")
            handle_error(self, 400, "Bad Request 400")
        except Exception:
            # Handle any other unexpected exceptions
            self.send_response(500, "Internal Server Error")
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Error: Unexpected error occurred")
            handle_error(self, 500, "Internal Server Error 500")        

def run_server(server_class=HTTPServer, handler_class=ValidRequestHandler):
    host = ('', 8010)
    server = server_class(host, handler_class)
    print("Starting Ustar API server, listening at: %s:%s" % host)
    print("You may minimize the terminal, please do not close this program.")
    server.serve_forever()

def signal_handler(signal, frame):
    print("Shutting down the server...")
    server.server_close()

if __name__ == '__main__':
    signal.signal(signal.SIGTERM, signal_handler)
    run_server()


