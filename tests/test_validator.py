from datavalidator import SchemaValidator
import pytest

def test_age_validation():
    schema = {"age": {"type": "int", "min": 18}}
    validator = SchemaValidator(schema)
    # Test with a sample DataFrame
    assert validator.validate("test_data.csv").has_errors() == False
