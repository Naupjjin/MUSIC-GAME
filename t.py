import time

class MillisecondTimer:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        if self.start_time is None:
            raise ValueError("Timer has not been started.")
        elapsed_time = (time.time() - self.start_time) * 1000  # 转换为毫秒
        self.start_time = None
        return elapsed_time

# 使用示例
timer = MillisecondTimer()

timer.start()
# 执行一些操作
time.sleep(2)
elapsed_time = timer.stop()

print(f"Elapsed time: {elapsed_time:.2f} milliseconds")
