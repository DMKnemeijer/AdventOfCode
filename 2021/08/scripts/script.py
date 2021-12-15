from aoc import aoc


class SevenSegDisplay:
    def __init__(self, definition: str):
        self._signal, self._output = self.split_signal_output(definition)
        self._mapping = {
            0: '',
            1: list([x for x in self._signal if len(x) == 2][0]),
            2: '',
            3: '',
            4: list([x for x in self._signal if len(x) == 4][0]),
            5: '',
            6: '',
            7: list([x for x in self._signal if len(x) == 3][0]),
            8: list([x for x in self._signal if len(x) == 7][0]),
            9: ''
        }
        self.construct_mapping()
        self._answer = self._get_answer()
        self._unique_seg_amount_in_output = self._get_unique_segments()

    @property
    def answer(self) -> int:
        return self._answer

    @answer.setter
    def answer(self, answer: int):
        self._answer = answer

    @property
    def unique_segs(self) -> int:
        return self._unique_seg_amount_in_output

    @unique_segs.setter
    def unique_segs(self, unique_segs: int):
        self._unique_seg_amount_in_output = unique_segs

    @staticmethod
    def split_signal_output(line: str) -> (list[str], list[str]):
        return line.split(' | ')[0].split(), line.split(' | ')[1].split()

    def construct_mapping(self):
        self._mapping[3] = self.find_three()
        self._mapping[9] = self.find_nine()
        self._mapping[0] = self.find_zero()
        self._mapping[6] = self.find_six()
        self._mapping[5] = self.find_five()
        self._mapping[2] = self.find_two()

    def _all_in_map(self, sig: str, num: int) -> bool:
        return all(x in sig for x in self._mapping[num])

    def find_three(self) -> list[str]:
        for s in self._signal:
            if len(s) == 5 and self._all_in_map(s, 1):
                return list(s)

    def find_nine(self) -> list[str]:
        return list(set(self._mapping[3] + self._mapping[4]))

    def find_zero(self) -> list[str]:
        for s in self._signal:
            if len(s) == 6 and self._all_in_map(s, 1) and not self._all_in_map(s, 9):
                return list(s)

    def find_six(self) -> list[str]:
        for s in self._signal:
            if len(s) == 6 and not self._all_in_map(s, 0) and not self._all_in_map(s, 9):
                return list(s)

    def find_five(self) -> list[str]:
        for s in self._signal:
            if len(s) == 5 and not self._all_in_map(s, 3) and set(s).issuperset(
                    set(self._mapping[4]) - set(self._mapping[1])):
                return list(s)

    def find_two(self) -> list[str]:
        for s in self._signal:
            if len(s) == 5 and not self._all_in_map(s, 3) and not self._all_in_map(s, 5):
                return list(s)

    def _get_answer(self) -> int:
        answer = ''
        for o in self._output:
            for k, v in self._mapping.items():
                if set(o) == set(v):
                    answer += str(k)
        aoc.logger(f"Answer = {answer}")
        return int(answer)

    def _get_unique_segments(self) -> int:
        answer = ''
        unique_segments = [1, 4, 7, 8]
        for o in self._output:
            for k, v in {key: self._mapping[key] for key in unique_segments}.items():
                if set(o) == set(v):
                    answer += str(k)
        return len(answer)


input = aoc.read_input('../input/in.txt')

displays = [SevenSegDisplay(definition=line) for line in input]

print(sum([d.answer for d in displays]))
print(sum([d.unique_segs for d in displays]))
