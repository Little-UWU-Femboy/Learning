## Basics

When it comes to making a antlr file, this uses the `.g4` extension.

Antlr4 (ANother Tool for Language Recognition) is a parser generator. A paraser is something that takes in tokens (text) and checks if they follows rules and builds a tree representing them called a parse tree.

Before parsing, there must be an *lexical analyzes* done to the text and the thing that does this is called a *lexer*. This is what group text together to form a token that meets a specific pattern and categorize the tokens.

After parsing there is *grammer*. The *grammer* will describe a set of rules that a token pattern follow. For example, to create an assignment identifier the pattern is `assignment: ID '=' expression ;`.



## Making Actual Files

When it comes to making the files, there are three different ways to make it:

1. Making a file to do only lexer analysis. This tells how to split the text passed in into tokens, but not how to parse it.
2. Making a file to do only grammer analysis. This tells how to parse the text with the tokens, but not make the tokens.
3. Making a file to do both grammer and lexar analysis. This can do both make and use the tokens.

To specify which type this will be, put at the top of the file: `lexer grammar <FileName>;`, `parser grammar <FileName>;`, or `grammar <FileName>;` in that respective order to make each.



### Lexer File Type

The first thing to do it put the `lexer grammar <FileName>;` at the top of the file.

When creating the rules for a token, it follows `TokenName: LexerRulePattern;` and this will help group them. The *lexer rule pattern* will be something LIKE regex, but not actually it. Here are the rules to make one for the following and anything else not told is not allowed:

- Using the [] is the same rule as regex
- The +, *, ? is the same rule as regex
- The () is the same rule as regex
- The | is the same rule as regex
- The . is the same rule as regex
- The ~[...] is the negation rule of whatever is in the brackets

> [!TIP]
>
> Is it convention to name the token name all uppercase

There is something called a **fragment**. This is like C #define syntax where it can be used to create a name macro for *lexer rule pattern*. Inside the actual pattern, that fragment name can be placed there and it will treat it as that pattern.

There is no actual way to make alias in this, so to mimic this, just create a token name followed by in single quotes the actual symbol or thing it should alias. For example, `EQUAL : '=';` will make it so that equal sign will now have the token name EQUAL and when being referenced it can be from the EQUAL token name.

There if there is something not wanted from the text, there is a way to do this. Just create a *lexer rule pattern* like normal, but before ending with the semicolon, add `--> skip`. This will make it so a token not created for that thing.

> [!TIP]
>
> A common *lexer rule pattern* to ignore is for white space which usually looks like `WS : [ \t\r\n]+ -> skip ;` which will completly remove this from the *lexer stream*. Another common one is `COMMENT : '//' ~[\r\n]* -> skip ;` to ignore commets in code

There is something called *lexer modes*. This gives the abilty to go from following one set of *lexer rule patterns* to a complete different set of them and back to the original. This is done with the **mode** keyword. The syntax for this is `mode ModeName;` and then right under it declare token *lexer rule patterns* like normal.

To actually enter and exit a mode, there is a special function called `pushMODE(ModeName)` and `popMODE()`. These each follow the same syntax with the skipping of a token with `--> pushMODE(ModeName)` and `--> popMODE()` going at the end of a *lexer rule pattern*. This makes it so if that particular token is found then it will enter into that mode and once gone then leaves that mode. This will create token in the end.

There is something called *lexer actions* and *semantic predicates*. These are a unique way to execute code for a language during lexing. The first one will is when executing code and this is done by putting a set of curlt braces at the end of the *lexer rule pattern* and then inside that running code of the language. For example `NUMBER : [0-9]+ { System.out.println("Number matched: " + getText()); } ;`. The second way is when wanting that particular token id to be made only if there is a case met. For example, `ID : [a-z]+ { getText().equals("special") }? ;`. The first example just 

> [!TIP]
>
> This is important for something like dealing with special rules in string patters. An example of this is:
> ```
> STRING : '"' -> pushMode(STRING_MODE) ;
> 
> mode STRING_MODE;
> CHAR    : ~["\\] ;
> ESC     : '\\' . ;
> END     : '"' -> popMode() ;
> ```

There is something called *Lexer Actions* and *Semantic Predicates*. This is a way to make 

```
lexer grammar MyLexer;

fragment DIGIT : [0-9];              // Kind of like the #define macro in C

// Tokens basics
ID      : [a-zA-Z_][a-zA-Z_0-9]* ;  // identifiers
INT     : DIGIT+ ;                      // integers
PLUS    : '+' ;                           // Acts as alias to + sign 
MINUS   : '-' ;
MULT    : '*' ;
DIV     : '/' ;
LPAREN  : '(' ;
RPAREN  : ')' ;
STRING : '"' -> pushMode(STRING_MODE) ; // Enter the STRING_MODE lexer rules now

// Special mode to handle strings
mode STRING_MODE;
CHAR    : ~["\\] ;
ESC     : '\\' . ;
END     : '"' -> popMode() ; // Leave the STRING_MODE lexer rules now




// Whitespace
WS      : [ \t\r\n]+ -> skip ;      // skip spaces and newlines by completly removing them from the stream
```



### Parser File Type

The first thing to do it put `parser grammar <FileName>;` at the top of the file. The second import thing is to use the special syntax `options {tokenVocab=LexerFileAntlrName; }`. This is needed because this file does not actually make tokens so it needs to know where the token it will use will come from.



### Grammer File Type

