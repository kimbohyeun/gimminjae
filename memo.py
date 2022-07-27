print("hello world")
print("진행할 작업을 선택해주세요")
print("1. 메모작업 2.메모읽기")

option = input()

print(option)

if option == '1':
    newmemo = input("메모를 입력해주세요\n")
    print(newmemo)
    filename = memo.txt
    f = open(filename, 'a')
    f.write(newmemo)
    f.colse()
elif option =="2":
    f = open("memo.txt")
    memo = f.read()
    print(type(memo))
    print(memo)
    f.close
else:
    print("잘못 입력 했습니다.")