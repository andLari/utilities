import requests
import socket
import platform

def get_system_info():
    info = {
        "hostname": socket.gethostname(),
        "ip_address": socket.gethostbyname(socket.gethostname()),
        "platform": platform.system(),
        "platform_release": platform.release(),
        "platform_version": platform.version(),
        "architecture": platform.machine(),
        "processor": platform.processor()
    }
    return info

def notify_server(info):
    url = "http://127.0.0.1:5000/notify"
    try:
        response = requests.post(url, json=info)
        if response.status_code == 200:
            print("Notification sent successfully")
        else:
            print("Failed to send notification, status code:", response.status_code)
    except Exception as e:
        print("Failed to send notification:", e)

if __name__ == "__main__":
    system_info = get_system_info()
    notify_server(system_info)
    print("Script has been executed!")
