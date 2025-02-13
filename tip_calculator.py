import customtkinter as ctk

# Function to calculate tip
def calculate_tip(event=None):
    try:
        bill = float(entry.get())
        tip_15.set(f"${bill * 0.15:.2f}")
        tip_18.set(f"${bill * 0.18:.2f}")
        tip_20.set(f"${bill * 0.20:.2f}")
        tip_100.set(f"${bill * 1.00:.2f}")
        
        total_15.set(f"${bill * 1.15:.2f}")
        total_18.set(f"${bill * 1.18:.2f}")
        total_20.set(f"${bill * 1.20:.2f}")
        total_100.set(f"${bill * 2.00:.2f}")

    except ValueError:
        tip_15.set("Invalid")
        tip_18.set("Invalid")
        tip_20.set("Invalid")
        total_15.set("Invalid")
        total_18.set("Invalid")
        total_20.set("Invalid")
        total_20.set("Invalid")

# Initialize window
ctk.set_appearance_mode("dark")  # Light, Dark, or System
ctk.set_default_color_theme("dark-blue")  # Change to "green", "dark-blue", etc.

root = ctk.CTk()
root.title("Tip Calculator")
root.geometry("550x600")

# Input Field
ctk.CTkLabel(root, text="How was our Service?", font=("Arial", 20)).pack(pady=5)
entry = ctk.CTkEntry(root, font=("Arial", 14), width=200)
entry.pack(pady=5)
entry.bind("<Return>", calculate_tip)  # Enter key to calculate

# Tip Output Variables
tip_15, tip_18, tip_20, tip_100 = ctk.StringVar(), ctk.StringVar(), ctk.StringVar(), ctk.StringVar()
total_15, total_18, total_20, total_100 = ctk.StringVar(), ctk.StringVar(), ctk.StringVar(), ctk.StringVar()

# Display Tips
ctk.CTkLabel(root, text="Bad 15% Tip:", font=("Arial", 14)).pack()
ctk.CTkLabel(root, textvariable=tip_15, font=("Arial", 14), text_color="red").pack()

ctk.CTkLabel(root, text="Good 18% Tip:", font=("Arial", 16)).pack()
ctk.CTkLabel(root, textvariable=tip_18, font=("Arial", 16), text_color="orange").pack()

ctk.CTkLabel(root, text="Great 20% Tip:", font=("Arial", 18)).pack()
ctk.CTkLabel(root, textvariable=tip_20, font=("Arial", 18), text_color="yellow").pack()

ctk.CTkLabel(root, text="Best Service of my life 100% Tip:", font=("Arial", 20)).pack()
ctk.CTkLabel(root, textvariable=tip_100, font=("Arial", 20), text_color="lightgreen").pack()

# Display Totals
ctk.CTkLabel(root, text="Total (15% Tip):", font=("Arial", 14)).pack()
ctk.CTkLabel(root, textvariable=total_15, font=("Arial", 14), text_color="red").pack()

ctk.CTkLabel(root, text="Total (18% Tip):", font=("Arial", 16)).pack()
ctk.CTkLabel(root, textvariable=total_18, font=("Arial", 16), text_color="orange").pack()

ctk.CTkLabel(root, text="Total (20% Tip):", font=("Arial", 18)).pack()
ctk.CTkLabel(root, textvariable=total_20, font=("Arial", 18), text_color="yellow").pack()

ctk.CTkLabel(root, text="Total (100% Tip):", font=("Arial", 20)).pack()
ctk.CTkLabel(root, textvariable=total_100, font=("Arial", 20), text_color="lightgreen").pack()

# Button to Calculate
ctk.CTkButton(root, text="Calculate", command=calculate_tip, font=("Arial", 14), width=150).pack(pady=10)

# Set focus to the entry field
entry.focus()

root.mainloop()
