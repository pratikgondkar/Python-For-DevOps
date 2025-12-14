import sys
import os

env = sys.argv[1]
admin_email = os.getenv("ADMIN_EMAIL")

servers = ["nginx", "apache", "docker", "jenkins"]

for server in servers:
    if server == "docker":
        print("Container service found")
    else:
        print(f"Service running: {server}")

if env == "prod":
    print("⚠ Production deployment")
else:
    print("Non-production deployment")

print("\n--- Summary ---")
print(f"Environment : {env}")
print(f"Admin Email : {admin_email}")
print(f"Total Servers : {len(servers)}")
