from tkinter import *
import requests


def get_quote():
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()
    data = response.json()
    quote = data['quote']
    bg_canvas.itemconfig(quote_text,text=quote, fill="white")



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50, )

kanye_img = PhotoImage(file="kanye.png")
background_img = PhotoImage(file="background.png")
bg_canvas = Canvas(width=350, height=416)
bg_canvas.create_image(175,208, image=background_img)
quote_text = bg_canvas.create_text(175,208,width=250,font=("Arial", 25, "bold"))
bg_canvas.grid(column=0, row=0)

get_quote()


kanye_button = Button(image=kanye_img,highlightthickness=0, command=get_quote)
kanye_button.grid(column=0, row=1)













window.mainloop()