import tkinter as tk

current_location = "The Inn"

world_map = {
    "The Inn": "You are in the cozy Inn",
    "The road": "You are walking on the road",
    "The Cathedral": "You are standing on front of Cathedral"
}

def move():
    global current_location
    if current_location == "The Inn":
        current_location = "The road"
    elif current_location == "The road":
        current_location = "The Cathedral"

    # update
    loc_label.config(text=f"Location: {current_location}")
    desc_label.config(text=world_map[current_location])

    if current_location == "The Cathedral":
        move_btn.config(text="Enter the Throne Room (Battle!)", bg="gold", fg="black")

root = tk.Tk()
root.geometry("800x600")

loc_label = tk.Label(root, text=f"Location: {current_location}", font=("Arial", 16, "bold"))
loc_label.pack(pady=10)

desc_label = tk.Label(root, text=world_map[current_location])
desc_label.pack(pady=20)

move_btn = tk.Button(root, text="Move Forward", command=move)
move_btn.pack(pady=20)

root.mainloop()