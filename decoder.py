import base64

base64_string = "WhYKCAoGb25saW5lEggKBmFzZGFzZBoA"  # Replace with your base64 string

# Convert base64 string to byte array
byte_array = base64.b64decode(base64_string)

# Replace with the desired file path
file_path = 'output.bin'

with open(file_path, 'wb') as file:
    file.write(byte_array)

print(f"Byte array saved to file: {file_path}")
