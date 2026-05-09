import re
import tkinter as tk

# GUI WINDOW

root = tk.Tk()

root.title("Password Complexity Checker")

# Fullscreen window
root.state("zoomed")

# Background color
root.configure(bg="#1E1E1E")

#HEADING

heading = tk.Label(
    root,
    text="Password Complexity Checker",
    font=("Arial", 28, "bold"),
    bg="#1E1E1E",
    fg="white"
)

heading.pack(pady=30)

# MAIN FRAME 

main_frame = tk.Frame(
    root,
    bg="#2D2D2D",
    padx=50,
    pady=40
)
main_frame.pack(pady=20)

# PASSWORD LABEL

password_label = tk.Label(
    main_frame,
    text="Enter Password:",
    font=("Arial", 14, "bold"),
    bg="#2D2D2D",
    fg="white"
)
password_label.grid(row=0, column=0, padx=10, pady=15)

# PASSWORD ENTRY 

password_entry = tk.Entry(
    main_frame,
    width=35,
    font=("Arial", 14),
    show="*"
)
password_entry.grid(row=0, column=1, padx=10, pady=15)

# SHOW PASSWORD FUNCTION 

show_password = False

def toggle_password():

    global show_password

    if show_password:

        password_entry.config(show="*")
        show_button.config(text="Show")
        show_password = False

    else:

        password_entry.config(show="")
        show_button.config(text="Hide")
        show_password = True

# SHOW BUTTON 

show_button = tk.Button(
    main_frame,
    text="Show",
    command=toggle_password,
    bg="#FFD966",
    fg="black",
    font=("Arial", 11, "bold"),
    width=10
)

show_button.grid(row=0, column=2, padx=10)

# STRENGTH LABEL 

strength_label = tk.Label(
    main_frame,
    text="Strength:",
    font=("Arial", 14, "bold"),
    bg="#2D2D2D",
    fg="white"
)

strength_label.grid(row=1, column=0, pady=15)

# RESULT LABEL 

result_label = tk.Label(
    main_frame,
    text="Not Checked",
    font=("Arial", 14, "bold"),
    bg="#2D2D2D",
    fg="orange"
)

result_label.grid(row=1, column=1)

# GAUGE CANVAS 

gauge_canvas = tk.Canvas(
    main_frame,
    width=320,
    height=160,
    bg="#2D2D2D",
    highlightthickness=0
)

gauge_canvas.grid(
    row=2,
    column=0,
    columnspan=3,
    pady=15
)

# SEMICIRCLE ARC

gauge_canvas.create_arc(
    50, 20, 270, 220,
    start=0,
    extent=180,
    style="arc",
    width=6,
    outline="white"
)

# LEVEL LABELS 

gauge_canvas.create_text(
    60, 115,
    text="0",
    fill="red",
    font=("Arial", 11, "bold")
)

gauge_canvas.create_text(
    100, 70,
    text="1",
    fill="orange",
    font=("Arial", 11, "bold")
)

gauge_canvas.create_text(
    140, 45,
    text="2",
    fill="yellow",
    font=("Arial", 11, "bold")
)

gauge_canvas.create_text(
    180, 45,
    text="3",
    fill="lightgreen",
    font=("Arial", 11, "bold")
)

gauge_canvas.create_text(
    220, 70,
    text="4",
    fill="green",
    font=("Arial", 11, "bold")
)

gauge_canvas.create_text(
    260, 115,
    text="5",
    fill="cyan",
    font=("Arial", 11, "bold")
)

# ================= NEEDLE =================

needle = gauge_canvas.create_line(
    160, 120,
    160, 35,
    width=4,
    fill="cyan"
)

# CRACK TIME LABEL 

crack_time_label = tk.Label(
    main_frame,
    text="Estimated Crack Time:",
    font=("Arial", 13, "bold"),
    bg="#2D2D2D",
    fg="white"
)

crack_time_label.grid(
    row=3,
    column=0,
    columnspan=3,
    pady=10
)

# FEEDBACK LABEL

feedback_label = tk.Label(
    main_frame,
    text="Password suggestions will appear here",
    font=("Arial", 12),
    bg="#2D2D2D",
    fg="lightgrey",
    justify="left",
    wraplength=550
)

feedback_label.grid(
    row=4,
    column=0,
    columnspan=3,
    pady=10
)

# PASSWORD ANALYSIS FUNCTION 

def analyze_password():

    password = password_entry.get()

    score = 0

    feedback = []

    # EMPTY PASSWORD 

    if password == "":

        result_label.config(
            text="Not Checked",
            fg="orange"
        )

        crack_time_label.config(
            text="Estimated Crack Time:"
        )

        feedback_label.config(
            text="Password suggestions will appear here"
        )

        gauge_canvas.coords(
            needle,
            160, 120,
            160, 35
        )

        return

    # LENGTH CHECK

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("• Password should contain at least 8 characters")

    # UPPERCASE CHECK

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("• Add at least one uppercase letter")

    # LOWERCASE CHECK

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("• Add at least one lowercase letter")

    # NUMBER CHECK

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("• Add at least one number")

    # SPECIAL CHARACTER CHECK 

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("• Add at least one special character")

    # PASSWORD STRENGTH 

    if score <=1:

        result_label.config(
            text="Too Weak",
            fg="light blue"
        )
    elif score == 2:

        result_label.config(
            text="Weak",
            fg="red"
        )

    elif score == 3:

        result_label.config(
            text="Medium",
            fg="orange"
        )

    elif score == 4:

        result_label.config(
            text="Strong",
            fg="yellow"
        )

    else:

        result_label.config(
            text="Very Strong",
            fg="lightgreen"
        )

    # NEEDLE POSITIONS

    positions = {
        0: (60, 115),
        1: (100, 70),
        2: (140, 45),
        3: (180, 45),
        4: (220, 70),
        5: (260, 115)
    }

    x, y = positions[score]

    gauge_canvas.coords(
        needle,
        160, 120,
        x, y
    )

    # CRACK TIME ESTIMATION

    if score <= 2:

        crack_time = "Few Seconds"

    elif score == 3:

        crack_time = "Few Hours"

    elif score == 4:

        crack_time = "Several Months"

    else:

        crack_time = "several Years"

    crack_time_label.config(
        text=f"Estimated Crack Time: {crack_time}"
    )

    # FEEDBACK

    if feedback:

        feedback_label.config(
            text="\n".join(feedback)
        )

    else:

        feedback_label.config(
            text="✔ Excellent Password!"
        )

# ANALYZE BUTTON

analyze_button = tk.Button(
    root,
    text="Analyze Password",
    command=analyze_password,
    bg="#00C853",
    fg="black",
    font=("Arial", 13, "bold"),
    width=20,
    height=2
)

analyze_button.pack(pady=20)

# REAL-TIME ANALYSIS

password_entry.bind(
    "<KeyRelease>",
    lambda event: analyze_password()
)

root.mainloop()