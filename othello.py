import tkinter
from tkinter import font

class Stone:
    NONE = 0
    WHITE = "w"
    RED = "R"
    ORANGE = "O"
    BLUE = "B"
    GREEN = "G"

class Cell:
    def __init__(self):
        self.stone = Stone.NONE

    def returnType(self):
        return self.stone

    def checkEquall(self, stone):
        return self.stone == stone

    """ def is_none(self):
        return self.stone in (Stone.NONE, Stone.CANDIDATE)

    def set_candidate(self):
        if self.stone == Stone.NONE:
            self.stone = Stone.CANDIDATE

    def reset_candidate(self):
        if self.stone == Stone.CANDIDATE:
            self.stone = Stone.NONE """
#[縦][横]
class Board:

    def __init__(self):
        self._cells = [[Cell() for x in range(8)] for y in range(8)]
        self._cells[3, 3], self._cells[3, 4] = Stone.GREEN, Stone.RED
        self._cells[4, 3], self._cells[4, 4] = Stone.ORANGE, Stone.BLUE

    def returnCell(self):
        return repr(self._cells)

    def __iter__(self):
        return (tuple(row) for row in self._cells)

    def getItem(self, pos):
        x, y = pos
        return self._cells[y][x].stone

    def setItem(self, pos, stone):
        x, y = pos
        self._cells[y][x].stone = stone

    def checkContain(self, pos):
        x, y = pos
        return 0 <= y < len(self._cells) and 0 <= x < len(self._cells[y])

    def is_used(self, x, y):
        return not self._cells[y][x].is_none()

    def set_candidates(self, candidates):
        for x, y in candidates:
            self._cells[y][x].set_candidate()

    def reset_candidates(self):
        for row in self:
            for cell in row:
                cell.reset_candidate()


#ルールの定義
class Othello:
    def __init__(self):
        self.board = ""
        self.main = main = Tkview(self.board)
        


class Tkview:
    def __init__(self,board):
        #画面定義
        self.window = window = tkinter.Tk()
        window.title("4colors")
        window.geometry("800x600")
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        

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

        attack_var = tkinter.IntVar()
        level_var = tkinter.IntVar()
        
        #先攻後攻をfとsとする
        
        attack_var.set(0)
        #強い普通弱いをpとnとwとする
        level_var.set(2)
        

        attack_first_buttton = tkinter.Radiobutton(battle_cpu_page,value=0,variable=attack_var,text="先攻")
        attack_first_buttton.place(relx=0.3,rely=0.3,anchor=tkinter.CENTER)
        attack_second_buttton = tkinter.Radiobutton(battle_cpu_page,value=1,variable=attack_var,text="後攻")
        attack_second_buttton.place(relx=0.3,rely=0.5,anchor=tkinter.CENTER)

        level_power_buttton = tkinter.Radiobutton(battle_cpu_page,value=2,variable=level_var,text="強い")
        level_power_buttton.place(relx=0.7,rely=0.3,anchor=tkinter.CENTER)
        level_normal_buttton = tkinter.Radiobutton(battle_cpu_page,value=3,variable=level_var,text="普通")
        level_normal_buttton.place(relx=0.7,rely=0.4,anchor=tkinter.CENTER)
        level_weak_buttton = tkinter.Radiobutton(battle_cpu_page,value=4,variable=level_var,text="弱い")
        level_weak_buttton.place(relx=0.7,rely=0.5,anchor=tkinter.CENTER)
        
        font_button = font.Font(size=10)
        back_mode_button = tkinter.Button(battle_cpu_page,text=u"-戻る-",font=font_button,command=lambda: self.movePage(mode_page))
        back_mode_button.place(relx=0.4,rely=0.8,anchor=tkinter.CENTER)

        battle_button = tkinter.Button(battle_cpu_page,text=u"-ゲームスタート-",font=font_button,command=lambda:[self.movePage(othello_cpu_page),self.getData(othello_cpu_page,attack_var.get(),level_var.get())])
        battle_button.place(relx=0.6,rely=0.8,anchor=tkinter.CENTER)     
        battle_cpu_page.grid(row=0, column=0, sticky="nsew")


        #CPU対戦画面
        othello_cpu_page = tkinter.Frame(window)

        
        font_text = font.Font(family="Times",size=50,weight="bold")
        othello_cpu_title = tkinter.Label(othello_cpu_page,text =u"test",font=font_text)        
        othello_cpu_title.place(relx = 0.5,rely=0.2,anchor=tkinter.CENTER)
        


        cells = tkinter.Canvas(othello_cpu_page,width=400,height=400)
        for i in range(8):
            for j in range(8):
                cells.create_rectangle(i*50,j*50,50+i*50,50+j*50,fill = "green",outline="black")
        cells.place(x=350,y=50)

        
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
        print("move")
        page.tkraise()
    
    def getData(self,page,turn,level):
        data = ["f","s","p","n","w"]
        #page["text"] = "turn:" + data[turn] + " , level:" + data[level] 
        


class Othelloapp:
    def __init__(self):
        self.othello = othello = Othello()


if __name__ == "__main__":
    #start_game()
    #Othello()
    Othelloapp()

