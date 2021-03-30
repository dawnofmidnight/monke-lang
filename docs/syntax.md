### Monke Syntax Guide
This guide aims to provide a complete understanding of Monke's syntax.

# Notation in This Guide
This guide will use the characters `<>` to enclose something that you can change in your Monke source code. Anything that is optional will be enclosed in `[]` characters. You do not need to include these items, though you can if you wish.
```
<somethingYouCanChange> [<totallyOptional>]
```

# General Syntax
Comments in Monke are preceded by the backtick character, found to the left of the `1` key on QWERTY keyboards.
```
`This is a comment. Monke will completly ignore this.
```
All commands, variable declarations, and such must be completed with a semicolon.
```
chatter("de wei of de M O N K E");
```
Code blocks must be fenced wih brackets.
```
foo () {
    chatter("This is foo");
}
```

# Variables - Not Yet Implemented
Variables in Monke are very simple. They can be declared using this syntax:
```
<varName> [: <type>] [= <value>];
```
For example,
```
a : int = 15;
a : str;
a = "monke";
a;
```
When you declare a variable, you can optionally specify what type it is. If you do not specify a type, that variable will be able to change its type later on. If a type is declared however, it cannot be changed.

# Mathematical Operations
Monke has mothematical operators for addition, subtraction, multiplication, and division. The following is a list of operators and their meaning.
- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division
These operators are used by placing one between two variables or values. The following example will print the number `5` in the terminal.
```
chatter(2 + 3)
```

# Functions

# Logic

# Comparison Operators