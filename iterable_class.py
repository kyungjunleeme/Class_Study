class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self  # iterator를 요구 받고, 현 instance에서 next 처리

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration  # 남은 요소가 없을 때, StopIteration 강제 발생 # StopIteration은 for ~ in 구문에서 잡아서 해결해줌
        value = self.start
        self.start += 1
        return value  # 다음 요소를 return


if __name__ == "__main__":
    myrange = MyRange(0, 3)
    # for ~ in 구문이 해주는 걸 하나씩 해봄
    iterator = iter(myrange)  # myrange.__iter__() 와 같은 효과임
    print(iterator)  # <__main__.MyRange object at 0x10fe6c310>
    print(next(iterator))  # myrange.__next__()가 호출되는 것임
    print(next(iterator))  # myrange.__next__()가 호출되는 것임
    print(next(iterator))  # myrange.__next__()가 호출되는 것임
    print(next(iterator))  # StopIteration 발생

    # 0, 1, 2 일련의 작업이 한 번에 실행 됨
    # myrange2 = MyRange(0, 3)
    # for i in myrange2:
    #     print(i)
