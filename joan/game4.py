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
    l = pixels[i + 3, j]
    r = pixels[i + 3, j + 7]
    t = pixels[i, j + 3]
    b = pixels[i + 7, j + 3]
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

    for i in range(col_b):
        for j in range(row_b):
            if blocks[i][j].t == col:
                print("Found at: ", i, j)
                return blocks[i][j]


def main():
    im = Image.open("puzzle.png")
    col, row = im.size
    pixels = im.load()
    block_cols = int(col / 8)
    block_rows = int(row / 8)

    blocks = []

    for i in range(0, row, 8):
        aux = []
        for j in range(0, col, 8):
            r = int(i / 8)
            c = int(j / 8)
            aux.append(create_block(pixels, i, j))
        blocks.append(aux)

    solution = []
    pixels = []
    image = Image.new('RGB', (block_rows, block_cols))
    imageBase = Image.new('RGB', (block_rows, block_cols))

    for i in range(block_cols):
        aux = []
        for j in range(block_rows):
            aux_sol = None
            print("Finding: ", i, j)
            if i < 8 and j < 8:
                print("Base block")
                aux_sol = blocks[i][j]
            else:
                if i < 8:
                    aux_sol = find_solution_left(aux[j - 1], blocks)
                else:
                    aux_sol = find_solution_top(solution[i - 1][j], blocks)
            aux.append(aux_sol)
            image.putpixel((j, i), aux_sol.c)
            imageBase.putpixel((j, i), blocks[i][j].c)
        solution.append(aux)

    image.save("prova.png")
    imageBase.save("base.png")

if __name__ == "__main__":
    main()
