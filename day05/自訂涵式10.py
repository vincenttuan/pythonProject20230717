# 自訂函數: * 與 **
def play_ground(name, age, *person, **ticket) :
    print(name, type(name))
    print(age, type(age))
    print(person, type(person))
    print(ticket, type(ticket))


if __name__ == '__main__':
    play_ground('兒童樂園', 12, '爸爸', '媽媽', '哥哥', '姊姊', 成人=50, 孩童=20)
    play_ground('水上樂園', 10, '兄弟', '姊妹', 成人=50, 孩童=20, 嬰兒=2)







