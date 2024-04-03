#    Author details for techsupport:
#        - Name: Joe Tan
#        - Email: joetkk@outlook.my
#        - Contact: 016-2010402
#        - Date: 2024-03-06
import json
from api.errorlog import write_errorlog

def handle_error(self, status_code, message):
    self.send_response(status_code)
    self.send_header('Content-Type', 'application/json')
    self.end_headers()

    response = {
        'status': 'error',
        'message': message
    }

    self.wfile.write(json.dumps(response).encode())

    # Write the error message to the log file
    write_errorlog(self, message)  # Add this line to call the write_errorlog() function