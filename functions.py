import ast

class function:
    def __init__():
        pass
    def save_coord(event,x,y,z):
        reste = event.message[len("?save-coord"):].replace(" ","")
        if not reste == "":
            coord_x = str(x)
            coord_y = str(y)
            coord_z = str(z)
            coord = {reste:{"x":coord_x,"y":coord_y,"z":coord_z}}
            return f"{coord}"
        else:
            return "false"
    def tp_coord(event,file):
        reste = event.message[len("?tp-coord"):].replace(" ","")
        list_lines = file 
        for line in list_lines:
            dictline = ast.literal_eval(line)
            if reste in dictline:
                return dictline[reste]
        return "false"
            