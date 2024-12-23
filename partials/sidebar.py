import flet as ft
from components.skills import SkillRing, SkillProgressBar
from datetime import datetime

idade = datetime.now().year - 1978

class SidebarHeader(ft.UserControl):
    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Badge(
                        content=ft.Image(
                            src='images/Foto02.png',
                            border_radius=ft.border_radius.all(100),
                            width=100,
                        ),
                        alignment=ft.alignment.bottom_right,
                        bgcolor=ft.colors.PRIMARY,
                        small_size=20,
                    ),
                    ft.Text(value='Emerson Ribeiro', theme_style=ft.TextThemeStyle.BODY_LARGE),
                    ft.Text(value='Desenvolvedor Fullstack', theme_style=ft.TextThemeStyle.BODY_MEDIUM)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=ft.padding.symmetric(vertical=20, horizontal=40),
            alignment=ft.alignment.center,
        )


class SidebarContent(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.expand = True

    def build(self):
        location = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(value='Residência:', theme_style=ft.TextThemeStyle.BODY_LARGE),
                        ft.Text(value='Brasil', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Row(
                    controls=[
                        ft.Text(value='Cidade:', theme_style=ft.TextThemeStyle.BODY_LARGE),
                        ft.Text(value='Jandira SP', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Row(
                    controls=[
                        ft.Text(value='Idade:', theme_style=ft.TextThemeStyle.BODY_LARGE),
                        ft.Text(value=idade, theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
            ]
        )

        languages = ft.Row(
            controls=[
                SkillRing(title='Português', value=1).build(),
                SkillRing(title='Inglês', value=0.1).build(),
                SkillRing(title='Espanhol', value=0.15).build(),
            ]
        )

        skills = ft.Column(
            controls=[
                SkillProgressBar(title='HTML', value=0.1).build(),
                SkillProgressBar(title='CSS', value=0.15).build(),
                SkillProgressBar(title='PYTHON', value=0.51).build(),
                SkillProgressBar(title='JS', value=0.18).build(),
                SkillProgressBar(title='PHP', value=0.16).build(),
            ]
        )

        technologies = ft.Column(
            controls=[
                ft.ListTile(
                    leading=ft.Icon(name=ft.icons.CHECK, color=ft.colors.PRIMARY),
                    title=ft.Text(value='Flet', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.icons.CHECK, color=ft.colors.PRIMARY), 
                    title=ft.Text(value='Versionamento com GIT', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.icons.CHECK, color=ft.colors.PRIMARY), 
                    title=ft.Text(value='Bootstrap, Webpack, Framer Motion, Tailwind', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.icons.CHECK, color=ft.colors.PRIMARY), 
                    title=ft.Text(value='Typescript, ReactJS, Angular', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.icons.CHECK, color=ft.colors.PRIMARY), 
                    title=ft.Text(value='Django, Flask, FastAPI', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=0,
        )


        cv = ft.TextButton(
            text='DOWNLOAD CV',
            style=ft.ButtonStyle(color=ft.colors.GREY),
            icon=ft.icons.DOWNLOAD,
            icon_color=ft.colors.GREY,
            url='https://docs.google.com/document/d/1uYvX9ekUY2YYBGfBuN6E73aYcTBgz_Oa/edit?usp=sharing&ouid=101262308388464893370&rtpof=true&sd=true',

            # https://sites.google.com/site/gdocs2direct/?pli=1
        )


        return ft.Container(
            bgcolor=ft.colors.BLACK12,
            padding=ft.padding.all(20),
            content=ft.Column(
                scroll=ft.ScrollMode.HIDDEN,
                controls=[
                    location,
                    ft.Divider(height=30),
                    languages,
                    ft.Divider(height=30),
                    skills,
                    ft.Divider(height=30),
                    technologies,
                    ft.Divider(height=30),
                    cv,
                ]
            )
        )


class SidebarFooter(ft.UserControl):
    def build(self):
        return ft.Container(
            padding = ft.padding.symmetric(vertical=10),
            content=ft.Row(
                controls=[
                    ft.IconButton(
                        content=ft.Image(src='icons/001-instagram.png', height=15, color='white'),
                        url='https://www.instagram.com/programadoraventureiro/',
                    ),
                    ft.IconButton(
                        content=ft.Image(src='icons/002-linkedin.png', height=15, color='white'),
                        url='https://www.linkedin.com/in/emerson-ribeiro-6a74ba82/',
                    ),
                    ft.IconButton(
                        content=ft.Image(src='icons/003-github.png', height=15, color='white'),
                        url='https://github.com/emersonribeiroaraujo',
                    ),
                    ft.IconButton(
                        content=ft.Image(src='icons/004-youtube.png', height=15, color='white'),
                        url='https://www.youtube.com/@ProgramadorAventureiro',
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )


class Sidebar(ft.UserControl):
    def build(self):
        return ft.Container(
            expand=True,
            content=ft.Column(
                controls=[
                    SidebarHeader(),
                    SidebarContent(),
                    SidebarFooter(),
                ]
            ),
            bgcolor=ft.colors.BACKGROUND,
        )