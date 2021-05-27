
import random
import xlrd
import xlwt

from tkinter import *
from PIL import ImageTk,Image

app = Tk()

#output_label declared as global to avoid overwriting
m_output_label = Label(app)
syn_output_label = Label(app)
n_output_label = Label(app)

#Listbox to display the output of the TRIE SEARCH ALGORITHMN(auto function here)
auto_list_box = Listbox(app)

#jout_label = Label(app)


class Node():
    def __init__(self):
        self.data= {}
        self.meaning = ''
        self.type = ''
        self.syn=''
        self.end = False

class Trie():
    def __init__(self):
        self.root=self.getNode()

    def getNode(self):
        return Node()



    def insert(self,word,meaning,type,syn):
        root=self.root

        for i in list(word):

            if not root.data.get(i):
                root.data[i] = self.getNode()
            root = root.data[i]

        root.end = True
        root.meaning = meaning
        root.type = type
        root.syn = syn
#-----------------------------------------------------------------------------------------------

    def search(self, word):
        root=self.root
        found = True

        for i in list(word):

            if not root.data.get(i):
                forund = False
                break

            root=root.data[i]

        return found

#-----------------------------------------------------------------------------------------------
#getData is same function as getMeaning
#Since tkinter does not allow function with arguments but it is needed since it is used in auto function


    def getData(self,word):
        root = self.root
        found = True

        for i in list(word):
            if not root.data.get(i):
                found= False
                return 0
            root = root.data[i]

        if found:
            return root.meaning

#-----------------------------------------------------------------------------------------------

#tkinter does not allow passing of function arguments
    def getMeaning(self):
        root = self.root
        found = True

        global m_output_label
        m_output_label.destroy()

        out = ""
        word = word_entry.get()

        #label to print the message to enter a word
        if( len(word) == 0):
            out = out + "Please Enter a word"

            m_output_label = Label(app, text= out,font=('times',12,'bold'),fg="white",bg="black")
            canvas1.create_window(150, 220, window=m_output_label)
            return 0

        for i in list(word):
            if not root.data.get(i):
                out = out+ "Word Not Found"

                #label to display message word not found
                m_output_label = Label(app, text= out,font=('times',12,'bold'),fg="white",bg="black")
                canvas1.create_window(150, 220, window=m_output_label)
                return 0

            root = root.data[i]


        if found:
            out = out + root.meaning

        #label to print meaning
        m_output_label = Label(app, text= out,font=('times',12,'bold'),fg="white",bg="black")
        canvas1.create_window(150, 220, window=m_output_label)

#-----------------------------------------------------------------------------------------------
    def getType(self):
        root = self.root
        found = True

        global n_output_label
        n_output_label.destroy()

        out = ""
        word = word_entry.get()

        if( len(word) == 0):
            out = out + "Please Enter a word"

            n_output_label = Label(app, text= out,font=('times',12,'bold'),fg="white",bg="black")
            canvas1.create_window(350, 220, window=n_output_label)
            return 0

        for i in list(word):

            if not root.data.get(i):
                found= False
                out = out + "Word Not Found"

                #label to display message word not found
                n_output_label = Label(app, text= out,font=('times',12,'bold'),fg="white",bg="black")
                canvas1.create_window(350, 220, window=n_output_label)

                return 0
            root = root.data[i]


        if found:
            out = out +root.type

        n_output_label = Label(app, text= out,font=('times',12,'bold'),fg="white",bg="black")
        canvas1.create_window(350, 220, window=n_output_label)
        return
#-----------------------------------------------------------------------------------------------

    def getSyn(self):
        root = self.root
        found = True

        global syn_output_label
        syn_output_label.destroy()

        out = ""
        word = word_entry.get()

        if( len(word) == 0):
            out = out + "Please Enter a word"

            syn_output_label = Label(app, text= out,font=('times',12,'bold'),fg="white",bg="black")
            canvas1.create_window(550, 220, window=syn_output_label)
            return 0

        for i in list(word):

            if not root.data.get(i):
                found= False
                out = out+"Word Not Found"

                syn_output_label = Label(app, text= out,font=('times',12,'bold'),fg="white",bg="black")
                canvas1.create_window(550, 220, window=syn_output_label)
                return 0

            root = root.data[i]

        if found:
            out = out + root.syn

        syn_output_label = Label(app, text= out,font=('times',12,'bold'),fg="white",bg="black")
        canvas1.create_window(550, 220, window=syn_output_label)
        return 0
#-----------------------------------------------------------------------------------------------

    def traverse(self, node, temp, final):
        if node.end == True:
            final.append(temp)

        for i,j in node.data.items():
            self.traverse(j,temp + i, final)
