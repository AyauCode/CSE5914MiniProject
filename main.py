import requests
import json
import tkinter as tk

entry = tk.Entry()

def generatePhrases():

    name = entry.get()
    api_url = "https://corporatebs-generator.sameerkumar.website/"

    for i in range(10):
        FirstResponse = requests.get(api_url)
        FirstPhrase = json.loads(FirstResponse.text)
        SecondResponse = requests.get(api_url)
        SecondPhrase = json.loads(SecondResponse.text)
        phrase = tk.Label(
            text="Here at " + name + " we " + FirstPhrase["phrase"].lower() + " and " + SecondPhrase["phrase"].lower() + ".",
            foreground="white",  # Set the text color to white
            background="black",  # Set the background color to black
        )
        phrase.pack()

def main():
    window = tk.Tk()
    label = tk.Label(
        text="Need a company motto? We have the solution you've been waiting for!",
        foreground="white",  # Set the text color to white
        background="black",  # Set the background color to black
    )

    button = tk.Button(
        text="Click to generate mottos!",
        width=25,
        height=5,
        bg="blue",
        fg="yellow",
        command = generatePhrases

    )
    label.pack()
    entry.pack()
    button.pack()
    window.mainloop()

if __name__ == '__main__':
    main()
