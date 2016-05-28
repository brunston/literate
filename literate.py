"""
literate
a text editor

(c) brunston
This program comes with absolutely zero warranty.
"""

import curses
import sys

def main(stdscr):
    
    stdscr.clear()
    while True:
        ch = stdscr.getch()
        csr_pos = curses.getsyx() #cursor position
        if ch == ord('`'):
            stdscr.addstr(curses.LINES-1, 0, chr(ch))
            menu(stdscr)


def menu(stdscr):
    ch_menu = stdscr.getch()
    ch_chr = chr(ch_menu)        
    
    if ch_menu == ord('q'):
        stdscr.addstr(ch_chr)
        sys.exit()
    
    if ch_menu == ord('w'):
        stdscr.addstr(ch_chr)

    if ch_menu == ord('t'):
        stdscr.addstr(ch_chr)
        stdscr.addstr("lol")
    
    curses.setsyx(csr_pos[0],csr_pos[1])
 

curses.wrapper(main)
