'''
Autor: 拾柒
Date: 2020-11-30 09:39:01
Description: brainfuck
Version: 1.0
'''
import sys
import os
import tkinter
from tkinter import filedialog


class brainfuck:
    def __init__(self):
        print("1.编码\n2.解码")
        input_type = int(input("请输入功能编号："))
        if input_type == 1:
            self.bfencode()
        elif input_type == 2:
            self.bfdecode()
        else:
            print("请输入正确的功能编号！")

    def bfencode(self):
        str = input("请输入要编码的字符串：")
        op = ''  # 输出
        for char in str:
            char_ascii = ord(char)  # 获取ascii码值
            op += "+" * char_ascii + ".[-]"
        print(op)

    def bfdecode(self):
        root = tkinter.Tk()    # 创建一个Tkinter.Tk()实例
        root.withdraw()       # 将Tkinter.Tk()实例隐藏
        default_dir = r"C:/"  # 设置默认打开目录
        file_path = filedialog.askopenfilename(
            title=u'选择文件', initialdir=(os.path.expanduser(default_dir)))  # 获取brainfuck编码文件名
        self.code = open(file_path).read().replace(
            ' ', '').replace('\n', '')  # 读取内容并删除空格和换行符
        self.array = [0, ]  # 数组，用于存放程序执行生成的数组
        self.p = 0  # 指针，程序执行对应的指针
        self.result = ' '  # 结果存放
        self.compile(0, len(self.code))  # 调动方法对brainfuck代码进行编译
        print(self.result)  # 输出结果

    def compile(self, start, end):
        for i in range(start, end):  # 遍历代码每个关键字
            if self.code[i] == '>':  # 右移指针
                self.array.append(0)
                self.p += 1
            elif self.code[i] == '<':  # 左移指针
                if self.p > 0:
                    self.p -= 1
                else:
                    print('指针溢出，无法计算！')
                    break
            elif self.code[i] == '+':  # 当前指针指向位置值加1
                self.array[self.p] = (self.array[self.p] + 1) % 256
            elif self.code[i] == '-':  # 当前指针指向位置值减1
                self.array[self.p] = (self.array[self.p] - 1) % 256
            elif self.code[i] == '.':  # 输出当前指针指向位置值对应字符
                self.result += chr(self.array[self.p])
            elif self.code[i] == '[':  # 循环体开始标记
                if self.array[self.p] != 0:
                    pass
                else:
                    temp1 = temp2 = i
                    for j in range(i+1, len(self.code)):  # 结束循环，程序跳转到']'之后运行
                        if self.code[j] == ']':
                            temp2 = j
                            self.compile(j+1, len(self.code))
                            return  # 不能用break，break只能结束当前小的for循环，外面还有一个大循环
                        else:
                            pass
                    if temp1 == temp2:
                        break
            elif self.code[i] == ']':  # 循环体结束标记
                for j in range(i-1, -1, -1):  # 重新开始循环
                    if self.code[j] == '[':
                        self.compile(j, i+1)
                        return  # 不能用break，break只能结束当前小的for循环，外面还有一个大循环
                    else:
                        pass
            elif self.code[i] == ',':  # 输入一个字符，存入当前指针指向位置
                inputchar = input("请输入一个字符")
                self.array[self.p] = inputchar
            else:  # 非关键字原样输出
                self.result += self.code[i]


bf = brainfuck()
