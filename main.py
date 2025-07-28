import flet as ft
from apps.stats_scraper import get_stats
from apps.stats_news_scraper import get_news
from apps.initial_data_scraper import get_initial_data
from apps.logo_scraper import get_company_logo
from apps.stock_utils import symbol_handler

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
                    ft.Text(self.text,color='#000000', weight=ft.FontWeight.BOLD, size=10),
                    ft.Text(self.label)
                ]
            )
        )
        
def main (page: ft.Page):
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.fonts = {'NunitoSans': 'https://github.com/googlefonts/NunitoSans/tree/main/fonts/ttf/NunitoSans-Medium.ttf?raw=true'}
    page.theme = ft.Theme(font_family='NunitoSans')
    
    avatar = ft.CircleAvatar(
                bgcolor="#FFFFFF",
                radius=50,
                content=ft.CircleAvatar(
                    foreground_image_src='',
                    bgcolor="#FFFFFF",
                    radius=30
                    )
                )

    user_input = ft.TextField(
                    width=150,
                    height=50,
                    color='#000000',
                    border_color=ft.Border('#000000'),
                    bgcolor="#B3B3B3",
                    focused_border_color="#000000",
                    cursor_color="#000000",
                    cursor_width=1,
                    label='Enter Stock',
                    value='',
                        label_style=ft.TextStyle(
                            color='#000000',
                            size=14,
                        )
                    )
    
    name_field = ft.Text(
                    size=36,
                    value='Ivan San Juan',
                    color='#000000',
                    weight=ft.FontWeight.BOLD,
                    font_family='NunitoSans'
                    )
    
    open_field = StockInitialData('OPEN:', '').render()
    
    def lock_stock_symbol(e):
        handle_symbol=symbol_handler(user_input.value).upper()
        image_url = get_company_logo(handle_symbol)
        avatar.foreground_image_src = image_url
        initial_data = get_initial_data(handle_symbol)
        open_value = initial_data.get('Open', 'N/A').strip()
        close = initial_data.get('Close', 'N/A').strip()
        high = initial_data.get('High', 'N/A').strip()
        low = initial_data.get('Low', 'N/A').strip()
        high_52 = initial_data.get('wk-high', 'N/A').strip()
        low_52 = initial_data.get('wk-low', 'N/A').strip()
        if not initial_data:
            print(f"⚠️ Data retrieval failed for {handle_symbol}")

        
        
        page.update()

    lock_stock = ft.ElevatedButton(
                    'Lock Symbol', 
                    width=100, 
                    height=50,
                    on_click=lock_stock_symbol,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=5),
                        text_style=ft.TextStyle(size=15, weight=ft.FontWeight.W_100, color='#ffffff')
                        )
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
                                            color='#000000',
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
                                        user_input,
                                        lock_stock
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
                    border_radius=10,
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
                                                                        avatar,
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
                                                                                    open_field,
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
                                                                                    StockInitialData('52wk HIGH:', '').render(),
                                                                                    StockInitialData('52wk LOW:', '').render()
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