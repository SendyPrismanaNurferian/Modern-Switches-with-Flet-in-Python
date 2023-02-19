'''''Flet Switches Animations'''

# Modules
import flet
from flet import *
from math import pi


class Toggle_1(UserControl):
    def __init__(self, on_color, animation):
        self.on_color = on_color
        self.animation = animation
        super().__init__()

    def toggle_switch(self, e):
        if self.toggle.offset == transform.Offset(-0.25, 0):
            self.toggle.offset = transform.Offset(0.25, 0)
            self.controls[0].bgcolor= self.on_color
            self.update()
        else:
            self.toggle.offset = transform.Offset(-0.25, 0)
            self.controls[0].bgcolor="white60"
            self.update()

    def build(self):
        self.toggle = Container(
            bgcolor='white',
            shape=BoxShape('circle'),
            offset=transform.Offset(-0.25, 0),
            animate_offset=animation.Animation(600, self.animation),
            on_click=lambda e: self.toggle_switch(e),
        )

        return Container(
            width=55,
            height=30,
            border_radius=28,
            bgcolor='white60',
            border=border.all(0.5, "white80"),
            padding=4,
            clip_behavior=ClipBehavior.HARD_EDGE,
            animate=400,
            content=self.toggle,
            on_click=lambda e: self.toggle_switch(e),
        )

class Toggle_2(UserControl):
    def __init__(self, animation):
        self.animation = animation
        super().__init__()

    def toggle_switch(self, e):
        if self.line_1.rotate == transform.Rotate(0):
           self.line_1.rotate = transform.Rotate(-pi / 4)
           self.line_2.rotate = transform.Rotate(pi / 4)
           self.update()
        else:
           self.line_1.rotate = transform.Rotate(0)
           self.line_2.rotate = transform.Rotate(0)
           self.update()

    def build(self):
        self.line_1 = Container(
            height= 2,
            width= 28,
            border_radius= 15,
            bgcolor='white',
            rotate=transform.Rotate(0),
            animate_rotation=animation.Animation(600, "easeOutBack")
        )
        self.line_2 = Container(
            height= 2,
            width= 28,
            border_radius= 15,
            bgcolor='white',
            rotate=transform.Rotate(0),
            animate_rotation=animation.Animation(600, "easeOutBack")
        )


        return Container(
            width=34,
            height=34,
            border_radius=4,
            gradient=RadialGradient(
                center=Alignment(-0.9, -0.9),
                radius=4,
                colors= ["#16A085", "#7C4DFF", "#4CAF50", "#C0CA33", "#F57F17", "#DD2C00", "#607D8B", "#F50057",],
            ),
            shape=BoxShape('rectangle'),
            padding=2,
            alignment=alignment.center,
            content=Stack([self.line_1, self.line_2]),
            on_click=lambda e: self.toggle_switch(e)
        )

def main(page: Page):
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'


    toggle_color = ['blue600', 'red600', 'green600', 'yellow600', 'purple600']
    toggle_animation = ['easeInOutBack', 'decelerate', 'bounceOut', 'linear', 'easeOutBack',]

    #
    toggle_column_1 = Column()
    for color in toggle_color:
        row = Row(alignment=MainAxisAlignment.CENTER)
        for amimation in toggle_animation:
            row.controls.append(
                Toggle_1(
                    color, amimation
                )
            )
        toggle_column_1.controls.append(row)

    toggle_column_2 =Column()
    row = Row(alignment=MainAxisAlignment.CENTER, spacing=30)
    for animation in toggle_animation:
        row.controls.append(Toggle_2(animation))
    toggle_column_2.controls.append(row)

    page.add(toggle_column_1)
    page.add(Divider(height=25, color="transparent"))
    page.add(toggle_column_2)
    page.update()


if __name__ == '__main__':
    flet.app(target=main)