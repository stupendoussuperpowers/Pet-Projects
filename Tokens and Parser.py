from pprint import pprint as pp

class TokenFormat:

        def __init__(self, ttype, name=None, op1=None, op2=None, value=None):
                self.ttype = ttype
                self.name = name
                self.op1 = op1
                self.op2 = op2
                self.value = value
                self.tokentree = {"type":self.ttype, "name":self.name, "op1":self.op1, "op2":self.op2, "value":self.value}
                self.nononetree()
                
        def nononetree(self):
                temp = {}
                for i in self.tokentree.keys():
                        if self.tokentree[i]:
                                temp[i] = self.tokentree[i]

                self.tokentree = temp


stack = []
infix = ["5","+","12","/","4","-","6","*","3"]
postfix = []

def order(a,b):
        op = {"-":0,"+":0,"*":1, "/":1, "**":2, "<":-1, ">":-1, "?":-1}
        return op[a]>op[b]

def intopost(infix):
        postfix = []
        stack = []
        for i in infix:
                if i.isdigit():
                        postfix.append(i)
                else:
                        while len(stack)>0 and order(stack[-1],i):
                                postfix.append(stack[-1])
                                del stack[-1]
                        stack.append(i)

        for i in stack[::-1]:
                postfix.append(i)
        return postfix
        

#print(postfix)

'''making a tree'''

stack = []

def posttotree(postfix):
        stack = []
        for i in postfix:
                if i.isdigit():
                        temp = TokenFormat(ttype="number", value = int(i)).tokentree
                        stack.append(temp)
                else:
                        temp = TokenFormat(ttype="operator", name=i, op2=stack.pop(), op1=stack.pop()).tokentree
                        stack.append(temp)
        return stack.pop()

def postree(postfix):
        stack = []
        for i in postfix:
                if i['type'] == "number":
                        temp = TokenFormat(ttype="number", value = int(i["value"])).tokentree
                        stack.append(temp)
                elif i['type'] == "binaryOp":
                        temp = TokenFormat(ttype="operator", name=i, op2=stack.pop(), op1=stack.pop()).tokentree
                        stack.append(temp)
        return stack.pop()


ifstat = 'if 2 > 3 then { 5 - 4 + 2 }'.split(" ")

stack = []

i = 0

def handleIf(ifstat):
        while i<len(ifstat):
                iftoken = TokenFormat(ttype = "if")
                if ifstat[i] == "if":
                        i+=1
                        while ifstat[i] != "then":
                                stack.append(ifstat[i])
                                i+=1

                        iftoken.tokentree['op1'] = posttotree(intopost(stack))
                        stack = []
                        i+=1
                        if ifstat[i] == "{":
                                i+=1
                                while ifstat[i] != "}":
                                        stack.append(ifstat[i])
                                        i+=1
                                iftoken.tokentree['op2'] = posttotree(intopost(stack))
                i+=1

#print(iftoken.tokentree)


file = "a = 4 ; b = 4 + 2 - 6 / 3 * 5 ; if a > b then { print a }"
file = file.split(" ")

i = 0
stack =[]
while i<len(file):
        
        if file[i] == ';' or file[i] == "}":
                
                stack = []
        else:
                stack.append(file[i])

        i+=1


def tokengenerator(string):
        tokenlist = []
        tokenlistfinal = []
        bufferword = ''
        for i in string:
                if i == " ":
                        tokenlist.append(bufferword)
                        bufferword = ''
                else:
                        bufferword += i
        for _i in tokenlist:
                if _i.isdigit():
                        tokenlistfinal.append({'type':'number', 'value':int(_i)})
                elif _i == "if" or _i == "then":
                        tokenlistfinal.append({'type': _i})
                elif _i == "{" or _i == "}":
                        tokenlistfinal.append({'type':'blockbrack', 'value':_i})
                elif _i == ";":
                        tokenlistfinal.append({'type':';'})
                elif _i in ['=','+','-','/','>','<','*']:
                        tokenlistfinal.append({'type':'binaryOp', 'value': _i})
                else:
                        tokenlistfinal.append({'variable':_i})
        
        return tokenlistfinal

p = tokengenerator("4 + 2 - 6 / 3 * 5")


testingfunctions = ['def','func','(', ')','{', 'a', '=', '5','+','4','}']


pp(postree(tokengenerator(' '.join(i for i in intopost(infix)))))
