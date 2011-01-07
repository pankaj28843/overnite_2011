import mechanize, os, re, sys
ROOT_PATH = os.path.dirname(__file__)

br = mechanize.Browser()
def bot(SERVER):    
    address = "http://%s/"%(SERVER)    
    br.open(address)    
    assert br.viewing_html()
    print br.title()


if __name__=='__main__':
    try:
        pass
        SERVER = sys.argv[1]
        bot(SERVER)
    except IndexError:
        print "Please provide the server address.\n"
    
