import re

lines = [""]   # all text lines; always at least one entry
active_row = 0      # index of the currently active line
cursor_col = 0      # column of cursor within the active line (0-indexed)
show_row_cursor = True   # highlight character under row cursor when True
show_line_cursor = False  # prefix active line with '*' when True


GREEN_BG_ON  = "\033[42m"
GREEN_BG_OFF = "\033[0m"


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
; - toggle line cursor on and off
j - move cursor up
k - move cursor down
o - insert empty line below
O - insert empty line above
dd - delete line
J - move line up
K - move line down
Line_No. - jump to specific line, first character
v - view editor content
q - quit program"""



#classification

TWO_CHAR_CMDS = {"dw", "de", "db", "dc", "sw", "sb", "dd"}
TEXT_INPUT_CMDS = {"i", "a", "I", "A"}
NO_INPUT_CMDS = {
    "?", ".", "h", "l", "^", "$", "w", "b", "e",
    "x", "X", ";", "j", "k", "o", "O", "J", "K", "v", "q"
}



#parsing

def is_line_number(raw):
    return bool(re.fullmatch(r'[1-9]\d*', raw))

def has_leading_whitespace(raw):
    return raw != raw.lstrip()

def parse_text_cmd(raw):
    first, rest = raw[0], raw[1:]
    if first in TEXT_INPUT_CMDS and len(rest) >= 1:
        return first, rest
    return None, None

def parse_user_input(raw):
    if not raw or has_leading_whitespace(raw):
        return None, None
    if raw in TWO_CHAR_CMDS or raw in NO_INPUT_CMDS:
        return raw, ""
    if is_line_number(raw):
        return "Line_No.", raw
    return parse_text_cmd(raw)



#active line(one place to read/write the active line)

def get_active_line():
    return lines[active_row]

def set_active_line(new_text):
    lines[active_row] = new_text



#find word postion

def find_all_words(line_text):
    return list(re.finditer(r'\S+', line_text))

def find_next_word_start(line_text, pos):
    for word in find_all_words(line_text):
        if word.start() > pos:
            return word.start()
    return len(line_text)

def find_prev_word_start(line_text, pos):
    for word in reversed(find_all_words(line_text)):
        if word.start() < pos:
            return word.start()
    return 0

def find_word_end(line_text, pos):
    for word in find_all_words(line_text):
        if word.end() - 1 > pos:
            return word.end() - 1
    return max(0, len(line_text) - 1)

def find_word_span(line_text, pos):
    #Return(start,end_excl)of the word covering pos, or None if pos is on a space.
    for word in find_all_words(line_text):
        if word.start() <= pos < word.end():
            return word.start(), word.end()
    return None

def find_space_block(line_text, pos):
    #Return(start,end_excl) of the contiguous run of spaces that contains pos.
    start = pos
    while start > 0 and line_text[start - 1] == " ":
        start -= 1
    end = pos + 1
    while end < len(line_text) and line_text[end] == " ":
        end += 1
    return start, end




def clamp_to_line_bounds(pos, line_text):
    #Clamp pos to [0, len-1] for a non-empty line.
    if not line_text:
        return 0
    return max(0, min(pos, len(line_text) - 1))

def update_cursor_col(new_col):
    #Set cursor_col clamped to the active line's valid range.
    global cursor_col
    cursor_col = clamp_to_line_bounds(new_col, get_active_line())



#display helpers

def build_highlighted_char(line_text, pos):
    safe_pos = clamp_to_line_bounds(pos, line_text)
    return (line_text[:safe_pos]
            + GREEN_BG_ON + line_text[safe_pos] + GREEN_BG_OFF
            + line_text[safe_pos + 1:])

def build_line_body(line_text, row_idx):
    is_active = row_idx == active_row
    if is_active and show_row_cursor and line_text:
        return build_highlighted_char(line_text, cursor_col)
    return line_text

def build_line_prefix(row_idx):
    if not show_line_cursor:
        return ""
    if row_idx == active_row:
        return "*"
    return " "

def print_all_lines():
    for idx, line_text in enumerate(lines):
        print(build_line_prefix(idx) + build_line_body(line_text, idx))




#cursor moving

def do_move_left(): #do h
    global cursor_col
    cursor_col = max(0, cursor_col - 1)

def do_move_right():  #do l
    global cursor_col
    if not get_active_line():
        cursor_col = 0
        return
    cursor_col = min(len(get_active_line()) - 1, cursor_col + 1)    #Move cursor one position right (l); stop at last character.

def do_move_to_line_start():  #do ^
    global cursor_col
    cursor_col = 0

def do_move_to_line_end():  #do $
    global cursor_col
    cursor_col = max(0, len(get_active_line()) - 1)

def do_move_to_next_word():  #do w
    result = find_next_word_start(get_active_line(), cursor_col)
    update_cursor_col(result)

def do_move_to_prev_word():  #do b
    update_cursor_col(find_prev_word_start(get_active_line(), cursor_col))

def do_move_to_word_end():  #do e
    update_cursor_col(find_word_end(get_active_line(), cursor_col))




#insertion

def build_line_with_text_at(line_text, pos, new_text):
    return line_text[:pos] + new_text + line_text[pos:]

def resolve_insert_pos(line_text):
    if not line_text:
        return 0
    return cursor_col

def resolve_append_pos(line_text):
    if not line_text:
        return 0
    return cursor_col + 1

def do_insert(new_text):  #do i
    global cursor_col
    pos = resolve_insert_pos(get_active_line())
    set_active_line(build_line_with_text_at(get_active_line(), pos, new_text))
    cursor_col = clamp_to_line_bounds(pos, get_active_line())

def do_append(new_text):  #do a
    global cursor_col
    pos = resolve_append_pos(get_active_line())
    set_active_line(build_line_with_text_at(get_active_line(), pos, new_text))
    cursor_col = clamp_to_line_bounds(pos + len(new_text) - 1, get_active_line())

def do_insert_at_start(new_text):  #do I
    global cursor_col
    set_active_line(new_text + get_active_line())
    cursor_col = 0

def do_append_at_end(new_text):  #do A
    set_active_line(get_active_line() + new_text)
    update_cursor_col(len(get_active_line()) - 1)




#deletion

def remove_text_range(start, end_excl):
    new_line = get_active_line()[:start] + get_active_line()[end_excl:]
    set_active_line(new_line)
    update_cursor_col(start)

def do_delete_char_at_cursor():  # do x
    if get_active_line():
        remove_text_range(cursor_col, cursor_col + 1)

def do_delete_char_before_cursor():  #do X
    if get_active_line() and cursor_col > 0:
        remove_text_range(cursor_col - 1, cursor_col)

def do_delete_to_next_word():  #do dw
    if get_active_line():
        remove_text_range(cursor_col, find_next_word_start(get_active_line(), cursor_col))

def do_delete_to_word_end():  #do de
    if get_active_line():
        remove_text_range(cursor_col, find_word_end(get_active_line(), cursor_col) + 1)

def do_delete_to_prev_word():  #do db
    if not get_active_line():
        return
    word_start = find_prev_word_start(get_active_line(), cursor_col)
    set_active_line(get_active_line()[:word_start] + get_active_line()[cursor_col + 1:])
    update_cursor_col(word_start)

def find_delete_span_at_cursor():
    #Return (start, end_excl) of what dc should delete: word or space block.
    span = find_word_span(get_active_line(), cursor_col)
    if span:
        return span
    return find_space_block(get_active_line(), cursor_col)


def do_delete_word_or_spaces():  #do dc
    if get_active_line():
        start, end_excl = find_delete_span_at_cursor()
        remove_text_range(start, end_excl)




#swap words

def build_swapped_line(line_text, span_a, span_b):
    word_a = line_text[span_a[0]:span_a[1]]
    word_b = line_text[span_b[0]:span_b[1]]
    gap    = line_text[span_a[1]:span_b[0]]
    return line_text[:span_a[0]] + word_b + gap + word_a + line_text[span_b[1]:]

def get_word_at_index(all_words, idx):
    if 0 <= idx < len(all_words):
        return all_words[idx]
    return None

def find_adjacent_word(cursor_span, direction):
    all_words = find_all_words(get_active_line())
    for idx, word in enumerate(all_words):
        if word.start() == cursor_span[0]:
            return get_word_at_index(all_words, idx + direction)
    return None

def cursor_col_after_swap(span_a, span_b, direction):
    gap_len = span_b[0] - span_a[1]
    if direction > 0:
        return span_a[0] + (span_b[1] - span_b[0]) + gap_len
    return span_a[0]

def ordered_word_spans(span_a, span_b):
    lo = (min(span_a[0], span_b[0]), min(span_a[1], span_b[1]))
    hi = (max(span_a[0], span_b[0]), max(span_a[1], span_b[1]))
    return lo, hi

def do_swap(direction):
    global cursor_col
    cursor_span = find_word_span(get_active_line(), cursor_col)
    if cursor_span is None:
        return
    neighbor = find_adjacent_word(cursor_span, direction)
    if neighbor is None:
        return
    span_a, span_b = ordered_word_spans(cursor_span, (neighbor.start(), neighbor.end()))
    set_active_line(build_swapped_line(get_active_line(), span_a, span_b))
    cursor_col = cursor_col_after_swap(span_a, span_b, direction)

def do_swap_with_next_word():  #do sw
    do_swap(+1)

def do_swap_with_prev_word():  #do sb
    do_swap(-1)



# Multi-line navigation and editing

def do_shift_active_row(delta):
    #Move active_row by delta; clamp cursor_col to the new line's length.
    global active_row, cursor_col
    target = active_row + delta
    if 0 <= target < len(lines):
        active_row = target
        cursor_col = clamp_to_line_bounds(cursor_col, get_active_line())

def do_move_row_up():  #do j
    do_shift_active_row(-1)

def do_move_row_down():  #do k
    do_shift_active_row(+1)

def do_insert_empty_line(offset):
    global active_row, cursor_col
    active_row += offset
    lines.insert(active_row, "")
    cursor_col = 0

def do_insert_line_below():  #do o
    do_insert_empty_line(1)

def do_insert_line_above():  #do O
    do_insert_empty_line(0)

def do_delete_active_line():
    global active_row, cursor_col
    if len(lines) == 1:
        lines[0] = ""
        cursor_col = 0
        return
    lines.pop(active_row)
    active_row = min(active_row, len(lines) - 1)
    cursor_col = clamp_to_line_bounds(cursor_col, get_active_line())

def do_swap_neighbor_row(delta):
    global active_row
    neighbor = active_row + delta
    if 0 <= neighbor < len(lines):
        lines[active_row], lines[neighbor] = lines[neighbor], lines[active_row]
        active_row = neighbor

def do_shift_line_up():  #do J
    do_swap_neighbor_row(-1)

def do_shift_line_down():  #do K
    do_swap_neighbor_row(+1)

def do_jump_to_line(line_number_str):
    global active_row, cursor_col
    active_row = min(int(line_number_str) - 1, len(lines) - 1)
    cursor_col = 0




def do_toggle_row_cursor():  #do .
    global show_row_cursor
    show_row_cursor = not show_row_cursor

def do_toggle_line_cursor():  #do ;
    global show_line_cursor
    show_line_cursor = not show_line_cursor



# Command dispatch tables  (defined once at module load)

NO_INPUT_CMD_TABLE = {
    "h":  do_move_left,           "l":  do_move_right,
    "^":  do_move_to_line_start,  "$":  do_move_to_line_end,
    "w":  do_move_to_next_word,   "b":  do_move_to_prev_word,
    "e":  do_move_to_word_end,
    "x":  do_delete_char_at_cursor,
    "X":  do_delete_char_before_cursor,
    "dw": do_delete_to_next_word,
    "de": do_delete_to_word_end,
    "db": do_delete_to_prev_word,
    "dc": do_delete_word_or_spaces,
    "sw": do_swap_with_next_word,  "sb": do_swap_with_prev_word,
    "j":  do_move_row_up,          "k":  do_move_row_down,
    "o":  do_insert_line_below,    "O":  do_insert_line_above,
    "dd": do_delete_active_line,
    "J":  do_shift_line_up,        "K":  do_shift_line_down,
    ".":  do_toggle_row_cursor,    ";":  do_toggle_line_cursor,
}

TEXT_INPUT_CMD_TABLE = {
    "i": do_insert,            "a": do_append,
    "I": do_insert_at_start,   "A": do_append_at_end,
}



#execution

def is_view_or_help(cmd):
    return cmd in ("?", "v")

def handle_view_or_help(cmd):
    if cmd == "?":
        print(HELP_TEXT)
    else:
        print_all_lines()

def dispatch_command(cmd, arg):
    if cmd == "Line_No.":
        do_jump_to_line(arg)
    elif arg:
        TEXT_INPUT_CMD_TABLE[cmd](arg)
    else:
        NO_INPUT_CMD_TABLE[cmd]()

def execute_command(cmd, arg):
    if cmd == "q":
        return False
    if is_view_or_help(cmd):
        handle_view_or_help(cmd)
        return True
    dispatch_command(cmd, arg)
    print_all_lines()
    return True




def main():
    """Repeatedly read, parse, and execute editor commands until quit."""
    while True:
        cmd, arg = parse_user_input(input(">"))
        if cmd is None:
            continue
        if not execute_command(cmd, arg):
            break


if __name__ == "__main__":
    main()