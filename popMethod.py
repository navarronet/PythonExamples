IDEs = ['vscode', 'pycharm', 'sublime', 'atom', 'pycharm', 'notepad++', 'visual studio','android studio','xcode']

print(IDEs) # ['vscode', 'pycharm', 'sublime', 'atom', 'pycharm', 'notepad++', 'visual studio', 'android studio', 'xcode']

# use pop() method with its default behavior

IDEs.pop() # removes the last element

print(IDEs) # ['vscode', 'pycharm', 'sublime', 'atom', 'pycharm', 'notepad++', 'visual studio', 'android studio']

# use pop() method to remove the element

IDEs.pop(1)

print(IDEs) # ['vscode', 'sublime', 'atom', 'pycharm', 'notepad++', 'visual studio', 'android studio', 'xcode']