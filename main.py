import flet as ft
from apps.stats_scraper import get_stats
from apps.stats_news_scraper import get_news
from apps.initial_data_scraper import get_initial_data
from apps.logo_scraper import get_company_logo
from apps.stock_utils import symbol_handler
from apps.div_yield import search_div
import pandas as pd

class StockFunctions(ft.Container):
    def __init__ (self, icon: str, label: str, on_click=None):
        super().__init__()
        self.icon = icon
        self.label = label
        self.on_click = on_click
        
    def render(self):
        return ft.Container(
            content=ft.ElevatedButton(
                width=260,
                height=40,
                bgcolor="#1F2134",
                on_click=self.on_click,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=8),
                    text_style=ft.TextStyle(size=16, weight=ft.FontWeight.NORMAL),
                    color='#ffffff'
                ),
                content=ft.Row(
                    controls=[
                        ft.Icon(self.icon),
                        ft.Text(self.label),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ),
            padding=ft.padding.only(20)
        )
        
# class StockInitialData(ft.Container):
#     def __init__(self,text: str, value):
#         super().__init__()
#         self.value = value
#         self.text = text
#         self.widget = ft.Container(
#             width=120,
#             height=30,
#             border=ft.border.all(color="#ACACAC"),
#             border_radius=3,
#             bgcolor="#c3c3c3",
#             content=ft.Row(
#                 controls=[
#                     ft.Text(self.text,color='#000000', weight=ft.FontWeight.BOLD, size=10),
#                     ft.Text(self.value)
#                 ]
#             )
#         )

