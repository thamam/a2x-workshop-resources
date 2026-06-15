## ADDED Requirements

### Requirement: One-shot evaluation from arguments
The system SHALL evaluate an arithmetic expression supplied as command-line arguments, print the result to standard output, and exit with status `0` on success.

#### Scenario: Expression passed as arguments
- **WHEN** the program is invoked as `calc "2 + 3 * 4"`
- **THEN** it prints `14` to standard output and exits with status `0`

#### Scenario: Expression passed as multiple arguments
- **WHEN** the program is invoked as `calc 2 + 3`
- **THEN** the arguments are joined into a single expression, it prints `5`, and exits with status `0`

### Requirement: One-shot error handling
The system SHALL, when a one-shot expression is invalid or fails to evaluate, print a descriptive error message to standard error and exit with a non-zero status.

#### Scenario: Invalid one-shot expression
- **WHEN** the program is invoked as `calc "2 +"`
- **THEN** it prints an error message to standard error and exits with a non-zero status

#### Scenario: Division by zero in one-shot mode
- **WHEN** the program is invoked as `calc "5 / 0"`
- **THEN** it prints a division-by-zero error to standard error and exits with a non-zero status

### Requirement: Interactive REPL mode
The system SHALL, when invoked with no expression arguments, start an interactive read-eval-print loop that reads one expression per line, prints the result of each, and continues accepting input until the user exits.

#### Scenario: Evaluate a line in the REPL
- **WHEN** the user starts the REPL and enters `2 + 3`
- **THEN** the program prints `5` and prompts for the next expression

#### Scenario: Error does not terminate the REPL
- **WHEN** the user enters an invalid expression such as `2 +` in the REPL
- **THEN** the program prints an error message and continues prompting for the next expression

#### Scenario: Exit the REPL
- **WHEN** the user enters `quit` (or sends end-of-file)
- **THEN** the program exits cleanly with status `0`

### Requirement: Result output formatting
The system SHALL print whole-number results without a trailing decimal point and SHALL print non-integer results as decimal numbers.

#### Scenario: Integer result formatting
- **WHEN** the expression `6 / 2` is evaluated
- **THEN** the printed result is `3` (not `3.0`)

#### Scenario: Decimal result formatting
- **WHEN** the expression `7 / 2` is evaluated
- **THEN** the printed result is `3.5`
