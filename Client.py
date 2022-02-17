import socket
import pygame

WIDHT_WINDOW,HEIGHT_WINDOW=1000,800
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY, 1)
sock.connect(('localhost',10000))

pygame.init()
screen=pygame.display.set_mode((WIDHT_WINDOW,HEIGHT_WINDOW))
pygame.display.set_caption('Бактерия обег из лабораторий')

running=True
while True:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    if pygame.mouse.get_focused():
        pos=pygame.mouse.get_pos()
        v= (pos[0]-WIDHT_WINDOW//2,pos[1]-HEIGHT_WINDOW//2)
        
    
    sock.send('Я хочу идти навверх'.encode())

    data=sock.recv(2**20)
    data=data.decode()

    screen.fill('grey25')
    pygame.draw.circle(screen, (255,0,0),
                       (WIDHT_WINDOW,HEIGHT_WINDOW//2), 50)
    pygame.display.update() 
pygame.quit()
