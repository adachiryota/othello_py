import tkinter
from tkinter import font
""" 
# ウィンドウ（フレーム）の作成
root = tkinter.Tk()

# ウィンドウの名前を設定
root.title("4colors")

# ウィンドウの大きさを設定(横×縦)
root.geometry("800x600")

stat1 = tkinter.Label(text = u"test")
#stat1.pack()
stat1.place(relx =0.5,rely=0.5)

# イベントループ（TK上のイベントを捕捉し、適切な処理を呼び出すイベントディスパッチャ）
root.mainloop() """

class Othello:
    def __init__(self):
        self.main = main = Tkview()

class Tkview:
    def __init__(self):
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

        font_button = font.Font(size=10)
        back_mode_button = tkinter.Button(battle_cpu_page,text=u"-戻る-",font=font_button,command=lambda: self.movePage(mode_page))
        back_mode_button.place(relx=0.5,rely=0.6,anchor=tkinter.CENTER)

        battle_button = tkinter.Button(battle_cpu_page,text=u"-ゲームスタート-",font=font_button,command=lambda: self.movePage(othello_cpu_page))
        battle_button.place(relx=0.5,rely=0.7,anchor=tkinter.CENTER)     
        battle_cpu_page.grid(row=0, column=0, sticky="nsew")


        #CPU対戦画面
        othello_cpu_page = tkinter.Frame(window)
        font_text = font.Font(family="Times",size=50,weight="bold")
        othello_cpu_title = tkinter.Label(othello_cpu_page,text = u"cpu",font=font_text)        
        othello_cpu_title.place(relx = 0.5,rely=0.2,anchor=tkinter.CENTER)

        font_button = font.Font(size=10)
        change_color1_button = tkinter.Button(othello_cpu_page,text=u"-赤-",font=font_button,command=lambda: self.movePage(start_page))
        change_color1_button.place(relx=0.5,rely=0.6,anchor=tkinter.CENTER)

        change_color2_button = tkinter.Button(othello_cpu_page,text=u"-オレンジ-",font=font_button,command=lambda: self.movePage(result_page))
        change_color2_button.place(relx=0.5,rely=0.7,anchor=tkinter.CENTER)

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


if __name__ == "__main__":
    #start_game()
    Othello()

