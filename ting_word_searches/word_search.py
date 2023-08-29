def exists_word(word, instance):
    word_occurrences = []

    for file_index in range(len(instance)):
        file = instance.search(file_index)
        occurrences = []

        for line_index, line in enumerate(file["linhas_do_arquivo"], start=1):
            if word.lower() in line.lower():
                occurrences.append({"linha": line_index})

        if occurrences:
            word_occurrences.append(
                {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )

    return word_occurrences


def search_by_word(word, instance):
    word_occurrences = []

    for file_index in range(len(instance)):
        file = instance.search(file_index)
        occurrences = []

        for line_index, line in enumerate(file["linhas_do_arquivo"], start=1):
            if word.lower() in line.lower():
                occurrences.append({"linha": line_index, "conteudo": line})

        if occurrences:
            word_occurrences.append(
                {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )

    return word_occurrences
