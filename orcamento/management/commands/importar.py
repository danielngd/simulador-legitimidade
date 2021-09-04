import csv
import pathlib
import os
from django.core.management.base import BaseCommand, CommandError
from orcamento.models import Produto

class Command(BaseCommand):
    help = 'Importa a lista de produtos em formato CSV'

    def handle(self, *args, **options):
         with open(os.path.join(pathlib.Path(__file__).parent.resolve(), './produtos.csv')) as f:
            reader = csv.reader(f)
            for row in reader:
                _, created = Produto.objects.get_or_create(
                    codigo=row[0],
                    nome=row[1],
                    tipo=row[2],
                    embalagens=row[3],
                    comp=row[4],
                    descricao=row[5],
                    cpv=float(row[6].replace(",", ".")),
                )