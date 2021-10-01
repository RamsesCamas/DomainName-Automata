import requests
from requests.exceptions import ConnectionError
import ast
from nfa import NFA
from dfa import DFA

URL = 'http://sabertech.com/'

def read_automata(filename):
    Auto_model = {}
    with open(filename,mode='r',encoding='utf-8') as f:
        for line in f:
            k, v = line.strip().split('=')
            Auto_model[k.strip()] = v.strip()
    Auto_model['S']  = Auto_model['S'][1:-1].replace(',','')
    s = set(Auto_model['S'])

    Auto_model['Q'] = Auto_model['Q'].replace('{','')
    Auto_model['Q'] = Auto_model['Q'].replace('}','')
    state_list = list(Auto_model['Q'].split(','))
    q = set(state_list)
    d = Auto_model['D']
    d = d.replace(' ','')
    d = d.replace('{(','(')
    d = d.replace(')}',')') 
    d = d.replace("(","('")
    d = d.replace(",","','") 
    d = d.replace(")','",",") 
    check_nfa = ',{'
    if check_nfa in Auto_model['D']:
        type_automata = 'NFA' 
        d = d.replace(",'{",",{") 
        d = d.replace("{","{'") 
        d = d.replace("}","'}") 
        d = d.replace("},","}),")     
    else:
        type_automata = 'DFA'
        d = d.replace(",(","),(") 
        d = d.replace(")","')") 
    delta =list(ast.literal_eval(d))
    states = {}
    for state in delta:
        states[(state[0],state[1])] = state[2]

    Auto_model['F'] = Auto_model['F'].replace('{','')
    Auto_model['F'] = Auto_model['F'].replace('}','')
    final_state_list = list(Auto_model['F'].split(','))

    final = set(final_state_list)
    Auto_model = {
        'S': s,
        'Q': q,
        'D': states,
        'q0':Auto_model['q0'],
        'F': final
    }
    return Auto_model,type_automata

def run_automata(automata,automata_type,string):
    if automata_type == 'NFA':
        my_nfa = NFA()
        res = my_nfa.nfa_simulation(string,automata)
    elif automata_type == 'DFA':
        my_dfa = DFA()
        res = my_dfa.accepts_dfa(string,automata)
    return res

def get_domain(url):
    try:
        new_url = 'http://'+url
        response = requests.get(new_url)
        if response.status_code == 200:
            return False
    except ConnectionError:
        return True

def start_automata(string):
    new_Automata,auto_type = read_automata('nfa_dominios.txt')
    result = run_automata(new_Automata,auto_type,string)
    return result