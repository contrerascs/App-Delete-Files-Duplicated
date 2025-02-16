import flet as ft

def main(page: ft.Page):
    page.title = 'Delete duplicates files'
    page.window.width = 1000
    page.window.height = 700
    page.padding = 0
    page.bgcolor = ft.colors.BACKGROUND
    page.theme_mode = ft.ThemeMode.DARK

    #ADD CUSTOM THEME
    page.theme = ft.Theme(
        color_scheme_seed=ft.colors.BLUE,
        visual_density=ft.VisualDensity.COMFORTABLE,
        color_scheme = ft.ColorScheme(
            primary=ft.colors.BLUE,
            secondary=ft.colors.ORANGE,
            background=ft.colors.GREY_900,
            surface=ft.colors.GREY_800
        )
    )

    def change_view(e):
        selected = e.control.selected_index
        if selected == 0:
            content_area.content = ft.Text('Duplicates view', size=24)
        elif selected == 1:
            content_area.content = ft.Text('Coming soon...', size=24)
        content_area.update()

    content_area = ft.Container(
        content=ft.Text('Duplicates view', size=24),
        expand=True,
        padding=30        
    )

    #LATERAL MENU
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=200,
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.DELETE_FOREVER,
                selected_icon=ft.icons.DELETE_FOREVER,
                label='Duplicates'
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.ADD_CIRCLE_OUTLINE,
                selected_icon=ft.icons.ADD_CIRCLE,
                label='Coming soon'
            )
        ],
        on_change=change_view,
        bgcolor=ft.colors.GREY_900
    )

    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                content_area
            ],
            expand=True
        )
    )



if __name__ == '__main__':
    ft.app(target=main)