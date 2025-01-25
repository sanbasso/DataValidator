# DataValidator  
A lightweight package to validate CSV/JSON data against custom schemas.

## Installation  
`pip install datavalidator`

## Usage  
```python
from datavalidator import SchemaValidator
schema = {"email": {"type": "string", "regex": "..."}}
validator = SchemaValidator(schema)
report = validator.validate("data.csv")
