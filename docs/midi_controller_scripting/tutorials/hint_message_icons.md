# Hint message icons

As well as showing basic strings, scripts can use a variety of icons alongside
hint messages. This can be done by placing `^c` at the start of the string
passed to [`ui.setHintMsg`][ui.setHintMsg], where `c` is a character from the
table below.

| Character | Icon                              |
|----------:|:----------------------------------|
|       `b` | Record                            |
|       `c` | Yellow smiling face               |
|       `d` | Mouse right click                 |
|       `e` | Red sad face                      |
|       `f` | Orange left-facing triangle       |
|       `g` | Fast-forward icon                 |
|       `h` | Exclamation point in a red circle |
|       `i` | Clock                             |
|       `j` | Rewind icon                       |
|       `k` | Link icon                         |
|       `l` | MIDI keyboard                     |
|       `m` | F1 (help) key icon                |
|       `n` | Image-Line icon                   |
|       `r` | Plugin icon                       |
|       `s` | File icon                         |
|       `t` | Eye                               |
|       `u` | Tempo tap icon                    |
|       `v` | Left-facing triangle              |
|       `w` | Right-facing triangle             |
|       `x` | Pencil                            |
|       `y` | Slice tool                        |
|       `z` | Brush tool                        |

For example, to display a tempo tap message with a relevant icon, the
following code could be used:

```py
ui.setHintMsg("^uTap tempo")
```

Note that these icon codes are not returned by
[`ui.getHintMsg()`][ui.getHintMsg].
