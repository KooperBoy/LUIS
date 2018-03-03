import os
import random
import datetime
from tkinter import *
import keyboard
username='Devlyn'
helptext=('sorry, i haven\'t coded this in yet!')
optiontext=('sorry, i haven\'t coded this in yet!')
def quitcode(*args):
    quit('user terminated code')
def helpcode(*args):
    print(helptext)
def optioncode(*args):
    print(optiontext)
root=Tk()
helptext=('sorry, i haven\'t coded this in yet!')
optiontext=('sorry, i haven\'t coded this in yet!')
class word():
    def codeit(*args):
        com=a12.get()
        if com.lower()=='hello':
            word.check('1x')
            print('var passed through codeit')
        else:
            makesentence(1)
    def check(sen_code):
        com=a12.get()
        if sen_code[0]=='1':
            if sen_code[1]=='x':
                response='hello, {}, How are you today?'.format(username)
                print('var passed through check')
        elif sen_code[0]=='2':
            response='awww, thats too bad'
        history(com,response)
    def convo(*args):
        print("")
########
root.title('LUIS')
root.minsize(width=760,height=760)
root.maxsize(width=760,height=760)
#######
previous_text_10=StringVar()
previous_text_9=StringVar()
previous_text_8=StringVar()
previous_text_7=StringVar()
previous_text_6=StringVar()
previous_text_5=StringVar()
previous_text_4=StringVar()
previous_text_3=StringVar()
previous_text_2=StringVar()
previous_text_1=StringVar()
com=StringVar()
########
a1=Button(root,text='options',command=optioncode)
b1=Button(root,text='help',command=helpcode)
c1=Button(root,text='exit',command=quitcode)
a2=Label(root,text='{}'.format(previous_text_10))
a3=Label(root,text=previous_text_9)
a4=Label(root,text=previous_text_8)
a5=Label(root,text=previous_text_7)
a6=Label(root,text=previous_text_6)
a7=Label(root,text=previous_text_5)
a8=Label(root,text=previous_text_4)
a9=Label(root,text=previous_text_3)
a10=Label(root,text=previous_text_2)
a11=Label(root,text=previous_text_1)
a12=Entry(root,textvariable=com)
a12.insert(0, 'talk to LUIS')
###########
a1.pack(fill=X)
b1.pack(fill=X)
c1.pack(fill=X)
a2.pack(fill=X)
a3.pack(fill=X)
a4.pack(fill=X)
a5.pack(fill=X)
a6.pack(fill=X)
a7.pack(fill=X)
a8.pack(fill=X)
a9.pack(fill=X)
a10.pack(fill=X)
a11.pack(fill=X)
a12.pack(fill=X)
######
#######
def callback(*args):
    print('variable changed!')
########
def history(text,response):
    global previous_text_10
    global previous_text_9
    global previous_text_8
    global previous_text_7
    global previous_text_6
    global previous_text_5
    global previous_text_4
    global previous_text_3
    global previous_text_2
    global previous_text_1
    a2.configure(text='{}: {}'.format(username,previous_text_8))
    a3.configure(text='LUIS: {}'.format(previous_text_7))
    a4.configure(text='{}: {}'.format(username,previous_text_6))
    a5.configure(text='LUIS: {}'.format(previous_text_5))
    a6.configure(text='{}: {}'.format(username,previous_text_4))
    a7.configure(text='LUIS: {}'.format(previous_text_3))
    a8.configure(text='{}: {}'.format(username,previous_text_2))
    a9.configure(text='LUIS: {}'.format(previous_text_1))
    a10.configure(text='{}: {}'.format(username,text))
    a11.configure(text='LUIS: {}'.format(response))
    previous_text_8=previous_text_6
    previous_text_7=previous_text_5
    previous_text_6=previous_text_4
    previous_text_5=previous_text_3
    previous_text_4=previous_text_2
    previous_text_3=previous_text_1
    previous_text_2=text
    previous_text_1=response
######
def respond(*args):
    var_to_send=a12.get()
    print('success')
    return var_to_send

sentences=['Hello there.','bob likes to run', 'what time is it?','they go to school']
txt=open('words.txt','r')
lines=txt.readlines()
file_length=int(lines[0])
previous_text_10=''
previous_text_9=''
previous_text_8=''
previous_text_7=''
previous_text_6=''
previous_text_5=''
previous_text_4=''
previous_text_3=''
previous_text_2=''
previous_text_1=''
com=''
class words():
    word_types={'noun':1,'verb':2,'pronoun':3,'adjective':4,'adverb':5,'conjunction':6,'interjection':7,'article':8,'preposition':9}
    word_conditions={'singular':1,'plural':2,'singular possessive':3,'plural possessive':4,'collective':5,'collective possessive':6}
    nouns={}
    verbs={}
    pronouns={}
    adjectives={}
    adverbs={}
    conjunctions={}
    interjections={}
    articles={}
    prepositions={}
    alls=[nouns,verbs,pronouns,adjectives,adverbs,conjunctions,articles,prepositions]
for n in range(1,file_length):
    current_line=lines[n]
    if current_line[0]=='1':
        words.nouns[current_line[1]]=current_line[2:-1]
    elif current_line[0]=='2':
        words.verbs[current_line[1]]=current_line[2:-1]
    elif current_line[0]=='3':
        words.pronouns[current_line[1]]=current_line[2:-1]
    elif current_line[0]=='4':
        words.adjectives[current_line[1]]=current_line[2:-1]
    elif current_line[0]=='5':
        words.adverbs[current_line[1]]=current_line[2:-1]
    elif current_line[0]=='6':
        words.conjunctions[current_line[1]]=current_line[2:-1]
    elif current_line[0]=='7':
        words.interjections[current_line[1]]=current_line[2:-1]
    elif current_line[0]=='8':
        words.articles[current_line[1]]=current_line[2:-1]
    elif current_line[0]=='9':
        words.prepositions[current_line[1]]=current_line[2:-1]
    else:
        break
print(words.alls)
sentence_types={'declarative':1,'interogative':2,'imperative':3,'response':4,'remark':5}
condition=1
response=''
def makesentence(condition):
    if condition==1:
        rand_noun_1=random.choice(list(words.nouns.values()))
        rand_verb_1=random.choice(list(words.verbs.values()))
        rand_pronoun_1=random.choice(list(words.pronouns.values()))
        rand_object=random.choice(list(words.nouns.values()))
        n_or_pn=random.choice([rand_noun_1,rand_pronoun_1])
        response=(n_or_pn,rand_verb_1,rand_object)
def entercheck(*args):
    word.codeit()
    a12.delete(0,END)
root.bind('<Return>', entercheck)
root.mainloop()

