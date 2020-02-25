import time


def printer(text, delay=0.2):
    """
    打字机效果
    """
    for i in text:
        print(i, end='', flush=True)
        time.sleep(delay)


printer('玄铁重剑，是金庸小说笔下第一神剑，持之则无敌于天下')
print('\n')


def waiting(cycle=20, delay=0.1):
    """
    旋转式进度指示
    """

    for i in range(cycle):
        for j in ['--', '\\', '|', '/']:
            print('\b%s' % j, end='', flush=True)
            time.sleep(delay)


waiting()

print('\n')


def cover(cycle=100, delay=0.2):
    """覆盖式打印效果"""
    for i in range(cycle):
        s = '\r%d' % i
        print(s.ljust(3), end='', flush=True)
        time.sleep(delay)


cover()
