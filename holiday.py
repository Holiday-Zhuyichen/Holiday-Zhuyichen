from turtle import *
from random import *
from time import *
from calendar import *
from typing import *
import pygame
import sys as py
from pygame.locals import *
import _thread as together
import tkinter as tk
import tkinter.font as tkf
from functools import partial
from maps import Map
import itertools
from tkinter.messagebox import *


class hc:
    # noinspection PyTypeChecker
    def hinsert(self, value, place, item, key_value: tuple = None, keys=None):
        if type(value) == dict:
            if key_value == keys is None:
                raise ValueError("argument not allowed")
            out=value
            while item in value:
                del out[keys]
            out[key_value[0]]=key_value[1]
            time=0
            while len(value) != len(out):
                out[keys]=value[keys]
                time+=1
        if type(value) == list:
            list.insert(value, place, item)
        return value

    def hlen(self, value):
        if type(value) in ("<class 'int'>", "<class 'float'>", "<class 'complex'>"):
            hc.hlen(str(value))
        return len(value)

    def happend(self, value, item_key: any):
        if type(value) == dict:
            value[item_key[0]]=item_key[1]
        return hc.hinsert(value, hc.hlen(value), item_key)

    def hcount(self, value, item):
        count=0
        for i in range(hc.hlen(value)):
            if value[i] == item:
                count+=1
        return count

    def hextent(self, value, add):
        for i in range(hc.hlen(list)):
            hc.happend(value, add[i])
        return value

    def hindex(self, value, item):
        if item in value:
            return type(value).index(value, item)
        else:
            raise IndexError("list index out of range")

    def hpop(x, value, find):
        del value[find]
        return value

    def hremove(x, value, del_value):
        return hc.hpop(value, hc.hindex(del_value))

    def hreverse(x, value):
        reverse=[]
        for i in range(hc.hlen(value)):
            reverse=hc.happend(value[hc.hlen(value) - i])
        return reverse

    def hmax(x, value):
        while hc.hlen(value) != 1:
            if value[0] < value[1]:
                hc.hpop(value, 0)
            else:
                hc.hpop(value, 1)
        return value[0]

    def hsort(x, value, reverse: bool | None = False):
        if reverse:
            for i in range(hc.hlen(reverse)):
                for j in range(hc.hlen(value) - i):
                    if value[i] > value[j]:
                        hfront=j
                        hback=i
                        value[j]=hback
                        value[i]=hfront
                        del hfront, hback
        else:
            for i in range(hc.hlen(reverse)):
                for j in range(hc.hlen(value) - i):
                    if value[i] < value[j]:
                        hfront=j
                        hback=i
                        value[j]=hback
                        value[i]=hfront
                        del hfront, hback

    def hclear(x, value: any):
        return type(value)()

    def hcopy(self, value):
        global copyed_value
        copy=value
        copyed_value=copy
        return copyed_value


def huseful():
    return "hfind"


class hnum_translate:
    def __init__(self, value, now, to, l, values):
        self.now=now
        self.to=to
        self.value=value
        self.l=l
        self.values=values

    @staticmethod
    def __get(*args):
        args=args[0]
        if args <= 10:
            return ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")[:10 - args + 1]
        if args <= 62:
            return hnum_translate.__get(args) + hletter(None).big_letter() + hletter(None).small_letter()
        if args <= hlen(hstrn.strn()):
            return hstrn.strn()
        else:
            return "ord"

    def __b_s(self):
        out=""
        if self.values is None:
            x=hnum_translate.__get(self.to)
        else:
            x=self.values
        while self.value > self.to:
            if x == "ord":
                out=f"{out}{ord(self.value % self.to)}"
            else:
                out=f"{out}{values[self.value % self.to]}"
            self.value//=self.to
        out=f"{out}{self.value}"
        if type(self.value) == int:
            return int(out[::-1])
        if type(self.value) == float and int(self.value) == self.value:
            return float(out[::-1])
        out=out[::-1]
        out=f"{out}."
        one=self.value - int(self.value)
        one=str(one)
        one=int(one[2:])
        return float(f"{out}.{hnum_translate(value=one, now=self.now, to=self.to).__b_s()}")

    def __s_b(self):
        out=0
        if self.values is None:
            x=hnum_translate.__get(self.to)
        else:
            x=self.values
        for part in str(self.value):
            get=int(part)
            if x == "ord":
                out=f"{out}{ord(self.value % self.to)}"
            else:
                out=f"{out}{values[self.value % self.to]}"
            out=f"{out}{self.l[get]}"
        del t_
        out=int(out)
        if type(self.value) == int:
            return out
        if type(self.value) == float and int(self.value) == self.value:
            return float(out)
        one=self.value - int(self.value)
        one=str(one)[2:]
        one=int(one)
        return float(f"{out}.{hnum_translate(one, self.now, self.to).__s_b}")

    def get(self):
        if self.now == self.to:
            return self.value
        if self.now < self.to:
            return hnum_translate(self.value, self.now, self.to).__s_b
        if self.now > self.to:
            return hnum_translate(self.value, self.now, self.to).__b_s()
        raise NameError("cannot run function!")

    def __change_check(self):
        if isinstance(self.now, self.to) != tuple:
            raise TypeError("argument type not allowed")
        if type(self.value) not in (int, float):
            return hnum_translate(1, 1, 1).__change_check()
        return False

    def change(self):
        if hnum_translate(self.value, self.now, self.to).__change_check():
            return hnum_translate(self.value, self.now, self.to).__change_check()


def hadd(value1: float | None = 0.0, value2: float | None = 0.2):
    value1=hnum_translate(value1, 10, 2).get()
    value2=hnum_translate(value2, 10, 2).get()
    value1l=value2l=[]
    for a in range(0, hc.hlen(value1)):
        value1l=hc.happend(value1l, value1[a])
    for b in range(0, hc.hlen(value2)):
        value2l=hc.happend(value2l, value2[b])
    value2=value2l
    del value2l
    value1=value1l
    del value1l
    if hc.hlen(value1) > hc.hlen(value2):
        while hc.hlen(value1) != hc.hlen(value2):
            hc.hinsert(value1, 0, 0)
    elif hc.hlen(value1) == hc.hlen(value2):
        print("", end="")
    else:
        while hc.hlen(value1) != hc.hlen(value2):
            hc.hinsert(value2, 0, 0)
    answerl, add, t=[], 0, 0
    for a, b in value1, value2:
        if not a:
            if not b:
                hc.happend(answerl, 0)
            else:
                hc.happend(answerl, 1)
        else:
            if not b:
                hc.happend(answerl, 0)
            else:
                hc.happend(answerl, 0)
                add="1"
                for i in range(t + 1):
                    addt=addt + 0
                add=int(add)
        t+=1
    if add:
        for i in range(hc.hlen(addt)):
            hc.happend(answerl, addt[i])
    answerf=""
    for combine in answerl:
        answerf=answerf + combine
    return answerf


def hminus(value1: float | None = 0.93, value2: float | None = 0.87):
    value1=hnum_translate(value1, 10, 2).get()
    value2=hnum_translate(value2, 10, 2).get()
    answerl=value1l=value2l=[]
    for a in range(0, hc.hlen(value1)):
        value1l=hc.happend(value1l, value1[a])
    for b in range(0, hc.hlen(value2)):
        value2l=hc.happend(value2l, value2[b])
    value2=value2l
    del value2l
    value1=value1l
    del value1l
    if hc.hlen(value1) > hc.hlen(value2):
        while hc.hlen(value1) != hc.hlen(value2):
            hc.hinsert(value1, 0, 0)
    elif hc.hlen(value1) == hc.hlen(value2):
        print("", end="")
    else:
        while hc.hlen(value1) != hc.hlen(value2):
            hc.hinsert(value2, 0, 0)
    minus=t=0
    for a, b in value1, value2:
        if not a:
            if not b:
                answerl=hc.happend(answerl, 0)
            else:
                answerl=hc.happend(answerl, 1)
                if not t:
                    minus+=1
                else:
                    minus+=10 ** t
        else:
            if not b:
                answerl=hc.happend(answerl, 1)
            else:
                answerl=hc.happend(answerl, 0)
        t+=1
    if minus:
        for i in range(hc.hlen(minus)):
            hc.happend(answerl, minus[i])
    answerf=""
    for combine in answerl:
        answerf=answerf + combine
    return answerf


def hmul(value1: float | None = 0.764, value2: float | None = 0.5432):
    answer=0
    if value1 > value2:
        times=value2
    else:
        times=value1
    for i in range(times):
        if value1 > value2:
            answer+=value1
        else:
            answer+=value2


class hdiv:
    def is_error(value1, value2):
        if not value2:
            return True
        return False

    def hdiv(value1: float | None = 0, value2: float | None = 1):
        if hdiv.is_error(value1, value2):
            raise ZeroDivisionError("value2 cannot be 0")
        else:
            answer=0
            while value1 < value2:
                answer+=1
                value1-=value2
            answer+=value1 / value2
        return answer

    def hfull(value1: float | None = 0.765, value2: float | None = 654):
        return int(hdiv.hdiv(value1, value2))

    def hno(value1: float | None = 0.765, value2: float | None = 654):
        if hdiv.is_error(value1, value2):
            raise ZeroDivisionError("value2 cannot be 0")
        else:
            answer=0
            while value1 < value2:
                answer+=1
                value1-=value2

        return value1


class __pow__:
    def __init__(self, *arg: object):
        pass


def hpow(value1: float | None = 0.765, value2: float | None = 654):
    answer=value1
    if not value2:
        if not value1:
            raise SyntaxError("0**0=Error")
    if not value2:
        return 1
    for i in range(value2 - 1):
        answer*=value1

    return answer


def hprint(q="", w="", e="", r="", t="", y="", u="", i="", o="", p="", a="", s="", d="", f="", g="", h="", j="", k="",
           l="", z="", x="", c="", v="", b="", n="", *m, sep=" ", end="\n"):
    print(q, w, e, r, t, y, u, i, o, p, a, s, d, f, g, h, j, k, l, z, x, c, v, b, n, sep=sep)
    for a in m:
        print(a, end="")
    print(end=end)
    return Literal[None]


def average(list_=None):
    if list_ is None:
        list_=[0, 1]
    avearge_value=0
    for averageFor in range(list.__len__(list_)):
        avearge_value+=list_[averageFor]
    avearge_value/=list.__len__(list_)


def sqrt(num, lowest=0, highest=""):
    if highest == "":
        sqrt(num, lowest, num)
    for i in range(2000):
        guess=haverage(lowest, highest)
        if guess ** 2 == num:
            return guess
        elif guess ** 2 > num:
            highest=guess
        else:
            lowest=guess
    return guess


def hpassword(do_set_change_del_forget="change"):
    can_cantain=(
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
        "w",
        "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
        "T",
        'U', 'V', 'W', 'X', 'Y', 'Z', '~', '`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$',
        '%',
        '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', ':', ';', "'", '"', '<', ",", ".", ">",
        "?",
        "/", "\\")
    if do_set_change_del_forget == "set":

        def password_set():
            correct_password=input("please type the password")
            password_answer=input("please type that again")
            for i in range(len(password_answer)):
                if not tuple.__contains__(can_cantain, password_answer[i]):
                    print("#password!_not allowed to use this please check to not use '\'")
                    return "#password!_not allowed to use this please check to not use '\'"
            if correct_password != password_answer:
                print("#password! not the same;please try it again")
                print("The correct password is password; use that to login again")
                return "#password! not the same;please try it again"
            print("set successfully")
            if list.__contains__(no_password, correct_password):
                print("not allowed you have used that already")
            input("please type a value to reset password")
            input("please type another value for the same reason")
            input("do the same thing as 1 and 2 but the value should be different")
            return {correct_password: "password"}

        password_set()
    elif do_set_change_del_forget == "change":
        password_type=input("please type your old password")
        if correct_password != password_type:
            print("#PASSWORD!_not equal to the password you set(you can try password to log in)")
            return "#PASSWORD!_not equal to the password you set(you can try password to log in)"
        password_set()
    elif do_set_change_del_forget == "del":
        password_type=input("please type the password")
        if password_type != correct_password:
            print("The password is closed sucessfully")
            del correct_password
            del password_type
            del password_set
            return
        else:
            print("password is wrong!")
            return "#Password is wrong"
    elif do_set_change_del_forget == "forget":
        global a
        global b
        global c
        reset_value=input("please type one of the reset codes")
        if reset_value == a or reset_value == b or reset_value == c or reset_value == correct_password:
            password_set()
        else:
            print("reset code is wrong!")
            return
    else:
        raise TypeError("argument not supported")


def hint(value, enable_base=False, error_value=0):
    if not type(value) in ("str", "float", "int", "complex"):
        return value[error_value]
    if enable_base:
        return int(value)
    return int(float(value))


def hfloat(value, error_value=0):
    if not type(value) in ["int", "float", "str", "complex"]:
        return value[error_value]
    return float(value)


def hstr(value):
    if not type(value) in ["int", "str", "float", "complex"]:
        return value
    return str(value)





def hcomplex(value, Xvalue=0):
    if not type(value) in ["int", "str", "float", "complex"]:
        return value[Xvalue]
    return complex(value)





def habs(value):
    if value < 0:
        return hminus(0, value)
    return value


def hceil(value):
    if type(value) != "float":
        value=hfloat(value)
    return hint(value) + 1


def hnup(value):
    return hceil(value)





def hfloor(value):
    return hceil(value) - 1


def hndown(value):
    return hfloor(value)




def hround(value, len_after_dot=0):
    return round(value, len_after_dot)




def haverage(tuple_=(1, 1)):
    a=0
    for _ in tuple_:
        a=hadd(a, 1)
    a=hdiv.hdiv(a, list.__len__(tuple_))
    return a


def hsqrt(num):
    lowest=0
    highest=num
    for i in range(2000):
        guess=haverage((lowest, highest))
        if guess ** 2 == num:
            # print(guess)
            return guess
        elif guess ** 2 > num:
            highest=guess
        else:
            lowest=guess
    # print(guess)
    return guess


def hrandom(min=0, max=1, aInclude=True, bInclude=False, step=1):
    allow_type=("float", "int", "complex")
    if type(min) not in allow_type:
        return "the first argument is not one of these types: [float,int,complex]"
    if type(max) not in allow_type:
        return "thnd secom argument is not one of these types: [float,int,complex]"
    if type(step) not in "float,int":
        return "the last argument is not one of these types: [float,int]"
    if aInclude:
        if bInclude:
            return randrange(min, max, step)
        elif not bInclude:
            return randrange(min, max - step, step)
        else:
            return "#value! The fourth argument is not a bool type"
    elif not aInclude:
        if bInclude:
            return randrange(min - step, max, step)
        elif not bInclude:
            return randrange(min, max, step)
        else:
            return "#value! The fourth argument is not a bool type"
    else:
        return "#value! The second argument is not a fourth type"


def hsuijishu(min=0, max=1, aInclude=True, bInclude=False, step=1):
    return hrandom(min, max, aInclude, bInclude, step)


def hsum_minus_times(sum_value=False, minus_value=1, times_value=2):
    if type(sum_value) in ["bool", "int", "float"]:
        if not (type(sum_value) == "bool" and sum_value in [True, False]):
            raise TypeError("not bool")
            # error of sum_value bool type
        else:
            sum_value="useless"
    else:
        return "#type! only allowed for (bool type that are True or False) and int&float numbers"
    if type(minus_value) in ["bool", "int", "float"]:
        if not (type(minus_value) == "bool" and minus_value in [True, False]):
            raise TypeError("not bool")
            # error of sum_value bool type
        else:
            minus_value="useless"
    else:
        return "#type! only allowed for (bool type that are True or False) and int&float numbers"
    if type(times_value) in ["bool", "int", "float"]:
        if not (type(times_value) == "bool" and times_value in [True, False]):
            raise TypeError("not bool")
            # error of sum_value bool type
        else:
            times_value="useless"
    else:
        return "#type! only allowed for (bool type that are True or False) and int&float numbers"
    if sum_value == "useless":
        return minus_value / (times_value - 1)
    else:
        if minus_value == "useless":
            return sum_value / (times_value + 1)
        else:
            return "big:", (sum_value - minus_value) / 2, "small:", (sum_value + minus_value) / 2


def hhechabei(sum, minus, times):
    return hsum_minus_times(sum, minus, times)


def hlist(values=()):
    return list(values)


def hliebiao(values=()):
    return hlist(values)


def htuple(values=None):
    if values is None:
        values=[]
    return tuple(values)


def hyuanzu(values=None):
    if values is None:
        values=[]
    return htuple(values)


def hdict(values=(), find=()):
    dict_out={}
    for i in values:
        dict_out={dict_out: dict_out, values[i]: find[i]}
    return dict(values)


def hzidian(values=(), find=()):
    return hdict(values, find)


def hdict_str(values=None):
    if values is None:
        values={}
    return __dict__(values)


def hlen(values):
    if type(values) in ["str", "complex", "float"]:
        return len(values)
    return type(values).__len__(values)


def hisBool(value, how1=True, how2=False):
    if value == how1 or value == how2:
        return True
    return False


def hfuldiv(start=10, end=30, num=5, add=0, times=1):
    if times == time:
        return go
    time=0
    count=start - 1
    go=[]
    while count == end:
        count+=1
        if count % num == add:
            continue
        print(count)
        go.append(count)
    hfuldiv(start, end, num, add, time + 1)


def hsquare(x=0.0, y=0.0, times=1):
    for drawing_times in range(1, hadd(times, 1)):
        shape("turtle")
        pu()
        goto(x, y)
        now_x, now_y=xcor(), ycor()
        goto(now_x + 50, now_y)
        pd()
        for square_drawing in range(4):
            fd(100 / 2)
            rt(90)
            fd(100 / 2)
    # draself.wing a square
    return "drawn......"
    # stop code and return None


def htriangle(x=xcor(), y=ycor(), side1=100, turn1=180 / 3, side2=100, turn2=180 / 3, side3=100, turn3=100):
    if turn2 == turn3 == 60 and side2 == side3:
        turn2=turn3=turn1
        side2=side3=side1
        # if these thing aren't typed or exactly equal to auto then set them the same
    goto(x, y + side1)
    fd(side1)
    rt(turn1)
    fd(side2)
    rt(turn2)
    fd(side3)
    rt(turn3)
    # draself.wing a triangle
    return
    # stop code and return None


def hudlr_30_30():
    hideturtle()
    colormode(1.0)
    setup(555, 555)
    screensize(555, 555)
    speed(0)
    pensize(randint(0, 3))
    pu()
    goto(-250, 250)
    for k in range(30):
        for j in range(30):
            pd()
            pencolor(random(), random(), random())
            fillcolor(random(), random(), random())
            begin_fill()
            for i in range(4):
                fd(15)
                rt(90)
            end_fill()
            pu()
            fd(15)
        pu()
        goto(-250, ycor() - 15)
    # stop on click
    exitonclick()


def hblinking_bg(wait=0.25, cmode=1.0, rgbr=True):
    # only change wait! or else it will have a problem of doing the job!
    colormode(cmode)
    while True:
        if rgbr:
            bgcolor(random(), random(), random())
        else:
            bgcolor("black")
        sleep(wait)


def hinput(out=("title", "text", "auto", "min", "max"), return_type="str", input_type=0):
    # input_type=0 means normal input;input_type=1 means turtle numinput;if it is other it will be divided with 2 and
    # round with 1 check for errors and translation
    if type(out) != "str":
        raise TypeError("value not allowed")
    if return_type not in ("str", "int", "float", "complex"):
        raise TypeError(
            "#ARUGUMENT VALUE RETURN TYPE TYPE! not avalible for not including on of these tuple element" +
            "('str','int','float','complex')")
    if type(input_type) not in ("int", "float", "complex"):
        raise "#Arugument INPUT TYPE TYPE! only can use ('int','float','complex')"
    input_type=hround(hdiv.hdiv(input_type, 2), 0)
    if not input_type:
        hprint(out[0], out[1], sep="", end="")
        input_answer=input("")
    else:
        if out == (out[0], out[1], "auto", "min", "max"):
            out=(out[0], out[1], None, None, None)
        input_answer=numinput(out[0], out[1], out[2], out[3], out[4])
    return input_answer


