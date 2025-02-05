Changing the terminal's font from within a Python programme is not straightforward, as the terminal emulator itself controls the font settings. However, if you're using a terminal emulator such as GNOME Terminal on Linux, you can use system commands (for example, via gsettings) to update its font configuration. This method will only work on systems where gsettings is available and correctly configured.

Below is a demo script that shows how you might change the font for GNOME Terminal. (Remember to replace the profile ID with your actual GNOME Terminal profile ID.)

```python
#!/usr/bin/env python3
import subprocess

# Retrieve the default GNOME Terminal profile ID
default_profile = subprocess.check_output(
    ["gsettings", "get", "org.gnome.Terminal.ProfilesList", "default"],
    text=True
).strip().strip("'")

# Define the desired font (e.g. "Monospace 14")
desired_font = "Monospace 14"

# Construct the gsettings key for the profile font
gsettings_key = f"org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:{default_profile}/"

# Set the font using gsettings
subprocess.run([
    "gsettings", "set", gsettings_key, "font", f"'{desired_font}'"
])
```

### How It Works

- **Retrieving the Profile ID:**  
  The script first retrieves the default profile ID by running a gsettings command. This ID is needed because GNOME Terminal stores its settings per profile.

- **Setting the Font:**  
  The script then constructs the correct gsettings key for the default profile and sets the font to the desired value (in this example, "Monospace 14").  
 
### Important Considerations

- **Terminal Emulator Dependency:**  
  This approach only works for GNOME Terminal (or other terminal emulators that support similar configuration methods). Other environments (e.g. Windows Command Prompt, macOS Terminal) have different methods or do not allow changing the font via a script.

- **User Permissions:**  
  Changing terminal settings may require that your user has permission to modify these settings. On some systems, additional configuration may be required.

- **Persistence:**  
  The change made by this script will affect your terminal's configuration until you change it again manually or via another script.

If you need to support other environments or want a more general solution, you would typically have to instruct users to change their terminal settings through the terminal emulator's configuration interface.

I hope this demo helps! Let me know if you have any further questions.