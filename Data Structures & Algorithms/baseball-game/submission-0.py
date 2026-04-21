class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record, output = [], 0
        index = 0

        for i in range(len(operations)):
            c = operations[i]

            match c:
                case "+":
                    curSum = int(record[index-1]) + int(record[index-2])
                    record.append(curSum)
                    index += 1
                case "D":
                    product = 2 * int(record[index-1])
                    record.append(product)
                    index += 1
                case "C":
                    record.pop()
                    index -= 1
                case _:
                    record.append(int(operations[i]))
                    index += 1
        for num in record:
            output += num

        return output