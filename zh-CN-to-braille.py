# -*- coding:utf-8 -*-
# github@InTmTnl Zh-CN-to-braille 
from pypinyin import lazy_pinyin,Style
import jieba
style=Style.TONE3

#节点
class node:
    pinYin = None
    blind = None
    sibling = None
    child = None
    def __init__(self, p, b):
        self.pinYin = p
        self.blind = b

#声母树
class blindTree1:
    __root=None
    def __init__(self):
        self.__root=node('b','⠃')
        p = self.__root
        p.sibling = node('p', '⠏')
        p=p.sibling
        p.sibling=node('m','⠍')
        p=p.sibling
        p.sibling=node('f','⠋')
        p=p.sibling
        p.sibling=node('d','⠙')
        p=p.sibling
        p.sibling=node('t','⠞')
        p=p.sibling
        p.sibling=node('n','⠝')
        p=p.sibling
        p.sibling=node('l','⠇')
        p=p.sibling
        p.sibling=node('g','⠛')
        p=p.sibling
        p.sibling=node('j','⠛')
        p=p.sibling
        p.child=node('u','⠛⠬')
        q=p.child
        q.child=node('a','⠛⠯')
        q.child.child=node('n','⠛⠯')
        q.child.sibling=node('e','⠛⠾')
        q.child.sibling.sibling=node('n','⠛⠸')
        p.sibling=node('k','⠅')
        p=p.sibling
        p.sibling=node('q','⠅')
        p=p.sibling
        p.child = node('u', '⠅⠬')
        q = p.child
        q.child = node('a', '⠅⠯')
        q.child.child = node('n', '⠅⠯')
        q.child.sibling = node('e', '⠅⠾')
        q.child.sibling.sibling = node('n', '⠅⠸')
        p.sibling=node('h','⠓')
        p=p.sibling
        p.sibling=node('x','⠓')
        p=p.sibling
        p.child = node('u', '⠓⠬')
        q = p.child
        q.child = node('a', '⠓⠯')
        q.child.child = node('n', '⠓⠯')
        q.child.sibling = node('e', '⠓⠾')
        q.child.sibling.sibling = node('n', '⠓⠸')

        p.sibling=node('r','⠚')
        p=p.sibling
        p.child=node('i','⠚')

        p.sibling=node('z','⠵')
        p=p.sibling
        p.child=node('i','⠵')
        q=p.child
        q.sibling=node('h','⠌')
        q=q.sibling
        q.child=node('i','⠌')

        p.sibling = node('c','⠉')
        p = p.sibling
        p.child = node('i','⠉')
        q = p.child
        q.sibling = node('h','⠟')
        q = q.sibling
        q.child = node('i','⠟')

        p.sibling = node('s','⠎')
        p = p.sibling
        p.child = node('i','⠎')
        q = p.child
        q.sibling = node('h','⠱')
        q = q.sibling
        q.child = node('i','⠱')

        p.sibling=node('y','⠊')
        p=p.sibling
        p.child=node('a','⠫')
        q=p.child
        q.sibling=node('o','⠊⠢')
        q.child=node('o','⠜')
        q.child.sibling=node('n','⠩')
        q.child.sibling.child=node('g','⠭')
        q=q.sibling
        q.sibling=node('e','⠑')
        q.child=node('n','⠹')
        q.child.child=node('g','⠹')
        q=q.sibling
        q.sibling=node('i','⠊')
        q=q.sibling
        q.child=node('n','⠣')
        q.child.child=node('g','⠡')
        q.sibling=node('u','⠬')
        q=q.sibling
        q.child=node('a','⠯')
        q.child.child=node('n','⠯')
        q.child.sibling=node('e','⠾')
        q.child.sibling.sibling=node('n','⠸')

        p.sibling = node('w','⠥')
        p = p.sibling
        p.child = node('a', '⠿')
        q = p.child
        q.sibling = node('o','⠕')
        q.child = node('i','⠽')
        q.child.sibling = node('n','⠻')
        q.child.sibling.child = node('g','⠶')
        q = q.sibling
        q.sibling = node('e', '⠥⠢')
        q=q.sibling
        q.child = node('i','⠺')
        q.child.sibling = node('n','⠒')
        q.child.sibling.child = node('g', '⠲')
        q.sibling=node('u','⠥')

    def getRoot(self):
        return self.__root

