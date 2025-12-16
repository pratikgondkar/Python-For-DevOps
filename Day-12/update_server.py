def update_config(file_path, key, value):
    with open (file_path , 'r') as file:
        lines = file.readlines()

        with open(file_path, 'w') as file:
            for line in lines:
                if key in line:
                    file.write(f"{key} = {value}\n")
                else:
                    file.write(line)

server_config_path = 'server.conf'
key_to_update = 'MAX_CONNECTIONS'
new_value = '200'

update_config(server_config_path, key_to_update, new_value)