class hc:
    def hinsert(value, place, item):
        if type(value) == "list":
            list.insert(value, place, item)
        return value

    def hlen(value):
        value=str(value)
        return len(value)

    def happend(value, item):
        return hc.hinsert(value, hc.hlen(value), item)

    def hcount(value, item):
        count=0
        for i in range(hc.hlen(value)):
            if value[i] == item:
                count+=1
        return count

    def hextent(value, add):
        for i in range(hc.hlen(list)):
            hc.happend(value, add[i])
        return value

    def hindex(value, item):
        if item in value:
            return type(value).index(value, item)
        else:
            raise TypeError("cannot find {} in {}".format(item, value))

    def hpop(value, find):
        del value[find]
        return value

    def hremove(value, del_value):
        return hc.hpop(value, hc.hindex(del_value))

    def hreverse(value):
        _reverse_=[]
        for i in range(hc.hlen(value), 0, -1):
            _reverse_=hc.happend(_reverse_, value[i])
        return _reverse_

    def hmax(value):
        while hc.hlen(value) != 1:
            if value[0] < value[1]:
                hc.hpop(value, 0)
            else:
                hc.hpop(value, 1)
        return value[0]

    def hsort(value, reverse: bool | None = False):
        if reverse:
            for i in range(hc.hlen(reverse)):
                for j in range(hc.hlen(value) - i):
                    if value[i] > value[j]:
                        hfront=j
                        hback=i
                        value[j]=hback
                        value[i]=hfront
                        del hfront, hback
        else:
            for i in range(hc.hlen(reverse)):
                for j in range(hc.hlen(value) - i):
                    if value[i] < value[j]:
                        hfront=j
                        hback=i
                        value[j]=hback
                        value[i]=hfront
                        del hfront, hback

    def hclear(self):
        return []

    def hcopy(value):
        global copyed_value
        copy=value
        copyed_value=copy
        return copyed_value


class t:
    def hfd(steps: float):
        fd(steps)

    def hforward(steps: float):
        t.hfd(steps)

    def hbd(steps: float):
        forward(-steps)

    def hbackward(steps: float):
        t.hbd(steps)

    def hback(steps: float):
        t.hbd(steps)

    def hbk(steps: float):
        t.hbd(steps)

    def hright(angle: float):
        rt(angle)

    def hrt(angle: float):
        rt(angle)

    def hleft(angle: float):
        lt(angle)

    def hlt(angle: float):
        t.hleft(angle)

    def hgoto(x: float, y: float):
        goto(x, y)

    def hgo(x: float, y: float):
        t.hgoto(x, y)

    def hset_pos(x: float, y: float):
        t.hgo(x, y)

    def hset_position(x: float, y: float):
        t.hgo(x, y)

    def hxfind(self):
        return xcor()

    def hyfind(self):
        return ycor()

    def hset_x(x: float):
        t.hgo(x, t.hyfind())

    def hset_y(y: float):
        t.hgo(t.hxfind(), y)

    def hseth(angle: float):
        seth(angle)

    def hset_heading(angle: float):
        t.hseth(angle)

    def hhome(self):
        home()

    def hcircle(radius: float, times: int = 360):
        pi=3.1415926
        pu()
        t.hgo(t.hxfind(), t.hyfind() - radius)
        pd()
        speed(0)
        for drawing_for in range(times):
            t.hfd(pi * pi * radius / times)
            t.hlt(1)

    def hdot(radius, times=360):
        t.hcircle(radius, times)

    @staticmethod
    def hstamp():
        stamp()

    def hclear_stamp(s: bool = False, many: int = 2):
        if s:
            clearstamp()
            return
        if not s:
            clearstamps(many)
            return

    def hundo(self):
        undo()

    def hspeed(speeds: int | str = None):
        if speed is None:
            return speed()
            # int
        try:
            speed(speeds)
        except TypeError:
            raise ValueError("not supported for arguement {}.".format(speeds))

        return speed()

    def hreturn(value):
        return value

    def hpos_find(self):
        return pos()
        # returing Vec2D

    def hposition_find(self):
        return t.hpos_find()

    def hheading_find(self):
        return heading()

    def hdistance(x: float, y: float):
        return distance(x, y)

    def hdegerees(circle_full: float):
        degrees(circle_full)

    def hradians(self):
        radians()

    def hpendown(self):
        pd()

    def hpd(self):
        t.hpendown()

    def hd(self):
        t.hpd()

    def hdown(self):
        t.hd()

    def hpenup(self):
        pu()

    def hpu(self):
        t.hpenup()

    def hu(self):
        t.hpu()

    def hup(self):
        t.hu()

    def hpen_size(width: int):
        pensize(width)

    def hpensize_find(self):
        return pensize()

    def hwidth(width: int):
        t.hpen_size(width)

    def hwidth_find(self):
        return t.hpensize_find()

    def his_down(self):
        return isdown()

    def his_up(self):
        return not isdown()

    def hfill(self):
        filling()

    def hbegin_fill(self):
        begin_fill()

    def hend_fill(self):
        end_fill()

    def hreset(self):
        reset()

    def hclear(self):
        clear()

    def hwrite(arg: object, move: bool = False, align: str = "left", font: tuple = (str, int, str)):
        write(arg, move, align, font)

    def hshow_turtle(self):
        showturtle()

    def hst(self):
        t.hshow_turtle()

    def hhide_turtle(self):
        hideturtle()

    def hht(self):
        ht()

    def is_visible(self):
        return isvisible()

    def is_unvisible(self):
        return not t.is_visible()

    def hshape(shapes: str = None):
        if shapes is None:
            return shape()
        shape(shapes)
        return shapes

    def hresize_mode(value: str = None):
        if value is None:
            return resizemode()
        resizemode(value)
        return value

    def hshape_size(width: float | None = None, height: float | None = None, out_line: float | None = 0):
        if width == height is None and out_line == 0:
            return shapesize()
        shapesize(width, height, out_line)
        return width, height, out_line

    def t_size(width: float | None = None, height: float | None = None, out_line: float | float | None = 0):
        return t.hshape_size(width, height, out_line)

    def hshear_factor(shear):
        if shear in None:
            return shearfactor()
        shearfactor(shear)
        return shear

    def hset_tilt_angle(angle: float | int = float):
        settiltangle(angle)

    def htilt_angle(angle: float | None = None):
        if angle is None:
            return tiltangle()
        tiltangle(angle)
        return tiltangle()

    def htilt(angle: float):
        tilt(angle)

    def hshape_transform(t1: float | None = None, t2: float | None = None, t3: float | None = None,
                         t4: float | None = None):
        if t1 == t2 == t3 == t4 is None:
            return shapetransform()
        shapetransform(t1, t2, t3, t4)
        return shapetransform()

    def hget_shape_poly(self):
        return get_shapepoly()

    def hon_click(fun, btn: int, add=None):
        onclick(fun, btn, add)

    def hon_release(fun, btn: int, add=None):
        onrelease(fun, btn, add)

    def hon_drag(fun, btn: int, add=None):
        ondrag(fun, btn, add)

    def hbegin_polly(self):
        begin_poly()

    def hend_polly(self):
        end_poly()

    def hget_polly(self):
        return get_poly()

    def hbgcolor(color_r=None, g=None, b=None):
        bgcolor(color_r)
        if g is not None:
            bgcolor(color_r, g, b)
        elif color_r is None:
            return bgcolor()
        return bgcolor()

    class hget_color:
        def __init__(self) -> NoReturn:
            raise NameError(
                f"name 't.hget_color' not defined. help: this fucntion is disenabled. try another function...")

        def yellow(value: str | None = None):
            raise NameError(
                f"name 't.hget_color.yellow({value}) not defined. help: this fucntion is disenabled. try another "
                f"function...")
            if value == "milk":
                # 乳
                return 254, 243, 201
            elif value == "fujiette":
                # 富春纺
                return 254, 244, 180
            elif value == "milk brown":
                # 乳褐
                return 235, 216, 184
            elif value == "corn":
                # 玉米
                return 239, 205, 169
            elif value == "barley":
                # 大麦彩
                return 219, 202, 166
            elif value == "branch":
                # 树枝
                return 219, 199, 166
            elif value == "magnolia":
                # 木兰彩
                return 191, 178, 150
            elif value == "elephant teeth":
                # 象牙
                return 253, 238, 175
            elif value == "kobato":
                # 小鸠
                return 239, 222, 176
            elif value == "teeth":
                # 牙
                return 238, 222, 176
            elif value == "licorice":
                # 甘草
                return 228, 207, 142
            elif value == "brimstone":
                # 硫磺石
                return 215, 193, 107
            elif value == "steamed chestnut":
                # 蒸䅇
                return 217, 205, 144
            elif value == "tender bud color":
                # 嫩芽彩
                return 183, 185, 154
            elif value == "vegetable flower":
                # 菜花
                return 247, 217, 76
            elif value == "tender ginger":
                # 嫩姜
                return 254, 242, 99
            elif value == "dandong stone":
                # 丹东石
                return 249, 228, 89
            elif value == "luffa flower":
                # 丝瓜花
                return 247, 231, 32

            return "value not found in list(type holiday.t.get_color.yellow_help() OR t.get_color.yellow_help() for " \
                   "help)"

        def yellow_help(high_level_option=None):
            if high_level_option is None:
                high_level_option={}
            avalible=["milk", "fujiette", "milk brown", "corn", "barley", "branch", "magnolia", "elephant teeth",
                      "kobato", "teeth", "licorice", "brimstone", "steamed chestnut", "tender bud color"]
            avalible=hc.hextent(avalible, ["vegetable flower", "tenger ginger", "dandong stone", "luffa flower"])
            out=f"only avalible for {avalible}"
            print(out)
            return out


class music:
    def mouse(value: int = 1, height: int = 1):
        if not height:
            if value == 5:
                open("holiday/music/mouse50.mp3")
            elif value == 6:
                open("holiday/music/mouse60.mp3")
            elif value == 7:
                open("holiday/music/mouse70.mp3")
            else:
                return "foundless"
        elif height == 1:
            if value == 1:
                open("holiday/music/mouse11.mp3")
            elif value == 2:
                open("/holiday/music/mouse21.mp3")
            elif value == 3:
                open("holiday/music/mouse31.mp3")
            elif value == 4:
                open("holiday/music/mouse41.mp3")
            elif value == 5:
                open("holiday/music/mouse51.mp3")
            elif value == 6:
                open("holiday/music/mouse61.mp3")
            elif value == 7:
                open("holiday/music/mouse71.mp3")
            else:
                return "foundless"
        elif height == 2:
            if value == 1:
                open("holiday/music/mouse12.mp3")
            elif value == 2:
                open("holiday/music/mouse22.mp3")
            elif value == 3:
                open("holiday/music/mouse32.mp3")
            elif value == 4:
                open("holiday/music/mouse42.mp3")
            elif value == 5:
                open("holiday/music/mouse52.mp3")
            elif value == 6:
                open("holiday/music/mouse62.mp3")
            elif value == 7:
                open("holiday/music/mouse72.mp3")
            elif value == 8:
                music.mouse(1, 3)
            else:
                return "foundless"
        elif height == 3:
            if value == 1:
                open("holiday/music/mouse13.mp3")
            else:
                return "foundless"
        else:
            return "foundless"


def hgcd(value1: int, value2: int):
    # value1*value2/t{max getting divided by both}
    t=0
    for i in range(hc.hmax((value1, value2)), 2, -1):
        if hdiv.hno(value1, i) == 0 == hdiv.hno(value2, i):
            t=i
            break
    return hdiv.hdiv(hmul(value1, value2), t)


class hnumber_train:
    def adder(hlen, one=1, two=1):
        # check for never stop error;:
        if hlen > 10 ** 44:
            raise ValueError(f"too big! 'cannot return more than 10**44 of the {'number train'}'")
        if one == two == 0:
            raise RecursionError("forever error! {'never end because 0,0,0,0'}")
        values=[one, two]
        for i in range(hlen):
            values=hc.happend(values, values[0] + values[1])
        values=htuple(values)
        return values


def big_equal_small(a=None, b=None, big=False, equal=False, small=False):
    if big:
        if equal:
            if small:
                return True
            else:
                return a >= b
        else:
            if small:
                return a != b
            else:
                return a > b
    else:
        if equal:
            if small:
                return a <= b
            else:
                return a == b
        else:
            if small:
                return a != b
            else:
                return False


class haon:
    def hand(*values):
        for a in values:
            if not a:
                return False
        return True

    def hor(*values):
        for a in values:
            if a:
                return True
        return False

    def hnot(value):
        if value:
            return False
        return True


def hstr_big_small(value1, value2):
    str_list={"1": 1, "2": 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0, "`": 10, "~": 11, "!": 12,
              "@": 13, "#": 14, "$": 15, "%": 16, "^": 17, "&": 18, "*": 19, "(": 20, ")": 21, "_": 22, "-": 23,
              "+": 24, "=": 25, " ": 26, "{": 27, "}": 28, "|": 32, "\\": 31, ":": 32, ";": 33, "'": 34, '"': 35,
              "<": 36, ",": 37, ">": 38, ".": 39, "?": 40, "/": 41, 29: "[", 30: "]", 42: " "}
    for i in range(hc.hmin([hc.hlen(value1), hc.hlen(value2)])):
        if str_list[value1[i]] < str_list[value2[i]]:
            return "a<b"
        elif str_list[value1[i]] > str_list[value2[i]]:
            return "a>b"
    if value1 == value2:
        return "exact equal"
    return "not equal len(front equal)"


def his_forever(value: str):
    value_list=[]
    for a in value:
        value_list=hc.happend(a)
    value_list=htuple(value_list)
    stable="<type 'bool'>"
    for i in range(hc.hlen(value_list)):
        if value_list[i]:
            # isn't stable value
            stable=False
            break
    if stable == "<type bool>":
        del codes, value, stable
        return {"answer": bool(value)}
    return {"answer": "TrueFalse", "error": "not be equaled", None: None}


def num_translate(max_1: int, value: float, number: tuple, show: tuple, error1="#Type-Error\nvalue=arguments",
                  error2="#len-error\nvalue=arugument_-_equal_len"):
    # arugument changing warning:change values expecting max_1, value, number, show values may cause code error!
    # error check=True
    if not type(max_1) == "int" and type(value) in ["float", "int"] and type(number) == type(show) == "tuple":
        raise TypeError(error1)
    if not hc.hlen(number) == hc.hlen(show) == max_1 - 1:
        raise IndexError(error2)
    # error check=False
    out_value=""
    for translate in range(0, hlen(value)):
        add=show[value]
        out_value=out_value + add
    del add
    return out_value


def hstr_add(value1, value2, str1=True, str2=True, appear_warn=False):
    if str1:
        if str2:
            out={"value": hstr(value1) + hstr(value2)}
        else:
            out={"value": hstr(value1) + value2}
    else:
        if str2:
            out={"value": value1 + hstr(value2)}
        else:
            out={"value": value1 + value2}
    if (str1, str2) != (True, True):
        out["warn"]=True
        out["warning"]="changed unsure argument"
    else:
        out["warn"]=False
        out["warning"]="None"
    if appear_warn and out["warn"]:
        print("warn", out["warn"], "warning:", out["warning"], sep="\n")
    return out
    # reminder of getting value:to get value type hstr_add(value1,value2)["value"] to get the value
    # if you want to get if warn: type hstr_add(value1,value2)["warn"] to get the bool{True,False} value
    # if you want to know why warning type hstr_add(value1,value2)["warning"] to know why


class hlistd:
    def hto(value: list):
        return_value={}
        for a in range(hc.hlen(value)):
            return_value[a]=value[a]
        for a in range(hc.hlen(value)):
            return_value[0 - (a + 1)]=value[hminus(hc.hlen(value), a)]
        return return_value

    def happend(value, add):
        list(value)
        a=hc.happend(add)
        a=hlistd.hto(a)
        return a

    def hinsert(value, where, add):
        list(value)
        a=hc.hinsert(value, where, add)
        a=hlistd.hto(a)
        return a

    def hothers(self):
        return


class hequ_minus:
    def ha(a: float, place: int, d: float, type_error="TypeError!"):
        # don't change the arguments expecting {a,place,d} or it might cause code ERROR!
        if not type(a) == type(d) == "float" and type(place) == "int":
            return TypeError("type is not allowed!")
        a_=a - (place - 1) * d
        if type_error != "TypeError":
            return {"value": a_, "warn": True, "warning": "changed arguments"}
        raise {"value": a_, "warn": False, "warning": None}
        # get value=ha(a,b,a_place,b_place)["value"]
        # if warn and why warn==same as get value with change {warn,warning}

    def hbetween(a: float, b: float, a_place: int, b_place: int):
        d=(a - b) / (a_place - b_place)
        return d

    def hminus(a: float, b: float, a_place: int, b_place: int):
        return hequ_minus.hbetween(a, b, a_place, b_place)

    def hlen(start: float, end: float, d: float):
        return (end - start) / d + 1

    def hsum(start: float, end: float, leng: int):
        return (start + end) / 2 * leng

    def hint(value=0):
        return hint(value, None)


def haddl(values: tuple):
    answer=0
    for i in range(hc.hlen(values)):
        answer=hadd(answer, values[i])
    return answer


def hminusl(values: tuple):
    answer=0
    for i in range(hc.hlen(values)):
        answer=hminus(answer, values[i])
    return answer


def hmull(values: tuple):
    answer=0
    for i in range(hc.hlen(values)):
        hmul(answer, values[i])
    return answer


def hdivl(values: tuple):
    answer=0
    for i in range(hc.hlen(values)):
        answer=hdiv(answer, values[i])
    return answer


def hpowl(values: tuple):
    answer=0
    for i in range(hc.hlen(values)):
        answer=hpow(answer, values[i])
    return answer


class hsquareQ:
    def hall(is_whole: bool = False, floorORa: float = None, aORn: float = None, is_easy: bool = True):
        if is_whole:
            return hpow(floorORa, 2)
        else:
            if is_easy:
                return hmull((floorORa, hminus(aORn, floorORa), 4))
            else:
                return aORn * floorORa - ((floorORa + 1) * floorORa / 2)


def hS(_type_: str, side_len1: float, side_len2: float = None, side_len3: float = None):
    if _type_ == "square":
        return hpow(side_len1, 2)
    if _type_ == "triangle":
        p=(side_len1 + side_len2 + side_len3) / 2
        return hsqrt(p * (p - side_len3) * (p - side_len2) * (p - side_len1))
    if _type_ == "rectangle":
        return side_len1 * side_len2
    if _type_ == "circle":
        pi=3.141592654
        return pi * side_len1 ** 2
    if _type_ == "trapezium":
        return (side_len1 + side_len2) * side_len3 / 2
    if _type_ == "parallelogram":
        return side_len1 * side_len2
    if _type_ == "diamond":
        return 0.5 * side_len1 * side_len2
    return "not avalible please make sure that your typing is one of in these groups:\
    \n(square,triangle,rectangle,circle,parallelogram,diamond)"


def hleap(year: int):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        if year % 4 == 0:
            return True
        else:
            return False


