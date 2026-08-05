class AgeError(Exception):
    pass

def check_age(age):
    if not isinstance(age, int):
        raise TypeError("年龄必须是整数")
    if age < 0 or age > 150:
        raise AgeError("年龄超出合理范围（0-150）")

try:
    check_age(200)
except AgeError as e:
    print(f"捕获自定义异常: {e}")
except TypeError as e:
    print(f"捕获类型错误: {e}")
else:
    print("验证通过，年龄合法")
finally:
    print("finally 块总是执行（常用于释放资源）")