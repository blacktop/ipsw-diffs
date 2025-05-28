## PerfPowerServicesMetadata

> `/System/Library/PrivateFrameworks/PerfPowerServicesMetadata.framework/PerfPowerServicesMetadata`

```diff

-1787.40.67.0.0
-  __TEXT.__text: 0x1c084
+1787.60.31.0.0
+  __TEXT.__text: 0x1c7dc
   __TEXT.__auth_stubs: 0x570
-  __TEXT.__objc_methlist: 0x1a08
+  __TEXT.__objc_methlist: 0x1a10
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0xde9
+  __TEXT.__cstring: 0xeaa
   __TEXT.__oslogstring: 0x109c
   __TEXT.__gcc_except_tab: 0xd4
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x5e8
+  __TEXT.__unwind_info: 0x5ec
   __TEXT.__objc_classname: 0x2b2
-  __TEXT.__objc_methname: 0x23d5
-  __TEXT.__objc_methtype: 0x4ac
-  __TEXT.__objc_stubs: 0x2560
+  __TEXT.__objc_methname: 0x2409
+  __TEXT.__objc_methtype: 0x4bd
+  __TEXT.__objc_stubs: 0x2580
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0x180
   __DATA_CONST.__objc_classlist: 0x130

   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x2238
-  __DATA_CONST.__objc_selrefs: 0xbd0
+  __DATA_CONST.__objc_selrefs: 0xbd8
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__cfstring: 0x1dc0
+  __AUTH_CONST.__cfstring: 0x1f80
   __AUTH_CONST.__const: 0x3e0
   __AUTH_CONST.__objc_const: 0xdc8
   __AUTH_CONST.__objc_intobj: 0x48

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 724
-  Symbols:   2338
-  CStrings:  986
+  Functions: 725
+  Symbols:   2341
+  CStrings:  1002
 
Symbols:
+ +[PPSBatteryMetrics smartChargingMetrics]
+ +[PPSDisplayMetrics displayMetricsWithStorage:timeToLive:category:]
+ _objc_msgSend$displayMetricsWithStorage:timeToLive:category:
+ _objc_msgSend$smartChargingMetrics
- +[PPSDisplayMetrics displayMetrics]
- _objc_msgSend$displayMetrics
CStrings:
+ "@32@0:8i16I20@24"
+ "Detected"
+ "DisplayStateExtended"
+ "FullyCharged"
+ "IdlePeriodSocCeiling"
+ "IdlePeriodSocFloor"
+ "IdlePeriodStart"
+ "Interrupted"
+ "Override"
+ "SmartCharging"
+ "TopOff"
+ "TopOffWithoutIdle"
+ "UserOverride"
+ "checkpoint"
+ "displayMetricsWithStorage:timeToLive:category:"
+ "isEngaged"
+ "smartChargingMetrics"
- "displayMetrics"

```
