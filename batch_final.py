import subprocess
import os
import tkinter as tk
from tkinter import messagebox

batch_process = None


def run_batch():
    global batch_process

    # Replace 'path_to_batch_file' with the actual path to your batch file
    batch_file_path = r"Indigenous AIS SYSTEM-v2.1.bat"

    # Get the user-provided IP address, port number, and s argument value
    ip_address = ip_address_entry.get()
    port_number = port_number_entry.get()
    s_argument_value = s_argument_entry.get()

    # Read the batch file contents
    with open(batch_file_path, 'r') as batch_file:
        batch_file_contents = batch_file.read()

    # Replace the default IP address, port number, and -s argument value with user-provided values
    batch_file_contents = batch_file_contents.replace('127.0.0.1 4159', f'{ip_address} {port_number}')
    batch_file_contents = batch_file_contents.replace('2048000', s_argument_value)

    # Write the modified batch file contents to a temporary file
    with open('temp.bat', 'w') as temp_file:
        temp_file.write(batch_file_contents)

    # Use subprocess to call the modified batch file
    # try:
    #     batch_process = subprocess.Popen(['temp.bat'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #     output, error = batch_process.communicate()
    #     output_text.insert(tk.END, output.decode('utf-8'))
    #     output_text.insert(tk.END, error.decode('utf-8'))
    # except FileNotFoundError:
    #     messagebox.showerror("Error", "Batch file not found.")
    # except:
    #     messagebox.showerror("Error", "An error occurred while running the batch file.")
    try:
        batch_process = subprocess.Popen(['temp.bat'])
    except FileNotFoundError:
        messagebox.showerror("Error", "Batch file not found.")
    except:
        messagebox.showerror("Error", "An error occurred while running the batch file.")


def stop_batch():
    global batch_process

    if batch_process is not None:
        batch_process.terminate()
    else:
        messagebox.showinfo("Info", "Batch process is not running.")

    # Remove the temporary file
    os.remove('temp.bat')


# Create a GUI window with input fields and buttons to run and stop the batch file
root = tk.Tk()
root.title("Maritime Monitoring System based on AIS: Developed by ")
root.geometry("900x450")

ip_address_label = tk.Label(root, text="Enter UDP IP address for Broadcasting decoded AIS traffic:  ----->")
ip_address_label.grid(row=0, column=0, padx=15, pady=15)
ip_address_entry = tk.Entry(root)
ip_address_entry.insert(0, '127.0.0.1')
ip_address_entry.grid(row=0, column=1, padx=15, pady=15)

port_number_label = tk.Label(root, text="Enter UDP Port for Broadcasting decoded AIS traffic:   ---->")
port_number_label.grid(row=1, column=0, padx=15, pady=15)
port_number_entry = tk.Entry(root)
port_number_entry.insert(0, '4159')
port_number_entry.grid(row=1, column=1, padx=15, pady=15)

s_argument_label = tk.Label(root, text="Sample Rate of SDR Device:  ------>")
s_argument_label.grid(row=2, column=0, padx=15, pady=15)
s_argument_entry = tk.Entry(root)
s_argument_entry.insert(0, '2048000')
s_argument_entry.grid(row=2, column=1, padx=15, pady=15)

run_button = tk.Button(root, text="Run MMSAIS System", command=run_batch)
run_button.grid(row=3, column=0, padx=15, pady=15)

stop_button = tk.Button(root, text="Stop MMSAIS System", command=stop_batch)
stop_button.grid(row=3, column=1, padx=15, pady=15)

output_text = tk.Text(root, height=10, width=80)
output_text.grid(row=4, column=0, columnspan=2, padx=15, pady=15)


root.mainloop()
