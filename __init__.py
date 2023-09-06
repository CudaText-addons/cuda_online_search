import os
from urllib.parse import quote
from cudatext import *
from cudax_lib import safe_open_url
from .word_proc import *

LIST = {
    'Wikipedia': 'https://en.wikipedia.org/w/index.php?title=Special:Search&search={sel}',
    'Google': 'https://www.google.com/search?q={sel}',
    'Bing': 'https://www.bing.com/search?q={sel}',
    'MSDN': 'https://social.msdn.microsoft.com/Search/en-US?query={sel}',
    'HTML4': 'https://www.w3schools.com/tags/tag_{word}.asp',
    'HTML5': 'https://www.w3.org/TR/html-markup/{word}.html',
    'PHP.net': 'https://www.php.net/{word}',
    'Laravel Docs': 'https://laravel.com/docs/{word}',
    '1C-Bitrix': 'https://dev.1c-bitrix.ru/search/?q={sel}',
    'WordPress': 'https://wordpress.org/search/{sel}/',
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
    safe_open_url(s)


class Command:
    menu_inited = False
    def do_wikipedia(self):
        work('Wikipedia')
    def do_google(self):
        work('Google')
    def do_bing(self):
        work('Bing')
    def do_msdn(self):
        work('MSDN')
    def do_html4(self):
        work('HTML4')
    def do_html5(self):
        work('HTML5')
    def do_php(self):
        work('PHP.net')
    def do_laravel(self):
        work('Laravel Docs')
    def do_wordpress(self):
        work('WordPress')
    def do_bitrix(self):
        work('1C-Bitrix')

    def on_click_right(self, ed_self, state):
        if self.menu_inited:
            return
        self.menu_inited = True
        menu_proc('text', MENU_ADD, caption='-')
        context_menu_id = menu_proc('text', MENU_ADD, caption='Online Search')
        menu_proc(context_menu_id, MENU_ADD, command='cuda_online_search.do_wikipedia', caption='Wikipedia')
        menu_proc(context_menu_id, MENU_ADD, command='cuda_online_search.do_google', caption='Google')
        menu_proc(context_menu_id, MENU_ADD, command='cuda_online_search.do_bing', caption='Bing')
        menu_proc(context_menu_id, MENU_ADD, command='cuda_online_search.do_msdn', caption='MSDN')
        menu_proc(context_menu_id, MENU_ADD, command='cuda_online_search.do_html4', caption='HTML4')
        menu_proc(context_menu_id, MENU_ADD, command='cuda_online_search.do_html5', caption='HTML5')
        menu_proc(context_menu_id, MENU_ADD, command='cuda_online_search.do_php', caption='PHP.net')
        menu_proc(context_menu_id, MENU_ADD, command='cuda_online_search.do_laravel', caption='Laravel Docs')
        menu_proc(context_menu_id, MENU_ADD, command='cuda_online_search.do_wordpress', caption='WordPress')
        menu_proc(context_menu_id, MENU_ADD, command='cuda_online_search.do_bitrix', caption='1C-Bitrix')
