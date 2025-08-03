import flet as ft
import webbrowser
from apps.stats_scraper import get_stats
from apps.initial_data_scraper import get_initial_data
from apps.logo_scraper import get_company_logo
from apps.stock_utils import symbol_handler
from apps.div_yield import search_div
from apps.revenue_scraper import get_revenue, get_revenue_history
from apps.stats_news_scraper import get_news
from apps.financials_scraper import get_company_financials
from apps.about_company_scraper import get_company_profile, get_company_profile_origin
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
                bgcolor="#FFFFFF",
                on_click=self.on_click,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=8),
                    text_style=ft.TextStyle(size=16, weight=ft.FontWeight.NORMAL),
                    color='#1F2134'
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

def main (page: ft.Page):
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.fonts = {'NunitoSans': 'https://github.com/googlefonts/NunitoSans/tree/main/fonts/ttf/NunitoSans-Medium.ttf?raw=true'}
    page.theme = ft.Theme(font_family='NunitoSans')
    
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
            output_section.controls.clear()
            print(f"⚠️ Data retrieval failed for {handle_symbol}")
        output_section.controls.clear()
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
            width=900,
        )
        output_section.controls.clear()
        output_section.controls.append(dividend_table)
        page.update()
        
    def get_revenue_report(e):
        handle_symbol=symbol_handler(user_input.value).upper()
        df = get_revenue_history(handle_symbol)
        revenue_summary = get_revenue(handle_symbol)
        total_revenue = revenue_summary.get('Total Revenue')
        revenue_growth = revenue_summary.get('Revenue Growth')
        revenue_per_employee = revenue_summary.get('Revenue per Employee')
        total_employees = revenue_summary.get('Total Employees')
        market_cap = revenue_summary.get('Market Cap')
        
        total_revenue_widget = ft.Text('', color='#000000',size=44,weight=ft.FontWeight.BOLD)
        total_revenue_widget.value = total_revenue
        
        revenue_growth_widget = ft.Text('', color='#000000', size=24, weight=ft.FontWeight.BOLD)
        revenue_growth_widget.value = revenue_growth
        
        revenue_per_employee_widget = ft.Text('', color='#000000', size=24, weight=ft.FontWeight.BOLD)
        revenue_per_employee_widget.value = revenue_per_employee
        
        total_employees_widget = ft.Text('', color='#000000', size=24, weight=ft.FontWeight.BOLD)
        total_employees_widget.value = total_employees
        
        market_cap_widget = ft.Text('', color='#000000', size=24, weight=ft.FontWeight.BOLD)
        market_cap_widget.value = market_cap
        
        def headers(df : pd.DataFrame):
            return [ft.DataColumn(ft.Text(col)) for col in df.columns]
        
        def rows(df : pd.DataFrame):
            rows = []
            for index, row in df.iterrows():
                row_cells = [
                ft.DataCell(ft.Text(str(row[header]), color='#1F2134'))
                for header in df.columns
                ]
                rows.append(ft.DataRow(cells=row_cells))

            return rows
        
        revenue_history_table = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(     
                    padding=ft.padding.only(left=30, top=0, right=0, bottom=0),          
                    height=125,
                    width=900,
                        content=ft.Row(  
                            alignment = ft.CrossAxisAlignment.CENTER,                                                      
                            controls=[
                                ft.Column(                                    
                                    alignment = ft.MainAxisAlignment.CENTER,
                                    spacing=0,
                                    controls=[
                                        ft.Text('Total Revenue:', color='#000000', size=20),
                                        total_revenue_widget
                                    ]
                                ),
                                ft.Container(width=10),
                                ft.Container(
                                    padding=ft.padding.all(10),
                                    content=ft.Column(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        spacing=0,
                                        controls=[
                                            ft.Container(height=5),
                                            ft.Container(
                                                bgcolor="#DFDFDF",
                                                border_radius=5,
                                                border=ft.border.all(color="#ACACAC"),
                                                width=300,
                                                height=40,
                                                content=ft.Row(
                                                    alignment=ft.CrossAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.Text(' Revenue Growth: ', color="#555555", size=16),
                                                        revenue_growth_widget
                                                    ]
                                                )
                                            ),
                                            ft.Container(height=10),
                                            ft.Container(
                                                bgcolor="#DFDFDF",
                                                border_radius=5,
                                                border=ft.border.all(color="#ACACAC"),
                                                width=300,
                                                height=40,
                                                content=ft.Row(
                                                    alignment=ft.CrossAxisAlignment.CENTER,  
                                                    controls=[
                                                        ft.Text(' Revenue per Employee: ', color='#555555', size=16),
                                                        revenue_per_employee_widget
                                                    ]
                                                )
                                            )
                                        ]
                                    )
                                ),
                                ft.Container(
                                    padding=ft.padding.all(10),
                                    content=ft.Column(                                        
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        spacing=0,
                                        controls=[
                                            ft.Container(height=5),
                                            ft.Container(
                                                bgcolor="#DFDFDF",
                                                border_radius=5,
                                                border=ft.border.all(color="#ACACAC"),
                                                width=300,
                                                height=40,
                                                content=ft.Row(
                                                    alignment=ft.CrossAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.Text(' Total Employees: ', color="#555555", size=16),
                                                        total_employees_widget
                                                    ]
                                                )
                                            ),
                                            ft.Container(height=10),
                                            ft.Container(
                                                bgcolor="#DFDFDF",
                                                border_radius=5,
                                                border=ft.border.all(color="#ACACAC"),
                                                width=300,
                                                height=40,
                                                content=ft.Row(
                                                    alignment=ft.CrossAxisAlignment.CENTER,  
                                                    controls=[
                                                        ft.Text(' Market Cap: ', color='#555555', size=16),
                                                        market_cap_widget
                                                    ]
                                                )
                                            )
                                        ]
                                    )
                                )                                
                            ]
                        )
                    ),
            ft.DataTable(
                columns=headers(df),
                rows=rows(df),
                column_spacing=20,
                heading_row_color='#1F2134',
                data_row_color={ft.ControlState.HOVERED: "0x30CCCCCC"},
                show_checkbox_column=True,
                border=ft.border.all(1, ft.Colors.GREY),
                height=300,
                width=900,
            )
                ]
            )

        )
        
        output_section.controls.clear()
        output_section.controls.append(revenue_history_table)
        page.update()

    def get_latest_news(e):
        handle_symbol = symbol_handler(user_input.value).upper()
        news_result = get_news(handle_symbol)
        date_1 = news_result.get('news_src_date_1')
        news_title_1 = news_result.get('news_headline_1')
        summary_1 = news_result.get('news_summary_1')
        featured_image_1 = news_result.get('news_img_1')
        news_link_1 = news_result.get('news_link_1')
        
        date_2 = news_result.get('news_src_date_2')
        news_title_2 = news_result.get('news_headline_2')
        summary_2 = news_result.get('news_summary_2')
        featured_image_2 = news_result.get('news_img_2')
        news_link_2 = news_result.get('news_link_2')
        
        def open_website_1(e):
            webbrowser.open(news_link_1)
            
        def open_website_2(e):
            webbrowser.open(news_link_2)
        
        news_date_widget_1 = ft.Text('', size=12, color='#333333')
        news_title_widget_1 = ft.Text('', size=22, color='#000000', weight=ft.FontWeight.BOLD, expand=True, text_align=ft.TextAlign.LEFT)
        news_summary_widget_1 = ft.Text('', size=15, color='#000000', expand=True, text_align=ft.TextAlign.LEFT)
        news_featured_image_widget_1 = ft.Image(src='', height=180, width=300, fit=ft.ImageFit.COVER, border_radius=5)
        news_link_widget_1 = ft.ElevatedButton(text='READ MORE', icon=ft.Icons.OPEN_IN_BROWSER, on_click=open_website_1)
        
        news_date_widget_1.value = date_1
        news_title_widget_1.value = news_title_1
        news_summary_widget_1.value = summary_1
        news_featured_image_widget_1.src = featured_image_1
        
        news_date_widget_2 = ft.Text('', size=12, color='#333333')
        news_title_widget_2 = ft.Text('', size=22, color='#000000', weight=ft.FontWeight.BOLD, expand=True, text_align=ft.TextAlign.LEFT)
        news_summary_widget_2 = ft.Text('', size=15, color='#000000', expand=True, text_align=ft.TextAlign.LEFT)
        news_featured_image_widget_2 = ft.Image(src='', height=180, width=300, fit=ft.ImageFit.COVER, border_radius=5)
        news_link_widget_2 = ft.ElevatedButton(text='READ MORE', icon=ft.Icons.OPEN_IN_BROWSER, on_click=open_website_2)
        
        news_date_widget_2.value = date_2
        news_title_widget_2.value = news_title_2
        news_summary_widget_2.value = summary_2
        news_featured_image_widget_2.src = featured_image_2
        
        news_section = ft.Container(
            padding=ft.padding.all(10),
            width=900,
            height=435,
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            news_featured_image_widget_1,
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        news_date_widget_1,                                
                                        ft.Container(
                                            width=580,
                                            content=ft.Column(
                                                controls=[
                                                news_title_widget_1,
                                                news_summary_widget_1
                                                ]
                                            )
                                        ),
                                        news_link_widget_1
                                    ]
                                )
                            )
                        ]
                    ),
                    ft.Container(height=5),
                    ft.Row(
                        controls=[
                            news_featured_image_widget_2,
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        news_date_widget_2,                                
                                        ft.Container(
                                            width=580,
                                            content=ft.Column(
                                                controls=[
                                                news_title_widget_2,
                                                news_summary_widget_2
                                                ]
                                            )
                                        ),
                                        news_link_widget_2
                                    ]
                                )
                            )
                        ]
                    )
                ]
            )
        )
        output_section.controls.clear()
        output_section.controls.append(news_section)
        page.update()
    
    
    def get_fundamentals(e):
        handle_symbol = symbol_handler(user_input.value).upper()    
        df = get_company_financials(handle_symbol)
        
    
        def headers(df : pd.DataFrame):
            return [ft.DataColumn(ft.Text(col)) for col in df.columns]
        
        def rows(df : pd.DataFrame):
            rows = []
            for index, row in df.iterrows():
                row_cells = [
                ft.DataCell(ft.Text(str(row[header]), color='#1F2134'))
                for header in df.columns
                ]
                rows.append(ft.DataRow(cells=row_cells))
                
            return rows
        
        fundamentals_history_table = ft.Container(
            content=ft.Column(
                controls=[
                    ft.DataTable(
                        columns=headers(df),
                        rows=rows(df),
                        column_spacing=20,
                        heading_row_color='#1F2134',
                        data_row_color={ft.ControlState.HOVERED: "0x30CCCCCC"},
                        show_checkbox_column=True,
                        border=ft.border.all(1, ft.Colors.GREY),
                        width=900,
                    )
                ]
            )
        )


        output_section.controls.clear()
        output_section.controls.append(fundamentals_history_table)
        page.update()

    def get_company_about(e):
        handle_symbol = symbol_handler(user_input.value).upper()
        company_profile = get_company_profile(handle_symbol)
        df = get_company_profile_origin(handle_symbol)
        company_name = company_profile.get('company_name')
        company_about = company_profile.get('company_about')
        
        company_name_widget = ft.Text(value='', size=24, color='#000000', weight=ft.FontWeight.BOLD)
        company_about_widget = ft.Text(value='', size=16, color="#727272")
        
        company_name_widget.value = company_name
        company_about_widget.value = company_about
            
        def header(df: pd.DataFrame):
            return [ft.DataColumn(ft.Text('')) for col in df.columns]
        
        def rows(df: pd.DataFrame):
            rows = []
            for index, row in df.iterrows():
                row_cells = [
                    ft.DataCell(ft.Text(str(row[header]),color='#000000'))
                    for header in df.columns
                ]
                rows.append(ft.DataRow(cells=row_cells))
        
            return rows
            
        about_origin = ft.DataTable(
            columns=header(df),
            rows=rows(df),
            width=200,
            column_spacing=20,
            heading_row_color='#1F2134',
            data_row_color={ft.ControlState.HOVERED: "0x30CCCCCC"},
            show_checkbox_column=True,
            border=ft.border.all(1, ft.Colors.GREY)
            )

        company_about_section =  ft.Container(
            padding=ft.padding.all(10),
            width=900,
            height=435,
            content=ft.Row(
                controls=[
                    ft.Container(
                        width=700,
                        content=ft.Column(
                                controls=[
                                    company_name_widget,
                                    company_about_widget
                                ]
                            )
                        ),
                    ft.Container(
                        content=about_origin
                    )
                ]
            )
        )
        output_section.controls.clear()
        output_section.controls.append(company_about_section)
        page.update()

