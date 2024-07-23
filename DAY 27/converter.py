from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())  # Convert input to float
    km = miles * 1.609  # Perform the conversion
    kilometer_result_label.config(text=f"{km:.2f}")  # Update the label with the result

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

# Entry for miles input
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

# Label for miles
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Label for "is equal to"
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

# Label for kilometer result
kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

# Label for kilometers
kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

# Calculate button
calculate_button = Button(text="Calculate", command=miles_to_km)  # Link to the conversion function
calculate_button.grid(column=1, row=2)

window.mainloop()
