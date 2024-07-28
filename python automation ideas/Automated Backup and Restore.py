import os
import subprocess
from datetime import datetime

# Backup database
def backup_database():
    backup_dir = "/path/to/backup"
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    backup_file = f"{backup_dir}/db_backup_{timestamp}.sql"
    subprocess.run(["pg_dump", "dbname", "-U", "username", "-f", backup_file])
    print(f"Backup completed: {backup_file}")

# Restore database
def restore_database(backup_file):
    subprocess.run(["psql", "dbname", "-U", "username", "-f", backup_file])
    print(f"Restore completed: {backup_file}")

if __name__ == "__main__":
    backup_database()
