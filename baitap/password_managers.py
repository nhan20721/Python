from cryptography.fernet import Fernet
'''
def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)
'''
def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():       #Phương thức readlines() trả về một danh sách chứa mỗi dòng trong tệp dưới dạng một mục danh sách.
            data = line.rstrip()         #Phương thức rstrip() loại bỏ mọi ký tự ở cuối chuỗi (các ký tự ở cuối chuỗi), dấu cách là ký tự cuối chuỗi mặc định cần loại bỏ.
            user, passw = data.split('|')
            print('User:', user,'|','Password:',passw) #fer.decrypt(passw.encode()).decode())

def add():
    name = input('Account name: ')
    pwd = input('Password: ')

    with open('passwords.txt', 'a') as f:
        f.write(name + '|' + pwd + '\n')#fer.encrypt(pwd.encode()).decode()

while True:
    mode = input('Would you like to add a new password or view existing ones (add/view)? Or press q to quit ')
    if mode == 'q':
        break
    elif mode == 'add':
        add()
    elif mode == 'view':
        view()
    else:
        print('Invalid mode.')
        continue