#     def get_widget(self):
#         return self.widget



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
                    radius=20
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
    
    open_field = ft.Text(value = '', color='#000000', weight=ft.FontWeight.BOLD, size=16)
    close_field = ft.Text(value = '', color='#000000', weight=ft.FontWeight.BOLD, size=16)   
    high_field = ft.Text(value = '', color='#000000', weight=ft.FontWeight.BOLD, size=16)   
    low_field = ft.Text(value = '', color='#000000', weight=ft.FontWeight.BOLD, size=16)
    wk_high_field = ft.Text(value = '', color='#000000', weight=ft.FontWeight.BOLD, size=16)
    wk_low_field = ft.Text(value = '', color='#000000', weight=ft.FontWeight.BOLD, size=16)
    
    company_name = ft.Text('Company Name',size=20,weight=ft.FontWeight.BOLD,color='#000000')
    latest_value = ft.Text('---', size=24,weight=ft.FontWeight.BOLD,color='#000000')
    latest_date = ft.Text('At close at text goes here', size=14, color="#545454")
    
    def lock_stock_symbol(e):
        handle_symbol=symbol_handler(user_input.value).upper()
        image_url = get_company_logo(handle_symbol)
        avatar.foreground_image_src = image_url
        initial_data = get_initial_data(handle_symbol)
        company_name.value = initial_data.get('Company Name', 'N/A').strip()
        latest_date.value = initial_data.get('Latest Date').strip()
        open = initial_data.get('Open', 'N/A').strip()
        close = initial_data.get('Close', 'N/A').strip()
        high = initial_data.get('High', 'N/A').strip()
        low = initial_data.get('Low', 'N/A').strip()
        high_52 = initial_data.get('wk-high', 'N/A').strip()
        low_52 = initial_data.get('wk-low', 'N/A').strip()
        open_field.value = open
        close_field.value = close
        latest_value.value = close
        high_field.value = high
        low_field.value = low
        wk_high_field.value = high_52
        wk_low_field.value = low_52
        
        if not initial_data:
            print(f"⚠️ Data retrieval failed for {handle_symbol}")
        
        page.update()
        
    def generate_dividend_report(e):
        handle_symbol=symbol_handler(user_input.value).upper()
        df = search_div(handle_symbol)
        dividend_table = ft.DataTable(
            columns = [ft.DataColumn(ft.Text(col)) for col in df.columns],
            rows = [
                ft.DataRow(
                    cells=[ft.DataCell(ft.Text(str(row[col]),color='#1F2134')) for col in df.columns]
                )
                for _ , row in df.iterrows()
            ],
            column_spacing=20,
            heading_row_color='#1F2134',
            data_row_color={ft.ControlState.HOVERED: "0x30CCCCCC"},
            show_checkbox_column=True,
            border=ft.border.all(1, ft.Colors.GREY),
            border_radius=ft.border_radius.all(10),
            width=900,
        )
        dividend_output_column.controls.clear()
        dividend_output_column.controls.append(dividend_table)
        page.update()

    dividend_output_column = ft.Column(
    controls=[],
    width=900,
    height=435,
    scroll="auto"
    )

    
    button_dividend_report = StockFunctions(ft.Icons.LIBRARY_BOOKS_SHARP,'Dividend Report', on_click=generate_dividend_report)
    
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
                            button_dividend_report.render(),
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
                    bgcolor="#CBDEEA",
                    width=300,
                    height=650,
                    border_radius=ft.border_radius.only(top_left=10,bottom_left=10,top_right=0,bottom_right=0),
                    content=first_column
                    ),
                ft.Container(
                    width=950,
                    height=650,
                    padding=ft.padding.only(left=10,bottom=0,top=20,right=0),
                    content=ft.Column(
                            controls=[
                                ft.Container(
                                    width=950,
                                    height=160,
                                    content=ft.Row(
                                        controls=[
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
                                                                                    company_name,                                                                                    
                                                                                    ft.Container(
                                                                                        width=30,
                                                                                        content=ft.Row(
                                                                                            width=50,
                                                                                            controls=[
                                                                                                ft.Text('₱', size=24,weight=ft.FontWeight.BOLD,color='#000000'),
                                                                                                latest_value
                                                                                            ]
                                                                                        )
                                                                                    ),
                                                                                    latest_date,
                                                                                ]
                                                                            ),
                                                                        padding=ft.padding.only(top=20,bottom=0,left=0,right=20)
                                                                        ),
                                                                        ft.Container(
                                                                            content=ft.Column(
                                                                                controls=[
                                                                                    ft.Container(
                                                                                    padding = ft.padding.only(left=5,top=0,right=0,bottom=0),
                                                                                    width=120,
                                                                                    height=30,
                                                                                    border=ft.border.all(color="#ACACAC"),
                                                                                    border_radius=3,
                                                                                    bgcolor="#c3c3c3",
                                                                                    content=ft.Row(
                                                                                        controls=[
                                                                                            ft.Text(value='OPEN:', color='#000000', weight=ft.FontWeight.BOLD, size=10),
                                                                                            open_field
                                                                                        ]
                                                                                    )
                                                                                ),
                                                                                    ft.Container(
                                                                                    padding = ft.padding.only(left=5,top=0,right=0,bottom=0),
                                                                                    width=120,
                                                                                    height=30,
                                                                                    border=ft.border.all(color="#ACACAC"),
                                                                                    border_radius=3,
                                                                                    bgcolor="#c3c3c3",
                                                                                    content=ft.Row(
                                                                                        controls=[
                                                                                            ft.Text(value='CLOSE:', color='#000000', weight=ft.FontWeight.BOLD, size=10),
                                                                                            close_field
                                                                                        ]
                                                                                    )
                                                                                )                                                                                ]
                                                                            ),
                                                                        padding=ft.padding.only(top=30,bottom=0,left=0,right=0)
                                                                        ),
                                                                        ft.Container(
                                                                            content=ft.Column(
                                                                                controls=[
                                                                                    ft.Container(
                                                                                    padding = ft.padding.only(left=5,top=0,right=0,bottom=0),
                                                                                    width=120,
                                                                                    height=30,
                                                                                    border=ft.border.all(color="#ACACAC"),
                                                                                    border_radius=3,
                                                                                    bgcolor="#c3c3c3",
                                                                                    content=ft.Row(
                                                                                        controls=[
                                                                                            ft.Text(value='HIGH:', color='#000000', weight=ft.FontWeight.BOLD, size=10),
                                                                                            high_field
                                                                                        ]
                                                                                    )
                                                                                ),
                                                                                    ft.Container(
                                                                                    padding = ft.padding.only(left=5,top=0,right=0,bottom=0),
                                                                                    width=120,
                                                                                    height=30,
                                                                                    border=ft.border.all(color="#ACACAC"),
                                                                                    border_radius=3,
                                                                                    bgcolor="#c3c3c3",
                                                                                    content=ft.Row(
                                                                                        controls=[
                                                                                            ft.Text(value='LOW:', color='#000000', weight=ft.FontWeight.BOLD, size=10),
                                                                                            low_field
                                                                                        ]
                                                                                    )
                                                                                )
                                                                                ]
                                                                            ),
                                                                        padding=ft.padding.only(top=30,bottom=0,left=0,right=0)
                                                                        ),
                                                                        ft.Container(
                                                                            content=ft.Column(
                                                                                controls=[
                                                                                    ft.Container(
                                                                                    padding = ft.padding.only(left=5,top=0,right=0,bottom=0),
                                                                                    width=130,
                                                                                    height=30,
                                                                                    border=ft.border.all(color="#ACACAC"),
                                                                                    border_radius=3,
                                                                                    bgcolor="#c3c3c3",
                                                                                    content=ft.Row(
                                                                                        controls=[
                                                                                            ft.Text(value='52wk-HIGH:', color='#000000', weight=ft.FontWeight.BOLD, size=10),
                                                                                            wk_high_field
                                                                                        ]
                                                                                    )
                                                                                ),
                                                                                    ft.Container(
                                                                                    padding = ft.padding.only(left=5,top=0,right=0,bottom=0),
                                                                                    width=130,
                                                                                    height=30,
                                                                                    border=ft.border.all(color="#ACACAC"),
                                                                                    border_radius=3,
                                                                                    bgcolor="#c3c3c3",
                                                                                    content=ft.Row(
                                                                                        controls=[
                                                                                            ft.Text(value='52wk-LOW:', color='#000000', weight=ft.FontWeight.BOLD, size=10),
                                                                                            wk_low_field
                                                                                        ]
                                                                                    )
                                                                                )
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
                                ),
                                ft.Container(
                                    bgcolor='#f4f4f4',
                                    width=900,
                                    height=435,
                                    border_radius=(10),
                                    content=dividend_output_column
                                    
                                )
                            ]
                    )
                )
            ]
        ),
        bgcolor="#DCDCDC",
        border_radius=(10),
        width=1250,
        height=650
    )

    page.add(container)

ft.app(target=main)