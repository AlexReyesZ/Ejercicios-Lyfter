def reverse_string(text):
    reversed_text = text[::-1]  # Slice that reverses the string
    return reversed_text  # Return the reversed string

# Example usage
original = "Hello World"
result = reverse_string(original)

print("Original string:", original)
print("Reversed string:", result)
