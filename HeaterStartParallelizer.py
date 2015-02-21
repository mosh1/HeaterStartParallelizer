#Name: Heater Start Parallelizer
#Info: Start extruder heating at specified temperature offset from target bed temperature.
#Depend: GCode
#Type: postprocess
#Param: startExtruderOffset(float:0) Temp offset (C)

import re

bedTargetTemp = 0
extruderTargetTemp = 0

def getValue(line, key, default = None):
	if not key in line or (';' in line and line.find(key) > line.find(';')):
		return default
	subPart = line[line.find(key) + 1:]
	m = re.search('^[0-9]+\.?[0-9]*', subPart)
	if m is None:
		return default
	try:
		return float(m.group(0))
	except:
		return default

with open(filename, "r") as f:
	lines = f.readlines()

# Find target extruder temp
for line in lines:
	if getValue(line, 'M', None) == 109:
		extruderTargetTemp = int(getValue(line, 'S', None))
		break

# if startHeatOffset > 0 and extruderTargetTemp > 0:
with open(filename, "w") as f:
	for line in lines:
		if getValue(line, 'M', None) == 190:
			targetBedTemp = getValue(line, 'S', None)
			offsetBedTemp = targetBedTemp - startExtruderOffset
			if startExtruderOffset > 0 and offsetBedTemp > 0:
				f.write("; Start extruder heater %i degrees before target bed temperature\n" % (startExtruderOffset))
				f.write("M190 S" + str(offsetBedTemp) + "\n")
				f.write("M104 S" + str(extruderTargetTemp) + "\n")
		f.write(line)