## ADDED Requirements

### Requirement: Evaluate basic arithmetic operators
The system SHALL evaluate expressions containing the binary operators `+`, `-`, `*`, `/`, `%` (modulo), and `**` (exponentiation) over numeric operands and return the numeric result.

#### Scenario: Addition and subtraction
- **WHEN** the expression `2 + 3 - 1` is evaluated
- **THEN** the result is `4`

#### Scenario: Multiplication and division
- **WHEN** the expression `6 * 7 / 2` is evaluated
- **THEN** the result is `21`

#### Scenario: Modulo
- **WHEN** the expression `10 % 3` is evaluated
- **THEN** the result is `1`

#### Scenario: Exponentiation
- **WHEN** the expression `2 ** 10` is evaluated
- **THEN** the result is `1024`

### Requirement: Honor operator precedence and associativity
The system SHALL evaluate operators using standard precedence (exponentiation highest, then multiplication/division/modulo, then addition/subtraction) and left-to-right associativity for operators of equal precedence, with exponentiation being right-associative.

#### Scenario: Precedence of multiplication over addition
- **WHEN** the expression `2 + 3 * 4` is evaluated
- **THEN** the result is `14`

#### Scenario: Left associativity of subtraction
- **WHEN** the expression `10 - 4 - 3` is evaluated
- **THEN** the result is `3`

#### Scenario: Right associativity of exponentiation
- **WHEN** the expression `2 ** 3 ** 2` is evaluated
- **THEN** the result is `512`

### Requirement: Support parentheses and unary minus
The system SHALL support parentheses to override precedence and SHALL support unary minus on numbers and parenthesized sub-expressions.

#### Scenario: Parentheses override precedence
- **WHEN** the expression `(2 + 3) * 4` is evaluated
- **THEN** the result is `20`

#### Scenario: Unary minus on a number
- **WHEN** the expression `-5 + 2` is evaluated
- **THEN** the result is `-3`

#### Scenario: Unary minus on a sub-expression
- **WHEN** the expression `-(3 + 4)` is evaluated
- **THEN** the result is `-7`

### Requirement: Support decimal numbers
The system SHALL accept integer and decimal (floating-point) operands and return floating-point results when the computation is non-integer.

#### Scenario: Decimal operands
- **WHEN** the expression `0.1 + 0.2` is evaluated
- **THEN** the result is approximately `0.3`

#### Scenario: Non-integer division result
- **WHEN** the expression `7 / 2` is evaluated
- **THEN** the result is `3.5`

### Requirement: Report errors without crashing
The system SHALL detect invalid syntax and math errors and SHALL surface them as structured, recoverable errors rather than uncaught exceptions or process crashes.

#### Scenario: Invalid syntax
- **WHEN** the expression `2 +` is evaluated
- **THEN** a syntax error is reported describing the problem

#### Scenario: Unbalanced parentheses
- **WHEN** the expression `(2 + 3` is evaluated
- **THEN** a syntax error is reported describing the unbalanced parenthesis

#### Scenario: Unknown character
- **WHEN** the expression `2 $ 3` is evaluated
- **THEN** a syntax error is reported identifying the invalid token

#### Scenario: Division by zero
- **WHEN** the expression `5 / 0` is evaluated
- **THEN** a math error is reported indicating division by zero
