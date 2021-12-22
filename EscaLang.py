from typing import Any, NamedTuple, Tuple
from types import LambdaType
from time import sleep


Shop_Names = """
ABS         ABSolute value
ADD         ADD
ADDP        ADD and Pop
AND         bitwise AND
CHS         CHange Sign
COM         COMpare
COMP        COMpare and Pop
COS         COSine
DEC         DECrement
DECP        DECrement and Pop
DIV         DIVide
DIVP        DIVide and Pop
HLT         HaLT
IN          INput from stream
INC         INCrement
INCP        INCrement and Pop
INT         INTerrupt
JIC         Jump If Condition
JMP         JuMP
LEN         LENgth
LENP        LENgth and Pop
MOV         MOVe
MUL         MULtiply
MULP        MULtiply
NEG         NEGative
NOP         No OPeration
NOT         bitwise NOT
OR          bitwise OR
OUT         OUTput to stream
POP         POP from escalator
POW         POWer
PUSH        PUSH to escalator
SIN         SINe
SUB         SUBtract
SUBP        SUBtract and Pop
TAN         TANgent
XOR         bitwise XOR
"""


class Shopper(NamedTuple): # data / item on stack
    value: Any


class Shop(NamedTuple): # instruction / function
    name: str
    func: function
    price: function


class Floor(NamedTuple): # escalator acts as stack
    no: int | None = None
    shops: dict[str, Shop] = {}
    shoppers: list[Shopper] = []

    def clear(self):
        self.shops = {}

    def set_shop(self, shop: Shop) -> Shop:
        self.shops[shop.name] = shop

        return shop
    
    def get_shop(self, shop: str) -> Shop | None:
        return self.shops.get(shop)
    
    def del_shop(self, shop: str) -> Shop | None:
        s = None

        if shop in self.shops:
            s = self.shops[shop]

            del self.shops[shop]
        
        return s


class Interpreter:
    def __init__(self, code: str) -> None:
        self.code: list[str] = [l.split(";")[0].strip() for l in code.split("\n") if l.split(";")[0].strip()]
        self.Loop: dict[Tuple] = [] 

        self.floors: list[Floor] = []

        if "DATA" not in self.code:
            return
        elif self.code.index("DATA") > self.code.index("CODE"):
            raise SyntaxError("CODE section comes before DATA section")

        for l in self.code:
            if l == "CODE":
                return

            line = l.split()

            op = line[0]
            if len(line) > 1:
                args = line[1:]

            # setup goes here

    def __call__(self) -> Any:
        for l in self.code[self.code.index("CODE") + 1:]:
            line = l.split()

            op = line[0]
            args = line[1:]

            # processing goes here

    def display(self):
        for f in reversed(self.floors):
            print(f"Floor {f.no} | " + " | ".join(f.shops.keys()))
            print("\n\\  \\        \n  \\  \\    \n    \\  \\\n      \\  \\\n        \\  \\\n") # escalator
            

    def clear(self):
        self.floors = {}

    def set_floor(self, floor: Floor, no: int | None=None) -> Floor:
        if no is not None:
            floor.no = no
        elif floor.no is None:
            floor.no = len(self.floors)

        if floor.no == len(self.floors):
            self.floors.append(floor)
        elif floor.no < len(self.floors):
            self.floors[floor.no] = floor
        else:
            raise ValueError("Floor number is too high")

        return floor
    
    def get_floor(self, floor: int) -> Floor | None:
        if floor < len(self.floors):
            return self.floors.get(floor)
        else:
            raise ValueError("Floor number is too high")
    
    def pop_floor(self, floor: int) -> Floor | None:
        if floor < len(self.floors):
            return self.floors.pop(floor)
        else:
            raise ValueError("Floor number is too high")