from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    files_queue = instance
    file = txt_importer(path_file)
    # if not file:
    file_info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }
    if file_info not in files_queue:
        files_queue.enqueue(file_info)
        sys.stdout.write(f"{file_info}\n")


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
