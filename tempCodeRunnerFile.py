for i, char in enumerate(textPanel):
    color = colors[i % len(colors)]
    print(colored(char, color), end="")
print()