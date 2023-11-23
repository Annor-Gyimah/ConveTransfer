import psutil as ps
import tkinter as tk
import ttkbootstrap as ttk

def update_drive_info_and_progress_bars(tab2):
    def get_drive_info():
        drive_info = []
        excluded_drive_types = ['cdrom', 'pendrive']  # Types to exclude

        for partition in ps.disk_partitions():
            drive_name = partition.device
            drive_mountpoint = partition.mountpoint
            drive_usage = ps.disk_usage(drive_mountpoint)

            # Check if the drive type is not in the excluded list
            if partition.fstype not in excluded_drive_types:
                drive_info.append((drive_name, drive_usage))

        return drive_info

    def update_progress_bars():
        drive_info = get_drive_info()
        for i, (drive_name, drive_usage) in enumerate(drive_info):
            total_capacity = drive_usage.total
            used_capacity = drive_usage.used
            free_capacity = drive_usage.free

            # Calculate the percentage used
            percentage_used = (used_capacity / total_capacity) * 100

            # Update the progress bar for the drive
            progress_bars[i]['value'] = percentage_used

    drive_info = get_drive_info()
    progress_bars = []

    for i, (drive_name, drive_usage) in enumerate(drive_info):
        ts = drive_usage.total / (1024 * 1024 * 1024)
        ts = f'{ts:.2f}'
        us = drive_usage.used / (1024 * 1024 * 1024)
        us = f'{us:.2f}'
        fr = drive_usage.free / (1024 * 1024 * 1024)
        fr = f'{fr:.2f}'
        label = tk.Label(tab2, text=f"Drive {drive_name} ", font=('Arial', 10, 'bold'))
        label.pack(side=tk.TOP, pady=12)
        boot = 'primary'
        progress = ttk.Floodgauge(tab2, mask=f"Used Space {us} | Total Space {ts} | Free Space {fr}",
                                  length=600, mode="determinate", bootstyle=boot)
        progress.pack(fill='x', padx=(5, 5), pady=2)
        progress_bars.append(progress)
        if us > str(100):
            progress.configure(bootstyle='danger')
        else:
            progress.configure(bootstyle='primary')

    updatebuttonf = ttk.Button(tab2, text='update', command=update_progress_bars)
    updatebuttonf.pack(pady=10)

    update_progress_bars()