#韵母树
class blindTree2:
    __root = None
    def __init__(self):
        self.__root = node('a','⠔')
        p = self.__root
        p.child=node('i','⠪')
        q=p.child
        q.sibling=node('o','⠖')
        q=q.sibling
        q.sibling=node('n','⠧')
        q=q.sibling
        q.child=node('g','⠦')

        p.sibling=node('e','⠢')
        p=p.sibling
        p.child=node('i','⠮')
        q=p.child
        q.sibling=node('n','⠴')
        q=q.sibling
        q.child=node('g','⠼')

        p.sibling=node('o','⠢')
        p=p.sibling
        p.child=node('u','⠷')
        q=p.child
        q.sibling=node('n','⠼')
        q=q.sibling
        q.child=node('g','⠼')

        p.sibling=node('i','⠊')
        p=p.sibling
        p.child=node('a','⠫')
        q=p.child
        q.child=node('o','⠜')
        q.child.sibling=node('n','⠩')
        q.child.sibling.child=node('g','⠭')
        q.sibling=node('o','⠹')
        q=q.sibling
        q.child=node('n','⠹')
        q.child.child=node('g','⠹')
        q.sibling=node('e','⠑')
        q=q.sibling
        q.sibling=node('u','⠳')
        q=q.sibling
        q.sibling=node('n','⠣')
        q=q.sibling
        q.child=node('g','⠡')

        p.sibling=node('u','⠥')
        p=p.sibling
        p.child=node('a','⠿')
        q=p.child
        q.child=node('i','⠽')
        q.child.sibling=node('n','⠻')
        q.child.sibling.child=node('g','⠶')
        q.sibling=node('o','⠕')
        q=q.sibling
        q.sibling=node('e','⠾')
        q=q.sibling
        q.sibling=node('i','⠺')
        q=q.sibling
        q.sibling=node('n','⠒')

        p.sibling=node('v','⠬')

    def getRoot(self):
        return self.__root

#声调列表
phonetic_symbols=['','⠁','⠂','⠄','⠆']

#词典：用于对字母、数字、标点符号等非汉字的转换
dictionary={"。": '⠐⠆', "，": '⠐', "、": '⠈', "；": '⠰', "？": '⠐⠄', "！": '⠰⠂', "：": '⠤',
            "“": '⠘', "”": '⠘', "‘": '⠘⠘', "’": '⠘⠘', "（": '⠰⠄', "）": '⠠⠆', "【": '⠰⠆',
            "】": '⠰⠆', "——": '⠠⠤', "……": '⠐⠐⠐', "—": '⠤', "《": '⠐⠤', "》": '⠤⠂', "〈": '⠐⠄',
            "〉": '⠠⠂', "·": '⠠⠄', " ": ' ', "\n":'\n',

            ".": '⠲', ",": '⠂', "!": '⠖', "?": '⠦', ";": '⠆', ":": '⠒', "-": '⠤', "'": '⠄',
            "(": '⠶', ")": '⠶', "/": '⠌', "…": '⠄⠄⠄', "_": '⠤⠤⠤', "[": '⠠⠶', "]": '⠶⠄',

            "1": '⠁', "2": '⠃', "3": '⠉', "4": '⠙', "5": '⠑', "6": '⠋', "7": '⠛', "8": '⠓',
            "9": '⠊', "0": '⠚',

            "A": '⠁', "B": '⠃', "C": '⠉', "D": '⠙', "E": '⠑', "F": '⠋', "G": '⠛', "H": '⠓',
            "I": '⠊', "J": '⠚', "K": '⠅', "L": '⠇', "M": '⠍', "N": '⠝', "O": '⠕', "P": '⠏',
            "Q": '⠟', "R": '⠗', "S": '⠎', "T": '⠞', "U": '⠥', "V": '⠧', "W": '⠺', "X": '⠭',
            "Y": '⠽', "Z": '⠵',

            "a": '⠁', "b": '⠃', "c": '⠉', "d": '⠙', "e": '⠑', "f": '⠋', "g": '⠛', "h": '⠓',
            "i": '⠊', "j": '⠚', "k": '⠅', "l": '⠇', "m": '⠍', "n": '⠝', "o": '⠕', "p": '⠏',
            "q": '⠟', "r": '⠗', "s": '⠎', "t": '⠞', "u": '⠥', "v": '⠧', "w": '⠺', "x": '⠭',
            "y": '⠽', "z": '⠵',

            "他":"⠞⠔", "她": "⠞⠔⠁", "它":"⠈⠞⠔"
            }

