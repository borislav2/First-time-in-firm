import datetime

def main():
    currentTime=datetime.datetime.now()
    print(currentTime.strftime('%A %d %B %Y %H:%M.%S'))

if __name__ == "__main__":
    main()
