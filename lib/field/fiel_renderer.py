import cv2 as cv


class FieldRenderer:
    def __init__(self, field, iters_per_gen=300):
        self.image = cv.imread("image.jpg")
        self.field = field
        self.image = cv.resize(self.image, (self.field.size_x, self.field.size_y), cv.INTER_NEAREST)
        self.height, self.width, c = self.image.shape
        self.iters_per_gen = iters_per_gen

    def draw_border(self):
        for x in range(self.field.size_x):
            self.image[0, x] = (127, 127, 127)
            self.image[self.width - 1, x] = (127, 127, 127)

        for y in range(self.field.size_y):
            self.image[y, 0] = (127, 127, 127)
            self.image[y, self.height - 1] = (127, 127, 127)

    def next_iter(self):
        self.field.next_iter()
        for y in range(1, self.field.size_y - 1):
            for x in range(1, self.field.size_x - 1):
                if self.field.board[y][x] == 0:
                    self.image[x, y] = (255, 255, 255)
                else:
                    self.image[x, y] = (0, 0, 0)
        # print(*self.field.board, sep='\n')
        # exit(0)

    def start_loop(self):
        self.draw_border()
        i = 0
        while True:
            i += 1
            self.field.next_iter()
            self.next_iter()
            width = self.width * 2
            height = self.height * 2
            dim = (width, height)
            cv.imshow('animation', cv.resize(self.image, dim, cv.INTER_AREA))
            if i >= self.iters_per_gen:
                self.field.next_gen()
                i = 0
            if cv.waitKey(1) == ord('q'):
                # press q to terminate the loop
                cv.destroyAllWindows()
                break
