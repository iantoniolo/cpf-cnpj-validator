# cpf_cnpj_validator

The `cpf_cnpj_validator` package provides simple functionalities for validating Brazilian CPF (Individual Taxpayer Registry) and CNPJ (National Registry of Legal Entities) numbers in Python.

## Key Features

- **CPF Validation:** Check the validity of CPF numbers, ensuring they meet the criteria established by the Brazilian Revenue Service.

- **CNPJ Validation:** Verify the validity of CNPJ numbers, ensuring compliance with the rules set for business registration.

## Usage

```python
from cpf_cnpj_validator.validators import validate_cpf, validate_cnpj

# Example of CPF validation
cpf_number = "123.456.789-09"
if validate_cpf(cpf_number):
    print(f"The CPF {cpf_number} is valid.")
else:
    print(f"The CPF {cpf_number} is invalid.")

# Example of CNPJ validation
cnpj_number = "12.345.678/0001-09"
if validate_cnpj(cnpj_number):
    print(f"The CNPJ {cnpj_number} is valid.")
else:
    print(f"The CNPJ {cnpj_number} is invalid.")
