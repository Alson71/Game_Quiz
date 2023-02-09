from tkinter.font import BOLD
from PIL import ImageTk
import PIL.Image
from tkinter import *
from playsound import playsound
class GameQuiz:
    global ok,index,answer
    global A,B,C,D
    global answerlist,answers
    global questionLabel,ALabel,BLabel,CLabel,DLabel, scoreLabel, percentLabel
    global rightAnswer
    global frame, image, pictureLabel, newImage, resizeImage
    
    answers= [[None,None,None,None]]* 5
    answers[0] = ["Fortnite","Minecraft","Roblox","Rust"]
    answers[1] = ["Valorant","Minecraft","Destiny","Muck"]
    answers[2] = ["Black Ops","Black Ops 2","Hi Fi Rush","Rocket League"]
    answers[3] = ["Rocket League","Elden Ring","Uncharted","No Man's Sky"]
    answers[4] = ["Zelda","Mario Bros","CSGO","League of Legends"]

    answerlist = [None] * 5
    answerlist[0] = 'A'
    answerlist[1] = 'B'
    answerlist[2] = 'B'
    answerlist[3] = 'C'
    answerlist[4] = 'D'

    ok = Tk()
    ok.geometry("700x575")
    ok.config(bg="purple")
    ok.title("Game Quiz")

    frame = [None] * 5
    frame[0] = Frame(ok, width = 200, height = 200)
    frame[1] = Frame(ok, width = 200, height = 200)
    frame[2] = Frame(ok, width = 200, height = 200)
    frame[3] = Frame(ok, width = 200, height = 200)
    frame[4] = Frame(ok, width = 200, height = 200)

    image = [None] * 5
    image[0] = PIL.Image.open("world.jpg")
    image[1] = PIL.Image.open("block.png")
    image[2] = PIL.Image.open("mason.jpg")
    image[3] = PIL.Image.open("drake.jpg")
    image[4] = PIL.Image.open("game.jpg")

    newImage = [None] * 5
    newImage[0] = image[0].resize((300,200))
    newImage[1] = image[1].resize((200,200))
    newImage[2] = image[2].resize((200,300))
    newImage[3] = image[3].resize((200,200))
    newImage[4] = image[4].resize((200,200))

    resizeImage = [None] * 5
    resizeImage[0] = ImageTk.PhotoImage(newImage[0])
    resizeImage[1] = ImageTk.PhotoImage(newImage[1])
    resizeImage[2] = ImageTk.PhotoImage(newImage[2])
    resizeImage[3] = ImageTk.PhotoImage(newImage[3])
    resizeImage[4] = ImageTk.PhotoImage(newImage[4])


    pictureLabel = [None] * 5
    pictureLabel[0] = Label(frame[0], image = resizeImage[0])
    pictureLabel[1] = Label(frame[1], image = resizeImage[1])
    pictureLabel[2] = Label(frame[2], image = resizeImage[2])
    pictureLabel[3] = Label(frame[3], image = resizeImage[3])
    pictureLabel[4] = Label(frame[4], image = resizeImage[4])

   
    index=0
    answer=''

    A=Button(ok,text="A",font=('Times',20))
    B=Button(ok,text="B",font=('Times',20))
    C=Button(ok,text="C",font=('Times',20))
    D=Button(ok,text="D",font=('Times',20))

    ALabel= Label(ok,text=answers[index][0],font=('Times',24),bg="purple",fg="white")  
    BLabel= Label(ok,text=answers[index][1],font=('Times',24),bg="purple",fg="white")
    CLabel= Label(ok,text=answers[index][2],font=('Times',24),bg="purple",fg="white")
    DLabel= Label(ok,text=answers[index][3],font=('Times',24),bg="purple",fg="white")



    def nextQuestion():
     global index

     frame[index].destroy()
     pictureLabel[index].destroy()
     
     index += 1
     if index == 5:
        GameQuiz.results()
     else:
        A.config(state="normal")
        B.config(state="normal")  
        C.config(state="normal")  
        D.config(state="normal")

        frame[index].pack()
        pictureLabel[index].pack()
        frame[index].place(x="320",y="200")
     
        ALabel.config(fg="white",text = answers[index][0])
        BLabel.config(fg="white",text = answers[index][1])
        CLabel.config(fg="white",text = answers[index][2])
        DLabel.config(fg="white",text = answers[index][3])



    rightAnswer = 0
    def showAnswer(arg):
     A.config(state="disabled")
     B.config(state="disabled")
     C.config(state="disabled")
     D.config(state="disabled")
     global rightAnswer

     if arg == 1:
        answer = 'A'
        
     elif arg == 2:
        answer = 'B'
       
     elif arg == 3:
        answer = 'C'
        
     elif arg == 4:
        answer = 'D'


     if answerlist[index] == 'A':  
         ALabel.config(fg="light green")           
     else:
         ALabel.config(fg="red")

     if answerlist[index] == 'B':  
         BLabel.config(fg="light green")      
     else:
         BLabel.config(fg="red")

     if answerlist[index] == 'C':  
         CLabel.config(fg="light green")       
     else:
         CLabel.config(fg="red")
     if answerlist[index] == 'D':  
         DLabel.config(fg="light green")      
     else:
         DLabel.config(fg="red")

     if answerlist[index] == answer:
         rightAnswer += 1
         playsound('ding.wav', block = False)
         ok.after(1000,GameQuiz.nextQuestion)
         
        
     else:
         playsound('wrong.wav', block = False)
         ok.after(2000,GameQuiz.nextQuestion)
         
     
     

         
    
    def results():
        global rightAnswer
        A.destroy()
        B.destroy()
        C.destroy()
        D.destroy()

        ALabel.destroy()
        BLabel.destroy()
        CLabel.destroy()
        DLabel.destroy()

        questionLabel.config(text = "Your Final Score:")
        scoreLabel = Label(ok,text = str(rightAnswer) + "/" + str(5) ,font=('Times',40),fg = "beige",bg = "red",width = 7)
        scoreLabel.pack()
        scoreLabel.place(x="245",y="200")
        total= ((float) (rightAnswer)/5) * 100
        percentLabel= Label(ok,text = str(total) + "%",font=('Times',40),fg="yellow",bg="black",width = 7)
        percentLabel.pack()
        percentLabel.place(x = "245",y = "265")
        



    questionLabel = Label(ok,text="Guess The Game",font=('Times',24,BOLD),fg="Blue",bg="green",borderwidth = 3)

    A.pack()
    B.pack()
    C.pack()
    D.pack()

    A.config(command= lambda: GameQuiz.showAnswer(1))
    B.config(command= lambda: GameQuiz.showAnswer(2))
    C.config(command= lambda: GameQuiz.showAnswer(3))
    D.config(command= lambda: GameQuiz.showAnswer(4))
   
    questionLabel.pack()
    questionLabel.place(x="230",y="0")

    A.place(x="0",y="200",height=70,width=60)
    B.place(x="0",y="275",height=70,width=60)
    C.place(x="0",y="350",height=70,width=60)
    D.place(x="0",y="425",height=70,width=60)

    
    def startGame():
     global index

     ALabel.pack()
     BLabel.pack()
     CLabel.pack()
     DLabel.pack()

     frame[index].pack()
     pictureLabel[index].pack()

     ALabel.place(x="75",y="215")
     BLabel.place(x="75",y="290")
     CLabel.place(x="75",y="365")
     DLabel.place(x="75",y="440")
     frame[index].place(x="320",y="200")
    
    
        
        
    
        
    
   
if __name__=="__main__":
    GameQuiz.startGame()
    ok.mainloop()
    
    
   








