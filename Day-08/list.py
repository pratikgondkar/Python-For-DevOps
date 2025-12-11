servers = ["app-server-1", "app-server-2", "db-server-1", "cache-server-1"]

add_web_server = servers.append("web-server-1")
print(servers)

remove_app_server = servers.remove("app-server-2")
print(servers)

servers.sort()
print(servers)

print(len(servers))