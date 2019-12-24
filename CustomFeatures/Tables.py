from manimlib.imports import *

from manimlib.mobject.types.vectorized_mobject import VGroup

class Table(Scene):
    CONFIG = {
        "line_color": WHITE,
        "text_color": WHITE,
    }
    def create_table(self,fields:list,records:dict,buff_space=0.2):
        table=VGroup()
        position=ORIGIN
        # sep_hor_lenght=TexMobject(max(fields,key=len)).get_width()
        for n in range(len(fields)):
            field=TexMobject(fields[n])
            
            if n<len(fields)-1:
                next_field=TexMobject(fields[n+1])
            field.move_to(position)

            table.add(field)
            position=field.get_right()+(next_field.get_width()/2,0,0)+(buff_space,0,0)
            line=Line(start=field.get_right()+(buff_space/2,0,0)+UP,end=field.get_right()+(buff_space/2,0,0)+DOWN)
            table.add(line)
        return table
    
    def construct(self):
        table=self.create_table(fields=["vowels","consonants","ambigous","other","more","hurricane","random"],records={"vowels":["alpha","epsilon","iota"],"consonants":["beta","gamma","delta","phi","kappa","mu","nu","pi"]})
        self.play(ShowCreation(table.move_to(ORIGIN)))
