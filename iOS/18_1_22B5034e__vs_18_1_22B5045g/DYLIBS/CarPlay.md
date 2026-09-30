## CarPlay

> `/System/Library/Frameworks/CarPlay.framework/CarPlay`

```diff

-337.3.0.0.0
-  __TEXT.__text: 0x3daf0
+337.5.1.0.0
+  __TEXT.__text: 0x3f2ac
   __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_methlist: 0x53c0
-  __TEXT.__const: 0x1e8
-  __TEXT.__cstring: 0x3266
-  __TEXT.__oslogstring: 0x1b36
+  __TEXT.__objc_methlist: 0x55a8
+  __TEXT.__const: 0x1f0
+  __TEXT.__cstring: 0x33e7
+  __TEXT.__oslogstring: 0x1b5d
   __TEXT.__gcc_except_tab: 0x790
-  __TEXT.__unwind_info: 0x1410
-  __TEXT.__objc_classname: 0xdc7
-  __TEXT.__objc_methname: 0xcbc7
-  __TEXT.__objc_methtype: 0x2032
-  __TEXT.__objc_stubs: 0x7f80
-  __DATA_CONST.__got: 0x548
-  __DATA_CONST.__const: 0x1880
-  __DATA_CONST.__objc_classlist: 0x2a0
-  __DATA_CONST.__objc_catlist: 0x30
+  __TEXT.__unwind_info: 0x1478
+  __TEXT.__objc_classname: 0xe11
+  __TEXT.__objc_methname: 0xd011
+  __TEXT.__objc_methtype: 0x2060
+  __TEXT.__objc_stubs: 0x8280
+  __DATA_CONST.__got: 0x580
+  __DATA_CONST.__const: 0x1940
+  __DATA_CONST.__objc_classlist: 0x2b0
+  __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b18
+  __DATA_CONST.__objc_selrefs: 0x2c00
   __DATA_CONST.__objc_protorefs: 0x100
-  __DATA_CONST.__objc_superrefs: 0x210
+  __DATA_CONST.__objc_superrefs: 0x218
   __AUTH_CONST.__auth_got: 0x318
-  __AUTH_CONST.__const: 0x7c0
-  __AUTH_CONST.__cfstring: 0x3540
-  __AUTH_CONST.__objc_const: 0x195c8
+  __AUTH_CONST.__const: 0x7e0
+  __AUTH_CONST.__cfstring: 0x3800
+  __AUTH_CONST.__objc_const: 0x19b30
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_ivar: 0x680
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x6a4
   __DATA.__data: 0x18c0
-  __DATA.__bss: 0x198
+  __DATA.__bss: 0x1a8
   __DATA_DIRTY.__objc_data: 0x1a40
   __DATA_DIRTY.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2079
-  Symbols:   2499
-  CStrings:  3203
+  Functions: 2122
+  Symbols:   2550
+  CStrings:  3281
 
Symbols:
+ _NSStringFromCPStopType
+ _OBJC_CLASS_$_NSUnitPower
+ _OBJC_CLASS_$_NSUnitEnergy
+ _OBJC_METACLASS_$_CPElectricVehicleWaypoint
+ _OBJC_CLASS_$_NSMeasurementFormatter
+ _OBJC_CLASS_$_NSUnitConverterLinear
+ _OBJC_CLASS_$_CPChargingStationConnector
+ _OBJC_CLASS_$_NSUnitElectricPotentialDifference
+ _OBJC_METACLASS_$_CPChargingStationConnector
+ _NSStringFromCPChargingStationConnectorType
+ _OBJC_CLASS_$_CPElectricVehicleWaypoint
CStrings:
+ "TQ,R,N,V_type"
+ "setArrivalBatteryLevel:"
+ "setConnectors:"
+ "setUnitStyle:"
+ "setChargePrecondition:"
+ "voltage"
+ "_electricVehicleDestination"
+ "T@\"CPElectricVehicleWaypoint\",C,N"
+ "T@\"NSUnitEnergy\",R,C"
+ "FinalWaypointBatteryLevel"
+ "chargePrecondition"
+ "connectors"
+ "setDepartureBatteryLevel:"
+ "CPChargingStationConnector"
+ "_finalWaypointBatteryLevel"
+ "DepartureBatteryLevel"
+ "finalWaypointBatteryLevel"
+ "v32@?0@8@16^B24"
+ "<%!@(MISSING): %!p(MISSING) connectors=[%!@(MISSING)] batteryLevel(arrival=%!@(MISSING) departure=%!@(MISSING) finalWaypoint=%!@(MISSING))>>"
+ "T@\"NSMeasurement\",R,N,V_power"
+ "setUnitOptions:"
+ "type"
+ "setStopType:"
+ "T@\"CPElectricVehicleWaypoint\",C,N,V_electricVehicleDestination"
+ "@\"CPElectricVehicleWaypoint\""
+ "initWithType:voltage:power:"
+ "_arrivalBatteryLevel"
+ "initWithSymbol:converter:"
+ "T@\"NSArray\",C,N,V_connectors"
+ "T@\"NSMeasurement\",&,N,V_finalWaypointBatteryLevel"
+ "setElectricVehicleDestination:"
+ "CCS2"
+ "ChargeStation_ChargingUncertain"
+ "electricVehicleDestination"
+ "stopType"
+ "Setting ChargePrecondition: %!{(MISSING)public}@"
+ "setFinalWaypointBatteryLevel:"
+ "ArrivalBatteryLevel"
+ "T@\"NSMeasurement\",R,N,V_voltage"
+ "CCS1"
+ "CHAdeMO"
+ "_stopType"
+ "departureBatteryLevel"
+ "initWithCoefficient:"
+ "ChargeStation"
+ "NACS_DC"
+ "volts"
+ "_voltage"
+ "power"
+ "_type"
+ "_connectors"
+ "@40@0:8Q16@24@32"
+ "Wh"
+ "GBT_AC"
+ "arrivalBatteryLevel"
+ "ChargingStationVoltage"
+ "T@\"NSMeasurement\",&,N,V_arrivalBatteryLevel"
+ "wattHours"
+ "watts"
+ "initWithCarSessionStatus:delegate:"
+ "Unclassified"
+ "_power"
+ "ChargeStation_ChargingExpected"
+ "ChargingStationPower"
+ "3\x12\x17"
+ "NACS_AC"
+ "J1772"
+ "CPElectricVehicleWaypoint"
+ "_valueFromDictionary:forParamKey:"
+ "T@\"NSMeasurement\",&,N,V_departureBatteryLevel"
+ "StopType"
+ "stringFromMeasurement:"
+ "_valueFromChargePrecondition:forParamKey:"
+ "Mennekes"
+ "GBT_DC"
+ "(%!@(MISSING) %!@(MISSING) %!@(MISSING))"
+ "CPChargePrecondition"
+ "TC,N,V_stopType"
+ "_departureBatteryLevel"
- "3\x12\x16"

```
