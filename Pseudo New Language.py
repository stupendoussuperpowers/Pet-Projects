#idk dont ask too embarrasing

inplines = ["a:2",
            "b: 5",
            "c: a+b",
            "print: c",
            "print: 'Hello World'"]

def tokenprt():
        print(tokens)
        
def process(string,tokens):
        string = string.strip()
        if string.strip()[0] == "'":
                if string.strip()[-1] == "'":
                        return string.replace("'","")
        
        ops = ["+","-","*","/"]
        for i in string:
                if i==" ":
                       string = string.replace(i,"")

        
                       
        for i in string:
                if i.isdigit():
                        pass
                else:
                        if i not in ops:
                                string = string.replace(i,str(tokens[i]))
        #print(string)
        
        #print(string)
        if string.isdigit():
                #print("-->",string)
                return int(string)
        else:
                
                if '+' in string:
                        temp = string.split("+")
                        #print(temp[0],"+",temp[1])
                        return process(temp[0],tokens)+process(temp[1],tokens)
                
                if '-' in string:
                        temp = string.split("-")
                        #print(temp[0],"-",temp[1])
                        return process(temp[0],tokens)-process(temp[1],tokens)
                
                
                if '*' in string:
                        temp = string.split("*")
                        #print(temp[0],"*",temp[1])
                        return process(temp[0],tokens)*process(temp[1],tokens)

                if '/' in string:
                        temp = string.split("/")
                        #print(temp[0],"/",temp[1])
                        return process(temp[0],tokens)/process(temp[1],tokens)
                

def opencust(file):
        t = {}
        f = open(file)
        for currlin in f.readlines():
                currlin = currlin.split(":")
                if currlin[0] in commands.keys():
                        commands[currlin[0]](process(currlin[1],t))
                else:
                        t[currlin[0]] = process(currlin[1],t)
        while True:
                currlin = input("prompt "+file+":|")
                if currlin == "quit":
                        return 0
                currlin = currlin.split(":")
                if currlin[0] in commands.keys():
                        commands[currlin[0]](process(currlin[1],t))
                else:
                        t[currlin[0]] = process(currlin[1],t)

def forcust(string):
        tokens = {}
        string = string.split("=")
        lvar = string[0].strip()
        vsta = string[1].split(":")[0].strip()
        vsto = string[1].split(":")[1].strip()
        
                                
commands = {'print': print,'open':opencust,'vars':tokenprt}

##for currlin in inplines:

#Prompt Generation
tokens = {}
while True:
        currlin = input("prompt:|")
        if currlin == "quit":
                break
        currlin = currlin.split(":")
        if currlin[0] in commands.keys():
                commands[currlin[0]](process(currlin[1],tokens))
        else:
                tokens[currlin[0]] = process(currlin[1],tokens)
