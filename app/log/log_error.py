
from datetime import datetime
from file_read_backwards import FileReadBackwards

def log_error(error):
    print(error)
    date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    with open('app/log/log_entries.txt', 'a') as file:
        file.write(str({date:error}) + "\n")


def get_errors():
    with FileReadBackwards('log_entries.txt', encoding='utf-8') as log:
        return log
