from clint.textui import colored 

def banner():
    tnote_banner = r"""
        _________ _        _______ _________ _______ 
        \__   __/( (    /|(  ___  )\__   __/(  ____ \
           ) (   |  \  ( || (   ) |   ) (   | (    \/
           | |   |   \ | || |   | |   | |   | (__    
           | |   | (\ \) || |   | |   | |   |  __)   
           | |   | | \   || |   | |   | |   | (      
           | |   | )  \  || (___) |   | |   | (____/\
           )_(   |/    )_)(_______)   )_(   (_______/
            
                                        - By prodicus(@tasdikrahman)
                                 
        """
    return colored.yellow(tnote_banner)


def menu(items):
    out = ""
    for key, value in items:
        out += colored.green("{}) {} : \n".format(key, value.__doc__))
    return out

def entry(entry, index, size, search_query, search_content):
    out = ""
    head = "\"{title}\" on \"{timestamp}\"".format(title=entry.title, timestamp=entry.timestamp)
    out += colored.red(head) + "\n"
    out += colored.green('='*len(head)) + "\n"
    if search_query and search_content:
        bits = re.compile("(%s)" % re.escape(search_query), re.IGNORECASE).split(entry.content)
        line = reduce(lambda x,y : x+y, [colored.green(b) if b.lower() == search_query.lower() 
            else colored.yellow(b) for b in bits])
        out += line + "\n"
    else:
        out += colored.yellow(entry.content) + "\n"
    out += colored.magenta(('\nTags:' + entry.tags) if entry.tags else '\nNo tags supplied') + "\n"
    out += colored.green('\n\n'+'='*len(head)) + "\n"
    out += colored.yellow("Viewing note " + str(index+1) + " of " + str(size+1)) + "\n"
    out += "n) next entry\n"
    out += "p) previous entry\n"
    out += "d) delete entry\n"
    out += "t) add tag(s)\n"
    out += "r) remove tag(s)\n"
    out += "q) to return to main menu\n"
    return out


