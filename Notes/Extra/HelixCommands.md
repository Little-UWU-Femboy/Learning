# Helix Commands

## Delete

| Action                      | Command  | Description                                                  |
| --------------------------- | -------- | ------------------------------------------------------------ |
| Delete one character        | `d`      | Deletes the current selection, normally one character        |
| Delete one word             | `wd`     | Deletes from the cursor through the start of the next word; may include whitespace |
| Delete current word         | `miwd`   | Selects the word's contents and deletes it                   |
| Delete line                 | `xd`     | Deletes the current line                                     |
| Delete multiple lines       | `#xd`    | Selects n lines and deletes them                             |
| Delete entire file          | `%d`     | Deletes all contents of the file                             |
| Delete without yanking      | `Alt-d`  | Deletes selected text without updating the yank register     |
| Delete word while inserting | `Ctrl-w` | Deletes the previous word in Insert mode                     |
| Delete to beginning of line | `Ctrl-u` | Deletes backward to start of line in Insert mode             |
| Delete to end of line       | `Ctrl-k` | Deletes forward to end of line in Insert mode                |

## Copy (Yank)

| Action                               | Command       | Description                                             |
| ------------------------------------ | ------------- | ------------------------------------------------------- |
| Copy one character                   | `y`           | Copies the currently selected character                 |
| Copy word/range                      | `wy`          | Copies through the start of the next word               |
| Copy exact word                      | `miwy`        | Copies the word without surrounding whitespace          |
| Copy line                            | `xy`          | Copies the entire current line                          |
| Copy multiple lines                  | `3xy`         | Copies three lines                                      |
| Copy entire file                     | `%y`          | Copies all contents                                     |
| Copy selection to system clipboard   | `Space y`     | Copies selected text into Windows/macOS/Linux clipboard |
| Copy character to system clipboard   | `Space y`     | Copies current character selection                      |
| Copy word to system clipboard        | `miw Space y` | Copies exact word to system clipboard                   |
| Copy line to system clipboard        | `x Space y`   | Copies current line to system clipboard                 |
| Copy entire file to system clipboard | `% Space y`   | Copies entire file to system clipboard                  |

Important: In Helix, moving with `w` and selecting with `w` are not always the same operation. If you want the exact word under your cursor, `miw` is more precise.

## Paste

| Action                             | Command   | Description                                       |
| ---------------------------------- | --------- | ------------------------------------------------- |
| Paste after                        | `p`       | Pastes internal yank register after selection     |
| Paste before                       | `P`       | Pastes internal yank register before selection    |
| Paste system clipboard after       | `Space p` | Pastes from the OS clipboard                      |
| Paste system clipboard before      | `Space P` | Pastes OS clipboard before selection              |
| Replace selection from clipboard   | `Space R` | Replaces selected text with clipboard contents    |
| Replace selection with yanked text | `R`       | Replaces selection with contents of yank register |

## Text Selection

| Action                      | Command        | Description                                    |
| --------------------------- | -------------- | ---------------------------------------------- |
| Select text                 | `v` + movement | Extends selection as you move                  |
| Select next word range      | `w`            | Selects from current cursor to next word start |
| Select exact word           | `miw`          | Selects inside the word                        |
| Select line                 | `x`            | Selects the entire current line                |
| Select entire file          | `%`            | Selects all file contents                      |
| Select multiple lines       | `x` repeatedly | Expands selection one line at a time           |
| Select inside parentheses   | `mi(`          | Selects contents of parentheses                |
| Select around parentheses   | `ma(`          | Includes the surrounding parentheses           |
| Select inside quotes        | `mi"`          | Selects content inside double quotes           |
| Select around quotes        | `ma"`          | Includes double quotes                         |
| Collapse selection          | `;`            | Reduces selection to one cursor                |
| Keep only primary selection | `,`            | Removes additional selections/cursors          |
| Undo                        | `u`            | Undoes last change                             |
| Redo                        | `U`            | Redoes last undone change                      |

## Editing

| Action                             | Command         | Description                                           |
| ---------------------------------- | --------------- | ----------------------------------------------------- |
| Insert before cursor               | `i`             | Enters Insert mode before selection                   |
| Insert after cursor                | `a`             | Enters Insert mode after selection                    |
| Insert at start of line            | `I`             | Inserts before indentation                            |
| Insert at first nonblank character | `gsi`           | Moves to first non-whitespace character, then inserts |
| Insert at end of line              | `A`             | Enters Insert mode at end of line                     |
| New line below                     | `o`             | Opens blank line below and starts editing             |
| New line above                     | `O`             | Opens blank line above and starts editing             |
| Change selection                   | `c`             | Deletes selection and enters Insert mode              |
| Change without yanking             | `Alt-c`         | Same as `c`, without updating yank register           |
| Replace character(s)               | `r` + character | Replaces selected characters with the typed character |
| Replace with copied text           | `R`             | Replaces selection with yank register                 |
| Repeat last insertion              | `.`             | Repeats previous insertion                            |
| Join lines                         | `J`             | Joins selected lines                                  |
| Indent selected text               | `>`             | Increases indentation                                 |
| Unindent selected text             | `<`             | Decreases indentation                                 |
| Toggle comment                     | `Ctrl-c`        | Adds/removes comment markers                          |
| Toggle comment alternative         | `Space c`       | Comments/uncomments selections                        |
| Switch uppercase/lowercase         | `~`             | Toggles letter case                                   |
| Increment number                   | `Ctrl-a`        | Increases number under cursor                         |
| Decrement number                   | `Ctrl-x`        | Decreases number under cursor                         |

