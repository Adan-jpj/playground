import tkinter as tk
import math
import time

root = tk.Tk()
root.title("Analog Clock with Numbers")
root.geometry("400x400")
root.configure(bg="black")

canvas = tk.Canvas(root, width=400, height=400, bg='black', highlightthickness=0)
canvas.pack()

center_x, center_y = 200, 200
clock_radius = 150

# Draw clock face with numbers
def draw_clock_face():
    canvas.create_oval(center_x - clock_radius, center_y - clock_radius,
                       center_x + clock_radius, center_y + clock_radius,
                       outline="cyan", width=4)

    for i in range(1, 13):
        angle = math.radians(i * 30)
        x = center_x + clock_radius * 0.82 * math.sin(angle)
        y = center_y - clock_radius * 0.82 * math.cos(angle)
        canvas.create_text(x, y, text=str(i), fill='cyan', font=('Arial', 14, 'bold'))

        # Optional: Tick marks
        x_outer = center_x + clock_radius * 0.9 * math.sin(angle)
        y_outer = center_y - clock_radius * 0.9 * math.cos(angle)
        x_inner = center_x + clock_radius * 0.75 * math.sin(angle)
        y_inner = center_y - clock_radius * 0.75 * math.cos(angle)
        canvas.create_line(x_inner, y_inner, x_outer, y_outer, fill='cyan', width=2)

# Update clock hands
def update_clock():
    canvas.delete("hands")

    t = time.localtime()
    seconds = t.tm_sec
    minutes = t.tm_min
    hours = t.tm_hour % 12

    # Calculate angles
    sec_angle = math.radians(seconds * 6)
    min_angle = math.radians(minutes * 6 + seconds * 0.1)
    hour_angle = math.radians(hours * 30 + minutes * 0.5)

    # Second hand
    sec_x = center_x + 120 * math.sin(sec_angle)
    sec_y = center_y - 120 * math.cos(sec_angle)
    canvas.create_line(center_x, center_y, sec_x, sec_y, fill='red', width=1, tags="hands")

    # Minute hand
    min_x = center_x + 100 * math.sin(min_angle)
    min_y = center_y - 100 * math.cos(min_angle)
    canvas.create_line(center_x, center_y, min_x, min_y, fill='white', width=3, tags="hands")

    # Hour hand
    hour_x = center_x + 70 * math.sin(hour_angle)
    hour_y = center_y - 70 * math.cos(hour_angle)
    canvas.create_line(center_x, center_y, hour_x, hour_y, fill='cyan', width=5, tags="hands")

    root.after(1000, update_clock)

draw_clock_face()
update_clock()
root.mainloop()
