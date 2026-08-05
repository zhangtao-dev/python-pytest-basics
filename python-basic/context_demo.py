class MyOpen:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"[__enter__] 打开文件 {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"[__exit__] 关闭文件 {self.filename}")
        if self.file:
            self.file.close()
        return False  

with MyOpen("test.txt", "w") as f:
    f.write("Hello, Context Manager!")

print("文件写入完成，已自动关闭。")