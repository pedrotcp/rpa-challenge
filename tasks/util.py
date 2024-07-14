import socket
from robocorp import log

def check_work_items(workitems):
    """
        Checks if payload is available and all the required parameters are present inside it
    """

    required_keys = ['search_term','category','months']
    
    for item in workitems.inputs:
        if not item.payload:
            raise ValueError("Work Items payload not available.")

        for key in required_keys:
            if key not in item.payload:
                raise ValueError(f"Input Work Item is missing key: '{key}'")
    
    log.info("Work Item payloads checked.")


def check_connection():
    """
        Quick and dirty method of checking if connection is available. Connects via socket to Google's DNS server.
        Should really only be useful for when the robot runs locally. 
        If somehow connection is offline while running with Control Room, this is the least of our problems. 
    """
    try:
        socket.setdefaulttimeout(5)
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(("8.8.8.8",53))
        s.close()
        log.info("Internet connection available.")
    except Exception as e:
        log.critical("No internet connection.")
        raise ConnectionError("Connection offline.")