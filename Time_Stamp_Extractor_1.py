import re
import pandas as pd
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


def extract_data(line):
    nmea_sentence, bracketed_info = line.strip().split(' (')
    mmsi = re.search(r"MMSI: ([0-9]+)", bracketed_info).group(1)
    timestamp = re.search(r"timestamp: ([0-9]+)", bracketed_info).group(1)
    signalpower = re.search(r"signalpower: ([-+]?[0-9]*\.?[0-9]+)", bracketed_info).group(1)

    utc_time = datetime.strptime(timestamp, '%Y%m%d%H%M%S')
    gmt_time = utc_time + timedelta(hours=5, minutes=30)
    gmt_timestamp = gmt_time.strftime("%Y-%m-%d %H:%M:%S")

    return (mmsi, gmt_timestamp, signalpower)


def main():
    root = tk.Tk()
    root.title("Time Stamp Extractor Tool : Developed by Vibhore Kumar, SFO(Tech), ARC")
    root.geometry("650x300")

    label1 = tk.Label(root, text="Please browse for the input AIS log file")
    label1.pack(pady=20)

    input_button = tk.Button(root, text="Browse", command=lambda: select_input_file(root))
    input_button.pack()

    label2 = tk.Label(root, text="Please select the output file path")
    label2.pack(pady=20)

    output_button = tk.Button(root, text="Save MMSI Time_Stamp Data", command=lambda: select_output_file(root))
    output_button.pack()

    root.mainloop()


def select_input_file(root):
    file_path = filedialog.askopenfilename(title="Select the input file", filetypes=(("Text Files", "*.txt"),))
    if not file_path:
        messagebox.showwarning("Warning", "No file was selected.")
        return

    with open(file_path, "r") as file:
        data = [extract_data(line) for line in file]

    df = pd.DataFrame(data, columns=["MMSI", "Date and Time of Intercept", "Signal Power"])
    root.df = df


def select_output_file(root):
    save_path = filedialog.asksaveasfilename(title="Select the output file", filetypes=(("Excel Files", "*.xlsx"),),
                                             defaultextension=".xlsx")
    if not save_path:
        messagebox.showwarning("Warning", "No file was selected.")
        return

    root.df.to_excel(save_path, index=False)
    messagebox.showinfo("Success", "Time_Stamp successfully extracted from AIS log file.")


if __name__ == "__main__":
    main()
https://crsorgi.gov.in/web/index.php/auth/birthCertificate/view/cert/B/ZWw3TnE5S3dhcW05R1NiT2pvdGJuQT09%3D%3D
