import tkinter
from PIL import Image, ImageTk
import time
BMS=[["A",1000],["P",2000],["P",2500],["L",2800],["E",3000],["K",4500],["O",4800]]
BMS_time=[]
BMS_type=[]
NOTE_COUNT=len(BMS)
COMBO=0
now_time=0
# [type,start_time] perfect ponit = srart time+
NOTE_ALL=[]
#205 perfect point
#<145 or >265 lost
#
	
key = ""
def key_down(e):  #處理按下
    global key   
    key = e.keycode   #存取當前按下的鍵
 
def key_up(e):  #處理放開
    global key
    key = ""    #清空當前的按下狀態
 


def detect_BMS():
    for i in BMS:
        BMS_type.append(ord(i[0]))
        BMS_time.append(i[1])


def set_note():
    init_x=1195
    init_y=200
    NOTE_ALL.append([1190,200,BMS_type[NOTE_NOW_COUNT_CREATIVE]])
    canvas.create_image(init_x, init_y,image=resized_photo, tag="NOTE") 

def note_move_and_remove():
    global NOTE_ALL,COMBO,combo_count
    canvas.delete("NOTE")
    canvas.delete('note_type_text')
    k=NOTE_ALL.copy()
    for i in range(len(NOTE_ALL)):
        #缺時間判定
        if len(k)!=0:
            if key==k[0][2]:
                
                k.pop(0)
                NOTE_ALL[0]=0
                COMBO=COMBO+1
                update_combo()
                

        

        if NOTE_ALL[i]!=0:
            note_type_text(canvas, chr(NOTE_ALL[i][2]), NOTE_ALL[i][0]-30, 100)
            canvas.create_image(NOTE_ALL[i][0]-30,NOTE_ALL[i][1] ,image=resized_photo, tag="NOTE") 
            NOTE_ALL[i][0]=NOTE_ALL[i][0]-30
            
            

    n=NOTE_ALL.copy()
    for i in range(len(NOTE_ALL)):
        if NOTE_ALL[i]==0:
            n.pop(0)

    NOTE_ALL=n.copy()

def note_type_text(canvas, text, x, y):
    
    label = canvas.create_text(x, y, text=text, font=("Times New Roman", 50), fill="blue", tag="note_type_text")
    return label    

def combo_counter(canvas, text, x, y):
    label = canvas.create_text(x, y, text=text, font=("Times New Roman", 80), fill="black", tag="combo")
    return label

def update_combo():
    global combo_count
    canvas.delete('combo')
    combo_count = combo_counter(canvas, COMBO, 770, 500)
#已創建第幾個note
NOTE_NOW_COUNT_CREATIVE=0

def main():

    global now_time,NOTE_NOW_COUNT_CREATIVE,COMBO
 
    if len(NOTE_ALL)!=0:

        note_move_and_remove()

    if NOTE_COUNT-NOTE_NOW_COUNT_CREATIVE!=0:
        
        if now_time==BMS_time[NOTE_NOW_COUNT_CREATIVE]:
            set_note()
            #
      
            NOTE_NOW_COUNT_CREATIVE=NOTE_NOW_COUNT_CREATIVE+1
        
    if len(NOTE_ALL)!=0:
        if NOTE_ALL[0][0]<145:
            NOTE_ALL.pop(0)
            COMBO=0
            update_combo()
            if NOTE_COUNT-NOTE_NOW_COUNT_CREATIVE==0:
                canvas.delete("note_type_text")
                canvas.delete("NOTE")
                update_combo()

    now_time+=50
    
    
    window.after(50, main)

#基礎設定
window = tkinter.Tk()
window.title("music game")
window.geometry("1300x600")
window.resizable(False, False)
window.bind("<KeyPress>",key_down)
window.bind("<KeyRelease>", key_up)

canvas = tkinter.Canvas(width=1300, height=600, bg="white")
canvas.pack()

bg_img = tkinter.PhotoImage(file="IMG/background.png")
before_note = Image.open("IMG/note.png")
before_note = before_note.resize((20, 100), Image.LANCZOS)
resized_photo = ImageTk.PhotoImage(before_note) 

canvas.create_image(650, 300,image=bg_img, tag="BG") 

#COMBO數

combo_count = combo_counter(canvas, 0, 770, 500)
#讀取譜面
detect_BMS()

#主循環
main()

window.mainloop()
