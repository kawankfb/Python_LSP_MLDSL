grammar MLDSL;

program: statement+ EOF;
statement: load | save | show | set | preprocess | split | train | validate | evaluate | tune | compare | predict | py_injection;


// Parser rules for Load
load: 'load' (load_dataset | load_model);
load_dataset: 'dataset' dataset_name? 'from' (file_path | sql_config | url);
load_model: 'model' model_name? 'from' file_path;

// Parser rules for Save
save: 'save' (save_dataset | save_model | save_metrics);
save_dataset: 'dataset' dataset_name? 'to' file_path;
save_model: 'model' model_name? 'to' file_path;
save_metrics: 'metrics' model_name? 'to' file_path;

// Parser rules for Show
show: 'show' (show_dataset | show_model | show_metrics);
show_dataset: 'dataset' dataset_name? dataset_details?;
show_model: 'model' model_name? model_details?;
show_metrics: 'metrics' model_name? metrics_details?;
// Problem: Both dataset_name and dataset_details cannot be optional
dataset_details: detail (',' detail)*;
model_details: detail (',' detail)*;
metrics_details: detail (',' detail)*;

// Parser rules for Set
set: 'set' var_id ':' (value);

// Parser rules for Preprocess
preprocess: 'preprocess' 'dataset' dataset_name? ('using' preprocess_method)? ('on' columns)?;
preprocess_method: method_name parameters?;
method_name: id;

// Parser rules for Split
split: 'split' 'dataset' dataset_name? ('using' split_method)? ('on' columns)?;
split_method: split_method_name parameters?;
split_method_name: id;

// Parser rules for Train
train: 'train' 'model' model_name? ('on' dataset_name)? ('using' model)?;
model: model_name parameters?;

// Parser rules for Validate
validate: 'validate' 'model' model_name? ('on' dataset_name)? ('using' validation_metrics)?;
validation_metrics: metric (',' metric)*;

// Parser rules for Evaluate
evaluate: 'evaluate' 'model' model_name? ('using' evalutaion_metrics)?;
evalutaion_metrics: metric (',' metric)*;

// Parser rules for Tune
tune: 'tune' 'model' model_name? ('using' hyperparameters)?;
hyperparameters: hyperparameter (',' hyperparameter)*;
hyperparameter: '(' id ':' value ')';

// Parser rules for Compare
compare: 'compare' 'models' model_list;
model_list: model_name (',' model_name)*;

// Parser rules for Predict
predict: 'predict' (var_id | dataset_name | record) ('using' model_name)?;

// Parser rules for Python injection
py_injection: python_code;
python_code: CODE;

// Common rarser rules
parameters: '(' parameter (',' parameter)* ')';
parameter: id ':' value;

value: id | string | number | range | list;
range: number 'to' number ('step' number)?;
list: list_element (',' list_element)*;
list_element: number | id | string;
number: INT | FLOAT;

dataset_name: id;
model_name: id;
file_path: string;
sql_config: string;
url: string;
detail: id;
var_id: id;
columns: column (',' column)*;
column: string;
record: string;
string: STRING;
metric: id;
id: ID;

// Lexical rules
INT: DIGIT+;
FLOAT: DIGIT+ '.' DIGIT* | DIGIT* '.' DIGIT+;
STRING: '"' (ESC | .)*? '"';
ID: LETTER (LETTER | DIGIT)*;
CODE: '@py_start' .*? '@py_end';

fragment DIGIT: [0-9];
fragment LETTER: [a-zA-Z_];
fragment ESC: '\\"' | '\\\\';

WS: [ \t\r]+ -> skip;
COMMENT: ('//'.*?'\n' | '/*'.*?'*/') -> channel(HIDDEN);
NEWLINE: ('\n' | '\r\n' | '\r') -> skip;