dictionaryB={"⠁": '100000', "⠂": '010000', "⠃": '110000', "⠄": '001000', "⠅": '101000', "⠆": '011000',
             "⠇": '111000', "⠈": '000100', "⠉": '100100', "⠊": '010100', "⠋": '110100', "⠌": '001100',
             "⠍": '101100', "⠎": '011100', "⠏": '111100', "⠐": '000010', "⠑": '100010', "⠒": '010010',
             "⠓": '110010', "⠔": '001010', "⠕": '101010', "⠖": '011010', "⠗": '111010', "⠘": '000110',
             "⠙": '100110', "⠚": '010110', "⠛": '110110', "⠜": '001110', "⠝": '101110', "⠞": '011110',
             "⠟": '111110', "⠠": '000001', "⠡": '100001', "⠢": '010001', "⠣": '110001', "⠤": '001001',
             "⠥": '101001', "⠦": '011001', "⠧": '111001', "⠨": '000101', "⠩": '100101', "⠪": '010101',
             "⠫": '110101', "⠬": '001101', "⠭": '101101', "⠮": '011101', "⠯": '111101', "⠰": '000011',
             "⠱": '100011', "⠲": '010011', '⠳': '110011', "⠴": '001011', "⠵": '101011', "⠶": '011011',
             "⠷": '111011', "⠸": '000111', "⠹": '100111', "⠺": '010111', "⠻": '110111', "⠼": '001111',
             "⠽": '101111', "⠾": '011111', "⠿": '111111', " ": ' '}

dictionaryN={"⠁": '1', "⠂": '2', "⠃": '12', "⠄": '3', "⠅": '13', "⠆": '23',
             "⠇": '123', "⠈": '4', "⠉": '14', "⠊": '24', "⠋": '124', "⠌": '34',
             "⠍": '134', "⠎": '234', "⠏": '1234', "⠐": '5', "⠑": '15', "⠒": '25',
             "⠓": '125', "⠔": '35', "⠕": '135', "⠖": '235', "⠗": '1235', "⠘": '45',
            "⠙": '145', "⠚": '245', "⠛": '1245', "⠜": '345', "⠝": '1345', "⠞": '2345',
            "⠟": '12345', "⠠": '6', "⠡": '16', "⠢": '26', "⠣": '126', "⠤": '36',
            "⠥": '136', "⠦": '236', "⠧": '1236', "⠨": '46', "⠩": '146', "⠪": '246',
            "⠫": '1246', "⠬": '346', "⠭": '1346', "⠮": '2346', "⠯": '12346', "⠰": '56',
            "⠱": '156', "⠲": '256', '⠳': '1256', "⠴": '356', "⠵": '1356', "⠶": '2356', "⠷": '12356', "⠸": '456',
            "⠹": '1456', "⠺": '2456', "⠻": '12456', "⠼": '3456', "⠽": '13456', "⠾": '23456', "⠿": '123456', " ": ' '}

parts=('无', '普通名词', '人名', '地名', '机构名', '作品名', '处所名词', '方位名词', '时间', '其他专名',
       '形容词', '数量词', '量词', '连词', '普通动词', '名动词', '动副词', '副词', '副形词', '名形词',
       '代词', '介词', '助词', '其他虚词', '标点符号')

partsDictionary={"无": '', "普通名词": 'n', "人名": 'nr', "地名": 'ns', "机构名": 'nt', "作品名": 'nw', "处所名词": 's',
                 "方位名词": 'f', "时间": 't', "其他专名": 'nz', "形容词": 'a', "数量词": 'm', "量词": 'q',
                 "连词": 'c', "普通动词": 'v', "名动词": 'vn', "动副词": 'vd', "副词": 'd', "副形词": 'ad',
                 "名形词": 'an', "代词": 'r', "介词": 'p', "助词": 'u', "其他虚词": 'xc', "标点符号": 'w'}

bpm=blindTree1()
p1=bpm.getRoot()
aoe=blindTree2()
p2=aoe.getRoot()

#分词函数
def cutWords(str):
    _str= jieba.cut(str, cut_all=False)
    newstr = " ".join(_str)
    return newstr

#转换函数
def Hanzi2Pinyin(text): #将汉字转换为拼音列表
    list1 = list(cutWords(text))
    listPinyin = lazy_pinyin(list1, style=style)
    return listPinyin

def HanziDictMatch(text, idx):
    """
    从 text[idx:] 开始，尝试匹配 dictionary 中的汉字/词条
    使用最长匹配原则
    返回 (matched_braille, matched_length)
    """
    max_len = 0
    result = None

    for k, v in dictionary.items():
        if not k:
            continue
        if text.startswith(k, idx):
            if len(k) > max_len:
                max_len = len(k)
                result = v

    if result is not None:
        return result, max_len
    return None, 0

def is_digit(ch):
    return '0' <= ch <= '9'

