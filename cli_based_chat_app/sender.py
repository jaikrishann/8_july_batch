import socket
# socket in python is used for network communication,
# allowing programs to communicate with each other over a network
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    ip_address = ""                     ###sender me samne wale ka ip add aayega jisko aap 
    #msg send kar rhe ho aur receiver me nhi samne wala ka he aayga jo receiver baan rhaa hai 
    port_number  = 9999                  #0-65536 #ports are dynamic in nature 
    # dono files me same port number rahega 
    target_add = (ip_address,port_number)
    message = input("enetr your message:- ")
    message.encode("ascii")
    encripted_message = message.encode("ascii")
    s.sendto(encripted_message,target_add)
except Exception as e:
    print("msg nahi gya🥲🥲")



    ## same connection se connect rehna padega 
    ## 