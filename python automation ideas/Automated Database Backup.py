import subprocess
import datetime

def backup_database(db_name, db_user, db_password, backup_dir):
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    backup_file = f"{backup_dir}/{db_name}_backup_{timestamp}.sql"
    subprocess.run([
        "pg_dump", 
        f"--dbname=postgresql://{db_user}:{db_password}@localhost/{db_name}",
        "--file", backup_file
    ])
    print(f"Database backup completed: {backup_file}")

if __name__ == "__main__":
    backup_database("mydatabase", "dbuser", "dbpassword", "/path/to/backup/dir")
