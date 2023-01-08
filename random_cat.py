from tkinter import *
from requests import get
from PIL import Image

url = 'https://aws.random.cat/meow'

width = 500
height = 500
base = 600

def get_image():
    request = get(url).json()
    image = get(request['file'])
    with open('cat.png', 'wb') as f:
        f.write(image.content)

def scale():
    global width, height

    img = Image.open('cat.png')
    if img.size[0] >= img.size[1]:
        width = base
        ratio = (width / float(img.size[0]))
        height = int((float(img.size[1]) * float(ratio)))
    else:
        height = base
        ratio = (height / float(img.size[1]))
        width = int((float(img.size[0]) * float(ratio)))
    img = img.resize((width, height))
    img.save('image.png')


def update():
    global temp

    get_image()
    scale()
    temp = PhotoImage(file='image.png')

def click():
    global new
    new = temp
    window.geometry(f'{width}x{height}')
    cat_label.configure(image=new)
    btn.place(x=width / 2, y=height - 20, anchor=CENTER)

    update()

scale()
window = Tk()
window.title('Random Cat Picture')
window.geometry(f'{width}x{height}')
window.resizable(width=False, height=False)

old = PhotoImage(file='image.png')
cat_label = Label(window, image=old)
cat_label.place(x=0, y=0, relwidth=1, relheight=1)
btn = Button(window, text='New cat!', command=click)
btn.place(x=width/2, y=height-20, anchor=CENTER)

update()

mainloop()