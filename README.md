# HeaterStartParallelizer
Cura plugin to start your bed and extruder heater in parallel. The extruder will start heating when the bed temperature reaches a specified offset from the target bed temperature. This allows for a timing so that both extruder and bed reaches their target temperatures at roughly the same time instead of the default behavior of waiting for the bed to reach temperature before starting the extruder heating.

Usage
==========
Specify a temperature offset from the target bed temperature that will start the extruder heater. The trick is to find an offset so that both will reach printing temps at about the same time (like the example image below) with your typical print temperatures. If the target bed temp is 65C and the offset is set to 10C, then the extruder heater will start heating at 55C.

![](https://raw.githubusercontent.com/mosh1/HeaterStartParallelizer/master/Example.jpg)
Installation
==========
Add to Cura as a plugin:

1. Open Cura
2. Go to the Plugins tab
3. Click on "Open plugin location"
4. Drag HeaterStartParallelizer.py into plugin location (or copy to ~/.cura/plugins for OSX)
5. Restart Cura
