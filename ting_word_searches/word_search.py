def exists_word(word, instance):
    word_search = []
    for file_index in range(0, len(instance)):
        file = instance.search(file_index)
        ocorrencias = []
        for index, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                ocorrencias.append({"linha": index + 1})
        if ocorrencias:
            word_search.append(
                {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": ocorrencias,
                }
            )
    return word_search


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