#-------------------------------------------VARIABLES-------------------------------------------#

    button_revenue_report = StockFunctions(ft.Icons.STACKED_LINE_CHART,'Revenue Report', on_click=get_revenue_report)
    button_dividend_report = StockFunctions(ft.Icons.LIBRARY_BOOKS_SHARP,'Dividend Report', on_click=generate_dividend_report)
    button_news_report = StockFunctions(ft.Icons.NEWSPAPER,'News', on_click=get_latest_news)
    button_financial_report = StockFunctions(ft.Icons.BUSINESS,'Fundamentals', on_click=get_fundamentals)
    button_about_company = StockFunctions(ft.Icons.INFO,'About the Company', on_click=get_company_about)

    open_field = ft.Text(value = '', color='#000000', weight=ft.FontWeight.BOLD, size=16)
    close_field = ft.Text(value = '', color='#000000', weight=ft.FontWeight.BOLD, size=16)   
    high_field = ft.Text(value = '', color='#000000', weight=ft.FontWeight.BOLD, size=16)   
    low_field = ft.Text(value = '', color='#000000', weight=ft.FontWeight.BOLD, size=16)
    wk_high_field = ft.Text(value = '', color='#000000', weight=ft.FontWeight.BOLD, size=16)
    wk_low_field = ft.Text(value = '', color='#000000', weight=ft.FontWeight.BOLD, size=16)
    company_name = ft.Text('Company Name',size=20,weight=ft.FontWeight.BOLD,color='#000000')
    latest_value = ft.Text('---', size=24,weight=ft.FontWeight.BOLD,color='#000000')
    latest_date = ft.Text('At close at text goes here', size=14, color="#545454")

    output_section = ft.Column(
                        controls=[],
                        width=900,
                        height=435,
                        scroll="auto"
                    )
    
    
    dividend_report_section = ft.Container(
                                    bgcolor='#f4f4f4',
                                    width=900,
                                    height=435,
                                    border_radius=(10),
                                    content=output_section
                                )
    
    lock_stock = ft.ElevatedButton(
                    'Lock Symbol', 
                    width=100, 
                    height=50,
                    on_click=lock_stock_symbol,
                    color='#1F2134',
                    bgcolor="#8EC63F",
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=5),
                        text_style=ft.TextStyle(size=14, weight=ft.FontWeight.W_500, color="#000000")
                        )
                    )
    
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
                    color="#000000",
                    border_color=ft.Border(1,"#FFFFFF"),
                    bgcolor="#B3B3B3",
                    focused_border_color="#FFFFFF",
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
                    color="#8EC63F",
                    weight=ft.FontWeight.BOLD,
                    font_family='NunitoSans'
                    )
    
    #-------------------------------------------START OF UI-------------------------------------------#
    
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
                                )
                            ),
                            ft.Container(
                                height=100,
                                padding=10,
                                content=ft.Column(
                                    controls=[
                                        ft.Text(
                                            value='Welcome!',
                                            color="#FFFFFF",
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
                            button_financial_report.render(),
                            button_revenue_report.render(),
                            button_dividend_report.render(),
                            button_news_report.render(),
                            button_about_company.render()
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
                    bgcolor="#0F0F0F",
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
                                                                                    bgcolor="#DFDFDF",
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
                                                                                    bgcolor="#DFDFDF",
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
                                                                                    bgcolor="#DFDFDF",
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
                                                                                    bgcolor="#DFDFDF",
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
                                                                                    bgcolor="#DFDFDF",
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
                                                                                    bgcolor="#DFDFDF",
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
                                dividend_report_section
                            ]
                    )
                )
            ]
        ),
        bgcolor="#1B1B1B",
        border_radius=(10),
        width=1250,
        height=650
    )

    page.add(container)

ft.app(target=main)