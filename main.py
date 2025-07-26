from flet import *

def main(page: Page):
    BGM = "#033f63"
    SBGM = "#b1c4b7"
    TEXT = '#fedc97'
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
                TextField(
                    label='Enter Stock Symbol',
                    label_style=TextStyle(size=14),
                    width=200,
                    multiline=False,
                    autofocus=True,
                    border_color = BGM,
                    bgcolor="#212020"
                ),
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
                                        on_click=lambda e: print('Company Fundamentals'),
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
    
    page_2 = Column(
        controls=[
            Container(
                width=1030,
                height=650,
                bgcolor=SBGM,
                padding=padding.only(top=50, left=20,right=20, bottom=5),
                content=Column(
                        controls=[
                        Text(
                        value="STOCK SYMBOL",
                        size=24,
                        color='#000000',
                        weight=FontWeight.BOLD
                        ),
                        Container(
                            Text(
                                "This is a long block of text that wraps nicely across multiple lines...",
                                max_lines=10,
                                overflow=TextOverflow.ELLIPSIS,
                                size=20
                            )
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
                    content=page_2
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