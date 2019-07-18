from time import sleep, ctime
import threading


class MyThread(threading.Thread):

    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)


def super_player(file, time):
    for i in range(2):
        print('Start playing： %s! %s' % (file, ctime()))
        sleep(time)


media_list = {'Love.mp3': 3, 'IronMan.mp4': 5, 'You.mp3': 4, 'Me.mp4': 4}


def play():
    # 播放的文件与播放时长
    threads = []
    count_list = range(len(media_list))
    # 创建线程
    for file, time in media_list.items():
        t = threading.Thread(target=super_player, args=(file, time))
        threads.append(t)
    # 启动线程
    for i in count_list:
        threads[i].start()
    for j in count_list:
        threads[j].join()
    # 主线程
    print('end:%s' % ctime())


def play_thread_class():
    # 播放的文件与播放时长
    threads = []
    count_list = range(len(media_list))
    for k, v in media_list.items():
        t = MyThread(super_player, (k, v), super_player.__name__)
        threads.append(t)
    # 启动线程
    for i in count_list:
        threads[i].start()
    for j in count_list:
        threads[j].join()

    # 主线程
    print('end:%s' % ctime())


if __name__ == '__main__':
    # play()
    # play_thread_class()
    a = 'ssss.png'
    b = a.replace('png', 'json')
    print(b)
