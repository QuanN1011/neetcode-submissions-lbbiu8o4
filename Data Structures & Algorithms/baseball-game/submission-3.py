class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record, output = [], 0

        for op in operations:
            match op:
                case "+":
                    record.append(record[-1] + record[-2])
                case "D":
                    record.append(2 * record[-1])
                case "C":
                    record.pop()
                case _:
                    record.append(int(op))
        return sum(record)