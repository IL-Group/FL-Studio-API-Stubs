# Hint message icons

As well as showing basic strings, scripts can use a variety of icons alongside
hint messages. This can be done by placing `^c` at the start of the string,
where `c` is a character from the table below.

| Character | Icon                              |
|----------:|:----------------------------------|
|       `b` | record                            |
|       `c` | yellow smiling face               |
|       `d` | mouse right click                 |
|       `e` | red sad face                      |
|       `f` | orange left-facing triangle       |
|       `g` | fast-forward icon                 |
|       `h` | exclamation point in a red circle |
|       `i` | clock                             |
|       `j` | rewind icon                       |
|       `k` | link icon                         |
|       `l` | midi keyboard                     |
|       `m` | F1 (help) key icon                |
|       `n` | Image-Line icon                   |
|       `r` | plugin icon                       |
|       `s` | file icon                         |
|       `t` | eye                               |
|       `u` | tempo tap icon                    |
|       `v` | left-facing triangle              |
|       `w` | right-facing triangle             |
|       `x` | pencil                            |
|       `y` | slice tool                        |
|       `z` | brush tool icon                   |

For example, to display a tempo tap message with a relevant icon, the
following code could be used.

```py
ui.setHintMsg("^uTap tempo")
```

Note that these icon codes are not returned by `ui.getHintMsg()`.
