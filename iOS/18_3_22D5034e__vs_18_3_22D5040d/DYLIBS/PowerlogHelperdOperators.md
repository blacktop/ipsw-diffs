## PowerlogHelperdOperators

> `/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`

```diff

-2308.80.15.502.1
-  __TEXT.__text: 0x1d2470
+2308.80.23.0.0
+  __TEXT.__text: 0x1d2e8c
   __TEXT.__auth_stubs: 0x1d40
-  __TEXT.__objc_methlist: 0xdf3c
+  __TEXT.__objc_methlist: 0xdf6c
   __TEXT.__const: 0x5f0
-  __TEXT.__cstring: 0x2460f
-  __TEXT.__oslogstring: 0x12722
-  __TEXT.__gcc_except_tab: 0x25d0
+  __TEXT.__cstring: 0x2489e
+  __TEXT.__oslogstring: 0x12744
+  __TEXT.__gcc_except_tab: 0x260c
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x3738
+  __TEXT.__unwind_info: 0x3748
   __TEXT.__objc_classname: 0xb9a
-  __TEXT.__objc_methname: 0x30016
-  __TEXT.__objc_methtype: 0x26de
-  __TEXT.__objc_stubs: 0x1da00
-  __DATA_CONST.__got: 0xe50
-  __DATA_CONST.__const: 0x43c0
+  __TEXT.__objc_methname: 0x300b3
+  __TEXT.__objc_methtype: 0x26f2
+  __TEXT.__objc_stubs: 0x1daa0
+  __DATA_CONST.__got: 0xe58
+  __DATA_CONST.__const: 0x43e8
   __DATA_CONST.__objc_classlist: 0x308
   __DATA_CONST.__objc_nlclslist: 0x110
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x91f0
+  __DATA_CONST.__objc_selrefs: 0x9218
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x290
   __DATA_CONST.__objc_arraydata: 0x15828
   __AUTH_CONST.__auth_got: 0xeb8
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x1800
-  __AUTH_CONST.__cfstring: 0x317e0
+  __AUTH_CONST.__cfstring: 0x319c0
   __AUTH_CONST.__objc_const: 0x12578
   __AUTH_CONST.__objc_intobj: 0x2838
   __AUTH_CONST.__objc_dictobj: 0x3340

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 7753
-  Symbols:   10768
-  CStrings:  15906
+  Functions: 7760
+  Symbols:   10776
+  CStrings:  15928
 
Symbols:
+ _OBJC_CLASS_$_PLFileStats
CStrings:
+ "@48@0:8@16@24@32d40"
+ "BHUIVisitsLastHour"
+ "BHUIVisitsToday"
+ "BHUIVisitsTotal"
+ "BUIVisits=%@, totalLogDuration=%f"
+ "BUIVisitsLastHour"
+ "BUIVisitsToday"
+ "BUIVisitsTotal"
+ "ChargingUIVisitsLastHour"
+ "ChargingUIVisitsToday"
+ "ChargingUIVisitsTotal"
+ "LogDuration"
+ "SELECT Visit, COUNT(*) AS Count FROM PLBatteryAgent_EventPoint_BatteryUIVisit GROUP BY Visit;"
+ "SELECT Visit, COUNT(*) AS Count FROM PLBatteryAgent_EventPoint_BatteryUIVisit WHERE timestamp > ((SELECT MAX(timestamp) FROM PLBatteryAgent_EventBackward_Battery)-3600) GROUP BY Visit;"
+ "SELECT Visit, COUNT(*) AS Count FROM PLBatteryAgent_EventPoint_BatteryUIVisit WHERE timestamp > ((SELECT MAX(timestamp) FROM PLBatteryAgent_EventBackward_Battery)-86400) GROUP BY Visit;"
+ "TKRP"
+ "aggregateBUIVisitData:withBUIVisitsToday:andBUIVisitsLastHour:andTotalLogDuration:"
+ "ftD1"
+ "getBUIVisitsLastHour"
+ "getBUIVisitsToday"
+ "getBUIVisitsTotal"
+ "totalLogDuration"

```
