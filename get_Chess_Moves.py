from requests_html import HTMLSession

def get_Moves_chess_dot_com():
    url = input("Enter the link of a Game please: ")
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)

    my_Moves = r.html.xpath('//*[@id="move-list"]',first=True).text
    removal_list = ["days","hr","min","mins","hrs","day","1:"]
    edit_string_as_list = my_Moves.split()
    final_list = [word for word in edit_string_as_list if word not in removal_list]
    no_integers = [x for x in final_list if not (x.isdigit() or x[0] == '.' and x[1:].isdigit())]
    def is_float(element):
        try:
            float(element)
        except ValueError:
            return False
        return True
    no_float = [x for x in no_integers if not is_float(x)]
    final_string = ' '.join(no_float)
    print(final_string)


def Get_Moves_Lichess_dot_org():
    url = input("Enter the link of a Game please: ")
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)
    my_Moves = r.html.xpath('//*[@class="analyse__moves areplay"]',first=True).text

    removal_list = ["days","hr","min","mins","hrs","day","White","victorious","time","out,","Black","is","0-1","1-0","resigned,"]
    edit_string_as_list = my_Moves.split()
    final_list = [word for word in edit_string_as_list if word not in removal_list]
    no_integers = [x for x in final_list if not (x.isdigit() or x[0] == '-' and x[1:].isdigit())]
    final_string = ' '.join(no_integers)
    print(final_string)


get_Moves_chess_dot_com()
#Get_Moves_Lichess_dot_org()

