class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        val = self.current
        self.current += 1
        return val

def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    print("自定义迭代器 Counter(1,5)：", list(Counter(1, 5)))
    print("斐波那契生成器（小于10）：", list(fibonacci(10)))