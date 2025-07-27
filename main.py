from flet import *
from apps.stats_scraper import get_stats
from apps.stats_news_scraper import get_news

symbol_field = TextField()

def main(page: Page):
    BGM = "#5e2760"
    SBGM = "#dcdcdc"
    TEXT = '#fedc97'
    
    symbol_field = TextField(
            label='Enter Stock Symbol',
            label_style=TextStyle(size=14),
            width=200,
            multiline=False,
            autofocus=True,
            border_color = '#ffffff',
            bgcolor="#3D3535"
        )
    result_text = Text(
            "Waiting for Data...",
            max_lines=10,
            overflow=TextOverflow.ELLIPSIS,
            size=20,
            color='#000000'
        )
    company_name = Text(
            value="",
            size=24,
            color=BGM,
            weight=FontWeight.BOLD
            )
    
    def get_fundamentals(e):
        symbol = symbol_field.value.upper()
        result = get_stats(symbol)
        result_text.value = f'''
        📊 Fundamentals for {symbol}:\n
        Date Change: {result.get('Date Change')}
        Price Today: {result.get('Price Today')}
        Change: {result.get('Change')}
        PE Ratio: {result.get('PE Ratio')}
        PS Ratio: {result.get('PS Ratio')}
        PEG Ratio: {result.get('PEG Ratio')}
        Return on Equity: {result.get('Return on Equity')}
        '''
        company_name.value = f'{result.get('Company Name')}'
        page.update()
    
    first_page_contents = Container(

        content=Column(
            controls=[
                Row(alignment='spaceBetween',
                    controls=[
                        Container(
                            content=Icon(Icons.MENU)
                        ),
                        Row(
                            controls=[
                                Icon(Icons.SEARCH),
                                Icon(Icons.NOTIFICATIONS_OUTLINED)
                            ]
                        )
                    ]
                ),
                Container(height=10),
                Text(value='Hi, Vash!', size=24, weight=FontWeight.BOLD),
                Container(height=5),
                symbol_field,
                Container(
                    height=300,
                    width=200,
                    content=Column(
                            controls=[
                                    Container(height=3),
                                    Container(
                                    ElevatedButton(
                                        text='Fundamentals',
                                        icon=Icons.BUSINESS,
                                        color="#110f0f",
                                        bgcolor = '#ffffff',
                                        on_click=get_fundamentals,
                                        ),
                                width=200,
                                border_radius=1,
                                padding=5
                                    ),
                                    Container(
                                    ElevatedButton(
                                    text='Technicals',
                                    color="#110f0f",
                                    bgcolor='#ffffff',
                                    icon=Icons.STACKED_LINE_CHART,
                                    on_click=lambda e: print('Technicals'),
                                    ),
                                width=200,
                                border_radius=1,
                                padding=5    
                                ),
                                    Container(
                                    ElevatedButton(
                                    text='Dividend Report',
                                    color="#110f0f",
                                    bgcolor='#ffffff',
                                    icon=Icons.ATTACH_MONEY,
                                    on_click=lambda e: print('Dividend Report'),
                                    ),
                                width=200,
                                border_radius=1,
                                padding=5    
                                ),
                                    Container(
                                    ElevatedButton(
                                    text='Company News',
                                    color="#110f0f",
                                    bgcolor='#ffffff',
                                    icon=Icons.NEWSPAPER,
                                    on_click=lambda e: print('Company News'),
                                    ),
                                width=200,
                                border_radius=1,
                                padding=5    
                                ),
                                    Container(
                                    ElevatedButton(
                                    text='Company News',
                                    color="#110f0f",
                                    bgcolor='#ffffff',
                                    icon=Icons.INFO,
                                    on_click=lambda e: print('About the Company'),
                                    ),
                                width=200,
                                border_radius=1,
                                padding=5    
                                )                                                                            
                            ],
                            alignment=MainAxisAlignment.START
                        )                
                )
                
            ]
        )
    )
    
    fundamentals = Column(
        controls=[
            Container(
                width=1030,
                height=650,
                bgcolor=SBGM,
                padding=padding.only(top=50, left=20,right=20, bottom=5),
                content=Column(
                        controls=[
                        Text(
                            value='COMPANY:',
                            size=16,
                            color='#000000',
                            weight=FontWeight.W_500
                        ),
                        Container(
                            content=company_name
                        ),
                        Container(
                            content=result_text
                        )
                    ]    
                )
            )
        ],
        horizontal_alignment=CrossAxisAlignment.END
    )

    
    page_1 = Column(
        controls=[
            Container(
                width=220,
                height=650,
                bgcolor=BGM,
                padding=padding.only(top=50, left=20,right=20, bottom=5),
                content=first_page_contents,
                border_radius=BorderRadius(
                    top_left=20,
                    bottom_left=20,
                    top_right=0,
                    bottom_right=0
                    )
            )
        ],
        horizontal_alignment=CrossAxisAlignment.START
    )
    
    container = Container(
        content=Row(
            controls=[
                Container(
                    width=220,
                    height=650,
                    bgcolor=SBGM,
                    content=page_1,
                    border_radius=BorderRadius(
                        top_left=20,
                        bottom_left=20,
                        top_right=0,
                        bottom_right=0
                    )
                ),
                Container(
                    width=1030,
                    height=650,
                    bgcolor='#ffffff',
                    content=fundamentals
                )    
            ]
        ),
        bgcolor=BGM,
        border_radius=20,
        width=1250,
        height=650
    )
    
    page.add(container)

app(target=main)