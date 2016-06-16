import os
import webbrowser
from urllib.parse import quote
from cudatext import *
from .word_proc import *

LIST = {
    'Wikipedia': 'http://en.wikipedia.org/w/index.php?title=Special:Search&search={sel}',
    'Google': 'http://www.google.com/search?q={sel}',
    'MSDN': 'http://social.msdn.microsoft.com/Search/en-US?query={sel}',
    'HTML4': 'http://www.w3schools.com/tags/tag_{word}.asp',
    'HTML5': 'http://www.w3.org/TR/html-markup/{word}.html',
    'PHP.net': 'http://www.php.net/{word}',
    }
    

def get_word():
    inf = get_word_info()
    if not inf: return ''
    return inf[3]
    

def work(name):
    if not name in LIST:
        msg_status('Cannot find name: '+name)
        return
    if not ed.get_sel_mode()==SEL_NORMAL:
        msg_status('Can use only normal selection')
        return

    #word
    s_word = get_word()
         
    #sel
    s_sel = ed.get_text_sel()
    if not s_sel:
        s_sel = s_word
        
    s = LIST[name]
    s = s.replace('{sel}', quote(s_sel))
    s = s.replace('{word}', quote(s_word))
    
    msg_status('Opening browser: '+s) 
    webbrowser.open_new_tab(s)
    

class Command:
    def do_wikipedia(self):
        work('Wikipedia')
    def do_google(self):
        work('Google')
    def do_msdn(self):
        work('MSDN')
    def do_html4(self):
        work('HTML4')
    def do_html5(self):
        work('HTML5')
    def do_php(self):
        work('PHP.net')
