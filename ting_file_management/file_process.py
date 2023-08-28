from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file = txt_importer(path_file)
    file_info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }
    if file_info not in instance:
        instance.enqueue(file_info)
        sys.stdout.write(f"{file_info}\n")


def remove(instance):
    if instance.is_empty():
        sys.stdout.write("Não há elementos\n")
    else:
        sys.stdout.write(
            f"Arquivo {instance.dequeue()['nome_do_arquivo']} "
            "removido com sucesso\n"
        )


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
