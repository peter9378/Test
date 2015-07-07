print "this is neng-jang-go program!"

rfg={}
def getdata():
    f=open('data','r')
    for i in f.readlines():
        temp = i
        name, many = temp.split()
        rfg[name]=many

def add():
    print 'what name?'
    name = raw_input()
    print 'how many?'
    many = int(raw_input())
    chk = name in rfg
    if chk == True:
        rfg[name]=int(rfg[name])+many
    else:
        rfg[name]=str(many)

def delete():
    print 'what name?'
    name = raw_input()
    print 'how many?'
    many = int(raw_input())
    chk = name in rfg
    if chk == True:
        if int(rfg[name])<many:
            del rfg[name]
        else:
            rfg[name]=int(rfg[name])-many
def look():
    print rfg

def exit():
    f=open('data','w')
    word = ""
    for i in rfg:
        word += i
        word += " "
        word += str(rfg[i])
        word += "\n"
    f.write(word)
    f.close()

if __name__ == '__main__':
    getdata()
    while True:
        print "1. Add   2. Delete   3. Look   4. Exit"
        menu = raw_input()
        if menu == '1':
            add()
        elif menu == '2':
            delete()
        elif menu == '3':
            look()
        elif menu == '4':
            exit()
            break
        else:
            print "wrong number man"