class hid_card_check_zip:
    def check_len(value: str, high_level_options=None):
        if high_level_options is None:
            high_level_options={"error value": 0}
        if type(value) in ("<class 'list'>", "<class 'tuple'>", "<class 'dict'>", "<class 'set'>"):
            hid_card_check_zip.check_len(value[high_level_options["error value"]])
        if type(value) != "<class 'str'>":
            hid_card_check_zip.check_len(str(value))
        if hc.hlen(value) == 18:
            return {"value": True, "len": 18}
        else:
            return {"value": False, "_len_": hc.hlen(value)}

    def things_in1(value: str):
        out={}
        let=0
        for valuep in value:
            if valuep in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                out[let]=False
            else:
                out[let]=True
                return True
            let+=1
        del let
        return False

    def things_in2(value: str):
        if value[17] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', "X"):
            return False
        else:
            return True

    def year(value: str):
        if int(strftime("%Y", localtime())) <= int(value[6:10]):
            return True
        else:
            return False

    def month(value: str):
        if value[10:13] in ("01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"):
            return True
        else:
            return False

    def day(value: str):
        month, day=int(value[10:13]), int(value[12:14])
        if month == 2:
            if hleap(int(value[6:10])):
                biggest1=30
            else:
                biggest1=29
            if 0 < day < biggest1:
                del biggest1, month, day
                return True
            else:
                del biggest1, month, day
                return False
        elif month in (1, 3, 5, 7, 8, 10, 12):
            if 0 < day < 32:
                del month, day
                return True
            else:
                del month, day
                return False
        else:
            if 0 < day < 31:
                del month, day
                return True
            else:
                del month, day
                return False


def hid_card_check(value: str):
    if not hid_card_check_zip.check_len(value)["value"]:
        _len_=hid_card_check_zip.check_len(value)["_len_"]
        out=f"the len is wrong! the correct len is 18 but your len is {_len_}"
        del _len_
        return out
    if hid_card_check_zip.things_in1(value):
        return "the value in the first 17 letters and not avalible"
    if hid_card_check_zip.things_in2(value):
        return "the value last letter can only be (0,1,2,3,4,5,6,7,8,9,X)"
    if not hid_card_check_zip.year(value):
        return "the year should not be future than now."
    if not hid_card_check_zip.month(value):
        return "the month is not real"
    if not hid_card_check_zip.day(value):
        return "the day is not real"
    return f"{value} have no easy problems.\nIs there still?"


class ammd:
    class a:
        def __init__(self, a, b):
            self.a=a
            self.b=b

        def get(self):
            return hadd(self.a, self.b)

    class mi:
        def __init__(self, a, b):
            self.a=a
            self.b=b

        def get(self):
            return hminus(self.a, self.b)

    class mu:
        def __init__(self, a, b):
            self.a=a
            self.b=b

        def get(self):
            return hmul(self.a, self.b)

    class d:
        def __init__(self, a, b):
            self.a=a
            self.b=b

        def d(self):
            return hdiv.hdiv(self.a, self.b)

        def g(self):
            return hdiv.hfull(self.a, self.b)

        def m(self):
            return hdiv.hno(self.a, self.b)


class hcircle:
    def __init__(self, radius):
        self.r=radius
        self.pi=3.1415926

    def S(self):
        return self.r * self.pi ** 2

    def whole(self):
        return 2 * self.pi * self.r


class human(object):
    name="human"

    @classmethod
    def outr(cls):
        return cls.name

    def outo(cls):
        print(cls.name)
        return human.outr()


class hwcircle(object):
    def __init__(self, radius):
        self.r=radius
        self.pi=3.1415926

    def __pow2(self):
        return self * self

    def __mul2(self):
        return self + self

    def S(self):
        return self.r * hwcircle.__pow2(self)

    def whole(self):
        return hwcircle.__mul2(self.pi * self.r)


class hcylinder(hwcircle):
    def __init__(self, radius, height):
        hwcircle.__init__(self, radius)
        self.h=height

    def S(self):
        return self.whole * self.h


class ball_paddle_game:
    class Ball(pygame.sprite.Sprite):
        def __init__(self, image_file, location, speed, lives=3):
            pygame.sprite.Sprite.__init__(self)
            self.image=pygame.image.load(image_file)
            self.rect=self.image.get_rect()
            self.rect.topleft=location
            self.speed=speed
            self.lives=lives
            self.score_point=0

        def __show_lives(self, scrobj):
            if self.lives > 0:
                for i in range(self.lives):
                    scrobj.blit(self.image, (scrobj.get_width() - 40 * i, 20))

        def __show_score(self, scrobj):
            score_font=pygame.font.Font(None, 50)
            score_text=score_font.render(str(self.score_point), True, (0, 255, 255))
            scrobj.blit(score_text, (10, 10))

        def move_ctrl(self, scrobj, padobj):
            self.__show_lives(scrobj)
            self.__show_score(scrobj)
            self.rect.move_ip(self.speed)
            scrobj.blit(self.image, self.rect)
            if self.rect.left < 0 or self.rect.right > scrobj.get_width():
                self.speed[0]=-self.speed[0]
            if self.rect.top <= 0:
                self.score_point+=1
                self.rect.top=0
                self.speed[1]=randint(5, 10)
            if pygame.sprite.collide_rect(self, padobj):
                self.rect.bottom=padobj.rect.top
                self.speed[1]=-self.speed[1]
            if self.rect.top >= scrobj.get_height():
                self.lives-=1
                self.rect.topleft=(50, 50)
                pygame.time.delay(500)

    class Paddle(pygame.sprite.Sprite):
        def __init__(self, location):
            pygame.sprite.Sprite.__init__(self)
            image_surface=pygame.surface.Surface((100, 10))
            image_surface.fill((0, 0, 0))
            self.image=image_surface.convert()
            self.rect=self.image.get_rect()
            self.rect.topleft=location

        def move_ctrl(self, scrobj):
            mouse_pos=pygame.mouse.get_pos()
            self.rect.centerx=mouse_pos[0]
            scrobj.blit(self.image, self.rect)

    pygame.init()
    screen=pygame.display.set_mode((640, 480))
    clock=pygame.time.Clock()
    initspeed=[randint(-10, -5), randint(5, 10)]
    myball=Ball("holiday/pygame.png/pingpang.png", (50, 50), initspeed, 3)
    mypaddle=Paddle((270, 400))
    while True:
        for event in pygame.event.get():
            if event.type == quit:
                pygame.quit()
                py.exit()
        clock.tick(30)
        screen.fill((255, 255, 255))
        if myball.lives > 0:
            myball.move_ctrl(screen, mypaddle)
            mypaddle.move_ctrl(screen)
        else:
            ft1_font=pygame.font.Font(None, 70)
            ft1_surf=ft1_font.render("Game over!", True, (255, 0, 255))
            ft1_rect=ft1_surf.get_rect()
            ft1_rect.center=(screen.get_rect().centerx, 100)
            ft2_font=pygame.font.Font(None, 50)
            ft2_surf=ft2_font.render("Your score: " + str(myball.score_point), True, (0, 255, 255))
            ft2_rect=ft2_surf.get_rect()
            ft2_rect.center=(screen.get_rect().centerx, 200)
            screen.blit(ft1_surf, ft1_rect)
            screen.blit(ft2_surf, ft2_rect)
            break
        pygame.display.flip()


def hrange(start: float | int = 0, end: float | int = None, step: int | float = 1,
           high_level_options=None):
    if high_level_options is None:
        high_level_options={"HOLIDAY-SETTINGS.include 'start'": True,
                            "HOLIDAY-SETTINGS.include 'end'": False, "HOLIDAY-SETTINGS.out type": tuple}
    if end is None:
        end, start=start, 0
    if not high_level_options["HOLIDAY-SETTINGS.include 'start'"]:
        hrange(start + step, end, step)
    if high_level_options["HOLIDAY-SETTINGS.include 'end'"]:
        hrange(start, end + step, step)
    out=[]
    while start < end:
        out=hc.happend(out, start)
        start+=step
    out=high_level_options["HOLIDAY-SETTINGS.out type"](out)
    del start, end, step, high_level_options
    return out