#-----------------------------------------------------------------------------------------------

    def auto(self):
        root=self.root
        final=[]
        temp = ''
        a=False

        global auto_list_box
        auto_list_box.destroy()

        auto_list_box = Listbox(app,bg = "black", bd = 10, fg = "white",font = "Castellar", cursor = "target")

        output = ""

        key = auto_entry.get()

        for i in list(key):

            if not root.data.get(i):
                a=True
                break
            temp +=i
            root=root.data[i]

        if a:
            return 0
        elif root.end and not root.data:
            return -1

        self.traverse(root,temp,final)

        count = 0
        for i in final:
            output = i +" - " + self.getData(i)
            auto_list_box.insert(count ,output)
            count +=1

        #label2 = tkr.Label(rt, text= output,font=('times',30,'bold'))
        canvas2.create_window(500, 260, window=auto_list_box)

        return 1
#-----------------------------------------------------------------------------------------------

    def random_word_generator(self):
        length = random.randint(4,8)
        key=""
        root = self.root
        final = []
        temp = ''
        a = False

        for i in list(key):

            if not root.data.get(i):
                a = True
                break
            temp += i
            root = root.data[i]

        if a:
            return 0
        elif root.end and not root.data:
            return -1

        self.traverse(root, temp, final)

        while(1):
            p=random.choice(final)
            if(len(p) > 3):
                return p
#-----------------------------------------------------------------------------------------------


# MINI GAME 1
#Function to generate random word and shuffe it
def jumbleShuffle():

    global correct_word
    #correct_word is declard as global so the next fucntion can know its value
    #Generating a random word
    correct_word = t.random_word_generator()
    for i in range(5):
        n = random.sample(range(0, len(correct_word)), len(correct_word))
    new = []

    #Creating a shuffled word
    for i in n:
        new.append(correct_word[i])
    jumbled=''.join(new)

    #Label to display suffled word
    jumb_label.config(text=jumbled)


def jumbleAnswer():

    if (correct_word == ans_entry.get() ):
        out_string = "Correct! You Win"
    elif( len(ans_entry.get()) == 0):
        out_string = "Please enter a word"
    else:
        out_string = "Wrong Answer!" +"\n" +"Correct Answer is " + correct_word

    #Label to display results of the function
    j_answer_label.config(text=out_string)
    #JUMBLE OVER
#-----------------------------------------------------------------------------------------------

#Mini Game 2:
def quiz_question():
    global a1,b1,c1,d1
    #They are declared as global so the next function can know thier value

    a1 = t.random_word_generator()
    b1 = t.random_word_generator()
    c1 = t.random_word_generator()
    d1 = t.random_word_generator()

    list = [a1,b1,c1,d1]

    global correct_ans
    #Choosing a correct word(answer) randomly out of any 4 randomly generated words
    correct_ans = list[random.randint(0,3)]

    #Getting the meaning of the word
    m = t.getData( correct_ans )

    #Question to be displayed
    dis = "\n"+ m + "\n" + "a."+a1+"\t" +"b."+b1+"\t" +"c."+c1+"\t" +"d."+d1+"\n"
    quiz_label.config(text=dis)



def quiz_answer():

    #Input options
    input_q = option_entry.get()
    input_ans = ""

    if input_q=="a":
        input_ans += a1
    elif input_q == "b":
        input_ans += b1
    elif input_q == "c":
        input_ans += c1
    elif input_q == "d":
        input_ans += d1

    #quiz_answer_label defined in canvas2 to display the results
    if input_ans == correct_ans:
        quiz_answer_label.config(text="Correct Answer")
    elif( len(input_ans) == 0):
        quiz_answer_label.config(text="Please enter a word")
    else:
        quiz_answer_label.config(text="Incorrect Answer")

    return
#QUIZ OVER
#-----------------------------------------------------------------------------------------------


