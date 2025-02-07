from mcpi import minecraft
from mcpi import block
import tkinter as tk
import functions
import random
import requests
import json

app = tk.Tk()

mc = minecraft.Minecraft.create()
mc.postToChat("Script connected")

coord_w = open("coords.txt","a+")
coord_r = open("coords.txt","r+")
doc_r = open("doc.txt","r+")

while True:
    # Récupérer les événements du chat
    chat_events = mc.events.pollChatPosts()
    
    for event in chat_events:
        print(event.message)
        if event.message.startswith("?save-coord"):
            fonction = functions.function.save_coord(event=event,x=mc.player.getTilePos().x,y=mc.player.getTilePos().y,z=mc.player.getTilePos().z)
            print(fonction)
            if not fonction == "false":
                coord_w.write(f"{fonction}\n")
                coord_w.flush()
                mc.postToChat("The coordinates are been saved")
            else:
                mc.postToChat("The warp name isn't precise")
            
        elif event.message.startswith("?tp-coord"):
            x, y, z = mc.player.getTilePos()
            # Définissez la direction devant le joueur
            # Utilisez l'orientation du joueur pour déterminer où "devant" se trouve
            direction = mc.player.getDirection()
            # Calculez la position du bloc devant les pieds
            front_x = x + int(round(direction.x))
            front_y = y
            front_z = z + int(round(direction.z))

            # Obtenez le type de bloc devant les pieds du joueur
            block_id = mc.getBlock(front_x, front_y, front_z)
            if block_id == block.IRON_BLOCK.id:
                mc.setBlock(front_x, front_y, front_z, block.AIR.id)
                fonction = functions.function.tp_coord(event,coord_r.readlines())
                if not fonction == "false":
                    coord_r.seek(0)
                    mc.player.setTilePos(int(fonction["x"]),int(fonction["y"]),int(fonction["z"]))
                    mc.postToChat(f"You are been teleport to {event.message[len("?tp-coord"):].replace(" ","")}")
                else:
                    mc.postToChat("This warp doesn't exist")
        
        elif event.message.startswith("?rtp"):
            mc.player.setTilePos(random.randint(-10000,10000),130,random.randint(-10000,10000))
             
        elif event.message.startswith("?help"):
            for line in doc_r.readlines():
                mc.postToChat(line)
            doc_r.seek(0)
        
        elif event.message.startswith("?"):
            mc.postToChat("This command does not exist")
    
    
        
        

