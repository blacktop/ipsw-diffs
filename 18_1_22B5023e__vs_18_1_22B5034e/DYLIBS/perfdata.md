## perfdata

> `/System/Library/PrivateFrameworks/perfdata.framework/perfdata`

```diff

-119.0.0.0.0
-  __TEXT.__text: 0x7658
+121.0.0.0.0
+  __TEXT.__text: 0x75e4
   __TEXT.__auth_stubs: 0x760
   __TEXT.__objc_methlist: 0x680
-  __TEXT.__const: 0x68
-  __TEXT.__cstring: 0xef9
-  __TEXT.__gcc_except_tab: 0x44
-  __TEXT.__unwind_info: 0x220
+  __TEXT.__const: 0x60
+  __TEXT.__cstring: 0xfe8
+  __TEXT.__gcc_except_tab: 0x14
+  __TEXT.__unwind_info: 0x210
   __TEXT.__objc_classname: 0x73
-  __TEXT.__objc_methname: 0x1286
+  __TEXT.__objc_methname: 0x12a0
   __TEXT.__objc_methtype: 0x208
-  __TEXT.__objc_stubs: 0x10a0
-  __DATA_CONST.__got: 0xb0
+  __TEXT.__objc_stubs: 0x10e0
+  __DATA_CONST.__got: 0xc8
   __DATA_CONST.__const: 0xe80
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x510
+  __DATA_CONST.__objc_selrefs: 0x520
   __DATA_CONST.__objc_superrefs: 0x20
   __AUTH_CONST.__auth_got: 0x3c0
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x40
+  __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0xa60
   __AUTH_CONST.__objc_const: 0xbb0
   __DATA.__objc_ivar: 0xb8

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libIOReport.dylib
   - /usr/lib/libMobileGestalt.dylib
+  - /usr/lib/libSMC.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 229
-  Symbols:   845
-  CStrings:  711
+  Functions: 227
+  Symbols:   843
+  CStrings:  727
 
Symbols:
+ _IOPSGetPowerSourceDescription
+ _SMCReadKeyAsNumeric
+ _SMCOpenConnection
+ _IOPSCopyPowerSourcesByTypePrecise
+ _CFArrayGetCount
+ _CFArrayGetValueAtIndex
+ _SMCCloseConnection
+ _IOPSCopyPowerSourcesList
- _IOReportSimpleGetIntegerValue
- _IOReportChannelGetChannelName
- _IOReportCopyChannelsInGroup
- _IOReportCreateSubscription
- _CFEqual
- _IOReportPrune
- _IOReportCreateSamples
- _IOReportIterate
CStrings:
+ "not-determinable"
+ "unknown"
+ "peak-power-capacity"
+ "nominal-charge-capacity"
+ "battery_max_capacity_percent"
+ "Battery Service State"
+ "replace"
+ "battery_cycle_count"
+ "battery_service_state"
+ "Maximum Capacity Percent"
+ "none"
+ "121"
+ "charge-discharge-cycled"
+ "battery_count"
+ "intValue"
+ "AppleSMC"
+ "battery_service_needed"
+ "data-not-migrated"
+ "unnamed"
+ "nominal-charge-peak-power"
+ "unsignedIntValue"
- "Battery"
- "i16@?0^{__CFDictionary=}8"
- "BatteryMaxRa0-8"
- "119"
- "max_battery_resistance_milliohms"

```
