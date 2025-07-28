import flet as ft
from apps.stats_scraper import get_stats
from apps.stats_news_scraper import get_news

class StockFunctions(ft.Container):
    def __init__ (self, icon: str, label: str):
        super().__init__()
        self.icon = icon
        self.label = label
        
    def render(self):
        return ft.Container(
            content=ft.ElevatedButton(
                width=260,
                height=40,
                bgcolor="#1F2134",
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=8),
                    text_style=ft.TextStyle(size=16, weight=ft.FontWeight.NORMAL),
                    color='#ffffff'
                ),
                content=ft.Row(
                    controls=[
                        ft.Icon(self.icon),
                        ft.Text(self.label)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ),
            padding=ft.padding.only(20)
        )
        
class StockInitialData(ft.Container):
    def __init__(self,text: str, label: str):
        super().__init__()
        self.label = label
        self.text = text
 
    def render(self):
        return ft.Container(
            width=120,
            height=30,
            border=ft.border.all(color="#ACACAC"),
            border_radius=3,
            bgcolor="#c3c3c3",
            content=ft.Row(
                controls=[
                    ft.Text(self.label),
                    ft.Text(self.text,color='#000000', weight=ft.FontWeight.BOLD, size=10)
                ]
            )
        )
        
def main (page: ft.Page):
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.fonts = {'NunitoSans': 'https://github.com/googlefonts/NunitoSans/tree/main/fonts/ttf/NunitoSans-Medium.ttf?raw=true'}
    page.theme = ft.Theme(font_family='NunitoSans')
    
    name_field = ft.Text(
        size=36,
        value='Vash San Juan',
        color='#000000',
        weight=ft.FontWeight.BOLD,
        font_family='NunitoSans'
    )
    
    first_column = ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(
                    width=300,
                    height=200,
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                height=80,
                                bgcolor="#785e5e",
                                content=ft.Column(
                                    controls=[

                                    ]
                                )
                            ),
                            ft.Container(
                                height=100,
                                padding=10,
                                content=ft.Column(
                                    controls=[
                                        ft.Text(
                                            value='Welcome!',
                                            weight=ft.FontWeight.NORMAL,
                                            size=24
                                            ),
                                        name_field
                                    ]
                                )
                                
                            )
                        ] 
                    ),
                    padding=ft.padding.only(top=0,bottom=0,left=10,right=0)
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.TextField(
                                            width=150,
                                            height=50,
                                            color='#000000',
                                            border_color=ft.Border('#000000'),
                                            bgcolor="#B3B3B3",
                                            focused_border_color="#000000",
                                            cursor_color="#000000",
                                            cursor_width=1,
                                            label='Enter Stock',
                                                label_style=ft.TextStyle(
                                                    color='#000000',
                                                    size=14,
                                                )
                                            ),
                                        ft.ElevatedButton(
                                            'Lock Symbol', 
                                            width=100, 
                                            height=50,
                                            style=ft.ButtonStyle(
                                                shape=ft.RoundedRectangleBorder(radius=5),
                                                text_style=ft.TextStyle(size=15, weight=ft.FontWeight.W_100, color='#ffffff')
                                                )
                                            )
                                    ]
                                ),
                                padding = ft.padding.only(top=15,left=20,right=20,bottom=20)
                            ),
                            StockFunctions(ft.Icons.BUSINESS,'Fundamentals').render(),
                            StockFunctions(ft.Icons.STACKED_LINE_CHART,'Technicals').render(),
                            StockFunctions(ft.Icons.LIBRARY_BOOKS_SHARP,'Dividend Report').render(),
                            StockFunctions(ft.Icons.NEWSPAPER,'News').render(),
                            StockFunctions(ft.Icons.INFO,'About the Company').render()
                        ]
                        
                    ),
                )
            ]
        ),
    )

    container = ft.Container(
        content = ft.Row(
            controls = [
                ft.Container(
                    bgcolor="#DCD6D6",
                    width=300,
                    height=650,
                    content=first_column
                    ),
                ft.Container(
                    bgcolor="#171717",
                    width=950,
                    height=650,
                    content=ft.Column(
                            controls=[
                                ft.Container(
                                    width=950,
                                    height=160,
                                    content=ft.Row(
                                        controls=[
                                            ft.Container(width=10),
                                            ft.Container(
                                                content=ft.Column(
                                                    controls=[
                                                        ft.Container(),
                                                            ft.Container(
                                                                bgcolor="#f4f4f4",
                                                                height=130,
                                                                width=900,
                                                                border_radius=(10),
                                                                content=ft.Row(
                                                                    controls=[
                                                                        ft.CircleAvatar(
                                                                            foreground_image_src='',
                                                                            bgcolor='#333333',
                                                                            radius=50
                                                                        ),
                                                                        ft.Container(
                                                                            content=ft.Column(
                                                                                width=330,
                                                                                spacing=2,
                                                                                controls=[
                                                                                    ft.Text('Company Name Goes Here',size=24,weight=ft.FontWeight.BOLD,color='#000000'),
                                                                                    ft.Text('Price Goes Here', size=20,weight=ft.FontWeight.W_500,color='#000000'),
                                                                                    ft.Text('At close at text goes here', size=14, color="#9F9F9F"),
                                                                                ]
                                                                            ),
                                                                        padding=ft.padding.only(top=20,bottom=0,left=0,right=20)
                                                                        ),
                                                                        ft.Container(
                                                                            content=ft.Column(
                                                                                controls=[
                                                                                    StockInitialData('OPEN:', '').render(),
                                                                                    StockInitialData('CLOSE:', '').render()
                                                                                ]
                                                                            ),
                                                                        padding=ft.padding.only(top=30,bottom=0,left=0,right=0)
                                                                        ),
                                                                        ft.Container(
                                                                            content=ft.Column(
                                                                                controls=[
                                                                                    StockInitialData('HIGH:', '').render(),
                                                                                    StockInitialData('LOW:', '').render()
                                                                                ]
                                                                            ),
                                                                        padding=ft.padding.only(top=30,bottom=0,left=0,right=0)
                                                                        ),
                                                                        ft.Container(
                                                                            content=ft.Column(
                                                                                controls=[
                                                                                    StockInitialData('FOREIGN:', '').render(),
                                                                                    StockInitialData('VOLUME:', '').render()
                                                                                ]
                                                                            ),
                                                                        padding=ft.padding.only(top=30,bottom=0,left=0,right=0)
                                                                        )                                                                                                                                                 
                                                                    ],
                                                                alignment=ft.CrossAxisAlignment.CENTER
                                                                ),
                                                            padding=ft.padding.only(left=20,right=0,top=0,bottom=0)
                                                            ),
                                                        ft.Container()
                                                    ]
                                                )
                                                ),
                                            ft.Container()
                                        ]
                                    )
                                )
                            ]
                    )
                )
            ]
        ),
        bgcolor="#171717",
        width=1250,
        height=650
    )

    page.add(container)

ft.app(target=main)