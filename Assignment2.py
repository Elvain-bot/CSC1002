#when i wrote this code, i partially referred to the ideas of Claude AI, a friend, and the lecture slides.I would like to express my appreciation to them here.
import re
content = ""
cursor = 0
show_cursor = True 
CURSOR_ON  = "\033[42m"
CURSOR_OFF = "\033[0m"

HELP_TEXT = """\
? - display this help info
. - toggle row cursor on and off
h - move cursor left
l - move cursor right
^ - move cursor to beginning of the line
$ - move cursor to end of the line
w - move cursor to beginning of next word
b - move cursor to beginning of current or previous word
e - move cursor to end of the word
i - insert <text> before cursor
a - append <text> after cursor
I - insert <text> from beginning
A - append <text> at the end
x - delete character at cursor
X - delete character before cursor
dw - delete to start of next word
de - delete to end of next word
db - delete to start of current or previous word
dc - delete whitespaces or entire word at cursor
sw - swap word at cursor with next word
sb - swap word at cursor with previous word
v - view editor content
q - quit program"""

#small helpers
def find_word_spans(line):
    #start and end spans for every word.
    spans = []
    for match in re.finditer(r'\S+', line):
        spans.append((match.start(), match.end()))
    return spans

def last_index():
    return max(0, len(content) - 1)

def eraser(start, end):
    #Delete content and reposition cursor.
     global content, cursor
     content = content[:start] + content[end:]
     if content:
        cursor = min(start, last_index())
     else:
        cursor = 0


def display_content():
    if not content or not show_cursor:
        print(content)
        return
    print(content[:cursor] + CURSOR_ON + content[cursor] + CURSOR_OFF + content[cursor + 1:])


#Cursors moving commands
def do_dot(_text=""):
    global show_cursor
    show_cursor = not show_cursor

def do_h(text=""):
    global cursor
    cursor = max(cursor - 1, 0)

def do_l(text=""):
    global cursor
    cursor = min(cursor + 1, last_index())

def do_caret(text=""):
    global cursor
    cursor = 0

def do_dollar(text=""):
    global cursor
    cursor = last_index()

def do_w(text=""):
    global cursor
    for start, _end in find_word_spans(content):
        if start > cursor:
            cursor = start
            return
    cursor = last_index()

def nearest_word_left():
    #Return start of the nearest word to the left of cursor, or 0.
    result = 0
    for start, _end in find_word_spans(content):
        if start < cursor:
            result = start
    return result

def next_word_start():
    #Return start of the next word after cursor.
    for start, _end in find_word_spans(content):
        if start > cursor:
            return start
    return None

def do_b(text=""):
    global cursor
    cursor = nearest_word_left()

def do_e(text=""):
    global cursor
    for _start, end in find_word_spans(content):
        if end - 1 > cursor:
            cursor = end - 1
            return
    cursor = last_index()


#Inserting and appending
def do_i(text):
    global content
    content = content[:cursor] + text + content[cursor:]

def do_I(text):
    global content, cursor
    content = text + content
    cursor = 0

def do_a(text):
    #cursor lands at end of inserted text.
    global content, cursor
    ins = cursor + 1 if content else 0
    content = content[:ins] + text + content[ins:]
    cursor = ins + len(text) - 1

def do_A(text):
    #cursor moves to last char.
    global content, cursor
    content = content + text
    cursor = last_index()


#Deleting single word
def do_x(_text=""):
    global content
    if not content:
        return
    eraser(cursor, cursor + 1)

def do_X(_text=""):
    global cursor
    if cursor == 0 or not content:
        return
    eraser(cursor - 1, cursor)


#Range deleting
def do_dw(text=""):
    start = cursor
    do_w()
    eraser(start, cursor)

def do_de(text=""):
    start = cursor
    do_e()
    eraser(start, cursor + 1)

def do_db(text=""):
    end = cursor + 1
    do_b()
    eraser(cursor, end)


#Delete at cursor
def word_under_cursor():
    for start, end in find_word_spans(content):
        if start <= cursor < end:
            return start, end
    return None

def do_dc(text=""):
    span = word_under_cursor()
    if span:
        eraser(span[0], span[1])
    else:
        _erase_spaces()

def _erase_spaces():
    #remove contiguous spaces surrounding cursor.
    lo, hi = cursor, cursor
    while lo > 0 and content[lo - 1] == ' ':
        lo -= 1
    while hi < len(content) and content[hi] == ' ':
        hi += 1
    eraser(lo, hi)


#Swapping commands
def _swap_words(spans, idx_a, idx_b):
    global content
    (s1, e1), (s2, e2) = spans[idx_a], spans[idx_b]
    content = content[:s1] + content[s2:e2] + content[e1:s2] + content[s1:e1] + content[e2:]
    return s2 - (e1 - s1) + (e2 - s2)

def word_index_at(spans):
    for idx, (start, end) in enumerate(spans):
        if start <= cursor < end:
            return idx
    return None

def do_sw(text=""):
    global cursor
    spans = find_word_spans(content)
    idx = word_index_at(spans)
    if idx is None:
        return
    if idx + 1 >= len(spans):
        return
    offset = cursor - spans[idx][0] #record offset,add it and go back to the new position
    cursor = _swap_words(spans, idx, idx + 1) + offset

def swapped_cursor(spans, idx, offset):
    #Compute cursor position after swapping word idx with idx-1.
    return spans[idx - 1][0] + min(offset, spans[idx][1] - spans[idx][0] - 1)

def do_sb(text=""):
    global cursor
    spans = find_word_spans(content)
    idx = word_index_at(spans)
    if idx is None or idx == 0:
        return
    offset = cursor - spans[idx][0]
    _swap_words(spans, idx - 1, idx)
    cursor = swapped_cursor(spans, idx, offset)

def do_v(text=""):
    return

def do_noop(text=""):
    #For command handled in the main loop (? and q).
    return


HANDLE_CMDS = {
    '?': do_noop,  'q': do_noop,
    '.': do_dot,   'h': do_h,   'l': do_l,
    '^': do_caret, '$': do_dollar,
    'w': do_w,     'b': do_b,   'e': do_e,
    'i': do_i,     'a': do_a,   'I': do_I,   'A': do_A,
    'x': do_x,     'X': do_X,   'v': do_v,
    'dw': do_dw,   'de': do_de, 'db': do_db, 'dc': do_dc,
    'sw': do_sw,   'sb': do_sb,
}

TEXT_CMDS = {'i', 'a', 'I', 'A'}


#Parsing
def split_cmd(raw):
    #Split raw into (cmd, text), expanding two-char prefixes. 
    if not raw:
        return None, None
    cmd, text = raw[0], raw[1:]
    if cmd in "ds":
        if len(raw) < 2 or raw[1] not in "ewbc":
            return None, None
        cmd, text = raw[:2], raw[2:]
    return cmd, text

def parse_cmd(raw):
    #Validate and return (cmd, text) or (None, None).
    cmd, text = split_cmd(raw) if raw else (None, None)
    if cmd not in HANDLE_CMDS:
        return None, None
    if cmd in TEXT_CMDS and not text:
        return None, None
    if cmd not in TEXT_CMDS and text:
        return None, None
    return cmd, text


display_content()
while True:
    cmd, text = parse_cmd(input('>'))
    if cmd is None:
        continue
    if cmd == 'q':
        break
    if cmd == '?':
        print(HELP_TEXT)
        continue
    HANDLE_CMDS[cmd](text)
    display_content()
