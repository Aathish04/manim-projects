from manimlib.imports import *
class Tables(Scene):
    
    def construct(self):
        tabledict={
            "Vowels":["\\alpha","\\epsilon","\\iota","\\omega","a","e","i","o"],
            "Consonants":["\\beta","\\gamma","\\delta","\\phi","\\eta","\\kappa","\\lambda","\\mu","\\nu","\\pi","\\chi","\\zeta"],
            "Words":["Must","add","proper","length","checking","for","use","with","LaTeX.","(No","wraparound","currently.)"],
        }
        table=Table.get_table(tabledict)
        table.scale(0.50)
        table.move_to((0,0,0))
        self.play(Write(table))

