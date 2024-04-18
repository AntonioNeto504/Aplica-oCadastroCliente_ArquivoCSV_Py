FROM python:3.9

WORKDIR /app

COPY cadastroCliente.py .

COPY clientes.csv .

CMD ["python", "cadastroCliente.py"]
