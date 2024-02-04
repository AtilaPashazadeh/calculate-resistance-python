import flet as ft
from reportlab.pdfgen import canvas
from tkinter import filedialog 
import time
def main(page: ft.Page):
    color_num={
        "black":0,
        "brown":1,
        "red":2,
        "orange":3,
        "yellow":4,
        "green":5,
        "blue":6,
        "purple":7,
        "gray":8,
        "white":9
    }
    color_num1={
        "black":'1',
        "brown":'10^1',
        "red":'10^2',
        "orange":'10^3',
        "yellow":'10^4',
        "green":'10^5',
        "blue":'10^6',
        "purple":'10^7',
        "gray":'10^8',
        "white":'10^9',
        "golden":'10^-1',
        "silver":'10^-2'
    }
    color_num2={
        "#FFC436":"%5",
        "#B6BBC4":"%10",
        "#F0ECE5":"%20"
    }
    
    def answer(e):
        
        answer_1=(str(color_num.get(list_first_color.value))+str(color_num.get(list_secend_color.value))+"x"+color_num1.get(list_third_color.value))
        tol=(color_num2.get(list_last_color.value))
        dlg = ft.AlertDialog(
            title=ft.Text("Resistance: %s Ω\nTolerance: %s"%(answer_1,tol))
        )
        page.dialog = dlg
        dlg.open = True
        page.update()
    page.window_width=400
    page.window_height=460
    def last_color_change(e):
        last_color_show.bgcolor=list_last_color.value
        list_last_color.color=list_last_color.value
        page.update()
    def third_color_change(e):
        third_color_show.bgcolor=list_third_color.value
        list_third_color.color=list_third_color.value
        page.update()
    def secend_color_change(e):
        secend_color_show.bgcolor=list_secend_color.value
        list_secend_color.color=list_secend_color.value
        page.update()
    def first_color_change(e):
        first_color_show.bgcolor=list_first_color.value
        list_first_color.color=list_first_color.value
        page.update()
    last_color=ft.Text(value="  Last Line Color :")
    fist_color=ft.Text(value=" First Line Color     :")
    third_color=ft.Text(value=" Third Line Color    :")
    secend_color=ft.Text(value=" Secend Line Color :")
    secend_color_show=ft.ElevatedButton(
        text="",
        bgcolor="black",
        style=ft.ButtonStyle(
            side={
                ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLUE)
            },
            shape=ft.CircleBorder(), padding=30
        ),
        
    )
    third_color_show=ft.ElevatedButton(
        text="",
        bgcolor="black",
        style=ft.ButtonStyle(
            side={
                ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLUE)
            },
            shape=ft.CircleBorder(), padding=30
        ),
        
    )
    last_color_show=ft.ElevatedButton(
        text="",
        bgcolor="#FFC436",
        style=ft.ButtonStyle(
            side={
                ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLUE)
            },
            shape=ft.CircleBorder(), padding=30
        ),

    )
    first_color_show=ft.ElevatedButton(
        style=ft.ButtonStyle(
            side={
                ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLUE)
            },
            shape=ft.CircleBorder(), padding=30
        ),
        text="",
        bgcolor="black",
        
        
    )
    def menu_info(e):
        dlg = ft.AlertDialog(
            title=ft.Text("Programmer: Atila Pashazadeh\nLanguage: Python\nFramework: Flet")
        )
    def menu_hlp(e):
        dlg = ft.AlertDialog(
            title=ft.Text("HELP:\nTo calculate the resistance. Just enter the color of the first,second,third and last lines.")
        )
        page.dialog = dlg
        dlg.open = True
        page.update()
    def save(e):
        answer_1=(str(color_num.get(list_first_color.value))+str(color_num.get(list_secend_color.value))+"x"+color_num1.get(list_third_color.value))
        tol=(color_num2.get(list_last_color.value))
        save_path=filedialog.askdirectory(title='save file')
        c = canvas.Canvas("%s\output.pdf"%(save_path))
        c.drawString(100, 750, "Resistance: %s Ω\nTolerance: %s"%(answer_1,tol))
        
        c.save()
        
    menu = ft.PopupMenuButton(
        items=[
            ft.PopupMenuItem(icon=ft.icons.HELP,text='HELP',on_click=menu_hlp),
            ft.PopupMenuItem(icon=ft.icons.INFO_SHARP,text="INFO",on_click=menu_info),
            ft.PopupMenuItem(icon=ft.icons.HELP,text='Print',on_click=save)
        
        ]
    )
    list_first_color=ft.Dropdown(
        options=[
            ft.dropdown.Option("black","BLACK"),
            ft.dropdown.Option("brown","BROWN"),
            ft.dropdown.Option("red","RED"),
            ft.dropdown.Option("orange","ORANGE"),
            ft.dropdown.Option("yellow","YELLOW"),
            ft.dropdown.Option("green","GREEN"),
            ft.dropdown.Option("blue","BLUE"),
            ft.dropdown.Option("purple","PURPLE"),
            ft.dropdown.Option("gray","GRAY"),
            ft.dropdown.Option("white","WHITE")
        ],
        width=100,
        value="black",
        border_color="green",
        on_change=first_color_change
    )
    page.theme_mode=ft.ThemeMode.DARK
    page.splash = ft.ProgressBar(visible=False)
    
    def change_theme(e):
        page.splash.visible=True
        page.theme_mode= 'dark' if page.theme_mode == 'light' else 'light'
        button.bgcolor= {ft.MaterialState.HOVERED: ft.colors.BLUE_900, "": ft.colors.RED} if page.theme_mode=="dark" else {ft.MaterialState.HOVERED: ft.colors.RED, "": ft.colors.BLUE_900}
        App_bar.bgcolor="blue" if page.theme_mode=="dark" else ft.colors.RED
        button.color={ft.MaterialState.HOVERED: ft.colors.RED, "": ft.colors.BLUE_900} if page.theme_mode== "dark" else {ft.MaterialState.HOVERED: ft.colors.BLUE_900, "": ft.colors.RED}
        list_first_color.border_color="green" if page.theme_mode=="dark" else "purple"
        list_secend_color.border_color="green" if page.theme_mode=="dark" else "purple"
        list_third_color.border_color="green" if page.theme_mode=="dark" else "purple"
        list_last_color.border_color="green" if page.theme_mode=="dark" else "purple"
        page.bgcolor="#E5D4FF" if page.theme_mode =="light" else ft.colors.BACKGROUND
        
        page.update()
        time.sleep(0.5)
        mode.selected=not mode.selected
        page.splash.visible=False
        page.update()
    mode=ft.IconButton(
        ft.icons.LIGHT_MODE,
        on_click=change_theme,
        selected_icon=ft.icons.DARK_MODE,
        style=ft.ButtonStyle(
            color={"":ft.colors.BLACK,"selected":ft.colors.WHITE}
        )

    )
    App_bar=ft.AppBar(
        bgcolor='blue',
        title=ft.Text("محاسبه مقاومت"),
        center_title=True,
        leading=menu,
        actions=[
                mode
            ]
    )
    list_third_color=ft.Dropdown(
        options=[
            ft.dropdown.Option("black","BLACK"),
            ft.dropdown.Option("brown","BROWN"),
            ft.dropdown.Option("red","RED"),
            ft.dropdown.Option("orange","ORANGE"),
            ft.dropdown.Option("yellow","YELLOW"),
            ft.dropdown.Option("green","GREEN"),
            ft.dropdown.Option("blue","BLUE"),
            ft.dropdown.Option("purple","PURPLE"),
            ft.dropdown.Option("gray","GRAY"),
            ft.dropdown.Option("white","WHITE"),
            ft.dropdown.Option("#FFC436","GOLDEN"),
            ft.dropdown.Option("#B6BBC4","SILVER"),
        ],
        width=100,
        border_color="green",
        value="black",
        
        on_change=third_color_change
    )
    list_secend_color=ft.Dropdown(
        options=[
            ft.dropdown.Option("black","BLACK"),
            ft.dropdown.Option("brown","BROWN"),
            ft.dropdown.Option("red","RED"),
            ft.dropdown.Option("orange","ORANGE"),
            ft.dropdown.Option("yellow","YELLOW"),
            ft.dropdown.Option("green","GREEN"),
            ft.dropdown.Option("blue","BLUE"),
            ft.dropdown.Option("purple","PURPLE"),
            ft.dropdown.Option("gray","GRAY"),
            ft.dropdown.Option("white","WHITE")
        ],
        width=100,
        border_color="green",
        value="black",
        
        on_change=secend_color_change
    )
    list_last_color=ft.Dropdown(
        options=[
            
            ft.dropdown.Option("#FFC436","GOLDEN"),
            ft.dropdown.Option("#B6BBC4","SILVER"),
            ft.dropdown.Option("#F0ECE5","COLORLESS"),
            
        ],
        width=120,
        border_color="green",
        value="#FFC436",
        
        on_change=last_color_change
    )
    button=ft.ElevatedButton(
                text="ENTER",
                width=page.window_width-35,
                bgcolor={ft.MaterialState.HOVERED: ft.colors.BLUE_900, "": ft.colors.RED},
                color={ft.MaterialState.HOVERED: ft.colors.RED, "": ft.colors.BLUE_900},
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),
                height=50,
                on_click=answer
            )
    
    page.add(
        App_bar,
        ft.Row([
            fist_color,
            list_first_color,
            first_color_show
            
        ],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            secend_color,
            list_secend_color,
            secend_color_show
        ],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            third_color,
            list_third_color,
            third_color_show
        ],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            last_color,
            list_last_color,
            last_color_show
        ],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            button
        ])
    )

ft.app(target=main)