## Movement and Navigation

| Action                   | Command           | Description                                              |
| ------------------------ | ----------------- | -------------------------------------------------------- |
| Move left                | `h`               | One character left                                       |
| Move down                | `j`               | One visual line down                                     |
| Move up                  | `k`               | One visual line up                                       |
| Move right               | `l`               | One character right                                      |
| Jump to top of file      | `gg`              | First line                                               |
| Jump to bottom of file   | `ge`              | Last line                                                |
| Go to specific line      | `G` + line number | Prompts for line number                                  |
| Start of line            | `gh`              | First character including whitespace                     |
| End of line              | `gl`              | End of current line                                      |
| First nonblank character | `gs`              | Skips indentation                                        |
| Next word                | `w`               | Beginning of next word                                   |
| Previous word            | `b`               | Beginning of previous word                               |
| End of word              | `e`               | Moves to word ending                                     |
| Next WORD                | `W`               | Moves across punctuation-separated text until whitespace |
| Previous WORD            | `B`               | Moves backward by whitespace-separated WORD              |
| Find next character      | `f` + character   | Moves forward to specified character                     |
| Find previous character  | `F` + character   | Moves backward to specified character                    |
| Find until character     | `t` + character   | Moves to just before matching character                  |
| Jump to visible word     | `gw`              | Shows jump labels for visible words                      |
| Half-page down           | `Ctrl-d`          | Scrolls/cursor down half page                            |
| Half-page up             | `Ctrl-u`          | Scrolls/cursor up half page                              |
| Full-page down           | `Ctrl-f`          | Moves down a page                                        |
| Full-page up             | `Ctrl-b`          | Moves up a page                                          |
| Jump back                | `Ctrl-o`          | Returns to previous jump location                        |
| Jump forward             | `Ctrl-i`          | Moves forward through jump history                       |

## Search

| Action                      | Command   | Description                                             |
| --------------------------- | --------- | ------------------------------------------------------- |
| Search file                 | `/`       | Searches current document using a regex                 |
| Search backward             | `?`       | Searches backward                                       |
| Next search result          | `n`       | Finds next match                                        |
| Previous search result      | `N`       | Finds previous match                                    |
| Search selected word        | `*`       | Searches for selected text with word-boundary detection |
| Search entire project       | `Space /` | Searches all files in workspace                         |
| Select matching occurrences | `s`       | Selects regex matches within current selections         |
| Keep matching selections    | `K`       | Retains selections matching a regex                     |
| Remove matching selections  | `Alt-K`   | Removes matching selections                             |

## Space Commands

| Action                           | Command   | Description                                       |
| -------------------------------- | --------- | ------------------------------------------------- |
| File explorer / picker           | `Space f` | Fuzzy file picker at workspace root               |
| File picker in current directory | `Space F` | Searches from current working directory           |
| Open buffers                     | `Space b` | Shows currently opened files                      |
| Changed files                    | `Space g` | Lists changed files                               |
| Jump history                     | `Space j` | Displays jump history                             |
| Documentation                    | `Space k` | Shows documentation for symbol under cursor (LSP) |
| Current file errors/warnings     | `Space d` | Opens document diagnostics                        |
| Project errors/warnings          | `Space D` | Opens workspace diagnostics                       |
| Quick fixes                      | `Space a` | Opens available code actions (LSP)                |
| Rename symbol                    | `Space r` | Renames symbol using language server              |
| Document symbols                 | `Space s` | Lists functions, classes, and symbols in file     |
| Project symbols                  | `Space S` | Searches symbols across workspace                 |
| Symbol references                | `Space h` | Selects references to symbol (LSP)                |
| Global text search               | `Space /` | Searches project                                  |
| Command palette                  | `Space ?` | Lists commands available in Helix                 |
| Copy to system clipboard         | `Space y` | Copies selection to system clipboard              |
| Paste from system clipboard      | `Space p` | Pastes clipboard contents                         |
| Toggle comment                   | `Space c` | Comments/uncomments selection                     |
| Split/window commands            | `Space w` | Enters window-management mode                     |

Correction: `Space e` is not the default Helix file explorer command. The built-in file picker is `Space f`. If you have `Space e`, it's likely a custom binding or integration.

## Surrounding Text

| Action                         | Command          | Description                                         |
| ------------------------------ | ---------------- | --------------------------------------------------- |
| Add surrounding characters     | `ms` + character | Surrounds selected text with quotes, brackets, etc. |
| Remove surrounding characters  | `md` + character | Removes matching surrounding characters             |
| Replace surrounding characters | `mr` + old + new | Changes surrounding characters                      |
| Jump to matching bracket       | `mm`             | Moves to matching bracket                           |
| Select inside surrounding text | `mi` + delimiter | Selects interior of quoted/bracketed text           |
| Select around surrounding text | `ma` + delimiter | Includes delimiters                                 |