def Hanzi2Braille(text):
    result = ""
    i = 0
    buffer = ""
    in_number = False   # 数字状态机

    while i < len(text):
        ch = text[i]

        # —— 数字处理（最高优先级之一）——
        if is_digit(ch):
            if buffer:
                pinyin_list = Hanzi2Pinyin(buffer)
                result += Pinyin2Braille(pinyin_list)
                buffer = ""

            if not in_number:
                result += '⠼'   # 3456 数字前缀
                in_number = True

            result += dictionary[ch]
            i += 1
            continue
        else:
            in_number = False

        # —— dictionary 汉字 / 词条优先匹配 ——
        braille, length = HanziDictMatch(text, i)
        if length > 0:
            if buffer:
                pinyin_list = Hanzi2Pinyin(buffer)
                result += Pinyin2Braille(pinyin_list)
                buffer = ""

            result += braille
            i += length
            continue

        # —— 其他 dictionary 字符（标点等）——
        if ch in dictionary:
            if buffer:
                pinyin_list = Hanzi2Pinyin(buffer)
                result += Pinyin2Braille(pinyin_list)
                buffer = ""
            result += dictionary[ch]
            i += 1
            continue

        # —— 普通汉字，进 buffer ——
        buffer += ch
        i += 1

    if buffer:
        pinyin_list = Hanzi2Pinyin(buffer)
        result += Pinyin2Braille(pinyin_list)

    return result



def Pinyin2Braille(list1): #将拼音列表转换为盲文

    capitalflag = True
    digitalflag = True

    text=''

    for i in range(len(list1)):
        res = dictionary.get(list1[i])
        if (res != None):
            if ('A' <= list1[i] <= 'Z' and capitalflag == True):
                res = ' ⠠[CAP_FLAG]' + res
                capitalflag = False
            elif ('0' <= list1[i] <= '9' and digitalflag == True):
                res = ' ⠼[NUM_FLAG]' + res
                digitalflag = False
            if (capitalflag == False and ('A' > list1[i] or list1[i] > 'Z') and list1[i] != ' '):
                capitalflag = True
            if (digitalflag == False and ('0' > list1[i] or list1[i] > '9') and list1[i] != ' '):
                digitalflag = True
            list1[i] = res
        else:
            capitalflag = True
            digitalflag = True

    for i in list1:
        flag = None
        if ('⠁' <= i <= '⠿' or ' ⠼⠁' <= i <=' ⠼⠁⠛'  or ' ⠠⠁' <= i <=' ⠠⠽'):
            text += i
            continue
        res = dictionary.get(i)
        if (res != None):
            text += res
            continue #dictionary中存在该字符，直接转换
        if ('a' < i[len(i) - 1] < 'z'):
            i += '0'
        j = 0
        p1 = bpm.getRoot()
        p2 = aoe.getRoot()
        p = p1
        while (len(i) - 1 > j and p1.sibling != None and (i[j] != p1.pinYin or i[j] == 'b')):
            if (i[j] != 'b'):
                p1 = p1.sibling
            if (p1.pinYin == i[j]):
                j += 1
                p = p1
                if (p1.child != None):
                    p1 = p1.child
                else:
                    break
                while (len(i) - 1 > j and p1.pinYin == i[j]):
                    j += 1
                    p = p1
                    if (p1.child != None):
                        p1 = p1.child
                if (i[j] == p1.pinYin):
                    j += 1
                    p = p1
        if (j != 0):
            text += p.blind
            flag = p.blind
        while (len(i) - 1 > j and p2.sibling != None and (i[j] != p2.pinYin or i[j] == 'a')):
            if (i[j] != 'a'):
                p2 = p2.sibling
            if (p2.pinYin == i[j]):
                j += 1
                p = p2
                if (p2.child != None):
                    p2 = p2.child
                else:
                    break
                while (len(i) - 1 > j and p2.pinYin == i[j]):
                    j += 1
                    p = p2
                    if (p2.child != None):
                        p2 = p2.child
                if (i[j] == p2.pinYin):
                    j += 1
                    p = p2
        if (j != 0 and flag != p.blind):
            text += p.blind + phonetic_symbols[int(i[len(i) - 1])] + ""
        elif (j != 0 and flag == p.blind):
            text += phonetic_symbols[int(i[len(i) - 1])] + ""
    return text

def Braille2BrailleB(text1): #通过字典将盲文字符转换为二进制表示
    text2=''
    for i in text1:
        if(dictionaryB.get(i)!=None):
            text2 += dictionaryB.get(i)
            text2 += ' '
        else:
            text2 += i
            text2 += ' '
    return text2

def Braille2BrailleN(text1): #通过字典将盲文字符转换为点阵码位表示
    text2=''
    for i in text1:
        if(dictionaryN.get(i)!=None):
            text2 += dictionaryN.get(i)
            text2 += ' '
        else:
            text2 += i
            text2 += ' '
    return text2

userDictionary=[] #用于存储自定义词典的内存空间

s = input("汉字：")
s1 = Hanzi2Braille(s)
s2 = Braille2BrailleB(s1)
s3 = Braille2BrailleN(s1)
print(f"盲文   ：{s1}")
print(f"二进制 ：{s2}")
print(f"点阵码位：{s3}")

