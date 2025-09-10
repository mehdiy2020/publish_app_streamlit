# 🔐 Python Password Generator Suite

A modular and extensible password generation toolkit built in Python, featuring multiple strategies for creating secure and memorable passwords. The project is structured around an abstract base class and three specialized subclasses, each offering a unique approach to password generation.

---

## 📦 Project Structure

### 1. `PasswordGenerator` (Abstract Base Class)
Defines the shared interface for all password generators using Python's `abc` module. It includes:
- An abstract method `generate()` that must be implemented by all subclasses.
- Common attributes and structure for extensibility.

---

### 2. `RandomPasswordGenerator`
Generates secure passwords using:
- Uppercase and lowercase letters
- Optional digits
- Optional symbols (from Python's `string.punctuation`)
- User-defined password length

Example output: `aB7$kL9@zQ`

---

### 3. `MemorablePasswordGenerator`
Creates human-friendly passwords using real English words from the NLTK corpus. Users can specify:
- Number of words
- Separator style:  
  `'hyphen': '-'`  
  `'space': ' '`  
  `'dot': '.'`  
  `'underscore': '_'`  
  `'comma': ','`  
  `'slash': '/'`
All separator are defined in a dictionary and user must the `dict[key]` if she/he desired separator. 
Example output: `sunshine-dream-forest`

---

### 4. `PicCodeGenerator`
Generates numeric-only passwords (PIN-style), ideal for use cases like verification codes or numeric access keys.

Example output: `849273`

---

## 🛠️ Requirements

- **Python 3.12.x** (Tested on 3.12.3)
- Required packages:
```python
import string
from random import choices
from abc import ABC, abstractmethod
from typing import List
import nltk
from nltk.corpus import words
