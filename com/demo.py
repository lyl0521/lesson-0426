import sys


def _fn_private():
    print('This is a private function')


def fn_test():
    print(sys.argv)
    _fn_private()


if __name__ == '__main__':
    fn_test()

