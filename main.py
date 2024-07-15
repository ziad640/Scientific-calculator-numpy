import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import numpy as np
import random

class CalculatorApp(App):
    def build(self):
        self.box = BoxLayout(orientation='vertical')
        
        self.display = TextInput(font_size=32, readonly=True, halign="right", multiline=False)
        self.box.add_widget(self.display)
        
        buttons = [
            ["7", "8", "9", "/", "sqrt"],
            ["4", "5", "6", "*", "exp"],
            ["1", "2", "3", "-", "log"],
            [".", "0", "C", "+", "="],
            ["sin", "cos", "tan", "**","[","]"],
            ["(", ")", "pi", "e", "abs", ",", "array", "Random", "Shuffle"]
        ]
        
        for row in buttons:
            h_box = BoxLayout()
            for label in row:
                button = Button(text=label, on_press=self.on_button_press)
                h_box.add_widget(button)
            self.box.add_widget(h_box)
        
        return self.box

    def on_button_press(self, instance):
        current = self.display.text
        button_text = instance.text
        
        if button_text == "C":
            self.display.text = ""
        elif button_text == "=":
            try:
                # Prepare a safe environment for eval
                safe_globals = {"np": np, "random": random}
                print(f"Evaluating expression: {current}")  # Debug message
                result = str(eval(current, safe_globals, {}))
                self.display.text = result
            except Exception as e:
                print(f"Error: {e}")  # Debug message
                self.display.text = "Error"
        elif button_text == "Random":
            # Generate a random value (you can customize this)
            random_value = np.random.rand()
            self.display.text += str(random_value)
        elif button_text == "Shuffle":
            # Shuffle the current displayed text in the specified format
            text_parts = current.split("[")
            if len(text_parts) == 2:
                left_part = text_parts[0]
                right_part = text_parts[1].split("]")[1] if len(text_parts[1].split("]")) == 2 else ""
                middle_part = text_parts[1].split("]")[0][::-1]
                self.display.text = f"{left_part}[{middle_part}]{right_part}"
        else:
            if button_text in ["sqrt", "sin", "cos", "tan", "log", "exp", "abs"]:
                # For functions, add np. prefix
                self.display.text += f"np.{button_text}("
            elif button_text in ["pi", "e"]:
                # For constants pi and e, append np. directly
                self.display.text += f"np.{button_text}"
            elif button_text == "array":
                # Add an array placeholder
                self.display.text += "np.array(["
            else:
                self.display.text += button_text

if __name__ == "__main__":
    CalculatorApp().run()
