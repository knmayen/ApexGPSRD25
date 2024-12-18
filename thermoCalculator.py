homeworks = [98, 98, 81, 90, 96.5, 100, 99, 100, 92, 84.5, 92.75]
exam1 = 82 / 100
exam2 = 47.5 * 2 / 100
final = 62 / 70
attendace = 20

homeworks.sort()
homeworks.pop(0)
print(homeworks)
HWavg = sum(homeworks) / 100 / len(homeworks)
# print(HWavg)

course = .25 * HWavg + .20 * exam1 + .25 * exam2 + .30 * final
print(course)