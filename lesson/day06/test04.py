from time import time, localtime, sleep


class Clock:

    def __init__(self, hour=0, minute=0, second=0):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour,ctime.tm_min,ctime.tm_sec)

    def run(self):
        self.__second +=1
        if self.__second == 60:
            self.__second =0
            self.__minute +=1
            if self.__minute == 60:
                self.__minute =0
                self.__hour += 1
                if self.__hour == 24:
                    self.__hour = 0

    def show(self):

        return '%02d:%02d:%02d' % \
               (self.__hour,self.__minute,self.__second)


def main():
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()

if __name__ == '__main__':
    main()