if __name__=="__main__":

    words = []
    type=[]
    meanings = []
    synonyms=[]

    # Give the location of the file
    loc = (r"C:\Users\admin\Desktop\DS mini project\Word List.xlsx")

    # To open Workbook
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    #Extracting words from excel file
    #And inserting them into the respective lists
    for i in range(1, 523):
        a = sheet.cell_value(i, 0)
        words.append(a)

    for i in range(1, 523):
        a = sheet.cell_value(i, 1)
        type.append(a)

    for i in range(1, 523):
        a = sheet.cell_value(i, 2)
        meanings.append(a)

    for i in range(1, 523):
        a = sheet.cell_value(i, 3)
        synonyms.append(a)


    t = Trie()

    #Insertion of words from excel file into trie
    for i in range(len(words)):
        t.insert(words[i],meanings[i],type[i],synonyms[i])

    #-----------------------------------------------------------------------------------------------
    #GUI starts

    #IMPORTANT POINT
    #get() function is used in many fucntions to take input enterd in entry boxes as tkinter does not
    #allow passing of functions with arguments

    app.title("Dictionary")
    app.geometry("1352x900")

    #Addition of background image
    load = Image.open("C:\\Users\\admin\\Desktop\\DS mini project\\photo2.jpg")
    render = ImageTk.PhotoImage(load)

    img = Label(app,image = render)
    img.place( x=0 ,y=0 )

    #Addition of background image done

    #canvas1 begins
    canvas1 = Canvas(app, bg='black',width = 1000, height = 250)
    canvas1.pack()

    #Additon of image at the top right corner
    logo_img = PhotoImage(file="logo.png")
    canvas1.create_image(720,0, anchor=NW, image=logo_img)

    #Title label
    title_label = Label(app,text="DICTIONARY",font=("Times",45),fg="white",bg="black" )
    canvas1.create_window(400,40,window=title_label)


    txt_label = Label(app, text='Enter the Word here :',font=('times',15,'bold'),fg="white",bg="black")
    canvas1.create_window(200, 120, window = txt_label)

    #First entry box which serves as input to provide meaning type and synonyms of the input word
    word_entry = Entry (app, font=('times',15,'bold') )
    canvas1.create_window(420, 120, window = word_entry)

    #Displays meaning of the word
    meaning_button = Button(text='Get Meaning', command = t.getMeaning,bg="#000000", fg="#ffffff",
                   activebackground="#ffffff", activeforeground="#000000", relief="raised", padx=12,
                   pady=4, bd=4)
    canvas1.create_window(150, 180, window = meaning_button)

    #Displays type of the word ie noun,adjective etc
    noun_button = Button(text='Get Word Type', command = t.getType,bg="#000000", fg="#ffffff",
                   activebackground="#ffffff", activeforeground="#000000", relief="raised", padx=12,
                   pady=4, bd=4)
    canvas1.create_window(350, 180, window = noun_button)

    #Displays synonym of the word
    syn_button = Button(text='Get Synonym', command = t.getSyn,bg="#000000", fg="#ffffff",
                   activebackground="#ffffff", activeforeground="#000000", relief="raised", padx=12,
                   pady=4, bd=4)
    canvas1.create_window(550, 180, window = syn_button)
    #canvas1 ends


    #canvas2
    canvas2 = Canvas(app, bg='black',width = 1000, height = 500)
    canvas2.pack()

    #Jumble starts
    #title label for jumble game
    j_label = Label(app,text="JUMBLE",font=("Times",30),fg="white",bg="black")
    canvas2.create_window(200,40,window=j_label)

    #Label used to display the jumbled word
    jumb_label =  Label(app,text="",font=("Times",20) ,fg="white",bg="black")
    canvas2.create_window(200,100,window=jumb_label)

    #Button to generate another word
    pick_button = Button(app,text="Pick another word",command=jumbleShuffle,bg="#000000", fg="#ffffff",
                   activebackground="#ffffff", activeforeground="#000000", relief="raised", padx=12,
                   pady=4, bd=4)
    canvas2.create_window(120,220,window=pick_button)

    #Taking the user answer as input with help of entry button
    ans_entry = Entry(app,font=('times',15,'bold'))
    canvas2.create_window(200,160,window=ans_entry)

    #Execution of the game
    ch_ans_button = Button(app,text="Check answer",command= jumbleAnswer,bg="#000000", fg="#ffffff",
                   activebackground="#ffffff", activeforeground="#000000", relief="raised", padx=12,
                   pady=4, bd=4)
    canvas2.create_window(280,220,window=ch_ans_button)

    #Displaying the result
    j_answer_label = Label(app,text = "",font=("Times",15),fg="white",bg="black" )
    canvas2.create_window(200,280,window = j_answer_label)
    #Jumble ends


    #QUIZ BEGINS
    #title label
    qz_label = Label(app,text="QUIZ",font=("Times",30),fg="white",bg="black")
    canvas2.create_window(800,40,window=qz_label)

    #Label to display the question
    quiz_label = Label(app,text="",fg="white",bg="black")
    canvas2.create_window(800,120,window=quiz_label)

    ##Taking the user answer as input with help of entry button
    option_entry = Entry (app, font=('times',15,'bold') )
    canvas2.create_window(820,200, window = option_entry)

    #Button to generate question
    quiz_q_button = Button(app,text="Get a question",command=quiz_question,bg="#000000", fg="#ffffff",
                   activebackground="#ffffff", activeforeground="#000000", relief="raised", padx=12,
                   pady=4, bd=4)
    canvas2.create_window(740,260, window = quiz_q_button)

    #Button to check the answer
    quiz_ans_button = Button(app,text="Check Answer",command=quiz_answer,bg="#000000", fg="#ffffff",
                   activebackground="#ffffff", activeforeground="#000000", relief="raised", padx=12,
                   pady=4, bd=4)
    canvas2.create_window(900,260, window = quiz_ans_button)

    #Label to display the results of the game
    quiz_answer_label = Label(app,text = "",font=("Times",20),fg="white",bg="black" )
    canvas2.create_window(850,320,window = quiz_answer_label)
    #Quiz ends

    #TRIE SEARCH ALGORITHMN
    #Auto begins
    auto_button = Button(app,text="Trie-Search",command= t.auto,bg="#000000", fg="#ffffff",
                   activebackground="#ffffff", activeforeground="#000000", relief="raised", padx=12,
                   pady=4, bd=4)
    canvas2.create_window(500,50, window = auto_button)

    auto_entry = Entry(app,font=('times',15,'bold'))
    canvas2.create_window(500,100,window=auto_entry)
    #AUTO ENDS


    app.mainloop()
