import tkinter as tk
from tkinter import messagebox

# Función para añadir una nueva tarea
def add_task(event=None):
    task = entry_task.get()  # Obtener el texto de la entrada
    if task != "":
        listbox_tasks.insert(tk.END, task)  # Insertar la tarea en la lista
        entry_task.delete(0, tk.END)  # Limpiar el campo de entrada
    else:
        messagebox.showwarning("Entrada vacía", "Por favor, escribe una tarea.")

# Función para marcar una tarea como completada
def mark_completed():
    try:
        selected_task_index = listbox_tasks.curselection()[0]  # Obtener el índice de la tarea seleccionada
        task = listbox_tasks.get(selected_task_index)  # Obtener la tarea seleccionada
        # Si la tarea ya está marcada como completada, no hacer nada
        if task.startswith("[COMPLETADA]"):
            messagebox.showinfo("Ya completada", "Esta tarea ya está completada.")
        else:
            listbox_tasks.delete(selected_task_index)  # Eliminar la tarea original
            listbox_tasks.insert(selected_task_index, f"[COMPLETADA] {task}")  # Insertar tarea completada
    except IndexError:
        messagebox.showwarning("Sin selección", "Por favor, selecciona una tarea para marcar como completada.")

# Función para eliminar una tarea
def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]  # Obtener el índice de la tarea seleccionada
        listbox_tasks.delete(selected_task_index)  # Eliminar la tarea seleccionada
    except IndexError:
        messagebox.showwarning("Sin selección", "Por favor, selecciona una tarea para eliminar.")

# Crear la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas")

# Crear los widgets de la interfaz gráfica
frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10)

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50, bd=0)
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=10)
entry_task.bind("<Return>", add_task)  # Permitir añadir tarea con Enter

button_add_task = tk.Button(root, text="Añadir Tarea", width=48, command=add_task)
button_add_task.pack(pady=5)

button_mark_completed = tk.Button(root, text="Marcar como Completada", width=48, command=mark_completed)
button_mark_completed.pack(pady=5)

button_delete_task = tk.Button(root, text="Eliminar Tarea", width=48, command=delete_task)
button_delete_task.pack(pady=5)

# Iniciar el bucle principal de la aplicación
root.mainloop()
