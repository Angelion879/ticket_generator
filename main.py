from imgWriter import img_writer
from emailSender import email_sender
from spreadsheeManager import build_code, append_client

def main():
    name_list = open('names.txt','r')

    for line in name_list:
        name = ' '.join(line.split(" ")[:2])
        email = line.split(" ")[-1]

        client_code = build_code()
        print(name)
        img_writer(name,str(client_code))
        append_client(name,email,client_code)
        email_sender(email)

main()