class amimud:
    def __init__(self, a, b):
        self.a=a
        self.b=b

    def get(self):
        return {"+": self.a + self.b, "-": self.a - self.b, "*": self.a * self.b, "/": self.a / self.b,
                "//": self.a // self.b, "%": self.a % self.b}


class aon:
    def __init__(self, values: tuple | bool):
        self.values=values

    def hand(self):
        return False not in self.values

    def hor(self):
        return True in self.values

    def hnot(self):
        return not self.values


def buy(money=1000, things=(2, 3, 5, 10, 188)):
    out=[]
    for item in things:
        out=hc.happend(f"He can buy {money // item} of them, have {money % item} money left, can buy {money / item}")
    out=htuple(out)
    return out


def test(values):
    out=[]
    for item in values:
        out.append(item == 100)
    out=tuple(out)
    return out


class split:
    def __init__(self, value="@required", seperator=" "):
        self.value=str(value)
        self.sep=str(seperator)

    def split(self):
        out=[]
        for find in range(hlen(self.value)):
            if self.value[find:find + hlen(self.sep)] == self.sep:
                out=hc.happend(out, self.value[:find])
        out=tuple(out)
        return out


class hsmm:
    def __init__(self, a: float | int = "float|int", b: float | int = "float|int", sum_: bool = False,
                 minus: bool = False, times: bool = False):
        self.a=a
        self.b=b
        self.add=sum_
        self.minus=minus
        self.mul=times

    def __checker(self):
        # checker:
        if self.add == self.minus == self.mul:
            raise ValueError("argument error: sum==minus==times==True 'do you mean sum=minus=True times=False'")
        if not self.add == self.minus == self.mul:
            raise ValueError(
                "argument error: sum==minus==times==False is auto 'please type two of the aruguments\
                 and change them all to True'")
        if (self.add and not (self.minus and self.mul)) or (self.minus and not (self.add and self.mul)) or (
                self.mul and not (self.add and self.minus)):
            raise ValueError("argument error: at least enter two arguments and make sure they are all True")
        if self.a == "float|int" or self.b == "float|int":
            raise ValueError("argument error: a and .b are required arguments")
        if not (type(self.a) in (int, float) or type(self.b) in (int, float)):
            raise ValueError("argument error: type of a and b are not supported")
        return "no problem"

    def run(self):
        # {"big":value,"small":value}
        hsmm.__checker(self)
        if self.add and self.minus:
            return {"big": (self.add + self.minus) / 2, "small": (self.add - self.minus) / 2}
        if self.add and self.mul:
            return {"small": self.add / (self.mul + 1), "big": self.add - (self.add / (self.mul + 1))}
        if self.minus and self.mul:
            return {"small": self.minus / (self.mul - 1), "big": (self.minus / (self.mul - 1)) + self.minus}
        raise RecursionError("not avalible")


class hletter:
    def __init__(self, value):
        self.value=value

    def small_letter(self):
        return (
            "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x",
            "c",
            "v", "b", "n", "m")

    def big_letter(self):
        return (
            "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "S", "D", "F", "G", "H", "J", "K", "L", "Z",
            "X",
            "C", "V", "B", "N", "M")

    def all(self):
        return hletter.small_letter() + hletter.big_letter()

    def __oppsite(self):
        s, b, out=hletter.small_letter(), hletter.big_letter(), {}
        for i in range(26):
            out[s[i]]=b[i]
            out[b[i]]=s[i]
        del s, b
        return out

    def oppsite(self):
        o=""
        for part in self.value:
            if part in hletter.all():
                o+=hletter.__oppsite()[part]
            else:
                o+=part
        return o

    def __small_to_big(self):
        small=hletter.small_letter()
        big=hletter.big_letter()
        out=hletter.oppsite()
        for number in range(hc.hmax((hc.hlen(small), hc.hlen(big)))):
            out[small[number]]=big[number]
            out[big[number]]=small[number]
        return out

    def small_to_big(self):
        sb=hletter.__small_to_big()
        out=""
        for part in self.value:
            if part in hletter.all():
                out=f"{out}{sb[part]}"
                continue
            out=f"{out}{part}"
        del bs
        return out

    def __big_to_small(self):
        small, big, out=hletter.small_letter(), hletter.big_letter(), hletter.oppsite()
        for change in range(26):
            out[small[change]]=big[change]
            out[big[change]]=small[change]
        del small, big
        return out

    def big_to_small(self):
        bs=hletter.__big_to_small()
        out=""
        for part in self.value:
            if part in hletter.all():
                out=f"{out}{bs[part]}"
                continue
            out=f"{out}{part}"
        del bs
        return out


class people:
    def __init__(self, name, age, phone_number, wechat, people_list=None):
        if people_list is None:
            people_list=[]
        self.peoplel=people_list
        self.name=name
        self.age=age
        self.pn=phone_number
        self.wechat=wechat

    def menu(self, run_type: int):
        # print("  ")
        # print("***--- people ---***")
        # print("---1. add people ---")
        # print("---2. find people ---")
        # print("---3. delete people ---")
        # print("---4. view people ---")
        # print("---5. exit ---------")
        if type(run_type) != int:
            raise TypeError("type not allowed")
        return run_type

    # noinspection PyAttributeOutsideInit
    def add(self):
        self.people={"name": self.name, "age": self.age, "num": self.pn, "wechat": self.wechat}
        self.peoplel=hc.happend(self.people, people)
        with open("/holiday/people(class)/people_information", "w") as f:
            f.write(str(self.peoplel))

    def find(self):
        flag=0
        for people in people.people_list:
            if self.name == people["name"]:
                return self.people
        if not flag:
            raise IndexError(f"cannot find {self.people}")

    def delete(self):
        flag=0
        for people in self.people:
            if self.name == self.people["name"]:
                self.people.remove(people)
                return self.people
        if not flag:
            raise IndexError(f"cannot find {self.people}")

    def view(self):
        if not len(self.people):
            return 0
        else:
            return self.people

    def run(self):
        if True:
            while True:
                a=people.menu()
                if a == 1:
                    people.add()
                elif a == 2:
                    people.find()
                elif a == 3:
                    people.delete()
                elif a == 4:
                    people.view()
                elif a == 5:
                    py.exit()


class hstrn:
    def __init__(self, value1, value2):
        self.value1=value1
        self.value2=value2

    def strn(high_level_options_keys: tuple = None):
        out={}
        warning=0
        if high_level_options_keys is not None:
            out[f"warning{warning}?"]=True
            out[f"warning{warning}"]="high_level_options1_typed!"
            warning+=1
        if high_level_options_values is not None:
            out[f"warning{warning}?"]=True
            out[f"warning{warning}"]="high_level_options2_typed!"
        if high_level_options_values is None:
            high_level_options_values=[' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', "$", "%",
                                       "^", "&", "*", "(", ")", "+", "-"]
            for i in range(26):
                high_level_options_values.append(hletter.small_letter()[i])
            for i in range(26):
                high_level_options_values.append(hletter.big_letter()[i])
            high_level_options_values.extent(['['], "]", "{", "}", "|", "\\", ":", ";", "\"", "\'", "<", ">", "=", ",",
                                             ".", "?", "/", "~", "`")
        out["out"]=tuple(high_level_options_values)
        return out

    def is_small(self):
        root=hstrn.strn()["value"]
        tn1=tn2=[]
        for a, b in self.value1, self.value2:
            tn1.append(a)
            tn2.append(b)
        self.value1=self.value2="delated"
        out=[]
        for i in range(min((tn1, tn2))):
            if root[tn1] < root[tn2]:
                return out.append(True)
            out.append(False)
        for i in range(hlen(tn1) - hlen(tn2)):
            out.append("Error! one of the two values are ended but one haven't")
        out=tuple(out)
        return out

    def is_big(self):
        out=hlist(hstrn(self.value1, self.value2).is_small())
        for part in range(hlen(out)):
            if out[type(part)] == bool:
                out[part]=not out[part]
                continue
            pass

    def is_equ(self):
        root=hstrn.strn()["value"]
        tn1=tn2=[]
        for a, b in self.value1, self.value2:
            tn1.append(a)
            tn2.append(b)
        self.value1=self.value2="delated"
        out=[]
        for i in range(min((tn1, tn2))):
            if root[tn1] == root[tn2]:
                return out.append(True)
            out.append(False)
        for i in range(hlen(tn1) - hlen(tn2)):
            out.append("Error! one of the two values are ended but one haven't")
        out=tuple(out)
        return out

    def is_es(self):
        root=hstrn.strn()["value"]
        tn1=tn2=[]
        for a, b in self.value1, self.value2:
            tn1.append(a)
            tn2.append(b)
        self.value1=self.value2="delated"
        out=[]
        for i in range(min((tn1, tn2))):
            if root[tn1] <= root[tn2]:
                return out.append(True)
            out.append(False)
        for i in range(hlen(tn1) - hlen(tn2)):
            out.append("Error! one of the two values are ended but one haven't")
        out=tuple(out)
        return out

    def is_eb(self):
        root=hstrn.strn()["value"]
        tn1=tn2=[]
        for a, b in self.value1, self.value2:
            tn1.append(a)
            tn2.append(b)
        self.value1=self.value2="delated"
        out=[]
        for i in range(min((tn1, tn2))):
            if root[tn1] >= root[tn2]:
                return out.append(True)
            out.append(False)
        for i in range(hlen(tn1) - hlen(tn2)):
            out.append("Error! one of the two values are ended but one haven't")
        out=tuple(out)
        return out

    def is_sb(self):
        root=hstrn.strn()["value"]
        tn1=tn2=[]
        for a, b in self.value1, self.value2:
            tn1.append(a)
            tn2.append(b)
        self.value1=self.value2="delated"
        out=[]
        for i in range(min((tn1, tn2))):
            if root[tn1] != root[tn2]:
                return out.append(True)
            out.append(False)
        for i in range(hlen(tn1) - hlen(tn2)):
            out.append("Error! one of the two values are ended but one haven't")
        out=tuple(out)
        return out

    def is_sbe(self):
        return (True,)

    def is_any(self):
        return (False,)


def hammd(values: tuple, middle: tuple):
    if type(values) != type(middle) or type(values) != tuple or type(middle) != tuple:
        raise TypeError("type not allowed")
    if hlen(values) < 2:
        raise TypeError("type not allowed")
    if hlen(values) == 2:
        if middle == "(+":
            return haddl(values)
        if middle == "(-":
            return hminusl(values)
        if middle == "(*":
            return hmull(values)
        if middle == "(/":
            return hdiv.hdiv(values[0], values[1])
        if middle == "(//":
            return hdiv.hfull(values[0], values[1])
        if middle == "(%":
            return hdiv.hno(values[0], values[1])
    # ——————————————————————————————————————————————————————————————————————————————————————————
    for dectecto in range(hlen(values) - 1):
        if middle[dectecto][0] != "(":
            continue

        for dectecti in range(hlen(values) - dectecto):
            if middle[dectecti] != ")":
                continue

            hammd()


class htimer:
    def __input(self):
        return input("time is up! know? (y/n)") == "y"

    def __alarm(self):
        print("\a")
        return "alarm"

    def hbs(start: int, every_warning: bool = False, end_warning: bool = True):
        global together
        while start > 0:
            start-=1
            if every_warning:
                print("\a")
            sleep(1)
        if end_warning:
            together.start_new_thread(htimer.__input())
            together.start_new_thread(htimer.__alarm())
            while True:
                pass
        else:
            del together
            htimer.__input()


def is_intg(n):
    try:
        hint(n)
    except ValueError:
        return False
    else:
        return True


def hraise(_type: any, out: str):
    out=str(out)
    raise _type(out)


def hpass(*args: any):
    return (args,)


class hfive_olympic_rings:
    def __one(self, x: int | float, y: int | float, r: int | float, c: str | None = None):
        pu()
        setpos(x, y)
        pd()
        pensize(5)
        pencolor(c)
        fillcolor("white")
        circle(r)
        return (
            "pu", f"pos=({x},{y})", "pd", "size=5", "pencolor={}".format(c), "fillcolor=white", "circle.r={}".format(r),
            "circle.d={}".format(r + r), "return=.return")

    def __init__(self, show=False):
        if show:
            hideturtle()
        else:
            showturtle()
        hfive_olympic_rings.__one(None, -100, 0, 50, "blue")
        hfive_olympic_rings.__one(None, 0, 0, 50, "black")
        hfive_olympic_rings.__one(None, 110, 0, 50, "red")
        hfive_olympic_rings.__one(None, -55, -50, 50, "yellow")
        hfive_olympic_rings.__one(None, 55, -50, 50, "green")
        return "locked"


class strl:
    def __init__(self, value):
        self.value=value

    def str_list(self):
        x=[]
        for a in self.value:
            x=hc.happend(x, a)
        x=tuple(x)
        return x

    def list_str(self):
        x=""
        for a in self.value:
            x="{}{}".format(x, a)
        return x


class hguess_prize:
    def __start(self):
        global user_info
        if self.self.out:
            name=input("please type your name")
            age=input("{} hello, please type your age(int)".format(name))
        else:
            try:
                name, age=self.high_level_options["name"], self.high_level_options["age"]
            except KeyError:
                raise KeyError("ValueError=key not found in high_level_options")
            else:
                hpass()
            finally:
                hpass()
        try:
            age=int(age)
        except ValueError:
            raise ValueError("not a number!")
        else:
            hpass()
        finally:
            hpass()
        self.__user_info={'name': name, 'age': int(age), "float-age": float(int(age))}
        if 10 < self.user_info["age"] < 18:
            self.__user_info["life"]=1000
        elif 17 < self.__user_info["age"] < 31:
            self.__user_info["life"]=1500
        else:
            self.__user_info["life"]=500
        self.__user_info["life"]=self.life
        if self.self.out:
            print("Hi {} with {} age, nice to see you playing this game, your life now is {}.".format(
                self.__user_info["name"], self.__user_info["age"], self.__user_info["life"]))
        sleep(1)
        if self.out:
            print("help of game".center(50, "*"))
            print('*'.ljust(53), '*')
            print('*', end="")
            print('computer will play the dice three times, [if sum>10 type > or type <]'.center(53), end="")
            print('*')
            print('*'.ljust(53), '*')
            for i in range(54):
                print('*', end='')
            print("")

    def __guessing(self):
        print("start guessing".center(53, "-"))
        dices=[]
        for i in range(3):
            dices=hc.happend(dices, randint(0, 6))
        dices=hc.happend(dices, haddl(dices))
        dices=dices[3]
        if self.out:
            typed=input("please type '>' or '<'")
        else:
            try:
                typed=self.high_level_options["n"]
            except KeyError:
                raise KeyError("n-key not find in high_level_options")
        if typed != '>' and typed != "<":
            wng="not avalible for not '>' and '<'"
            if self.out:
                print(wng)
                hguess_prize.__guessing()
            else:
                raise ValueError(str(wng))
            del wng
        self.__sums=dices
        self.__user=typed

    def __usports(self):
        self.__times=1
        if len(self.__user_properties) > 0:
            if self.self.out:
                do=input("do you want to use sports? {'smile':yes,'frown':no}:")
                if do != "smile" or do != "frown":
                    if self.self.out:
                        print("only avalible for [smile(means yes)&frown(means no)]")
                        hguess_prize.__usports()
            else:
                try:
                    do=self.high_level_options["use"]
                except KeyError:
                    raise KeyError("cannot find use key in high_level_options")
                else:
                    hpass()
                finally:
                    hpass()
            if do == ">":
                if self.self.out:
                    do=input("which one? {} avalible only.".format(self.__user_properties))
                else:
                    try:
                        do=self.high_level_options["do-n"]
                    except KeyError:
                        raise KeyError("do-n-key not find in high_level_options")
                    else:
                        hpass()
                    finally:
                        hpass()
                try:
                    self.self.out=int(self.self.out)
                except ValueError:
                    if self.self.out:
                        print("not a number!")
                        hguess_prize.__usports()
                    else:
                        raise ValueError("not a int number!")
                else:
                    hpass()
                finally:
                    hpass()
                if do > hlen(self.__user_info) - 1:
                    if self.self.out:
                        print('type error! not use sports this time.')
                    else:
                        raise ValueError("TypeError! not use sports this time!")
                    return 1
                if self.__user_properties[str(do)] == "X3":
                    self.time=3
                    if self.self.out:
                        print("get 3 times prize")
                if self.__user_properties[str(do)] == "X5":
                    self.time=5
                    if self.self.out:
                        print("get 5 times prize")
                del self.user_properties[str(do)]
            else:
                pass

    def __bsports(self):
        if self.__user_info["life"] % 400 == 0:
            if self.self.out:
                shop=input(
                    "you, [who named as {} with {}], have {} lifes,\
                     do you want to buy sports? frown=no;smile=yes".format(
                        self.__user_info["name"], self.__user_info["age"], self.__user_info["life"]))
            else:
                try:
                    shop=self.high_level_options["buy"]
                except KeyError:
                    raise KeyError("ValueError! buy-key not find in high_level_options")
                else:
                    hpass()
                finally:
                    hpass()
            if shop != "frown" or shop != "smile":
                if self.self.out:
                    print("only avalible for frown and smile (yes and no)")
                    hguess_prize.__bsports()
                else:
                    raise ValueError("only avalible for frown and smile({'frown':'no!','smile','yes!'})")
            if shop == "smile":
                if self.self.out:
                    use=input("whick one?" + str(self.__properties))
                else:
                    try:
                        use=self.high_level_options["choose-str"]
                    except KeyError:
                        raise KeyError("key not find in use(choose-str)")
                    else:
                        hpass()
                    finally:
                        hpass()
                if use == str(0):
                    self.__user_properties[str(hlen(self.__user_properties))]="X3"
                    self.user_info["life"]-=100
                    if self.self.out:
                        print("buying sport is sucessful")
                        print("your life is {}".format(self.user_info["life"]))
                elif use == str(1):
                    self.__user_properties[str(hlen(self.__user_properties))]="X5"
                    self.user_info["life"]-=200
                    if self.self.out:
                        print("buying sport is sucessful")
                        print("your life is {}".format(self.user_info["life"]))
                else:
                    if self.self.out:
                        print("there aren't this sport, please try again.")
                        hguess_prize.__bsports()
                    else:
                        raise ValueError("RecursionError, IndexError also includes! only avalible for [0,1]")

    def __guess(self):
        # sums&user
        if (self.__sums >= 10 and self.__user == ">") or (self.__sums < 10 and self.__user == "<"):
            if self.out:
                print("you self.win!")
            self.__user_info["life"]+=100 * self.__times
        else:
            if self.out:
                print("you lose!")
            self.__user_info["life"]-=100 * self.__times
        if self.out:
            print("now you have {} lifes".format(self.__user_info["life"]))
        if not self.__user_info["life"]:
            if self.out:
                print("you have used all of your lifes. {} Thanks for playing this fun game".format("\n"))
            return 0
        else:
            return "continue playing!"

    def __init__(self, out: bool = True, high_level_options: dict = None):
        self.out=out
        self.high_level_options=high_level_options
        self.__user_info=self.__user_properties={}
        self.__properties=("0-X3-(-100lifes)", "1-X5-(-200lifes)")
        # self.__life="||int|number-according|to|age||"(code is broken!)
        self.__times=1
        self.__sums="int"
        self.__user="> OR <"
        hguess_prize(self.out, self.high_level_options).__start()
        while True:
            hguess_prize.__guess()
            hguess_prize.__bsports()
            if not hguess_prize(self.out, self.high_level_options).__guessing():
                if self.out:
                    hpass()
                else:
                    raise ValueError("there are no lifes left!")


class hwhole_len:
    def __init__(self, *args: object):
        raise NameError(f"name 'hwhole_len({args}) use hC instead")


class hC:
    def __init__(self):
        hpass()

    def __check_error(*args: tuple):
        for item in args:
            if not type(item) in (int, hint, float, hfloat):
                raise TypeError("arguement type not allowed! allowed types: {}".format([int, float, hint, hfloat]))
        return False

    class rectangle:
        def __init__(self, a: int | hint | float | hfloat, b: int | hint | float | hfloat):
            try:
                hC.__check_error((a, b))
            except TypeError:
                raise TypeError("argument type is only allowed with: {}".format([int, float]))
            else:
                hpass()
            finally:
                hpass()
            return (a + b) * 2

    class square:
        def __init__(self, a: int | hint | float | hfloat):
            try:
                hC.__check_error((a,))
            except TypeError:
                raise TypeError("argument type is only allowed with: {}".format([int, float]))
            else:
                hpass()
            finally:
                hpass()
            return hC.rectangle(a, a)

    class circle:
        def __init__(self, dORr: int | float, pi: float | hfloat = 3.1415926, d: bool = True):
            try:
                hC.__check_error((dORr, pi))
            except TypeError:
                raise TypeError("argument type is only allowed with: {}".format([int, float]))
            else:
                hpass()
            finally:
                hpass()
            if type(d) != bool:
                raise TypeError("argument 'd' can only be bool")
            if not d:
                hC.circle(dORr * 2)
            return pi * dORr

    class many_sides:
        def __init__(self, *sides: tuple | htuple | int | hint | float | hfloat):
            try:
                hC.__check_error((sides,))
            except TypeError:
                raise TypeError("argument type is only allowed with: {}".format([int, float]))
            else:
                hpass()
            finally:
                hpass()
            return haddl(sides)

    class part:
        def __init__(self, times: int | hint | float | hfloat, out: int | hint | float | hfloat):
            try:
                hC.__check_error((times, out))
            except TypeError:
                raise TypeError("argument type is only allowed with: {}".format([int, float]))
            else:
                hpass()
            finally:
                hpass()
            return hmul(times, out)


class hBMI:
    def __checker(*args: tuple | htuple | hint | int | hfloat | float) -> False:
        for item in args:
            if not type(item) in (int, float, hint, hfloat):
                raise TypeError("argument error: type only allowed for {}.".format([int, float, hint, hfloat]))
        return False

    def __init__(self, height_m: float | hfloat | int | hint,
                 weight_kg: float | hfloat | int | hint) -> float | int | hfloat | hint:
        hBMI.__checker((height_m, weight_kg))
        return height_m * 100 / weight_kg


class tkinter:
    def __init__(self):
        hpass()

    class amimud:
        def __main(self, __type):
            text=tk.Text(self.win, width=30, height=2)
            try:
                a=int(self.__a1)
            except ValueError:
                try:
                    a=float(self.__a1)
                except ValueError:
                    if self.__out:
                        print("ValueError! first typing area!")
                    else:
                        return True
                    hpass()
                else:
                    hpass()
                    del a
                finally:
                    hpass()
            else:
                hpass()
            finally:
                hpass()
            try:
                a=int(self.__a2)
            except ValueError:
                try:
                    a=float(self.__a2)
                except ValueError:
                    if self.__out:
                        print("ValueError! first typing area!")
                    else:
                        return True
                    hpass()
                else:
                    hpass()
                    del a
                finally:
                    hpass()
            else:
                hpass()
            finally:
                hpass()
            if __type == "+":
                x=a + b
            elif __type == "-":
                x=a - b
            elif __type == "*":
                x=a * b
            elif __type == "/":
                x=a / b
            elif __type == "//":
                x=a // b
            elif __type == "%":
                x=a % b
            else:
                raise NameError("__type argument")
            text.delate(0.0, "end")
            text.insert(tk.INSERT, x)

        def __a(self):
            return tkinter.amimud(self.__out, self.__high_level_options).__main("+")

        def __mi(self):
            return tkinter.amimud(self.__out, self.__high_level_options).__main("-")

        def __mu(self):
            return tkinter.amimud(self.__out, self.__high_level_options).__main("*")

        def __dd(self):
            return tkinter.amimud(self.__out, self.__high_level_options).__main("/")

        def __df(self):
            return tkinter.amimud(self.__out, self.__high_level_options).__main("//")

        def __dl(self):
            return tkinter.amimud(self.__out, self.__high_level_options).__main("%")

        def __init__(self, out: bool = True,
                     high_level_options=None) -> None:
            if high_level_options is None:
                high_level_options={"title": "add&minus&multiply&divide", "self.win_width": 330,
                                    "self.win_height": 300,
                                    "texts-2": ("first number:", "second number:"), "buttons": (
                        "add", "minus", "multiply", "float-divide", "full-divide", "cannot-divide"),
                                    "use_buttons": (True, True, True, True, True, True)}
            self.__out, self.__high_level_options=out, high_level_options
            if (type(out), type(high_level_options)) != (bool, dict):
                raise TypeError("type not allowed")
            self.win=tk.Tk()
            try:
                self.win.title(high_level_options["title"])
            except KeyError:
                if out:
                    print("KeyError of title")
                else:
                    raise KeyError("key-title cannot be found in high_lvel_options")
            else:
                hpass()
            finally:
                hpass()
            try:
                x=high_level_options["self.win_width"]
            except KeyError:
                if out:
                    print("key error of self.win_width")
                else:
                    raise KeyError("cannot find key self.win_width in high_level_options")
            else:
                if (type(x)) not in (float, int):
                    if out:
                        print("x type error!")
                    else:
                        raise TypeError("x type error with ({},{})".format(float, int))
                hpass()
            finally:
                del x
                hpass()
            try:
                x=high_level_options["self.win_height"]
            except KeyError:
                if out:
                    print("key error of self.win_height")
                else:
                    raise KeyError("cannot find key self.win_height in high_level_options")
            else:
                if (type(x)) not in (float, int):
                    if out:
                        print("x type error!")
                    else:
                        raise TypeError("x type error with ({},{})".format(float, int))
                hpass()
            finally:
                del x
                hpass()
            self.win.geometry(
                "{}x{}".format(high_level_options["self.win_width"], high_level_options["self.win_height"]))
            try:
                x=high_level_options["texts"]
            except KeyError:
                if out:
                    print("key-texts not find in high_level_options")
                else:
                    raise KeyError("cannot find key texts in high_level_options")
            else:
                if (type(x)) not in (tuple, list, set):
                    if out:
                        print("high_level_options.key: texts only allowed for tuple,list,set")
                    else:
                        raise TypeError("high_level_options.key: texts only allow {} types".format((tuple, list, set)))
                    hpass()
                if (hlen(x)) != 2:
                    if out:
                        hprint("len error!", "only support for 2")
                    else:
                        raise ValueError("len error!", "\\", "len should ==2")
                    hpass()
                hpass()
            finally:
                del x
                hpass()
            l=tk.Label(self.win, text=str(high_level_options["texts"][0]))
            l.pack()
            a1=tk.Variable()
            e=tk.Entry(self.win, textvariable=a1, show=None)
            e.pack()
            l=tk.Label(self.win, text=str(high_level_options["texts"][1]))
            l.pack()
            a2=tk.Variable()
            e=tk.Entry(self.win, textvariable=a2, show=None)
            e.pack()
            self.__a1, self.__a2=a1, a2
            check=tkinter.amimud.__main()
            if check:
                if out:
                    print("not a number")
                else:
                    raise TypeError("ValueError,TypeError! a or b is not a number")
            if "buttons" not in high_level_options.keys():
                if out:
                    hprint("buttons not found!")
                raise KeyError("key buttons not found in high_level_options")
            if type(high_level_options["buttons"]) not in (tuple, list, set):
                if out:
                    print("TypeError of arguemnt high_level_option's buttons key")
                else:
                    raise TypeError("arguement high_level_options/\\key buttons type_error!")
            if len(high_level_options["buttons"]) != 6:
                if out:
                    print("LenError of arguement high_level_options//\\\\key, button.len()!=6")
                else:
                    raise ValueError("LengthError('len should==6 in high_level_options.key\nlen==6 is correct!')")

            if "use_buttons" not in high_level_options.keys():
                if out:
                    hprint("use_buttons not found!")
                raise KeyError("key use_buttons not found in high_level_options")
            if type(high_level_options["use_buttons"]) not in (tuple, list, set):
                if out:
                    print("TypeError of arguemnt high_level_option's use_buttons key")
                else:
                    raise TypeError("argument high_level_options/\\key use_buttons type_error!")
            if len(high_level_options["buttons"]) != 6:
                if out:
                    print("LenError of arguement high_level_options//\\\\key, use_button.len()!=6")
                else:
                    raise ValueError(
                        "LengthError('use_button key!\nlen should==6 in high_level_options.key\nlen==6 is correct!')")
            if high_level_options["use_buttons"][0]:
                bn1=tk.Button(self.win, text=high_level_options["button"][0], command=tkinter.amimud.__a)
                bn1.pack()
            if high_level_options["use_buttons"][1]:
                bn2=tk.Button(self.win, text=high_level_options["button"][1], command=tkinter.amimud.__mi)
                bn2.pack()
            if high_level_options["use_buttons"][2]:
                bn3=tk.Button(self.win, text=high_level_options["button"][2], command=tkinter.amimud.__mu)
                bn3.pack()
            if high_level_options["use_buttons"][3]:
                bn4=tk.Button(self.win, text=high_level_options["button"][3], command=tkinter.amimud.__dd)
                bn4.pack()
            if high_level_options["use_buttons"][4]:
                bn5=tk.Button(self.win, text=high_level_options["button"][4], command=tkinter.amimud.__df)
                bn5.pack()
            if high_level_options["use_buttons"][5]:
                bn6=tk.Button(self.win, text=high_level_options["button"][5], command=tkinter.amimud.__dl)
                bn6.pack()
            text=tk.Text(self.win, width=30, height=2)
            text.pack()
            self.win.mainloop()

    class key_calculator:
        def __get_input(self, __argu):
            self.__font.insert(tk.END, __argu)

        def __backspace(self):
            input_len=hlen(self.__entry.get)
            self.entry.delate(input_len - 1)

        def __delate(self):
            self.entry.delate(0, tk.END)

        def __calc(self):
            __input__=self.entry.get()
            __output__=str(eval(__input__.strip()))
            tkinter.key_calculator(self.out, self.high_level_options).__delate()
            self.entry.insert(tk.END, __output__)

        def __init__(self, out: bool, high_level_options=None):
            if high_level_options is None:
                high_level_options={"title": "calculator", "button-bg": "#D5E0EE",
                                    "button-press-bg": "#E5E35B", "texts": (
                        "7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "*", "0", ".", "/", "<-", "C", "="),
                                    "rows": (
                                        1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4,
                                        4, 4, 4, 5, 5, 5, 5), "columns": (
                        0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 2, 3, 0, 1, 2)}
            self.out, self.high_level_options=out, high_level_options
            self.__root=tk.Tk()
            try:
                self.__root.title(str(high_level_options["title"]))
            except KeyError:
                if out:
                    print("KeyError cannot find title")
                raise KeyError("title key in high_level_options is not found")
            else:
                hpass()
            finally:
                hpass()
            self.__root.resizable(0, 0)
            self.__main_font=tkf.Font(size=16)
            self.__font=tkf.Font(self.__root, justify="right", font=self.__main_font)
            self.__font.grid(row=0, column=0, columnspan=4, sticky=tk.W + tk.E + tk.N + tk.S)
            self.__button_font=tkf.Font(size=16, weight=tkf.BOLD)
            try:
                self.__button_bg=str(high_level_options["button-bg"])
                self.__button_press_bg=str(high_level_options["button-press-bg"])
            except KeyError:
                if out:
                    print("key button-bg button-press-bg not found!")
                raise KeyError("button-bg\\\\button-press-bg")
            self.__button=partial(tk.Button, self.__root, bg=self.__button_bg, padx=15, pady=5,
                                  activebackground=self.__button_press_bg)
            if hlen(high_level_options["texts"]) != hlen(("7", "8", "9", "+", "4", "5", "6", "-", "1", "2",
                                                          "3", "*",
                                                          "0", ".", "/", "<-", "C", "="
                                                          )) or hlen(high_level_options["rows"]) != 18:
                if out:
                    print("arguments!\nLenError! avalible only for len {}".format("*not avalible"))
                raise ValueError("texts\nlen should = {}".format("*not avalible"))
            for _button_ in range(0, 15, 1):
                button=self.__button(text=high_level_options["texts"][_button_],
                                     command=lambda: tkinter.key_calculator(out, high_level_options).__get_input(
                                         high_level_options["texts"][_button_]))
                button.grid(row=high_level_options["rows"][_button_], column=high_level_options["column"], pady=5)

            button=self.__button(high_level_options["texts"[16]],
                                 command=lambda: tkinter.key_calculator(self.out,
                                                                        self.high_level_options).__backspace(
                                     high_level_options["texts"[16]]))
            button.grid(row=self.high_level_options["rows"][16], column=self.high_level_options["column"][16])
            button=self.__button(high_level_options["texts"[17]],
                                 command=lambda: tkinter.key_calculator(self.out, self.high_level_options).__delate(
                                     high_level_options["texts"[17]]))
            button.grid(row=self.high_level_options["rows"][17], column=self.high_level_options["column"][17])
            button=self.__button(high_level_options["texts"[18]],
                                 command=lambda: tkinter.key_calculator(self.out, self.high_level_options).__calc(
                                     high_level_options["texts"[18]]))
            button.grid(row=self.high_level_options["rows"][18], column=self.high_level_options["column"][18],
                        columnspan=2, padx=3, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)
            self.__root.mainloop()


class ball_racket_game:
    class ball:
        def __init__(self, canvas, colors, racket, brickl, SYSTEM, *args: object) -> tuple[any, ...]:
            self.__canvas=canvas
            self.__id=canvas.create_oval(10, 10, 25, 25, fill=colors)
            self.__racket=racket
            self.__brickl=brickl
            self.SYSTEM=SYSTEM
            possible=hrange(-hlen(self.SYSTEM["background"]), hlen(self.SYSTEM["background"]) + 1)
            possible.remove(0)
            self.__x=choice(possible)
            self.BALL_MODE=1
            self.canvas.move(self.__id, 245, 100)
            return args

        def draw(self, *args: object) -> tuple[any, ...]:
            self.__canvas.move()
            self.__pos=self.__canvas.coords(self.__id)
            if self.__pos[0] <= 0:
                self.__x=1
            elif self.__pos[1] <= 0:
                self.__y=1
            elif self.__pos[2] >= 500:
                self.__x=-1
            elif self.__pos[3] >= 400:
                self.BALL_MODE=0
            else:
                hpass()
            return args

        def hit_racket(self) -> None:
            self.__pos=self.__canvas.coords(self.id)
            self.__racket_pos=self.__canvas.coords(self.__racket.id)

        def hit_brick(self) -> None:
            self.__pos=self.__canvas.coords(self.__id)
            for brick in self.__brickl:
                self.__brick_pos=self.__canvas.coords(brick.id)
                if self.__pos[2] >= self.__brick_pos[0] and self.__pos[0] <= self.__brick_ops[2]:
                    if self.__pos[3] >= self.__brick_pos[1] and self.__pos[1] <= self.__brick_pos[3]:
                        self.__brickl=hc.hremove(self.__brickl, brick)
                        brick.set_color(self.SYSTEM["brick_info"][3])
                        self.__y=0 - self.__y

    class racket:
        def __init__(self, canvas, colors):
            self.__canvas, self.__color=canvas, colors
            self.__x=0
            self.__canvas.blind_all('<KeyPress-Left>', self.__turnleft)
            self.__canvas.blind_all("<KeyPress-Right", self.__turnright)

        def draw(self):
            self.__canvas.move(self.__id, self.__x, 0)
            self.__pos=self.__canvas.coords(self.__id)
            if self.__pos[0] <= 0:
                self.x=-3
            elif self.__pos[2] >= 500:
                self.x=3
            else:
                hpass()

    class brick:
        def __init__(self, canvas, color, x, y, *args: object) -> tuple:
            self.__canvas, self.__x=canvas, x
            self.__id, self.__y=canvas.create_rectangle(0, 0, fill=color), y
            self.__canvas_width=canvas.winfo_width()
            return args

        def __set_color(self, color, *args: object) -> tuple:
            self.__id=self.__canvas.create_rectangle(0, 0, 30, 10, fill=color)
            self.__canvas.move(self.id, self.x, self.__y)
            return args

    def __init__(self, *, out: bool,
                 high_level_options=None):
        if high_level_options is None:
            high_level_options={"title": "everyone plays hit brick game",
                                "window_info": (500, 400, "green"),
                                "ball_appearence": "purple",
                                "paddle_color": "white",
                                "brick_info": (4, 8, "yellow", "white"),
                                "end": ("you are wonderful(smile)",
                                        "you failed(frown)")}
        self.SYSTEM=high_level_options
        if not ("title" in high_level_options.keys() and "windows_info" in high_level_options.keys() and hlen(
                high_level_options[
                    "window_info"]) == 3 and "background" in high_level_options.keys() and "paddle_color" in
                high_level_options.keys() and "brick_info" in high_level_options.keys and hlen(
                    high_level_options["brick_len"] == 4 and "end" in high_level_options.keys() and hlen(
                        high_level_options["end"]) == 2)):
            if out:
                print("argument error")
            raise ValueError("TypeError sometimes...... check high_level_options argument {}".format(
                "stored as self.SYSTEM, active value={}".format(self.SYSTEM)))
        self.__bricks=hlist()
        self.__game=tk.Tk()
        self.__game.title(high_level_options["title"])
        self.__game.resizable(0, 0)
        self.__canvas=tk.Canvas(self.__game, width=float(high_level_options["window_info"][0]),
                                height=float(high_level_options["window_info"][1]),
                                background=str(high_level_options["window_info"][2]))
        self.__canvas.pack()
        self.__balll=[]
        for i in range(hlen(self.SYSTEM["background"])):
            self.__balll.append(ball_racket_game.ball(self.__canvas, self.SYSTEM["colors"][i]))
        self.__racket=ball_racket_game.racket(self.__canvas, str(high_level_options["paddle_color"]))
        self.__bricks=hlist()
        for i in range(1, self.SYSTEM["brick_info"][0] + 1):
            for j in range(1, self.SYSTEM["brick_info"][1] + 1):
                self.__bricks.append(self.brick(self.__canvas, "yellow", i, j))

        while True:
            if not hc.hcount(self.__balll, 0):
                for i in range(hlen(self.SYSTEM["background"])):
                    self.__balll.append(ball_racket_game.ball(self.__canvas, self.SYSTEM["colors"][i]))
                    self.__balll[i].draw()
                    self.__balll[i].hit_racket()
                    self.__balll[i].hit_brick()

                self.__racket.draw()
                self.__game.update()
                sleep(0.01)
                if not hlen(self.__bricks):
                    self.__canvas.create_text(230, 200, text=str(self.SYSTEM["end"][0]))
                    sleep(2)
                    return
            else:
                self.__canvas.create_text(230, 200, text=str(self.SYSTEM["end"][1]))
                sleep(2)
                return


class enemy_plane_hit:
    def __event_det(self, fj):
        for event in pygame.event.get():
            if event.type() == pygame.QUIT:
                py.exit("clicked to end code")
            elif event.type() == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    fj.RIGHT=True
                elif event.key == pygame.K_LEFT:
                    fj.LEFT=True
                elif event.key == pygame.K_UP:
                    fj.UP=True
                elif event.key == pygame.K_DOWN:
                    fj.DOWN=True
                elif event.key == pygame.K_SPACE:
                    if hlen(self.__HITTER) < 20:
                        self.__HITTER=hc.happend(enemy_plane_hit.hitter(fj))
                    else:
                        hpass()
                else:
                    hpass()
        fj.up()
        fj.down()
        fj.left()
        fj.right()

    class plane:
        def __init__(self, x1: float | int, y1: float | int):
            self.x=x1
            self.y=y1
            self.__image__=pygame.image.load(r"/holiday/enemy&self&b_hit_a/Self-TYPE=GAME_PICTURE.png")
            self.LEFT=False
            self.RIGHT=False
            self.UP=False
            self.DOWN=False

        def up(self):
            if self.UP:
                if self.y > 0:
                    self.y-=0.5

        def down(self):
            if self.DOWN:
                if self.y < 450:
                    self.y+=0.5

        def left(self):
            if self.LEFT:
                if self.x > 0:
                    self.x-=0.5

        def right(self):
            if self.RIGHT:
                if self.x < 322:
                    self.x+=0.5

    class enemy:
        def __init__(self, x1, y1, *vtuple, **vdict) -> dict[str, tuple | dict]:
            self.x, self.y=x1, y1
            self.image=pygame.image.load(r"holiday/enemy&self&b_hit_a/Enemy-TYPE=GAME_PICTURE.png")
            return {"vtuple": vtuple, "vdict": vdict}

        def DOWN(self):
            self.y+=2

    class hitter:
        def __init__(self, fj):
            self.x=fj.x + 36
            self.y=fj.y
            self.image=pygame.image.load(r"holiday/enemy&self&b_hit_a/Enemy-TYPE=GAME_PICTURE.png")

        def UP(self):
            if self.y > 0:
                self.y-=0.5

    def __init__(self, *, __out: bool | int | hint,
                 __high_level_options=None):
        if __high_level_options is None:
            __high_level_options={"width": 400, "height": 500, "title": "hit enemy game"}
        pygame.init()
        self.__SYSTEM=__high_level_options
        self.__WARNING=__out
        self.__ENEMYL=[]
        self.__HITTER=[]
        self.LIFES=300
        if htuple(__high_level_options.keys()) != ("width", "height", "title"):
            raise KeyError("high_level_options key")
        self.__screen=pygame.display.set_mode((__high_level_options["width"], __high_level_options["height"]))
        pygame.display.set_caption(str(__high_level_options["title"]))
        self.__bg=pygame.image.load(r"holiday/enemy&self&b_hit_a/background.png").convert()
        self.__screen.blit(self.__bg, (0, 0))
        self.__plane=enemy_plane_hit.plane(400 / 2 - 78 / 2, 400)
        self.__screen.blit(self.__plane.__image__, (self.__plane.x, self.__plane.y))
        while True:
            enemy_plane_hit.__event_det()
            self.__screen.blit(self.__bg, (0, 0))
            self.__screen.blit(enemy_plane_hit.plane.__image__, (enemy_plane_hit.plane.x, enemy_plane_hit.plane.y))
            if hlen(self.__ENEMYL) < 3:
                self.__ENEMYL=hc.happend(self.__ENEMYL, enemy_plane_hit.enemy(randint(50, 350)), randint(50, 350))
            for enemy in self.__ENEMYL:
                enemy.DOWN()
                if enemy.y > 500:
                    self.__ENEMYL=hc.happend(self.__ENEMYL, enemy)
                else:
                    self.__screen.blit(enemy.image, (enemy.x, enemy.y))
            for hitter in self.__HITTER:
                hitter.UP()
                if hitter.y < 11:
                    self.__HITTER=hc.hremove(self.__HITTER, hitter)
                else:
                    self.__screen.blit(hitter.image, (hitter.x, hitter.y))
            for hitter, enemy in self.__HITTER, self.__HITTER:
                if hitter.x > enemy.x and enemy.x < hitter.x + 67:
                    if enemy.y > hitter.y and enemy.y < hitter.y + 40:
                        self.__HITTER.remove(hitter)
                        self.__ENEMYL.remove(enemy)
                        self.LIFES+=100
            for enemy in self.__ENEMYL:
                if self.__plane.x + 78 > enemy.x and enemy.x + 67 > self.__plane.x:
                    if self.__plane.y + 50 > enemy.y and enemy.y + 40 > self.__plane.y:
                        self.__ENEMYL.remove(enemy)
                        self.LIFES-=100
            pygame.display.update()


class hstr_special_value:
    def alarm(self, password: float, *at, **ad):
        if password != self.__password:
            raise ValueError("wrong password!")
        print("\a")
        return at, ad

    def __init__(self, main_type: str = "@requires",
                 value: str = "@requires", *vt, **vd) -> tuple[str, str, str, tuple, dict]:
        self.__password=randint(0, py.maxsize ** py.maxsize) - random()
        if main_type == "\\":
            if value == "":
                return (str(), "a\\\n    b\\\n        c", "a\
                    b\
                        c", vt, vd)
            if value == "\\":
                return "\\", "a\\\\b", "a\\b", vt, vd
            if value == "'":
                return "\'", "a\\'b", "a\'b", vt, vd
            if value == '"':
                return "\"", 'a\\"b', "a\"b", vt, vd
            if value == "a":
                return (
                    "**not supported**(password={})".format(self.__password), "print(\"\\a\")",
                    hstr_special_value.alarm(),
                    vt, vd)
            if value == "b":
                return "**not supported**(backspace)", "asdf\\bjkl\\b", "asdf\bjkl\b", vt, vd
            if value == "000" or value == 0:
                return "", "\\000", "", vt, vd
            if value == "n":
                return "\n", "line1\\nline2", "line1\nline2", vt, vd
            if value == "v":
                return "**not supported**", "a\\vb", "a\vb", vt, vd
            if value == "t":
                return "**not supported**", "a\\tb", "a\tb", vt, vd
            if value == "r":
                return ("**not supported**", "the first value is replaced \\rby the second value.",
                        "the first value is replaced\rby the second value", vt, vd)
            if value == "f":
                return "**not supported**", "a\\fb", "a\fb", vt, vd
            if value == "yyy":
                texts=["", ""]
                for i in range(7):
                    for j in range(7):
                        texts[0]=texts[0] + f"\\{i}{j}"
                        texts[1]=texts[1] + f"\\{i}{j}"
                return "**not supported", texts[0], texts[1], vt, vd
            if value == "xyy":
                texts=["", ""]
                for i in htuple(range(10)) + ("A", "B", "C", "D", "E", "F"):
                    for j in htuple(range(10)) + ("A", "B", "C", "D", "E", "F"):
                        texts[0]=texts[0] + f"\\{i}{j}"
                        texts[1]=texts[1] + f"\\{i}{j}"
                return "**not supported", texts[0], texts[1], vt, vd
            if type(main_type) != str:
                raise TypeError("supports str type only...")
            else:
                raise ValueError("only supports \"\\ and %%\"")
        else:
            if type(main_type) != str:
                raise TypeError("supports str type only...")
            else:
                raise ValueError("only supports \"\\ and %%\"")


def function():
    return NoReturn


class hstr_change:
    def __init__(self, value: str):
        self.__value=hstr(value)

    def capitalize(self):
        self.__value=hletter(self.__value).big_to_small()
        self.__value=hletter(self.__value[0]) + self.__value[1:]
        return self.__value

    def center(self, width: int | float, filler: str = " "):
        return width / 2 - hlen(self.__value) * filler + self.__value + width / 2 - hlen(self.__value) * filler

    def count(self, find: str, start: int = 0, end: int = False):
        if not end:
            return hstr_change(self.__value).count(find, start, hlen(find))
        if (start, end) != (0, hlen(find)):
            return hstr_change(self.__value[start:end + 1]).count(find)
        out=0
        for part in self.__value:
            if part == find:
                out+=1
                continue
        return out

    def end_suffix(self, suffix: str, start: int = 0, end: int = None):
        if end is None:
            return hstr_change(self.__value).end_suffix(suffix, start, hlen(self.__value))
        if (start, end) != (0, hlen(self.__value)):
            return hstr_change(self.__value[start:end]).end_suffix(suffix)
        return self.__value[hlen(self.__value) - hlen(suffix):] == suffix

    def expand_space(self, spaces: int = 8):
        for i in self.__value:
            if i == " ":
                self.__value[self.__value.index(i)]=spaces * " "
        return self.__value

    def find(self, find: str, start: int = 0, end: int = "int@str.end"):
        if end == "int@str.end":
            end=hlen(self.__value)
        if (start, "->", end) != (0, "->", hlen(self.__value)):
            self.__value=self.__value[start:end]
        s=0
        for part in self.__value:
            if part == find:
                return s
            s+=1
        return -1

    def finds(self, find: str, start: int = 0, end: int = "int@str.end"):
        if end == "int@str.end":
            end=hlen(self.__value)
        if (start, "->", end) != (0, "->", hlen(self.__value)):
            self.__value=self.__value[start:end]
        s=0
        o=[]
        for part in self.__value:
            if part == find:
                o=hc.happend(o, s)
            s+=1
        return htuple(o)

    def index(self, find: str, start: int = 0, end: int = "int@start.end"):
        o=hstr_change(self.__value).find(find, start, end)
        if o == -1:
            raise ValueError("{} is not found in {}".format(find, self.__value))
        return o

    def is_al_num(self, root=hletter.all() + ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")):
        for part in self.__value:
            if part not in root:
                return False
        return True

    def is_alpha(self):
        return hstr_change(self.__value).is_al_num(root=hletter.all())

    def is_decimal(self):
        return hstr_change(self.__value).is_al_num(root=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"))

    def is_digit(self):

        return hstr_change(self.__value).is_al_num(
            root=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 'A', "B", "C", "D", "E", "F"))

    def is_lower(self, root=hletter.small_letter()):
        valuel=[]
        for part in self.__value:
            valuel.append(part)
        self.__value=""
        x=True
        while x:
            x=hstrn.strn()["out"]
            for a in range(26 * 2):
                x.remove(hletter.all()[a])
            x=hstr_change(self.__value).count(x) != 0
            for part in valuel:
                if part not in hletter.all():
                    valuel.remove(part)
                    break
            hpass()
        for part in valuel:
            self.__value+=part
        del valuel, x
        return hstr_change(self.__value).is_al_num(root=root)

    def is_num_eric(self):
        return hstr_change(self.__value).is_al_num(
            root=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "*", "/", "%", "^", "&"))

    def is_space(self):
        return hstr_change(self.__value).is_al_num(root=(" ",))

    def is_upper(self):
        return hstr_change(self.__value).is_lower(root=hletter.big_letter())

    def join(self, sep=","):
        while hstr_change(self.__value).count(sep):
            x=0
            for a in self.__value:
                if a == sep:
                    del self.__value[x]
                    break
                x+=1
                continue
        return self.__value

    def ljust(self, width, filler=" "):
        return self.__value + (width - hlen(self.__value)) * filler

    def lower(self):
        return hletter(self.__value).big_to_small()

    def lstrip(self, filler=" "):
        x=[0, []]
        for part in self.__value:
            if part == filler:
                x[1].append(x[0] - hlen(x[1]))
            x[0]+=1
        for part in x[1]:
            del self.__value[part]
        return self.__value

    def max(self, root=hletter.all()):
        for part in root:
            if part in self.__value:
                return part
        return NoReturn

    def min(self):
        return hstr_change(self.__value).max(root=hc.hreverse(hletter.all()))

    def partition(self, find: tuple[str, str] | list[str, str] | set[str, str] | str):
        if type(find) not in (tuple, list, str, set):
            raise TypeError("find")
        if hlen(find) == 1 or type(find) == str:
            find=(find, find)
        o=[]
        for _i_ in range(3):
            x=0
            for i in self.__value:
                if i == find:
                    o.append(self.__value[:x])
                    del self.__value[:x]
                    break
        o=htuple(o)
        return o

    def replace(self, old: str, new: str, times: int | None = "@self.len", __break__: bool = True):
        if times == "@self.len":
            hlen(self.__value)
        x=0
        for part in self.__value:
            if part == old:
                self.__value[x]=new
                if __break__:
                    return self.__value
        return self.__value

    def rreplace(self, old: str, new: str, times: int | None = "@self.len", __break__: bool = True):
        return hstr_change(self.__value[::-1]).replace(old, new, times, True)[::-1]

    def replaces(self, old: str, new: str, times: int | None = "@self.len", __break__: bool = True):
        return hstr_change(self.__value).replace(old, new, times, False)

    def rfind(self, finder: str):
        return hstr_change(self.__value[::-1]).find(finder)[::-1]

    def rindex(self, finder: str):
        try:
            x=hstr_change(self.__value[::-1]).index(finder)[::-1]
        except ValueError:
            raise ValueError("cannot find {} in {}".format(finder, self.__value))
        else:
            return x
        finally:
            hpass()

    def rjust(self, width: int, filler: str = " "):
        return (width - hlen(self.__value)) * filler + self.__value

    def rpartition(self, finder: tuple[str, str] | list[str, str] | set[str, str] | str = " "):
        return hstr_change(self.__value[::-1]).partition(finder)[::-1]

    def rstrip(self, filler: str):
        return hstr_change(self.__value[::-1]).lstrip(filler)

    def split(self, spliter: str = " ", times: int = False):
        if not times:
            times=hstr_change(self.__value).count(spliter)
        o=[]
        for i in range(times):
            y=0
            for j in self.__value:
                if j == spliter:
                    o.append(self.__value[:y])
                    del self.__value[:y]
                    break
                y+=1
        return htuple(o)

    def split_lines(self, spliter: str = "\n", keep_spliter=True):
        o=""
        while hstr_change(self.__value).count(spliter):
            x=0
            for i in self.__value:
                if i == spliter:
                    o=f"{o}{self.__value[:x - hlen(spliter)]}"
                    del self.__value[:x]
                    if keep_spliter:
                        o=f"{o}\n"
                    break
        return o

    def start_prefix(self, prefix: str, start: int = 0, end: int = "@self.__value.__len__@int@returned@different-way"):
        if end == "@self.__value.__len__@int@returned@different-way":
            end=hlen(self.__value)
        if (start, end) != (0, hlen(self.__value)):
            self.__value=self.__value[start:end]
        "@broken@str@value"
        return self.__value[:hlen(prefix) + 1] == prefix

    def strip(self, filler1: str = " ", filler2: str = " "):
        return hstr_change(hstr_change(self.__value).rstrip(filler2)).lstrip(filler1)

    def swap_case(self):
        return hletter(self.__value).oppsite()

    def title(self):
        x=0
        t=0
        for part in self.__value:
            if part != " " and t == 0:
                self.__value[x]=hletter(self.__value[x]).small_to_big()
            else:
                t=0
            t+=1
            x+=1

    def translate(self, main: tuple = hstrn.strn()["out"]):
        x=""
        for part in self.__value:
            try:
                x=f"{x}{main[part]}"
            except KeyError:
                x=f"{x}{part}"
            else:
                hpass()
            finally:
                continue
        return x

    def upper(self):
        return hletter(self.__value).big_to_small()

    def zfill(self, width: int):
        return self.__value + (width - hlen(self.__value)) * " "

    def is_title(self):
        return self.__value == hstr_change(self.__value).title()


class max_min:
    class sum_get_mul:
        # int numbers only
        def __init__(self, _sum: int):
            self.__sum=_sum

        def biggest(self):
            return hmul(hceil(self.__sum / 4), hfloor(self.__sum / 4))

        def smallest(self):
            return self.__sum - 1 * 1

    class mul_get_sum:
        def __init__(self, mul):
            self.__mul=mul

        def biggest(self):
            return 1 + self.__mul

        def smallest(self):
            if hsqrt(self.__mul) == hint(hsqrt(self.__mul)):
                return hsqrt(self.__mul) * 2
            raise ValueError("cannot fully sqrt")

    class few_add_get_mul:
        def __init__(self, xsum):
            self.__sum=xsum

        def smallest(self):
            return 1

        class biggest:
            def __init__(self, xsum):
                self.__sum=xsum
                if xsum <= 0:
                    raise ValueError(hstr(self.__sum) + " is forbidden")
                elif xsum == 1:
                    return 1
                elif xsum == 2:
                    return 2
                elif xsum == 3:
                    return 3
                elif xsum == 4:
                    return 4
                elif xsum == 5:
                    return 6
                elif xsum == 6:
                    return 9
                else:
                    a=[max_min.few_add_get_mul.biggest(xsum - 3)]
                    while hc.hcount(a, 2) >= 3:
                        for i in range(3):
                            del a[hc.hindex(a, 2)]
                        a.append(3)
                        a.append(3)
                    return a

        class two_twos:
            def __init__(self, a, b, c, d):
                self.__values=htuple(hc.hsort([a, b, c, d]))

            def biggest(self):
                return int(f"{self.__values[0]}{self.__values[3]}") * int(f"{self.__values[1]}{self.__values[2]}")

            def smallest(self):
                return int(f"{self.__values[-1]}{self.__values[-2]}") * int(f"{self.__values[-3]}{self.__values[-4]}")


class square:
    class type_1:
        # a rectangle, if length decrase by {len_decrase} and width decarse by {wid_decrase}, then S minus {
        # S_decrase}, return before.S
        def __init__(self, a_decarse, b_decarse, S_decrase):
            self.__S3=a_decarse * b_decarse
            self.__S2=self.__S4=(S_decrase - self.__S3) / 2
            self.__a2=self.__a4=self.__S2 / (a_decarse + b_decarse)
            return self.__a2 ** 2 + S_decrase

    class type_2:
        # a rectangle a=s , if a+=s_add, b+=b_add , S+=S_add, return before.S
        def __init__(self, a, a_add, b_add, S_add):
            self.__a_return=a + a_add
            self.__S2=self.__a_return * b_add
            self.__S1=S_add - self.__S2
            self.__b_return=self.__S1 / a_add + b_add
            self.__S_return=self.__a_return * self.__b_return
            return self.__S_return

    class type_3:
        # a rectangle, if b==BM1 and a not change, S-=SM1; if b==BM2 and a not change, S-=SM2. return (A0,B0,S0)
        def __init__(self, BM1, SM1, BA2, SA2):
            SM1_ADD_SM2=SM1 + SA2
            A0=SM1_ADD_SM2 / (abs(BM1 - BA2))
            B1=SM1 / SM1_ADD_SM2
            A1=BM1 + B1
            return A0, A1, hmul(A0, A1)

    class type_4:
        # four same rectangle, make a square, big square a = BA , small squre A = SA. return (RECT_A,RECT,B,RECT_S)
        def __init__(self, BA, SA):
            RECT_B=(BA - SA) / 2
            RECT_A=(SA + RECT_B)
            RECT_S=RECT_B * RECT_A
            return RECT_A, RECT_B, RECT_S


class group:
    class grouped:
        @classmethod
        def __init__(cls, group, get, run_by_try: bool = False):
            if run_by_try:
                group*=get // hlen(group) + 1
                for i in group:
                    if i == group[-1]:
                        return i
                pass
            else:
                return group[get % hlen(group) - 1]
            pass

        pass

    class dates:
        def __init__(self, year1, month1, day1, year2, month2, values=(1, 2, 3, 4, 5, 6, 7)):
            DAYS=0
            if isleap(year1):
                months=(31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
            else:
                months=(31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
            DAYS+=months[month1] - day1
            DAYS+=haddl(months[month1 + 1:])
            DAYS+=leapdays(month1 + 1, month2 + 1) * 366
            DAYS+=(year2 - leapdays(month1 + 1, month2 + 1)) * 365
            return values[hdiv.hno(hdiv.hno(DAYS, 7), 7)]

        pass


class past:
    class looking:
        # try_mode=True
        def __init__(self, changes, wrong_answer, __start=0, __runtime=RuntimeError):
            x=__start
            while True:
                try:
                    if x - changes == wrong_answer:
                        return x
                except RuntimeWarning:
                    raise __runtime("this code have run out of time... try changing __start argument.")
                except KeyboardInterrupt:
                    raise KeyboardInterrupt("this code is stopped by user by pressing Ctrl+C")
            pass


class square_standing:
    def no(self, _ni, _f):
        return _ni + (_f - 1) * 8

    def whole(self, _f, _no):
        return _f * (_no * _f) * 4

    def ni(self, _no, _f):
        return _no - (_f - 1) * 8

    def ao(self, _ai, _f):
        return _ai + (_f - 1) * 2

    def ai(self, _ao, _f):
        return _ao - (_f - 1) * 2

    def fn(self, _ni, _no):
        return (_no - _ni) / 8

    def fa(self, _ai, _ao):
        return (_ao - _ai) / 2


class hitter_hit_enemy_game:
    class player(pygame.sprite.Sprite):
        def __init__(self, main_self, pos):
            pygame.sprite.Sprite.__init__(self)
            self.__images=[
                pygame.image.load('holiday/hitter_hit_enemy/lead(n=0).png'),
                pygame.image.load('holiday/hitter_hit_enemy/lead(n=1).png'),
            ]
            self.__rect=self.__images[0].get_rect()
            self.__rect.__topleft=pos
            self.__main_self=main_self
            self.__speed=main_self.__MAIN["speed"]
            self.__ground=main_self.__MAIN["ground"]
            self.__jump_height=main_self.__MAIN["jump_height"]
            self.__jump_start=False
            self.__jump_power=main_self.__MAIN["jump_power"]
            self.__player_bullets=pygame.sprite.Group()
            self.__player_hit=False
            self.__shoot_frequency=0

        def return_images(self):
            return self.__images

        def return_rect(self):
            return self.__rect

        def return_player_bullets(self):
            return self.__player_bullets

        def __move(self):
            self.__key_press=pygame.key.get_pressed()
            if self.__key_press[K_LEFT]:
                if self.__rect.x <= 0:
                    self.__rect.x=0
                else:
                    self.__rect.x+=self.__speed
            if self.__key_press[K_RIGHT]:
                if self.__rect.x >= 800 - self.__rect.width:
                    self.__rect.x=800 - self.__rect.width
                else:
                    self.__rect.x+=self.__speed
            self.__order=next(self.__iteration)
            self.__main_self.__screen.blit(self.__images[self.__order], self.__rect)
            if self.__key_press[K_UP]:
                self.__jump_start=True
            if self.__jump_start:
                if self.__rect.y == self.__ground:
                    self.__jump_speed=self.__jump_power
                elif self.__rect.y <= self.__jump_height:
                    self.__jump_speed=-self.__jump_power
                self.__rect.y+=self.__jump_speed
                if self.__rect.y == self.__ground:
                    self.__jump_start=False

        def shoot(self):
            self.__key_press=pygame.key.get_pressed()
            if self.__key_press[K_SPACE]:
                if not self.__player_hit:
                    if self.__shoot_frequency % self.__main_self.__MAIN["shoot_frequency"] == 0:
                        self.__player_bullets.add(
                            self.__main_self.bullet(self.__rect.centerx, self.__rect.centery + 25))
                    self.__shoot_frequency+=1
                    if self.__shoot_frequency == self.__main_self.__MAIN["shoot_frequency"]:
                        self.__shoot_frequency=0
                for b in self.__player_bullets:
                    b.update_player_bullet()
                    if b.return_rect().left > b.return_rect().x + 500:
                        self.__player_bullets.remove(b)
                self.__player_bullets.draw(self.__main_self.__screen)

        def die_one_time(self):
            self.__life-=1

        def life_line(self):
            self.__life=self.__main_self.__life
            pygame.draw.rect(self.__main_self.__screen, self.__main_self.__MAIN["color=blood=0"],
                             (self.__rect.x + 18, self.__rect.y - 10, 40, 8))
            pygame.draw.rect(self.__main_self.__screen, self.__main_self.__MAIN["color=blood=1"], (
                self.__rect.x + 18 + self.__main_self.__life * 8, self.__rect.y - 10,
                (40 - self.__main_self.__life * 8),
                8))

    class enemy(pygame.sprite.Sprite):
        def __init__(self, images, main_self):
            pygame.sprite.Sprite.__init__(self)
            self.__image=images
            self.__rect=self.__image.get_rect()
            self.__main_self=main_self
            self.__rect.x=randint(700, 800)
            self.__rect.bottom=main_self.__MAIN["ground"]
            self.__speed=main_self.__MAIN["enemy_speed"]
            self.__enemy_bullets=pygame.sprite.Group()
            self.__enemy_hit=False
            self.__enemy_frequency=0

        def update_enemy(self):
            self.__rect.x=-self.__speed

        def return_rect(self):
            return self.__rect

        def shoot_enemy(self):
            if not self.__enemy_hit:
                if self.__enemy_frequency % self.__main_self.__MAIN["enemy_hitting_frequency"] == 0:
                    self.__enemy_bullets.add(self.__main_self.bullet(self.__rect.centerx, self.__rect.centery + 5))
                self.__enemy_frequency+=1
                if self.__enemy_frequency == self.__main_self.__MAIN["enemy_hitting_frequency"]:
                    self.__enemy_frequency=0
                for b in self.__enemy_bullets:
                    b.update_enemy_bullet()
                    if b.return_rect().right < self.__rect.x - 500:
                        self.__enemy_bullets.remove(b)
                self.__enemy_bullets.draw(self.__main_self.__screen)

        def change_enemy_hit(self):
            self.__enemy_hit=True

        def return_enemy_bullets(self):
            return self.__enemy_bullets

        def empty_enemy_bullets(self):
            self.__enemy_bullets.empty()

    class bullet(pygame.sprite.Sprite):
        def __init__(self, x, y, main_self):
            pygame.sprite.Sprite.__init__(self)
            self.__image=pygame.image.load("holiday/hitter_hit_enemy/bullet.png")
            self.__rect.self.__image.get_rect()
            self.__rect.left=x
            self.__rect.bottom=y
            self.__speed=main_self.__MAIN["bullet_moving_speed"]

        def update_player_bullet(self):
            self.__rect.x+=self.__speed

        def update_enemy_bullet(self):
            self.__rect.x-=self.__speed

        def return_rect(self):
            return self.__rect

    class scoreboard:
        def __init__(self, main_self, score, life):
            self.__main_self, self.__score, self.__life=main_self, score, life

        def score_life(self):
            self.__score1="score : " + hstr(self.__score)

        def return_life(self):
            return self.__life

        def game_over(self):
            self.__font_3=pygame.font.Font(r"c:\windows\Fonts\simhei.ttf", 72)
            self.__text_3=self.__font_3.render(self.__main_self.__MAIN["end_text"], True,
                                               self.__main_self.__MAIN["end_color"])
            self.__main_self.__screen.blit(self.__text_3, (261, 200))

        def restart_game(self):
            self.__restart_image=pygame.image.load("holiday/hitter_hit_enemy/restart_game;type=button.png")
            self.__main_self.__screen.blit(self.__restart_image, (600, 500))

    def __init__(self, high_level_options=None):
        if high_level_options is None:
            high_level_options={"width": 800, "height": 600, "title": "unimaginable hitter",
                                "frequency": 60, "leadpos": (45, 384), "speed": 5, "ground": 384,
                                "jump_height": 200, "jump_power": 10, "enemy_speed": 2,
                                "enemy_frequency": 200, "bullet_moving_speed": 5,
                                "shoot_frequency": 10, "enemy_hitting_frequency": 60,
                                "disappear_attack_enemy": (True, True),
                                "color=blood=0": (255, 0, 0), "color=blood=1": (0, 0, 255),
                                "end_text": "GAME OVER", "end_color": (255, 0, 0)}
        try:
            pygame.init()
            self.__running=True
            self.__change=True
            self.__MAIN=high_level_options
            self.__enemy_frequency=0
            self.__screen=pygame.display.set_mode((high_level_options["width"], high_level_options["height"]))
            pygame.display.set_caption(high_level_options["title"])
            self.__clock=pygame.time.Clock()
            self.__map_image_1=Map(self.__screen, 0, 173)
            self.__map_image_2=Map(self.__screen, 800, 173)
            self.__map_image_1.update_screen()
            self.__map_image_2.update_screen()
            self.__leadpos=(45, 384)
            self.__lead=self.player(self, leadpos)
            self.__enemy_images=[
                pygame.image.load("holiday/hitter_hit_enemy/enemy(n=0).png"),
                pygame.image.load("holiday/hitter_hit_enemy/enemy(n=1).png"),
                pygame.image.load("holiday/hitter_hit_enemy/enemy(n=2).png"),
                pygame.image.load("holiday/hitter_hit_enemy/enemy(n=3).png")
            ]
            self.__lifes=5
            self.__enemys=pygame.sprite.Group()
            self.__stats=self.scoreboard(main_self, 0, self.__lifes)
            while self.__running:
                if self.__change:
                    high_level_options["jump_power"]=-high_level_options["jump_power"]
                    self.__change=False
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        raise BaseException("closed window by user")
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        restart_pos_x, restart_pos_y=pygame.mouse.get_pos()
                        if 720 >= restart_pos_x >= 600 and 560 >= restart_pos_y >= 500 and not self.__restart:
                            self.__restart=True
                            try:
                                hitter_hit_enemy_game()
                            except Exception as e:
                                if e in (RecursionError, RuntimeError):
                                    raise RuntimeError("recursion limit reaches")

                self.__screen.fill((135, 180, 255))
                if self.__enemy_frequency % high_level_options["enemy_frequency"] == 0:
                    self.__enemys.add(self.enemy(self.__enemy_images[randint(0, 3)], self))
                self.__enemy_frequency+=1
                if self.__enemy_frequency == high_level_options["enemy_frequency"]:
                    self.__enemy_frequency=0
                for enemy in self.__enemys:
                    enemy.update_enemy()
                    enemy.shoot_enemy()
                    if enemy.return_rect().right > 0:
                        self.__enemys.remove(enemy)
                self.__enemys.draw(self.__screen)
                enemy_shot=pygame.sprite.groupcollide(self.__lead.return_player_bullets(), self.__enemys,
                                                      high_level_options["disappear_attack_enemy"][0],
                                                      high_level_options["disappear_attack_enemy"][1])
                if hlen(enemy_shot):
                    del enemy_shot
                    enemy.change_enemy_hit()
                del enemy_shot
                player_shot=pygame.sprite.spritecpllideany(self.__lead, enemy.return_enemy_bullets())
                if player_shot is not None:
                    if self.__stats.return_life() > 0:
                        self.__stats.die_one_time()
                        enemy.empty_enemy_bullets()
                    else:
                        self.__stats.game_over()
                        self.__stats.restart_game()
                        self.__restart=Falsr
                self.__lead.move()
                self.__lead.shoot()
                self.__screen.blit(self.__lead.return_images(), self.__lead.return_rect())
                self.__stats.score_life()
                self.__lead.life_line(self.__stats.return_life())
                pygame.display.update()
                self.__clock.tick(high_level_options[high_level_options["frequency"]])
        except KeyError:
            raise KeyError("check high_level_options key")
        except ValueError:
            raise ValueError("check high_level_options key")
        except TypeError:
            raise TypeError("check high_level_options key")


class plane_enemy_hits_game:
    class plane:
        def __init__(self, x, y, main_self):
            self.__x=x
            self.__y=y
            self.__MAIN=main_self.__MAIN
            self.__main_self=main_self
            self.__image=pygame.image.load(r"me.png")
            self.__sy=pygame.mixer.Sound(r"me_down.wav")
            self.__sy.set_volume=self.__MAIN["sounds"]
            self.__UP=False
            self.__DOWN=False
            self.__LEFT=False
            self.__RIGHT=False
            self.__blood=10
            self.__moving_speed=self.__MAIN["plane_move_speed"]

        def up(self):
            if self.__UP:
                if self.__y > 0:
                    self.__y-=self.__moving_speed

        def down(self):
            if self.__DOWN:
                if self.__y < 400:
                    self.__y+=self.__moving_speed

        def left(self):
            if self.LEFT:
                if self.__x > 0:
                    self.__x-=0.5

        def right(self):
            if self.RIGHT:
                if self.__x < 270:
                    self.__x+=0.5

        def change_direction(self, up=None, down=None, left=None, right=None):
            value=[]
            for i in (up, down, left, right):
                if i is None:
                    value.append(self.__UP)
                else:
                    value.append(i)
            self.__UP=value[0]
            self.__DOWN=value[1]
            self.__LEFT=value[2]
            self.__RIGHT=value[3]

        def return_x(self):
            return self.__x

        def return_y(self):
            return self.__y

        def return_blood(self):
            return self.__blood

        def change_blood(self, step=1):
            self.__blood-=step

        def return_image(self):
            return self.__image

    def main_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.__plane.change_direction(right=True)
                elif event.key == pygame.K_LEFT:
                    self.__plane.change_direction(left=True)
                elif event.key == pygame.K_UP:
                    self.__plane.change_direction(up=True)
                elif event.key == pygame.K_DOWN:
                    self.__plane.change_direction(down=True)
                elif event.key == pygame.K_SPACE:
                    try:
                        if hlen(self.__plane_bullet_list) < self.__MAIN["max-bullets_len"]:
                            b=self.bullet(self)
                            b.play_sy()
                            self.__plane_bullet_list.append(b)
                    except KeyError:
                        raise KeyError()
                else:
                    try:
                        if self.__MAIN["not-event-key-warning"]:
                            print("you start pressing a key on the keyboard down, but it is not an event key")
                    except KeyError:
                        raise KeyError()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.__plane.change_direction(right=False)
                elif event.key == pygame.K_LEFT:
                    self.__plane.change_direction(left=False)
                elif event.key == pygame.K_UP:
                    self.__plane.change_direction(up=False)
                elif event.key == pygame.K_DOWN:
                    self.__plane.change_direction(down=False)
                elif event.key == pygame.K_SPACE:
                    if hlen(self.__plane_bullet_list) < self.__MAIN["max-bullets_len"]:
                        b=self.bullet(self)
                        b.play_sy()
                        self.__plane_bullet_list.append(b)
                else:
                    try:
                        if self.__MAIN["not-event-key-warning"]:
                            print("you stop pressing a key on the keyboard down, but it is not an event key")
                    except KeyError:
                        raise KeyError()
            self.__plane.right()
            self.__plane.left()
            self.__plane.up()
            self.__plane.down()

    class enemy:
        def __init__(self, x, y, main_self):
            self.__x=x
            self.__y=y
            self.__image=pygame.image.load(r"holiday/enemy&self&a_hit_b&b_hit_a/enemy.png").convert_alpha()
            self.__sy=pygame.mixer.Sound(r"holiday/enemy&self&a_hit_b&b_hit_a/me_down.wav")
            self.__main_self=main_self
            self.__MAIN=main_self.__MAIN
            try:
                retry=True
                for i, j in self.__MAIN["enemy-life"].values()[:-1], self.__MAIN["enemy-life"].keys()[:-1]:
                    if main_self.score <= j:
                        self.__life=i
                        retry=False
                        break
                if retry:
                    self.__life=self.__MAIN["else"]
                del retry
                self.__sy.set_volume(self.__MAIN["sounds"])
            except KeyError:
                raise KeyError()

        def play_sy(self):
            self.__sy.play()

        def move_down(self):
            if self.__y < 450:
                try:
                    self.__y+=self.__MAIN["enemy-moving_speed"]
                except KeyError:
                    raise KeyError()
            else:
                del self

        def return_x(self):
            return self.__x

        def return_y(self):
            return self.__y

        def return_life(self):
            return self.__life

        def return_image(self):
            return self.__image

    def __me_enemy_impact(self):
        ds=self.__enemy_list
        for d in ds:
            if self.__plane.return_x() + 78 > d.return_x() and self.__plane.return_x() < d.return_x() + 57:
                if self.__plane.return_y() + 50 > d.return_y() and self.__plane.return_y < d.return_y() + 43:
                    if self.__plane.return_blood() > 0:
                        try:
                            self.__plane.change_blood(self.__MAIN["die_blood"])
                        except KeyError:
                            raise KeyError()
                    else:
                        self.__flag=False

    class plane_bullet:
        def __init__(self, main_self):
            self.__main_self=main_self
            self.__MAIN=main_self.__MAIN
            self.__x=self.__plane.return_x() + 36
            self.__y=self.__plane.return_y()
            self.__image=pygame.image.load(r"holiday/enemy&self&a_hit_b&b_hit_a/bullet2.png").convert_alpha()
            self.__sy=pygame.mixer.Sound(r"holiday/enemy&self&a_hit_b&b_hit_a/bullet.wav")
            self.__sy.set_volume(self.__MAIN["sounds"])

        def up(self):
            try:
                if self.__y > 0:
                    self.__y-=self.__MAIN["plane_bullet_flying_speed"]
                else:
                    del self
            except KeyError:
                raise KeyError()

        def play_sy(self):
            self.__sy.play()

        def return_x(self):
            return self.__x

        def return_y(self):
            return self.__y

        def return_image(self):
            return self.__image

    def __attack_enemy(self):
        for e in self.__enemy_list:
            for b in self.__plane_bullet_list:
                if b.return_y() > e.return_y() and b.return_x() > e.return_y() + 43:
                    if not e.return_life():
                        self.__enemy_list.remove(e)
                        try:
                            self.__score+=self.__MAIN["die_score"]
                        except KeyError:
                            raise KeyError()
                    self.__plane_bullet_list.remove(b)
                    try:
                        self.__score+=self.__MAIN["hit_score"]
                    except KeyError:
                        raise KeyError()

    class enemy_bullet(plane_bullet):
        def __init__(self, main_self):
            v=randint(0, hlen(self.__main_self.__enemy_bullet_list - 1))
            self.__x=main_self.__enemy_bullet_list[v].return_x() + 33
            self.__y=main_self.__enemy_bullet_list[v].return_y() + 40
            self.__main_self=main_self
            self.__MAIN=main_self.__MAIN
            self.__image=pygame.image.load(r"holiday/enemy&self&a_hit_b&b_hit_a/bullet2.png").convert_alpha()
            self.__sy=pygame.mixer.Sound(r"holiday/enemy&self&a_hit_b&b_hit_a/bullet.wav")
            self.__sy.set_volume(self.__MAIN["sounds"])

        def up(self) -> NoReturn:
            raise NameError("move_up function is only available for plane_bullet class")

        def down(self):
            try:
                moving_speed=self.__MAIN["enemy_bullet_attack-speed"]
            except KeyError:
                raise KeyError()
            if self.__y < 450:
                self.__y+=moving_speed
            else:
                del self

    def __being_attacked(self):
        fj=self.__plane
        z_list=self.__enemy_bullet_list
        for z in z_list:
            if z.return_x() > fj.return_x() and z.return_x() < fj.return_x() + 78:
                if z.return_y() > fj.return_y() and z.return_y() < fj.return_y() + 50:
                    if fj.return_blood() > 0:
                        fj.change_blood(self.__MAIN["die_blood"])
                    else:
                        self.__flag=False
                    z_list.remove(z)
        self.__enemy_bullet_list=z_list

    def __init__(self, high_level_options=None):
        if high_level_options is None:
            high_level_options={"sounds": 0.5, "plane_move_speed": 0.5, "max-bullet_len": 5,
                                "not-event-key-warning": True, "enemy-moving_speed": 0.1,
                                "die_blood": 1, "plane_bullet_flying_speed": 0.2,
                                "enemy-life": {"1000": 1, "else": 2}, "die_score": 100,
                                "hit_score": 0, "enemy_bullet_attack-speed": 0.1,
                                "ending_font": ("arial", 20), "screen_main_appearance": (360, 460),
                                "title": "Python Planes Fighting Game",
                                "running-score_rgb-color": (100, 150, 200),
                                "blood_color": (100, 150, 200),
                                "ending-score_color": (100, 150, 200)}
        self.__enemy_list=[]
        self.__enemy_bullet_list=[]
        self.__plane_bullet_list=[]
        self.__score=0
        self.__flag=True
        self.__MAIN=high_level_options
        pygame.init()
        try:
            font=pygame.font.Sysfont(high_level_options["ending_font"])
            self.__screen=pygame.display.set_mode(high_level_options["screen_main_appearance"])
            pygame.display.set_caption(high_level_options["title"])
            self.__background=pygame.image.load(r"background1.jpg").convert()
            self.__screen.blit(self.__background, (0, 0))
            self.__plane=self.plane(122, 400, self)
            while self.__flag:
                self.__screen.blit(self.__background, (0, 0))
                self.__screen.blit(self.__plane.return_image(), (self.__plane.return_x(), self.__plane.return_y()))
                if hlen(self.__enemy_list) < 8:
                    newest_enemy=self.enemy(randint(0, 320), randint(0, 30), self)
                    self.__enemy_list.append(newest_enemy)
                for i in self.__enemy_list:
                    i.move_down()
                    if i.return_y() > 420:
                        self.__enemy_list.remove(i)
                    else:
                        self.__screen.blit(i.return_image, (i.return_x(), i.return_y()))
                for pb in self.__plane_bullet_list:
                    pb.up()
                    if pb.return_y() < 10:
                        self.__plane_bullet_list.remove(pb)
                    else:
                        self.__screen.blit(pb.return_image(), (pb.return_x(), pb.return_y()))
                if hlen(self.__enemy_bullet_list) < 2:
                    self.__enemy_bullet_list.append(self.__enemy_list[randint(0, hlen(self.__enemy_list))])
                for eb in self.__enemy_bullet_list:
                    eb.down()
                    if eb.return_y() > 420:
                        self.__enemy_bullet_list.remove(eb)
                    else:
                        eb.down()
                        self.__screen.blit(eb.return_image(), (eb.return_x(), eb.return_y()))
                self.__me_enemy_impact()
                self.__attack_enemy()
                self.__being_attacked()
                self.__text1=font.render("Score : %s" % str(self.__score), True,
                                         high_level_options["running-score_rgb-color"])
                self.__screen.blit(self.__text1, (10, 5))
                self.__text2=font.render(
                    "Blood : %s" % str(self.__plane.return_blood(), True, high_level_options["blood_color"]))
                self.__screen.blit(self.__text2, (230, 5))
                pygame.display.update()
                self.main_event()
            self.__screen.blit(self.__background, (0, 0))
            self.__text1=font.render("Score : %s" % str(self.__score), True, high_level_options["ending-score_color"])
            self.__screen.blit(self.__text1, (10, 5))
            pygame.display.update()
            sleep(2)
            raise BaseException("blood is 0")
        except NameError:
            raise NameError("some functions are not defined")
        except KeyError:
            raise KeyError("check the keys of high_level_options, which is needed while running code")
        except ValueError:
            raise ValueError("check the values of high_level_options, which is used in the code")
        except TypeError:
            raise TypeError("the types of the value in high_level_options may be wrong, please have a look")
        except BaseException:
            raise BaseException("user closed the window or game have been over since the blood is 0")
        except Exception as exception:
            if exception not in (NameError, KeyError, ValueError, TypeError, BaseException):
                raise Exception("there are some errors that cannot be explained, please check carefully your values")


class wordle:
    # output
    def __init__(self):
        letters=hletter.all(None)
        correct=""
        for i in range(randint(5, 7)):
            correct+=sample(letters)
        run=True
        while run:
            user=input("type some letters with len %d." % hlen(correct))
            if user == correct:
                run=False
                print("you are right!")
                continue
            for ui, ci in user, correct:
                if ui == ci:
                    print("full correct", end=",")
                    continue
                if ui in correct:
                    print("position wrong, letter correct", end=",")
                    continue
                print("fully wrong", end=",")
            print()
        return True


class element:
    def main(self, *options):
        raise ValueError("Sorry, this feature is not enabled. try elements() instead.")

    def __init__(self, value, find, elements=()):
        if elements == ():
            elements=['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl',
                      'Ka', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As',
                      'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In',
                      'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb',
                      'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl',
                      'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk',
                      'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh',
                      'Fl', 'Mc', 'Lv', 'Ts', 'Og']
        self.__value=value
        self.__error=IndexError("not found")
        self.__find=find
        ending_two_elements=elements
        for i in ending_two_elements:
            if i.__len__() == 2:
                ending_two_elements.append(i[-1])
        if self.__find.__len__() == 2:
            ending_two_elements.remove(self.__find[-1])
        j=0
        for i in self.__value:
            if i == self.__find[0] and self.__value[j + 1] not in ending_two_elements:
                return i + self.__value[j + 1]
        return False

    def __str__(self):
        print("elements help")
        return "elements help"

    def __filename__(self):
        print("filename is not available in this class")
        return "filename is not available in this class"


def his_prime(n):
    prime=True
    for i in range(n - 1, 1, -1):
        if n % i == 0:
            prime=False
            break
    return prime


class password_game:
    def __read(self):
        return input("please type a password (your password now is %s)" % self.__value)

    def __1(self):
        if hlen(self.__value) < 5:
            print("your password should at least len 5")
            return True

    def __2(self):
        go=False
        for x in self.__value:
            if x.isdigit():
                go=True
                break
        if not go:
            print("your password must contain a number")
            return True

    def __3(self):
        go=False
        for x in self.__value:
            if x.isalpha():
                go=True
                break
        if not go:
            print("your password must contain a letter")
            return True

    def __4(self):
        go=False
        for x in self.__value:
            if not (x.isdigit() and x.isalpha()):
                go=True
                break
        if not go:
            print("your password must contain a special character")
            return True

    def __5(self):
        self.__changed_value=""
        for i in self.__value:
            if i.isdigit():
                self.__changed_value+=i
        self.__canswer=0
        for i in self.__changed_value:
            self.__canswer+=int(i)
        pygame.display.set_caption("")
        self.__screen=pygame.display.set_mode((2100, 100))
        self.__screen.blit(r"holiday/password_game/key pressing.png")
        run=True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    pygame.quit()
                    run=False
        if not canswer == 25:
            print("all the numbers should add=25")
            return True

    def __6(self):
        fail=True
        for i in (
                "january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
                "november",
                "december"):
            x=self.__value.lower().find(i)
            if x != -1:
                fail=False
                break
        if fail:
            print("your password must contain a month full name")
            return True

    def __7(self):
        fail=True
        for i in ("I", "V", "X", "C", "M", "L"):
            x=self.__value.upper().find(i)
            if x != -1:
                fail=False
                break
        if fail:
            print("your password must contain a roman number")
            return True

    def __8(self):
        main={"i": 1, "v": 5, "x": 10, "c": 100, "m": 1000, "l": 50}
        mul=1
        for oi in self.__value:
            i=oi.lower()
            if i in ("i", "v", "x", "c", "m", "l"):
                mul*=main[i]
        if mul != 35:
            print("all roman number(single only) should multiply to 35")
            return True

    def __9(self):
        pygame.display.set_caption("")
        screen=pygame.display.set_mode((2100, 800))
        screen.blit(r"holiday/password_game/mouse-button down.png")
        run=True
        while run:
            for event in pygame.evnt.get():
                if eevnt.type == pygame.MOUSEBUTTONDOWN:
                    run=False
                    pygame.quit()
        scanner=""
        numbers=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0").extent((9,) * 5)
        letters=hletter.all(None).extent(("I", "X", "V", "C", "L", "M") * 2)
        special_characters=hstrn.strn()
        for i in numbers + letters:
            special_characters.remove(i)
        for _ in range(randint(2, 3)):
            scanner+=sample(numbers)
        for _ in range(randint(1, 3)):
            scanner+=sample(letters)
        for _ in range(randint(1, 4)):
            scanner+=sample(special_characters)
        if self.__value.find(scanner) == -1:
            print("your password must contain this password : %s" % scanner)
            return True

    def __10(self):
        wordle()

    def __11(self):
        elements=self.__elements
        jj=1
        for j in elements:
            if element(self.__value, j):
                j+=jj
            jj+=1
        del jj
        if j != 200:
            print("all elements symbol should add = %d" % 200)
            return True

    def __12(self):
        fail=False
        for i in self.__value:
            if i in ("a", "e", "i", "o", "u"):
                fail=True
                break
        if fail:
            print("all the vowels must be capitalized")
            return True

    def __13(self):
        fail=False
        v=hletter.small_letter()
        for i in ("a", "e", "i", "o", "u"):
            v.remove(i)
        for i in self.__value:
            if i in v:
                fail=True
                break
        if fail:
            print("all the vowels must be capitalized")
            return True

    def __14(self):
        egg="🥚"
        if self.__value.find(egg) == -1:
            print(
                "%s <-- This is my chicken's egg. She haven't hatched yet. \
                Put her in your password and keep her safe." % egg)
            return True

    def __15(self):
        exercise="🏋️"
        values=randint(10, 25)
        if self.__value.count(exercise) != values:
            print("Your password should include ate least %d %ss" % (values, exercise))
            return True

    def __16(self):
        passwords=[
            "i am happy",
            "i am worthy",
            "i am enough strong"
        ]
        passwords=str(passwords)[1:-1] + ","
        none=[]
        for i in range(3):
            none.append(self.__value.find(passwords[i]))
        if not none.count(-1):
            del none
            return
        del none
        print("your password must contain one of these passwords:", end="")
        for i in passwords:
            if i == ",":
                print()
            else:
                print(i, end="")
        return True

    def __time(self):
        bug="🐛"
        while not self.__stop:
            sleep(1)
            self.__time+=1
            if self.__time % 20 == 0:
                if self.__time_start:
                    if self.__value.count(bug) > 8:
                        raise ValueError("the bug which named Paul is over fed")
                    if not self.__value.count(bug):
                        raise ValueError("the bug which named Paul is starved")
                    print("Your password have been changed.")
                    print("Reason: Paul eats one of your bugs.")
                    self.__value.replace(bug, "", 1)
                    print("your password is %s now." % self.__value)

    def __17(self):
        print("Paul is hatched!")
        bug="🐛"
        print("don't forget to feed her, 20 seconds eat one %s" % bug)
        self.__time_start=True

    def __18(self):
        xl=("https://microsoftedge.microsoft.com/addons/Get-started-with-microsoft-edge-extensions?hl=en-US",
            "https://www.perfect-english-grammar.com/support-files/50_irregular_verbs_past_simple_part_1.pdf",
            "https://pcmanager.microsoft.com/en?channel=303405",
            "https://pcmanager.microsoft.com/en?channel=303405"
            "https://educator-slz05.cercba.com/resources/dp-int/dist/#/forgot-password",
            "https://steptodown.com/")
        x=sample(xl)
        if self.__value.find(x) == -1:
            print("when the window starts, press mouse button to close")
            self.__screen.blit("holiday/password_game/link-n=%d" % xl.index(x))
            RUN=True
            while RUN:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        RUN=False
                        pygame.quit()
                        del xl
            del RUN
            print('your password must contain this link which you have seen')
            return True

    def __19(self):
        if not self.__19_run:
            self.__19_run=True
            letter=input("two letter you don't use in your password (separator=|)")
        if hlen(self.__value) != 3:
            print("length error (needed.length()=3)")
            return True
        if self.__value.count("|") != 1:
            print("| can only appear once")
            return True
        if not (self.__value[0].isalpha() and self.__value[-1].isalpha()):
            print("the character before and after | should be a letter")
            return True
        l1, l2=letter.split("|")

    def __20(self):
        values=("0", "1", "2", "3", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f")
        including="#"
        for i in range(6):
            including+=sample(values)
        if self.__value.lower().find(including):
            input("The screen will appear a window, type the color format like this #AABBCC")
            bgcolor(including)
            exitonclick()

    def __21(self):
        if self.__value.find(hlen(self.__value)) == -1:
            print("your password must include your password length")
            return True

    def __22(self):
        if not his_prime(hlen(self.__value)):
            print("length of your password needed to be a prime number")
            return True

    def __23(self):
        values=strftime("%Y%m%d%H%a", localtime())
        if self.__value.find(values) == -1:
            print("values format like this '%Y%m%d%H%a', %Y=year(2023), %m=month(07), %d= day in month(07)\
                  ,%H=hour in day(9), %a=short writing of weekday(Thu).")
            return True

    def __24(self):
        print("You win!")
        input("Going to Verity if you are a human")
        main=tk.Tk("")
        tk.Label("")

    def __main(self):
        while not self.__stop:
            self.__value=self.__read()
            self.__fail=False
            for i in (
                    self.__1, self.__2, self.__3, self.__4, self.__5, self.__6, self.__7, self.__8, self.__9, self.__10,
                    self.__11, self.__12, self.__13, self.__14, self.__15, self.__16, self.__17, self.__18, self.__19,
                    self.__20, self.__21,
                    self.__22, self.__23, self.__24):
                if i == self.__17:
                    self.__time_start=True
                x=i()
                if x:
                    self.__fail=True
                    break

    def __init__(self):
        self.__elements=['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl',
                         'Ka', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As',
                         'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In',
                         'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb',
                         'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl',
                         'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk',
                         'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh',
                         'Fl', 'Mc', 'Lv', 'Ts', 'Og']
        inx=0
        self.__time=0
        self.__stop=False
        self.__time_start=False
        self.__19_run=False
        for i in self.__elements:
            self.__elements[inx]=i.lower()
            inx+=1
        del inx
        together.start_new_thread(self.__main, ())
        together.start_new_thread(self.__time, ())


class tkinker_messagebox:
    def __init__(self):
        pass

    @staticmethod
    def __(*, method, title, message, print_=True, **options):
        if print_:
            print(method(title, message, options))
        else:
            x=method(title, message, options)
        return {"method": method, "title": title, "message": message, "options": options, "value": x}

    @staticmethod
    def show_info(title, message, options):
        return self.__(showinfo, title, message, False, options)

    @staticmethod
    def show_warning(title, message, options):
        return self.__(showwarning, title, message, False, options)

    @staticmethod
    def show_error(title, message, options):
        return self.__(showerror, title, message, False, options)

    @staticmethod
    def ask_yes_no(title, message, options):
        return self.__(askyesno(), title, message, options)

    @staticmethod
    def ask_ok_cancel(title, message, options):
        self.__(askokcancel, title, message, options)

    @staticmethod
    def ask_question(title, message, options):
        self.__(askquestion, title, message, options)

    @staticmethod
    def ask_retry_cancel(title, message, options):
        self.__(askretrycancel, title, message, options)

    @staticmethod
    def show_yes_no_cancel(title, message, options):
        self.__(askyesnocancel, title, message, options)

    def __str__(self):
        print("let's start learning tkinker.messagebox by functions(in tkinker_learning)")


class tkinker_learning:
    def __init__(self):
        self.__=tk.Tk()

    def __str__(self):
        print("Let us start learning tkinker module.")

    def Label(self, options=None):
        if options is None:
            options={"text": "Hello, Tkinker", "bg": "green", "font_style": "Arial", "font_size": 12}
        self.__.title("Label")
        self.__.geometry("500x300")
        l=tk.Label(self.__, text=options["text"], bg=options["bg"], font=(options["font_style"], options["font_size"]))
        l.pack()
        self.__.mainloop()

    def Button(self, options=None):
        if options is None:
            options={"text": "Hello, Tkinker", "bg": "green", "font_style": "Arial", "font_size": 12,
                     "button": {"text": "try hitting me", "font": ("Arial", 12), "width": 15,
                                "height": 1, "command": self.__HIT}}
        self.__.title("Button&StringVar&Label")
        self.__.geometry("500x300")
        self.__var=tk.StringVar()
        l=tk.Label(self.__, textvariable=self.__var, text=options["text"], bg=options["bg"],
                   font=(options["font_style"], options["font_size"]))
        l.pack()
        self.__hit=False
        b=tk.Button(self.__, text=options["button"]["text"], font=options["button"]["font"],
                    width=options["button"]["width"], height=options["button"]["height"],
                    command=options["button"["command"]])
        b.pack()
        self.__.mainloop()

    def __HIT(self):
        self.__hit=not self.__hit
        if not self.__hit:
            self.__var.set("you hit me")
        else:
            self.__var.set("you hit me again")

    def Entry(self, options=None):
        if options is None:
            options={"appear": "?"}
        self.__.title("Entry")
        self.__.geometry("500x300")
        e=(
            tk.Entry(self.__, show=options["appear"], font=("Arial", 14)),
            tk.Entry(self.__, show=None, font=("Arial", 14)))
        for i in e:
            i.pack()
        self.__.mainloop()

    def __point(self):
        var=self.__e.get()
        self.__text.insert("insert", var)

    def __end(self):
        var=self.__e.get()
        self.__text.insert("end", var)

    def Text(self):
        self.__.title("Text&Entry&Button")
        self.__.geometry("500x300")
        self.__e=tk.Entry(self.__, show="e")
        self.__e.pack()
        b=(tk.Button(self.__, text="insert point", width=10, height=2, command=self.__point),
           tk.Button(self.__, text="insert end", width=10, height=2, command=self.__end))
        for i in b:
            i.pack()
        self.__text=tk.Text(self.__, height=3)
        self.__.mainloop()

    def __Listbox_helper(self, n=1):
        if n == 0 or type(n) != int:
            return
        value=self.__lb.get(self.__lb.curselection())
        self.__var.set(value)
        self.__Listbox_helper(n - 1)
        if n - 1 != 0:
            self.__Listbox_helper(n - 1)

    def Listbox(self):
        self.__.title("Listbox&StringVar&Label")
        self.__.geometry("500x300")
        self.__var=tk.StringVar()
        l=tk.Label(self.__, bg="green", fg="yellow", font=("Arial", 12), width=10, textvariable=self.__var)
        l.pack()
        b=tk.Button(self.__, text="print selection", width=15, height=2, command=self.__Listbox_helper)
        b.pack()
        var=tk.StringVar()
        var.set(list(range(1, 5)))
        lb=tk.Listbox(self.__, listvariable=var)
        list_items=list(range(11, 55, 11))
        for i in list_items:
            lb.insert("end", i)
        lb.insert(1, "first")
        lb.insert(2, "second")
        lb.delate(4)
        lb.pack()
        self.__.mainloop()

    def __Radiobutton_helper(self, n=1):
        if n == 0 or type(n) != int:
            return
        self.__packs[0].config(text="you have selected {selected_item}".format(selected_item=self.__var.get()))
        self.__Radiobutton_helper(n - 1)

    def Radiobutton(self):
        self.__.title("Radiobutton")
        self.__.geometry("500x300")
        self.__var=tk.StringVar
        self.__var.set(NameError("choice collection value have not been collected"))
        self.__packs=(tk.Label(self.__, bg="yellow", width=20, text="select a choice..."),
                      tk.Radiobutton(self.__, text="a", variable=self.__var, value="a",
                                     command=self.__Radiobutton_helper),
                      tk.Radiobutton(self.__, text="b", variable=self.__var, value="b",
                                     command=self.__Radiobutton_helper),
                      tk.Radiobutton(self.__, text="c", variable=self.__var, value="c",
                                     command=self.__Radiobutton_helper))
        for i in self.__packs:
            i.pack()
        self.__.mainloop()

    def __Checkbutton_helper(self, n=1):
        if n == 0 or type(n) != int:
            return
        var=self.__var.get()
        if var[0]:
            if var[1]:
                if var[2]:
                    value_write="you selected a, b, c"
                else:
                    value_write="you selected a,b"
            else:
                if var[2]:
                    value_write="you selected a, c"
                else:
                    value_write="you selected a"
        else:
            if var[1]:
                if var[2]:
                    value_write="you selected b, c"
                else:
                    value_write="you selected b"
            else:
                if var[2]:
                    value_write="you selected c"
                else:
                    value_write="you selected no options"
        self.__packs[0].config(value_write)
        return value_write

    def __Scale_helper(self, v=None):
        self.__packs[0].config(text="you have selected {argument_v_value}".format(argument_v_value=v))

    def Checkbutton(self):
        self.__.title("Checkbutton")
        self.__.geometry("500x300")
        self.__varA=tk.IntVar()
        self.__varB=tk.IntVar()
        self.__varC=tk.IntVar()
        self.__packs=(tk.Label(self.__, bg="yellow", width=20, text="select a few items..."),
                      tk.Checkbutton(self.__, text="a", variable=self.__varA, onvalue=1, offvalue=0,
                                     command=self.__Checkbutton_helper),
                      tk.Checkbutton(self.__, text="b", variable=self.__varB, onvalue=1, offvalue=0,
                                     command=self.__Checkbutton_helper),
                      tk.Checkbutton(self.__, text="c", variable=self.__varC, onvalue=1, offvalue=0,
                                     command=self.__Checkbutton_helper))
        self.__var=(self.__varA, self.__varB, self.__varC)
        for i in self.__packs:
            i.pack()
        self.__.mainloop()

    def Scale(self):
        self.__.title("Scale")
        self.__.geometry("500x300")
        self.__packs=(tk.Label(self.__, bg="green", fg="white", width=20),
                      tk.Scale(self.__, label="move your mouse button to change the number in the label", from_=0,
                               to=600, orient=tk.HORIZONTAL, length=600, showvalue=0, tickinterval=2,
                               resolution=0.00001, command=self.__Scale_helper))
        for i in self.__packs:
            i.pack()
        self.__.mainloop()

    def __shel(self, l: str = None, r: str = None, command: hpass | self.__restart_shell = hpass, obj=self.__shell,
               _foreground=...) -> Literal["NoReturn"]:
        obj.add_command(label=l + " " * (35 - len(l) - len(r)) + r, command=command, foreground=_foreground)
        return Literal["NoReturn"]

    def __restart_shell(self):
        self.__.quit()
        self.Menu()
        return Literal["restart successfully"]

    def __option(self, l: str = None, r: str = None, command: hpass | self.__restart_shell = hpass, obj=self.__shell,
                 _foreground=...) -> Literal["NoReturn"]:
        return self.__shel(l, r, command, self.__options, obj=obj)

    def Menu_IDLE_new_file(self):
        __=tk.Tk()
        __.title()
        __.title('untitled-1')
        __.geometry("500x300")
        menu=tk.Menu()
        file=tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file)
        f=file.add_command
        f(label="New File                     Ctrl+N", command=self.__Menu_IDLE_new_file)
        f(label="Open...                      Ctrl+O", command=hpass)
        f(label="Open Module...               Alt+M", command=hpass)
        file_recent_files=tk.Menu(file)
        file.add_cascade(label="Recent Files", menu=file_recent_files, underline=0)
        file_recent_files.add_command(label="No recent Files", command=hpass)
        f(label="Module Browser                Alt+C", command=hpass)
        f(label="Path Browser                       ", command=hpass)
        file.add_separator()
        f(label="Save                         Ctrl+S", command=hpass)
        f(label="Save As...             Ctrl+Shift+S", command=hpass)
        f(label="Save Copy As...         Alt+Shift+S", command=hpass)
        file.add_separator()
        f(label="Print Window                 Ctrl+P", command=hpass)
        file.add_separator()
        f(label="Close Window                 Alt+F4", command=__.quit)
        f(label="Exit IDLE                    Ctrl+Q", command=__.quit, )
        edit=tk.Menu(menu, tearoff=0)
        e=edit.add_command
        es=edit.add_separator
        e(label="Undo                         Ctrl+Z", command=hpass)
        e(label="Redo                   Ctrl+Shift+Z", command=hpass)
        es()
        e(label="Select All                   Ctrl+A", command=hpass)
        e(label="Cut                          Ctrl+X", command=hpass)
        e(label="Copy                         Ctrl+C", command=hpass)
        e(label="Paste                        Ctrl+V", command=hpass)
        es()
        e(label="Find...                      Ctrl+F", command=hpass)
        e(label="Find Again                   Ctrl+G", command=hpass)
        e(label="Find selection              Ctrl+F3", command=hpass)
        e(label="Find in Files...            Alt+F3", command=hpass)
        e(label="Replace                     Ctrl+H", command=hpass)
        es()
        e(label="Go to Line                   Alt+G", command=hpass)
        e(label="Show Completions        Ctrl+space", command=hpass)
        e(label="Expand Word                  Alt+/", command=hpass)
        e(label="Show Call Tip      Ctrl+back_slash", command=hpass)
        e(label="Show Surrounding Parens     Ctrl+0", command=hpass)
        self.__shell=tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Shell", menu=self.__shell)
        self.__shel("View Last Restart", "F6")
        self.__shel("Restart Shell", "Ctrl+F6", self.__restart_shell)
        self.__shell.add_separator()
        self.__shel("Previous History", "Alt+P")
        self.__shel("Next History", "Alt+P")
        self.__shell.add_separator()
        self.__shel("Interrupt Execution", "Ctrl+C")
        debug=tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Debug", menu=debug)
        self.__shel("Go to File/Line", "", obj=debug)
        self.__shel("Debugger", "", obj=debug)
        self.__shel("Stack Viewer", "", obj=debug)
        self.__shel("Auto-open Stack Viewer", "", obj=debug)
        self.__options=tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Options", menu=self.__options)
        self.__option("Configure IDLE", "")
        self.__option("Show Code Context", "")
        self.__option("Show Line Numbers", "")
        self.__option("Zoom Height", "Alt+2")
        window=tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Window", menu=window)
        self.__shel("IDLE Shell 3.11.4", obj=window)
        self.__shel("untitled-1", obj=window)
        help=tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Help", menu=help)
        self.__shel("About IDLE", "", obj=help)

    def Menu_IDLE_main(self):
        self.__.title('IDLE Shell 3.10.11')
        self.__.geometry("500x300")
        menu=tk.Menu()
        file=tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file)
        f=file.add_command
        f(label="New File                     Ctrl+N", command=self.__Menu_IDLE_new_file)
        f(label="Open...                      Ctrl+O", command=hpass)
        f(label="Open Module...               Alt+M", command=hpass)
        file_recent_files=tk.Menu(file)
        file.add_cascade(label="Recent Files", menu=file_recent_files, underline=0)
        file_recent_files.add_command(label="No recent Files", command=hpass)
        f(label="Module Browser                Alt+C", command=hpass)
        f(label="Path Browser                       ", command=hpass)
        file.add_separator()
        f(label="Save                         Ctrl+S", command=hpass)
        f(label="Save As...             Ctrl+Shift+S", command=hpass)
        f(label="Save Copy As...         Alt+Shift+S", command=hpass)
        file.add_separator()
        f(label="Print Window                 Ctrl+P", command=hpass)
        file.add_separator()
        f(label="Close Window                 Alt+F4", command=self.__.quit)
        f(label="Exit IDLE                    Ctrl+Q", command=self.__.quit, )
        edit=tk.Menu(menu, tearoff=0)
        e=edit.add_command
        es=edit.add_separator
        e(label="Undo                         Ctrl+Z", command=hpass)
        e(label="Redo                   Ctrl+Shift+Z", command=hpass)
        es()
        e(label="Select All                   Ctrl+A", command=hpass)
        e(label="Cut                          Ctrl+X", command=hpass)
        e(label="Copy                         Ctrl+C", command=hpass)
        e(label="Paste                        Ctrl+V", command=hpass)
        es()
        e(label="Find...                      Ctrl+F", command=hpass)
        e(label="Find Again                   Ctrl+G", command=hpass)
        e(label="Find selection              Ctrl+F3", command=hpass)
        e(label="Find in Files...            Alt+F3", command=hpass)
        e(label="Replace                     Ctrl+H", command=hpass)
        es()
        e(label="Go to Line                   Alt+G", command=hpass)
        e(label="Show Completions        Ctrl+space", command=hpass)
        e(label="Expand Word                  Alt+/", command=hpass)
        e(label="Show Call Tip      Ctrl+back_slash", command=hpass)
        e(label="Show Surrounding Parens     Ctrl+0", command=hpass)
        self.__shell=tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Shell", menu=self.__shell)
        self.__shel("View Last Restart", "F6")
        self.__shel("Restart Shell", "Ctrl+F6", self.__restart_shell)
        self.__shell.add_separator()
        self.__shel("Previous History", "Alt+P")
        self.__shel("Next History", "Alt+P")
        self.__shell.add_separator()
        self.__shel("Interrupt Execution", "Ctrl+C")
        debug=tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Debug", menu=debug)
        self.__shel("Go to File/Line", "", obj=debug)
        self.__shel("Debugger", "", obj=debug)
        self.__shel("Stack Viewer", "", obj=debug)
        self.__shel("Auto-open Stack Viewer", "", obj=debug)
        self.__options=tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Options", menu=self.__options)
        self.__option("Configure IDLE", "")
        self.__option("Show Code Context", "", _foreground="gray")
        self.__option("Show Line Numbers", "", _foreground="gray")
        self.__option("Zoom Height", "Alt+2")
        window=tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Window", menu=window)
        self.__shel("*IDLE Shell 3.11.4*", obj=window)
        help=tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Help", menu=help)
        self.__shel("About IDLE", "", obj=help)

    def Frame(self):
        self.__.title("Frame")
        self.__.geometry("500x300")
        s=((tk.Label(self.__, text="Frame", bg="red", font=("Arial", 16)), ...),
           (tk.Frame(self.__), ...),
           (tk.Frame(s[1]), "left"),
           (tk.Frame(s[1]), "right"),
           (tk.Label(s[2], text="l1", bg="green"), ...),
           (tk.Label(s[2], text="l2", bg="green"), ...),
           (tk.Label(s[2], text="l3", bg="green"), ...),
           (tk.Label(s[3], text="r1", bg="yellow"), ...),
           (tk.Label(s[3], text="r2", bg="yellow"), ...),
           (tk.Label(s[3], text="r3", bg="yellow"), ...))
        for s0, s1 in s:
            s0.pack(side=s1)
        self.__.mainloop()

    def message_box(self):
        _=tkinker_messagebox
        _s=dir(_)
        for i in _s:
            if i.startswith("__"):
                _s.remove(i)
        _s=htuple(_s)
        for i in _s:
            _.i(title=i, message="{i} message".format(i=i))


class tkinker_guess_big_small:
    def __go(self):
        try:
            bg=self.__["bg"]
            tk.Label(self.__win, text=" ", bg=bg).pack_forget()
            self.__guess=content.get()
            self.__times+=1
            tk.Label(self.__win, text=self.__["guess_format"].format(guessing_times=self.__times), bg=bg).place(
                x=self.__["guess_position"][0], y=self.__["guess_position"][1])
            self.__guess=int(self.__guess)
            _=self.__["<=>"]
            for bool_, (__item) in (
                    self.__guess == self.__correct, self.__guess < self.__correct, self.__guess > self.__correct), _:
                if bool_:
                    tk.Label(self.__, text=__item[0], width=__item[1], bg=bg).place(__item[2], __item[3])
                    break
            del _
        except Exception as error:
            if self.__error_type == tk.Tk and type(error) == ValueError and error.args[
                0] == "invalid literal for int() " \
                      "with base 10: " \
                      "'%s'" % self.__guess:
                tk.Label(self.__, text="")
            raise type(error)(error.args)

    def __init__(self, error_out_type: tk.Tk | Exception = tk.Tk, high_level_options=None):
        try:
            if high_level_options is None:
                high_level_options={"min": 100, "max": 1000, "bg": "lightblue",
                                    "guess_format": "The {guessing_times} try",
                                    "guess_position": (10, 60),
                                    "<=>": ((i, 20, 10, 80) for i in ("correct, human", "Too big, "
                                                                                        "my "
                                                                                        "whale",
                                                                      "Too small, butterfly")),
                                    "NaN_Warning": "NaN"}
            self.__=high_level_options
            self.__correct=randint(self.__["min"], self.__["max"])
            self.__running=True
            self.__guess=None
            self.__times=0
            self.__error_type=error_out_type
        except KeyError:
            raise KeyError("high_level_options key missing")
        except ValueError:
            raise ValueError("values in high_level_options might not be usable, check carefully")
        except TypeError:
            raise TypeError("types are not usable in high_level_options, for e.g. min set as \"AA\"")
        except KeyboardInterrupt:
            pass
        except SystemExit:
            pass
        except Exception as x:
            raise BaseException(
                "exception type: {__type__}, error words: {__word__}".format(__type__=type(x), __word__=x.args))
