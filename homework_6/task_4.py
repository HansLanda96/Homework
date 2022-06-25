from datetime import datetime


def countdown(function):
    from time import sleep

    def wrap(*args, **kwargs):
        for sec in range(3, 0, -1):
            print(sec)
            sleep(1)
        function(*args, **kwargs)
    return wrap


@countdown
def actual_time():
    time = datetime.now().strftime('%H:%M')
    print(time)


if __name__ == '__main__':
    actual_time()

