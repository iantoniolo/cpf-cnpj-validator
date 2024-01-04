from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    page_description = f.read()

setup(
    name="cpf_cnpj_validator",
    version="0.0.1",
    author="Ian Victor Toniolo Silva",
    author_email="iantoniolo@hotmail.com",
    description="The `cpf_cnpj_validator` package provides simple functionalities for validating Brazilian CPF (Individual Taxpayer Registry) and CNPJ (National Registry of Legal Entities) numbers in Python.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iantoniolo/cpf-cnpj-validator",
    python_requires='>=3.6',
)