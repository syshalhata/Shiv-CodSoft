import tkinter as tk
from tkinter import ttk, messagebox

class ShivsTodoListApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Shiv's To-Do List")
        self.geometry("400x400")
        self.task_input = ttk.Entry(self, font=("TkDefaultFont", 16), width=30)
        self.task_input.pack(pady=10)
        self.task_input.insert(0, "Enter your todo here...")
        self.task_input.bind("<FocusIn>", self.clear_placeholder)
        self.task_input.bind("<FocusOut>", self.restore_placeholder)

        ttk.Button(self, text="Add", command=self.add_task).pack(pady=5)
        self.task_list = tk.Listbox(self, font=("TkDefaultFont", 16), height=10, selectmode=tk.NONE)
        self.task_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        ttk.Button(self, text="Done", command=self.mark_done).pack(side=tk.LEFT, padx=10, pady=10)
        ttk.Button(self, text="Delete", command=self.delete_task).pack(side=tk.RIGHT, padx=10, pady=10)
        ttk.Button(self, text="View Stats", command=self.view_stats).pack(side=tk.BOTTOM, pady=10)
        
        self.tasks = []
    
    def view_stats(self):
        done_count = 0
        total_count = len(self.tasks)
        for task in self.tasks:
            if task["done"]:
                done_count += 1
        messagebox.showinfo("Task Statistics", f"Total tasks: {total_count}\nCompleted tasks: {done_count}")

    def add_task(self):
        task_text = self.task_input.get()
        if task_text and task_text != "Enter your todo here...":
            self.tasks.append({"text": task_text, "done": False})
            self.task_list.insert(tk.END, task_text)
            self.task_list.itemconfig(tk.END, fg="orange")
            self.task_input.delete(0, tk.END)

    def mark_done(self):
        task_index = self.task_list.curselection()
        if task_index:
            index = task_index[0]
            self.tasks[index]["done"] = True
            self.task_list.itemconfig(index, fg="green")
    
    def delete_task(self):
        task_index = self.task_list.curselection()
        if task_index:
            index = task_index[0]
            del self.tasks[index]
            self.task_list.delete(index)
    
    def clear_placeholder(self, event):
        if self.task_input.get() == "Enter your todo here...":
            self.task_input.delete(0, tk.END)

    def restore_placeholder(self, event):
        if self.task_input.get() == "":
            self.task_input.insert(0, "Enter your todo here...")

if __name__ == '__main__':
    app = ShivsTodoListApp()
    app.mainloop()

