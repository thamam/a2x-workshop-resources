## ADDED Requirements

### Requirement: Square root function

The expression evaluator SHALL provide a `sqrt(...)` function that returns the non-negative square root of its argument. The argument MUST be a parenthesized sub-expression, which the evaluator SHALL fully evaluate before applying the square root. The function name `sqrt` is case-sensitive and SHALL be recognized only when immediately followed by `(`.

#### Scenario: Square root of a perfect square

- **WHEN** the user evaluates `sqrt(9)`
- **THEN** the result is `3`

#### Scenario: Square root of a non-perfect square

- **WHEN** the user evaluates `sqrt(2)`
- **THEN** the result is `1.4142135623730951`

#### Scenario: Square root of zero

- **WHEN** the user evaluates `sqrt(0)`
- **THEN** the result is `0`

### Requirement: Square root accepts arbitrary sub-expressions

The `sqrt(...)` argument SHALL accept any valid expression, and `sqrt(...)` SHALL itself be usable as an operand within a larger expression with the same precedence as a parenthesized value.

#### Scenario: Argument is a compound expression

- **WHEN** the user evaluates `sqrt(2 + 7)`
- **THEN** the result is `3`

#### Scenario: Square root combined with other operators

- **WHEN** the user evaluates `sqrt(16) * 2`
- **THEN** the result is `8`

#### Scenario: Nested square roots

- **WHEN** the user evaluates `sqrt(sqrt(16))`
- **THEN** the result is `2`

### Requirement: Square root rejects negative operands

The evaluator SHALL raise a math error when `sqrt(...)` is applied to a negative value. It SHALL NOT return a complex or `NaN` result.

#### Scenario: Negative literal argument

- **WHEN** the user evaluates `sqrt(-4)`
- **THEN** a math error is raised with a message indicating the square root of a negative number is undefined

#### Scenario: Expression that evaluates to a negative value

- **WHEN** the user evaluates `sqrt(3 - 10)`
- **THEN** a math error is raised with a message indicating the square root of a negative number is undefined

### Requirement: Square root rejects malformed usage

The evaluator SHALL raise a syntax error when `sqrt` is not followed by a parenthesized argument or when the argument is empty.

#### Scenario: Missing parentheses

- **WHEN** the user evaluates `sqrt 9`
- **THEN** a syntax error is raised

#### Scenario: Missing argument

- **WHEN** the user evaluates `sqrt()`
- **THEN** a syntax error is raised

#### Scenario: Unknown identifier

- **WHEN** the user evaluates `foo(9)`
- **THEN** a syntax error is raised indicating an unknown function or identifier
