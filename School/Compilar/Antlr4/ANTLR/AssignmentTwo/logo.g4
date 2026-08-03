grammar logo;

stmt
  : 'fd' expr                       #fd
  | 'bk' expr                       #bk
  | 'rt' expr                       #rt
  | 'lt' expr                       #lt
  | 'pu'                            #pu
  | 'pd'                            #pd
  | 'hm'                            #hm
  | 'sc' expr                       #sc
  | 'wd' expr                       #width
  | 'as' ID expr                    #assign
  | 'rp' expr stmts                 #repeat
  | 'ifz' expr stmts stmts          #ifZero
  ;

stmts
  : '[' stmt* ']'
  ;

expr
  : '-' expr                        #negation
  | '(' expr ')'                    #parens
  | expr op=('*'|'/'|'%') expr      #mulDivMod
  | expr op=('+'|'-') expr          #addSub
  | ID                              #idExpr
  | INT                             #intExpr
  ;

ID  : [a-zA-Z_][a-zA-Z0-9_]* ;
INT : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;
