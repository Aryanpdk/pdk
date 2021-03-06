# -*- coding: utf-8 -*-
"""ai.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xCzbEahHZvGEnVwl6lQDNr11SyTwatQQ
"""

from nltk.chat.util import Chat,reflections
pairs = [
         ['My name is (.*)', ['Hello %1, How are you today ?']],

         ['(hello|hi|hey|holla|hola)',['hey there','hi there','haayee']],

         ['(.*) in (.*) is fun',['%1 in %2 is indeed fun']],

         ['(.*)(location|city) ?',['Tokoyo,Japan']],

         ['(.*) created you ?',['Aryan did using NLTK']],

         ['How is the weather in (.*)',['The Weather in %1 is amazing like always.']],

         ['(.*) help (.*)',['I can help you']],

         ['(.*) your name',["My name is J.A.R.V.I.S like in Iron Man, but you can just call me Jarvis and I'm a chatbot ?"]],

         ['Book my appointment with (.*) at (.*)',['ok your appointment has been booked with %1 at %2']],

         ["what (.*) want ?",["Make me an offer I can't refuse !!!"]],

         ["I work (in|at) (.*)?",["%1 is an amazing company, I have heard about it."]],

         ["quit",["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]]


      ]
print("Hi, I'm J.A.R.V.I.S and I want to help and chat with you ! \nPlease type lowercase English language to start a conversation. Type quit to leave ")
chat=Chat(pairs,reflections)
chat.converse()