lexer grammar XMLLexer;

fragment LT: '<' ;
fragment LTS: '</' ;
fragment GT: '>' ;
fragment SGT: '/>' ;

fragment NAME: (LETTER | UNDERSCORE) (LETTER | DIGIT | UNDERSCORE)* ;
fragment LETTER: [a-z] ;
fragment DIGIT: [0-9] ;
fragment UNDERSCORE: '_' ;

OPEN: LT NAME GT ;
CLOSE: LTS NAME GT ;
SELF: LT NAME SGT ;
TEXT: ~[<>]+ ;

WS: [ \t\r\n]+ -> skip ;