import tkinter
from tkinter import font

class Stone:
    def __init__(self):
        self.dic = {"none":0,"white":"W","red":"R","orange":"O","blue":"B","green":"G"}
        self.friend_dic = {"R":"O","O":"R","B":"G","G":"B"}

    def getColor(self,var):
        return self.dic[var]
    
    def getFriend(self,var):
        return self.friend_dic[self.dic[var]]


#[縦][横]
#置けるかどうかの判断を行う
class Board:
    def __init__(self):
        self.stone = Stone()
        self.cells = [[0 for j in range(8)] for i in range(8)]
        self.cells[3][3] = self.stone.getColor("green")
        self.cells[4][3] = self.stone.getColor("red")
        self.cells[3][4] = self.stone.getColor("orange")
        self.cells[4][4] = self.stone.getColor("blue")
        
        

    def returnCell(self):
        return repr(self.cells)

    def __iter__(self):
        return (tuple(row) for row in self.cells)

    def getItem(self, pos):
        x, y = pos
        return self.cells[y][x]

    def setItem(self, pos, stone):
        x, y = pos
        self.cells[y][x] = stone

    def checkContain(self, pos):
        x, y = pos
        return 0 <= y < len(self.cells) and 0 <= x < len(self.cells[y])


    def is_used(self, x, y):
        return not self.cells[y][x].is_none()

    def set_candidates(self, candidates):
        for x, y in candidates:
            self.cells[y][x].set_candidate()

    def reset_candidates(self):
        for row in self:
            for cell in row:
                cell.reset_candidate()
    
    def canPlace(self,tag,color):
        print(self.cells)
        self.x,self.y = int(tag.split("_")[0]),int(tag.split("_")[1])
        whites = []
        self.color1,self.color2 = self.stone.getColor(color),self.stone.getFriend(color)
        flag = 0
        for i in range(-1,2):
            for j in range(-1,2):
                flag = 0
                if i == 0 & j == 0:
                    continue

                
                if self.checkContain((self.x+i,self.y+j)):
                    self.next_x,self.next_y= i + self.x,j + self.y
                else:
                    self.next_x,self.next_y= self.x,self.y
                
                
                #メモ
                """
                現状：駒のおける位置の認識はほぼできているが、自分の色同士で挟めない問題がある
                """
                while self.cells[self.next_x][self.next_y] != self.color1 and self.cells[self.next_x][self.next_y] != self.color2 and self.cells[self.next_x][self.next_y] != self.stone.getColor("none") and self.cells[self.next_x][self.next_y] != self.stone.getColor("white"):
                   
                    flag = 1
                    if self.checkContain((self.next_x+i,self.next_y+j)):
                        self.next_x += i
                        self.next_y += j
                    else:
                        break

                
                
                if flag == 1 and (self.cells[self.next_x][self.next_y] == self.color1 or self.cells[self.next_x][self.next_y] == self.color2):
                    
                    print(self.cells[self.next_x][self.next_y]) 
                    whites.append((self.next_x,self.next_y))


        if len(whites):
            self.setItem((self.x,self.y),self.stone.getColor(color))
            return True
        else:
            return False

class Othello:
    def __init__(self):
        self.board = board = Board()
        self.main = main = Tkview(board)
        main.initWindow()
        
class Player:
    def __init__(self,turn):
        self.myturn = turn
        if self.myturn == "f":
            self.mycolor_1 = "red"
            self.mycolor_2 = "orange"
            self.encolor_1 = "blue"
            self.encolor_2 = "green"
            self.myturnlang = "先攻"
        else:
            self.mycolor_1 = "blue"
            self.mycolor_2 = "green"
            self.encolor_1 = "red"
            self.encolor_2 = "orange"
            self.myturnlang = "後攻"

    def returnMycolor(self):
        return [self.mycolor_1,self.mycolor_2]
    
    def returnEnecolor(self):
        return [self.encolor_1,self.encolor_2]
    
    def returnLang(self,color):
        color_lang = {"red":"レッド","orange":"オレンジ","blue":"ブルー","green":"グリーン"}
        return color_lang[color]

    def returnTurnlang(self):
        return self.myturnlang
    
#CPUのレベルに合わせた深さを読む
class Cpu:
    def __init__(self,turn,level):
        self.myturn = turn
        self.level = level
        level_data = {"p":"強い","n":"普通","w":"弱い"}
        self.level_lang = level_data[self.level]
    def returnLang(self):
        return self.level_lang


