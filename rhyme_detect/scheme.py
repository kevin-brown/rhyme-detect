from rhyme_detect import rhymes

DEFAULT_SYMBOLS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def from_lines(lines, symbols=DEFAULT_SYMBOLS):
    rhyme_scheme = [None, ] * len(lines)
    current_symbol_idx = 0

    for idx, line in enumerate(lines):
        if rhyme_scheme[idx]:
            continue

        start_idx = idx + 1

        if start_idx == len(lines):
            continue

        for compare_idx, compare_line in enumerate(lines[start_idx:], start=start_idx):
            similarity = rhymes.line_similarity(line, compare_line)

            if similarity > 0.5:
                current_symbol = symbols[current_symbol_idx]
                rhyme_scheme[idx] = rhyme_scheme[compare_idx] = current_symbol

                current_symbol_idx += 1

                break

    return rhyme_scheme
