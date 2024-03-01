from faker import Faker
import difflib
import tkinter as tk
import time

fake = Faker()

fake_text=""
label_list=[]
entry_list=[]
similarity_list=[]
objects_to_destroy=[]

def start_again():
    global objects_to_destroy,fake_text,label_list,entry_list,similarity_list
    for item in objects_to_destroy:
        item.destroy()
    objects_to_destroy=[]
    fake_text=""
    label_list=[]
    entry_list=[]
    similarity_list=[]
    show_text(1)

def show_text(num):
    for _ in range(num):
        global fake_text,timer
        timer = time.time()
        fake_text += fake.text()
    #Divide text into sentences
    fake_list= fake_text.split(".")
    # For every sentence add label and entry (for last entry add another function to calculate result)
    for sentence in fake_list[:-1]:
        if sentence !="":
            label=tk.Label(root,text=sentence.strip(),font=("Helvetica", 12))
            label.pack()
            entry = tk.Entry(root,font=("Helvetica", 12))
            entry.pack(fill=tk.BOTH, expand=True)
            entry.bind("<Return>", on_enter)
            label_list.append(label)
            entry_list.append(entry)
    entry_list[-1].bind("<Return>", calculate)
#Calculate function, calculates, deletes old layout 
def calculate(event):
    global timer
    timer=time.time()-timer
    for label_number,label in enumerate(label_list):
        text1 = label.cget("text")
        text2=entry_list[label_number].get()
        matcher = difflib.SequenceMatcher(None,text1.strip(),text2)
        similarity_ratio = matcher.ratio()
        similarity_list.append(similarity_ratio)
    for label in label_list:
        label.destroy()
    for entry in entry_list:
        entry.destroy()
    Result_Label = tk.Label(root, text=f'Your task was to enter {len(fake_text)} letters, you did it in {round(timer)} seconds, and your precision was {round((sum(similarity_list)*100)/len(similarity_list))}%',font=("Helvetica", 12))
    Result_Label.pack()
    objects_to_destroy.append(Result_Label)
    button = tk.Button(root, text="Try again",font=("Helvetica", 12), command=start_again)
    button.pack()
    objects_to_destroy.append(button)

            
root = tk.Tk()
root.title("Typing master")
# Function to focus on the next entry field
def on_enter(event):
    event.widget.tk_focusNext().focus()

show_text(1)

root.mainloop()

#print(fake.text())