from netmiko import ConnectHandler

# Bemeneti adatok bekérése
device_ip = input("Hálózati eszköz IP: ")
username = input("Felhasználónév: ")
password = input("Jelszó: ")

# Eszköz paramétereinek beállítása
device = {
    "device_type": "cisco_ios",
    "host": device_ip,
    "username": username,
    "password": password,
}

try:
    connection = ConnectHandler(**device)
    
    hostname = connection.find_prompt().strip("#> ")

    config = connection.send_command("show running-config")

    filename = f"{hostname}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(config)

    print(f"A konfiguráció mentve: {filename}")

    connection.disconnect()

except Exception as e:
    print(f"Hiba történt: {e}")