class Tkview:
    def __init__(self,board):
        self.board = board
        #画面定義
        

    def initWindow(self): 
        self.window = window = tkinter.Tk()
        window.title("4colors")
        window.geometry("800x600")
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)
        window.resizable(width=False, height=False)

        self.data = {0:["f","s"],1:["s","f"],2:"p",3:"n",4:"w"}
        #スタート画面
        start_page = tkinter.Frame(window)
        font_title = font.Font(family="Times",size=100,weight="bold")
        game_title = tkinter.Label(start_page,text = u"4colors",font=font_title)        
        game_title.place(relx = 0.5,rely=0.2,anchor=tkinter.CENTER)

        font_button = font.Font(size=10)
        start_button = tkinter.Button(start_page,text=u"-ゲームスタート-",font=font_button,command=lambda: self.movePage(mode_page))
        start_button.place(relx=0.5,rely=0.6,anchor=tkinter.CENTER)
        rule_button = tkinter.Button(start_page,text=u"-ルール-",font=font_button,command=lambda: self.movePage(rule_page))
        rule_button.place(relx=0.5,rely=0.7,anchor=tkinter.CENTER)
        start_page.grid(row=0, column=0, sticky="nsew")

        #ルール画面
        rule_page = tkinter.Frame(window)
        font_text = font.Font(family="Times",size=50,weight="bold")
        rule_title = tkinter.Label(rule_page,text = u"rule",font=font_text)        
        rule_title.place(relx = 0.5,rely=0.2,anchor=tkinter.CENTER)

        font_button = font.Font(size=10)
        back_start_button = tkinter.Button(rule_page,text=u"-戻る-",font=font_button,command=lambda: self.movePage(start_page))
        back_start_button.place(relx=0.5,rely=0.6,anchor=tkinter.CENTER)
        
        rule_page.grid(row=0, column=0, sticky="nsew")
        
        #モード選択画面
        mode_page = tkinter.Frame(window)
        font_text = font.Font(family="Times",size=50,weight="bold")
        mode_title = tkinter.Label(mode_page,text = u"mode",font=font_text)        
        mode_title.place(relx = 0.5,rely=0.2,anchor=tkinter.CENTER)

        font_button = font.Font(size=10)
        back_start_button = tkinter.Button(mode_page,text=u"-戻る-",font=font_button,command=lambda: self.movePage(start_page))
        back_start_button.place(relx=0.5,rely=0.6,anchor=tkinter.CENTER)

        battle_button = tkinter.Button(mode_page,text=u"-対戦-",font=font_button,command=lambda: self.movePage(battle_page))
        battle_button.place(relx=0.5,rely=0.7,anchor=tkinter.CENTER)

        battle_cpu_button = tkinter.Button(mode_page,text=u"-CPU-",font=font_button,command=lambda: self.movePage(battle_cpu_page))
        battle_cpu_button.place(relx=0.5,rely=0.8,anchor=tkinter.CENTER)        
        mode_page.grid(row=0, column=0, sticky="nsew")


        #対戦画面
        battle_page = tkinter.Frame(window)
        font_text = font.Font(family="Times",size=50,weight="bold")
        mode_title = tkinter.Label(battle_page,text = u"battle",font=font_text)        
        mode_title.place(relx = 0.5,rely=0.2,anchor=tkinter.CENTER)

        font_button = font.Font(size=10)
        back_mode_button = tkinter.Button(battle_page,text=u"-back-",font=font_button,command=lambda: self.movePage(start_page))
        back_mode_button.place(relx=0.5,rely=0.8,anchor=tkinter.CENTER)        
        battle_page.grid(row=0, column=0, sticky="nsew")

        #CPU選択画面
        battle_cpu_page = tkinter.Frame(window)
        font_text = font.Font(family="Times",size=50,weight="bold")
        battle_cpu_title = tkinter.Label(battle_cpu_page,text = u"choice",font=font_text)        
        battle_cpu_title.place(relx = 0.5,rely=0.2,anchor=tkinter.CENTER)

        self.attack_var = tkinter.IntVar()
        self.level_var = tkinter.IntVar()
        
        
        
        self.attack_var.set(0)
        #強い普通弱いをpとnとwとする
        self.level_var.set(2)

        """ self.attack = 0
        self.level = 2 """
        

        attack_first_buttton = tkinter.Radiobutton(battle_cpu_page,value=0,variable=self.attack_var,text="先攻")
        attack_first_buttton.place(relx=0.3,rely=0.3,anchor=tkinter.CENTER)
        attack_second_buttton = tkinter.Radiobutton(battle_cpu_page,value=1,variable=self.attack_var,text="後攻")
        attack_second_buttton.place(relx=0.3,rely=0.5,anchor=tkinter.CENTER)

        level_power_buttton = tkinter.Radiobutton(battle_cpu_page,value=2,variable=self.level_var,text="強い")
        level_power_buttton.place(relx=0.7,rely=0.3,anchor=tkinter.CENTER)
        level_normal_buttton = tkinter.Radiobutton(battle_cpu_page,value=3,variable=self.level_var,text="普通")
        level_normal_buttton.place(relx=0.7,rely=0.4,anchor=tkinter.CENTER)
        level_weak_buttton = tkinter.Radiobutton(battle_cpu_page,value=4,variable=self.level_var,text="弱い")
        level_weak_buttton.place(relx=0.7,rely=0.5,anchor=tkinter.CENTER)
        
        font_button = font.Font(size=10)
        back_mode_button = tkinter.Button(battle_cpu_page,text=u"-戻る-",font=font_button,command=lambda: self.movePage(mode_page))
        back_mode_button.place(relx=0.4,rely=0.8,anchor=tkinter.CENTER)

        battle_button = tkinter.Button(battle_cpu_page,text=u"-ゲームスタート-",font=font_button,command=lambda:[self.movePage(othello_cpu_page),self.getChoiced(othello_cpu_page)])
        battle_button.place(relx=0.6,rely=0.8,anchor=tkinter.CENTER)     
        battle_cpu_page.grid(row=0, column=0, sticky="nsew")


        #CPU対戦画面
        othello_cpu_page = tkinter.Frame(window)

        self.player = Player(self.data[self.attack_var.get()][0])
        self.cpu = Cpu(self.data[self.attack_var.get()][1],self.data[self.level_var.get()])
        self.stone = Stone()

        
        font_text = font.Font(family="Times",size=20,weight="bold")
        self.othello_cpu_title = tkinter.Label(othello_cpu_page,text = "",font=font_text)        
        self.othello_cpu_title.place(relx = 0.7,rely=0.12,anchor=tkinter.CENTER)

        cells_tag = []

        # tagがキー、座標がバリューの辞書定義
        self.tag_to_coord = {}

        # 座標がキー、tagがバリューの辞書定義
        self.coord_to_tag = {}

        # クリックされたtag保存変数
        self.clicked_tag = "null"

        # 座標がキー、駒の状態を示す値をバリューとする辞書定義
        # (駒なし:0, 黒:1, 白:2)
        self.coord_to_piece = {}
        
        #置く色（デフォルト）
        self.place_color = self.player.mycolor_1
        print(self.place_color)

        self.cells = tkinter.Canvas(othello_cpu_page,width=400,height=400)
        for i in range(8):
            for j in range(8):
                tags = "{}_{}".format(j, i)
                coord = (i*50,j*50,50+i*50,50+j*50)
                self.cells.create_rectangle(*coord,fill = "green",outline="black",tag=tags)
                
                cells_tag.append(tags)
                self.tag_to_coord[tags] = coord
                self.coord_to_tag[coord] = tags

                #i:横、j:縦

                if i == 3 and j == 3:
                    self.coord_to_piece[coord] = self.stone.getColor("green")
                    self.cells.create_oval(*coord,fill="green yellow",tag=tags)
                elif i == 4 and j == 3:
                    self.coord_to_piece[coord] = self.stone.getColor("red")
                    self.cells.create_oval(*coord,fill="red",tag=tags)
                elif i == 3 and j == 4:
                    self.coord_to_piece[coord] = self.stone.getColor("orange")
                    self.cells.create_oval(*coord,fill="orange",tag=tags)
                elif i == 4 and j == 4:
                    self.coord_to_piece[coord] = self.stone.getColor("blue")
                    self.cells.create_oval(*coord,fill="blue",tag=tags)
                else:
                    self.coord_to_piece[coord] = self.stone.getColor("none")
        self.cells.place(x=350,y=100)

        for tags in cells_tag:
            self.cells.tag_bind(tags,"<ButtonPress-1>",self.checkClick)

        font_score,font_total = "courier 15 bold","Impact 30"
        self.score = tkinter.Canvas(othello_cpu_page,width=300,height=250)
        self.score.create_rectangle(2,2,299,249,fill = "white",tag="score_board")
        self.score.create_text(150,30,text="score",tag="score_1",font=font_score,fill="#6091d3",anchor=tkinter.CENTER)
        self.score.create_text(150,60,text="score",tag="score_2",font=font_score,fill="#6091d3",anchor=tkinter.CENTER)
        self.score.create_text(150,90,text="score",tag="score_diff",font=font_score,fill="#6091d3",anchor=tkinter.CENTER)
        self.score.create_text(150,145,text="score",tag="score_total",font=font_total,fill="#6091d3",anchor=tkinter.CENTER)
        self.score.create_text(150,180,text="score",tag="score_total_en",font=font_total,fill="#6091d3",anchor=tkinter.CENTER)

        self.score.place(x=20,y=50)
        self.choice = tkinter.Canvas(othello_cpu_page,width=300,height=170)
        self.choice.create_rectangle(2,2,299,169,fill = "white")
        self.choice.create_text(150,10,text="色選択(レッド)",font=("FixedSys",30),anchor="n",tag="choice_board")
        self.choice.create_oval(35,70,115,150,fill = "white",outline="yellow",tag="color1",width=3)
        self.choice.create_oval(185,70,265,150,fill = "white",outline="black",tag="color2")

        self.changeScore(self.coord_to_piece)

        self.choice.itemconfig("color1",fill=self.player.returnMycolor()[0])
        self.choice.itemconfig("color2",fill=self.player.returnMycolor()[1])
        self.choice.tag_bind("color1","<ButtonPress-1>",self.changeColor)
        self.choice.tag_bind("color2","<ButtonPress-1>",self.changeColor)



        #self.choice.create_rectangle(,fill = "green",outline="black",tag=color2)
        self.choice.place(x=20,y=350)
        othello_cpu_page.grid(row=0, column=0, sticky="nsew") 

        


        #結果画面
        result_page = tkinter.Frame(window)
        font_text = font.Font(family="Times",size=50,weight="bold")
        result_title = tkinter.Label(result_page,text = u"result",font=font_text)        
        result_title.place(relx = 0.5,rely=0.2,anchor=tkinter.CENTER)

        font_button = font.Font(size=10)
        all_back_button = tkinter.Button(result_page,text=u"-戻る-",font=font_button,command=lambda: self.movePage(start_page))
        all_back_button.place(relx=0.5,rely=0.6,anchor=tkinter.CENTER)

        result_page.grid(row=0, column=0, sticky="nsew")


        start_page.tkraise()
        window.mainloop()

    
    
    def movePage(self,page):
        page.tkraise()
    
    def getChoiced(self,page):
        self.player = Player(self.data[self.attack_var.get()][0])
        self.cpu = Cpu(self.data[self.attack_var.get()][1],self.data[self.level_var.get()])
        
        #ページ更新処理
        self.choice.itemconfig("choice_board",text="色選択("+self.player.returnLang(self.player.mycolor_1)+")")
        self.choice.itemconfig("color1",fill=self.player.mycolor_1)
        self.choice.itemconfig("color2",fill=self.player.mycolor_2)

        self.othello_cpu_title.configure(text="あなた:" + self.player.returnTurnlang() + "  CPU:" + self.cpu.returnLang())

    def checkClick(self,event):
        for i in range(8):
            for j in range(8):
                coord = (i*50,j*50,50+i*50,50+j*50)
                if i*50 <= event.x <= 50+i*50 and j*50 <= event.y <= 50+j*50:
                    self.clicked_tag = self.coord_to_tag[coord]
        if self.board.canPlace(self.clicked_tag,self.place_color):
            self.cells.create_oval(*(self.tag_to_coord[self.clicked_tag]),fill=self.place_color,tag=self.clicked_tag)
            self.coord_to_piece[self.tag_to_coord[self.clicked_tag]] = self.stone.getColor(self.place_color)
            self.changeScore(self.coord_to_piece)
        

    def changeColor(self,event):
        if event.x <= 150:
            choice_color = self.player.mycolor_1
            choice_button = "color1"
            not_choice_button = "color2"
        else:
            choice_color = self.player.mycolor_2
            choice_button = "color2"
            not_choice_button = "color1"

        self.place_color = choice_color
        self.choice.itemconfig("choice_board",text="色選択("+self.player.returnLang(choice_color)+")")
        self.choice.itemconfig(choice_button,outline="yellow",width=3)
        self.choice.itemconfig(not_choice_button,outline="black",width=1)
        
    def changeScore(self,board_dic):
        values = list(board_dic.values())
        #print(values)
        count_red,count_orange,count_blue,count_green = values.count("R"),values.count("O"),values.count("B"),values.count("G")
        self.score.itemconfig("score_1",text="オレンジ("+str(count_orange)+"枚×5点):"+str(count_orange*5))
        self.score.itemconfig("score_2",text="レッド("+str(count_red)+"枚×2点):"+str(count_red*2))
        self.score.itemconfig("score_diff",text="枚数の差分("+str(abs(count_orange-count_red))+"枚×-5点):"+str(abs(count_orange-count_red)*(-5)))
        self.score.itemconfig("score_total",text="Total:"+str(count_orange*5+count_red*2+abs(count_orange-count_red)*(-5)))
        self.score.itemconfig("score_total_en",text="(あいて:"+str(count_blue*5+count_green*2+abs(count_blue-count_green)*(-5))+")")

class Othelloapp:
    def __init__(self):
        self.othello = othello = Othello()


if __name__ == "__main__":
    #start_game()
    #Othello()
    Othelloapp()

