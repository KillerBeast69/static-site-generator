def markdown_to_blocks(markdown):
    list_of_block = markdown.split("\n\n")
    final_blocks = []
    for block in list_of_block:
        stripped_block = block.strip()
        if stripped_block != "":
            final_blocks.append(stripped_block)
    return final_blocks
    