import flet as ft
from Delete_Duplicates import find_duplicates, delete_files

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

    #VARIABLES DE ESTADO
    state = {
        'current_duplicates': []
    }

    selected_dir_text = ft.Text(
        'No folder selected',
        size=14,
        color=ft.colors.BLUE_200
    )

    result_text = ft.Text(size=14, weight=ft.FontWeight.BOLD)

    duplicates_list = ft.ListView(
        expand=1,
        spacing=10,
        height=200
    )

    delete_all_btn = ft.ElevatedButton(
        'Delete all duplicates',
        color=ft.colors.WHITE,
        bgcolor=ft.colors.RED_900,
        icon=ft.icons.DELETE_SWEEP,
        visible=False,
        on_click=lambda e: delete_all_duplicates()
    )

    def change_view(e):
        selected = e.control.selected_index
        if selected == 0:
            content_area.content = duplicate_files_view
        elif selected == 1:
            content_area.content = ft.Text('Coming soon...', size=24)
        content_area.update()

    def hanlde_folder_picker(e: ft.FilePickerResultEvent):
        if e.path:
            selected_dir_text.value = f'Selected folder: {e.path}'
            selected_dir_text.update()
            scan_directory(e.path)

    def scan_directory(directory):
        duplicates_list.controls.clear()
        state['current_duplicates'] = find_duplicates(directory)

        if not state['current_duplicates']:
            result_text.value = 'Not find duplicates files'
            result_text.color = ft.colors.GREEN_400
            delete_all_btn.visible = False
        else:
            result_text.value = f'Find {len(state["current_duplicates"])} duplicates files'
            result_text.color = ft.colors.ORANGE_400
            delete_all_btn.visible = True

            for dup_file, original in state['current_duplicates']:
                dup_row = ft.Row([
                    ft.Text(
                        f'Duplicate: {dup_file}\nOriginal: {original}',
                        size=12,
                        expand=True,
                        color=ft.colors.BLUE_200
                    ),
                    ft.ElevatedButton(
                        'Delete',
                        color=ft.colors.WHITE,
                        bgcolor=ft.colors.RED_900,
                        on_click=lambda e, path=dup_file: delete_duplicate(path)
                    )
                ])
                duplicates_list.controls.append(dup_row)
        duplicates_list.update()
        result_text.update()
        delete_all_btn.update()

    def delete_duplicate(filepath):
        if delete_files(filepath):
            result_text.value = f'File deleted: {filepath}'
            result_text.color = ft.colors.GREEN_400
            for control in duplicates_list.controls[:]:
                if filepath in control.controls[0].value:
                    duplicates_list.controls.remove(control)
            state['current_duplicates'] = [(dup, orig) for dup, orig in state['current_duplicates'] if dup != filepath]
            if not state['current_duplicates']:
                delete_all_btn.visible = False
        else:
            result_text.value = f'Error at delete: {filepath}'
            result_text.color = ft.colors.RED_400  

        duplicates_list.update()
        result_text.update()
        delete_all_btn.update()


    def delete_all_duplicates():
        deleted_count = 0
        failed_count = 0

        for dup_file, _ in state['current_duplicates'][:]:
            if delete_files(dup_file):
                deleted_count += 1
            else:
                failed_count += 1

            duplicates_list.controls.clear()
            state['current_duplicates'] = []
            delete_all_btn.visible = False

            if failed_count == 0:
                result_text.value = f'{deleted_count} Files duplicates delete succesfully.'
                result_text.color = ft.colors.GREEN_400
            else:
                result_text.value = f'{deleted_count} Files duplicates delete succesfully. Error try delete {failed_count} files.'
                result_text.color = ft.colors.RED_400
            
            duplicates_list.update()
            result_text.update()
            delete_all_btn.update()

    #Configure folder selector
    folder_picker = ft.FilePicker(on_result=hanlde_folder_picker)
    page.overlay.append(folder_picker)

    #View files duplicates
    duplicate_files_view = ft.Container(
        content=ft.Column([
            ft.Container(
                content=ft.Text(
                    'Delete files duplicates',
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.BLUE_200
                ),
                margin=ft.margin.only(bottom=20)
            ),
            ft.Row([
                ft.ElevatedButton(
                    'Select Folder',
                    icon=ft.icons.FOLDER_OPEN,
                    color=ft.colors.WHITE,
                    bgcolor=ft.colors.BLUE_900,
                    on_click=lambda _: folder_picker.get_directory_path()
                ),
                delete_all_btn,
            ]),
            ft.Container(
                content=selected_dir_text,
                margin=ft.margin.only(top=10, bottom=10)
            ),
            result_text,
            ft.Container(
                content=duplicates_list,
                border=ft.border.all(2, ft.colors.BLUE_400),
                border_radius=10,
                padding=20,
                margin=ft.margin.only(top=10),
                bgcolor=ft.colors.GREY_800,
                expand=True
            )
        ]),
        padding=30,
        expand=True
    )

    content_area = ft.Container(
        content=duplicate_files_view,
        expand=True,   
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