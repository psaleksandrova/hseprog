def isint(st):
    return st.isdigit()

st = input("Введите массу тела в килограммах: ")
if isint(st):
    m = int(st)
st = input("Введите рост в сантиметрах, отличный от 0: ")
if isint(st):
    h = int(st) / 100
    if h == 0:
        print("Рост должен быть отличным от 0")
    else:
        i = m / (h * h)
        if i <= 16:
            print("Выраженный дефицит массы тела")
        elif 16 < i < 18.5:
            print("Недостаточная (дефицит) масса тела")
        elif 18.5 <= i < 25:
            print("Норма")
        elif 25 <= i < 30:
            print("Избыточная масса тела (предожирение)")
        elif 30 <= i < 35:
            print("Ожирение первой степени")
        elif 35 <= i < 40:
            print("Ожирение второй степени")
        elif 40 <= i:
            print("Ожирение третьей степени (морбидное)")
