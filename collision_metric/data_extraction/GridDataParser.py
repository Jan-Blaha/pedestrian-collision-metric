

class GridDataParser:
    def __init__(self, path):
        self.path = path
        self.f = open(path, "r")

    def generator(self):
        for line in self.f:
            line = line.strip('\n')
            line = line.strip('\r')  # if someone ends a "WindowsLineEnded" document
            line = line.split(':')
            yield (
                # position coords
                (
                    int(line[0]),
                    int(line[1])
                ),
                # values at position
                [float(i) for i in line[2:]]
            )

    def __del__(self):
        self.f.close()
