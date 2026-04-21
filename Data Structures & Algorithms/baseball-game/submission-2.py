class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record, output = [], 0

        for op in operations:
            match op:
                case "+":
                    record.append(int(record[-1]) + int(record[-2]))
                case "D":
                    record.append(2 * int(record[-1]))
                case "C":
                    record.pop()
                case _:
                    record.append(int(op))

        for num in record:
            output += num

        return output