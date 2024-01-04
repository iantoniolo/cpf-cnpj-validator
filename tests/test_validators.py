import pytest

from cpf_cnpj_validator.validators import validate_cpf, validate_cnpj

@pytest.mark.parametrize("cpf, expected", [
    ("123.456.789-09", True),
    ("12345678909", True),
    ("000.000.000-00", False),
    ("111.111.111-11", False),
    ("invalid-cpf", False),
    ("123.456.789-01", False),
    ("999.999.999-99", False),
])
def test_validate_cpf(cpf, expected):
    assert validate_cpf(cpf) == expected

@pytest.mark.parametrize("cnpj, expected", [
    ("12.345.678/0001-09", True),
    ("12345678000109", True),
    ("00.000.000/0000-00", False),
    ("11.111.111/1111-11", False),
    ("invalid-cnpj", False),
    ("12.345.678/0001-00", False),
    ("99.999.999/9999-99", False),
])
def test_validate_cnpj(cnpj, expected):
    assert validate_cnpj(cnpj) == expected
