from PIL import Image


class Block:
    def __init__(self, left, right, top, bottom, color):
        self.l = left
        self.r = right
        self.t = top
        self.b = bottom
        self.c = color

    def __str__(self):
        return str(self.l) + " " + str(self.r) + " " + str(self.t) + " " + str(self.b)


def create_block(pixels, i, j):
    l = pixels[i, j + 3]
    r = pixels[i + 7, j + 3]
    t = pixels[i + 3, j]
    b = pixels[i + 3, j + 7]
    color = pixels[i, j]
    return Block(l, r, t, b, color)


def find_solution_left(reference, blocks):
    col_b = len(blocks)
    row_b = len(blocks[0])
    col = reference.r

    for i in range(col_b):
        for j in range(row_b):
            if blocks[i][j].l == col:
                print("Found at: ", i, j)
                return blocks[i][j]
    return None


def find_solution_top(reference, blocks):
    col_b = len(blocks)
    row_b = len(blocks[0])
    col = reference.b

    found = None
    for i in range(col_b):
        for j in range(row_b):
            if blocks[i][j].t == col:
                print("Found at: ", i, j)
                if not found is None:
                    print("Ep! caca")
                found = blocks[i][j]
    return found


def main():
    im = Image.open("puzzle.png")
    col, row = im.size
    pixels = im.load()
    block_cols = int(col / 8)
    block_rows = int(row / 8)

    blocks = []
    image_base = Image.new('RGB', (block_rows, block_cols))
    image_col = Image.new('RGB', (block_rows, block_cols))

    for i in range(0, row, 8):
        aux = []
        for j in range(0, col, 8):
            r = int(i / 8)
            c = int(j / 8)
            block = create_block(pixels, i, j)
            aux.append(block)
        blocks.append(aux)

    for i in range(block_rows):
        for j in range(block_cols):
            image_base.putpixel((i, j), blocks[i][j].c)

    solution = []
    pixels = []
    image = Image.new('RGB', (block_rows, block_cols))
    image_debug = Image.new('RGB', (3*block_rows, 3*block_cols))

    for i in range(block_rows):
        aux = []
        for j in range(block_cols):
            aux_sol = None
            print("Finding x:", i, "y:", j)
            if i < 7 and j < 7:
                print("Base block")
                aux_sol = blocks[i][j]
            else:
                if i < 7:
                    aux_sol = find_solution_left(aux[j - 1], blocks)
                else:
                    aux_sol = find_solution_top(solution[i - 1][j], blocks)
            aux.append(aux_sol)
            image.putpixel((i, j), aux_sol.c)
            image_debug.putpixel((3*i + 1, 3*j + 1), aux_sol.c)
            image_debug.putpixel((3 * i + 1, 3 * j), aux_sol.l)
            image_debug.putpixel((3 * i + 1, 3 * j + 2), aux_sol.r)
            image_debug.putpixel((3 * i, 3 * j + 1), aux_sol.t)
            image_debug.putpixel((3 * i + 2, 3 * j + 1), aux_sol.b)
        solution.append(aux)

    image.save("prova.png")
    image_base.save("base.png")
    image_col.save("color.png")
    image_debug.save("debug.png")

if __name__ == "__main__":
    main()
