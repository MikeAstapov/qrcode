import segno


def make_qr(user_req):
    qrcode = segno.make(user_req, micro=False)
    try:
        qrcode.save(f"{user_req.split()[0]}" + ".png", scale=7)
        print(f"QR-code сохранен в файл {user_req.split()[0]}.png. Чтобы посмотреть введите 1.Закрыть программу - введите 0")

        while True:
            user_choice = input('Введите число 1 или 0: ')
            if user_choice == '1':
                qrcode.show()
                break
            if user_choice == '0':
                break
            else:
                print("Введите 1 чтобы посмотреть qr-code или 0 чтобы закрыть программу")

    except:
        qrcode.save(f"{user_req.split('https://')[1].split('.')[0]}" + ".png", scale=7)
        print(f"QR-code сохранен в файл {user_req.split('https://')[1].split('.')[0]}.png. Чтобы посмотреть введите 1.Закрыть программу - введите 0")

        while True:
            user_choice = input('Введите число 1 или 0: ')
            if user_choice == '1':
                qrcode.show()
                break
            if user_choice == '0':
                break
            else:
                print("Введите 1 чтобы посмотреть qr-code или 0 чтобы закрыть программу")


if __name__ == '__main__':
    make_qr(input('Введите текст для QR кода: '))
