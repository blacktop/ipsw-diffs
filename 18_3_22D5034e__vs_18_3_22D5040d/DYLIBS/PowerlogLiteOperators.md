## PowerlogLiteOperators

> `/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`

```diff

-2308.80.15.502.1
-  __TEXT.__text: 0x44746c
+2308.80.23.0.0
+  __TEXT.__text: 0x447e88
   __TEXT.__auth_stubs: 0x2e80
-  __TEXT.__objc_methlist: 0x23cb4
+  __TEXT.__objc_methlist: 0x23ce4
   __TEXT.__const: 0x1398
   __TEXT.__swift5_typeref: 0x33c
   __TEXT.__constg_swiftt: 0x1ac
   __TEXT.__swift5_reflstr: 0x179
   __TEXT.__swift5_fieldmd: 0x200
-  __TEXT.__cstring: 0x7d39b
+  __TEXT.__cstring: 0x7d756
   __TEXT.__swift5_proto: 0x74
   __TEXT.__swift5_types: 0x20
-  __TEXT.__oslogstring: 0xf8f0
+  __TEXT.__oslogstring: 0xf912
   __TEXT.__swift5_capture: 0x80
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__gcc_except_tab: 0x287c
+  __TEXT.__gcc_except_tab: 0x28b8
   __TEXT.__ustring: 0x22
-  __TEXT.__unwind_info: 0x6ac8
+  __TEXT.__unwind_info: 0x6ad8
   __TEXT.__eh_frame: 0x6e8
   __TEXT.__objc_classname: 0x1897
-  __TEXT.__objc_methname: 0x5cb25
-  __TEXT.__objc_methtype: 0x6f14
-  __TEXT.__objc_stubs: 0x31880
-  __DATA_CONST.__got: 0x1800
-  __DATA_CONST.__const: 0x8e50
+  __TEXT.__objc_methname: 0x5cbc2
+  __TEXT.__objc_methtype: 0x6f28
+  __TEXT.__objc_stubs: 0x31920
+  __DATA_CONST.__got: 0x1808
+  __DATA_CONST.__const: 0x8ea8
   __DATA_CONST.__objc_classlist: 0x798
   __DATA_CONST.__objc_nlclslist: 0x250
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x126a8
+  __DATA_CONST.__objc_selrefs: 0x126d0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x898
   __DATA_CONST.__objc_arraydata: 0x15b30
   __AUTH_CONST.__auth_got: 0x1758
-  __AUTH_CONST.__auth_ptr: 0x270
+  __AUTH_CONST.__auth_ptr: 0x268
   __AUTH_CONST.__const: 0x1ca0
-  __AUTH_CONST.__cfstring: 0x6c040
+  __AUTH_CONST.__cfstring: 0x6c4e0
   __AUTH_CONST.__objc_const: 0x2d138
   __AUTH_CONST.__objc_intobj: 0x7218
   __AUTH_CONST.__objc_dictobj: 0x4d80

   __AUTH.__objc_data: 0x1280
   __AUTH.__data: 0xae8
   __DATA.__objc_ivar: 0x1414
-  __DATA.__data: 0xef8
+  __DATA.__data: 0xfc8
   __DATA.__bss: 0x1190
   __DATA.__common: 0x188
   __DATA_DIRTY.__objc_ivar: 0x1674

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 16283
-  Symbols:   20571
-  CStrings:  34553
+  Functions: 16290
+  Symbols:   20611
+  CStrings:  34597
 
Symbols:
+ _OBJC_CLASS_$_PLFileStats
+ _kAct
+ _kConfig
+ _kDataPower
+ _kGsmCs
+ _kSleep
+ _kVoicePower
+ _kcc_activated_0
+ _kcc_activated_1
+ _kcc_activated_2
+ _kcc_activated_3
+ _kcc_activated_4
+ _kcc_activated_5
+ _kcc_activated_6
+ _kcc_configured_0
+ _kcc_configured_1
+ _kcc_configured_2
+ _kcc_configured_3
+ _kcc_configured_4
+ _kcc_configured_5
+ _kcc_configured_6
+ _kcc_configured_7
+ _kcc_configured_8
+ _kcc_configured_9
+ _kdirtecion_0
+ _kdirtecion_1
+ _kdirtecion_2
+ _kdirtecion_3
+ _kdirtecion_4
+ _kdirtecion_5
+ _kdirtecion_6
+ _kdirtecion_7
+ _kdirtecion_8
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
+ "DATA_POWER"
+ "GSM_CS"
+ "SELECT Visit, COUNT(*) AS Count FROM PLBatteryAgent_EventPoint_BatteryUIVisit GROUP BY Visit;"
+ "SELECT Visit, COUNT(*) AS Count FROM PLBatteryAgent_EventPoint_BatteryUIVisit WHERE timestamp > ((SELECT MAX(timestamp) FROM PLBatteryAgent_EventBackward_Battery)-3600) GROUP BY Visit;"
+ "SELECT Visit, COUNT(*) AS Count FROM PLBatteryAgent_EventPoint_BatteryUIVisit WHERE timestamp > ((SELECT MAX(timestamp) FROM PLBatteryAgent_EventBackward_Battery)-86400) GROUP BY Visit;"
+ "TKRP"
+ "VOICE_POWER"
+ "act"
+ "aggregateBUIVisitData:withBUIVisitsToday:andBUIVisitsLastHour:andTotalLogDuration:"
+ "cc_activated_0"
+ "cc_activated_1"
+ "cc_activated_2"
+ "cc_activated_3"
+ "cc_activated_4"
+ "cc_activated_5"
+ "cc_activated_6"
+ "cc_configured_0"
+ "cc_configured_1"
+ "cc_configured_2"
+ "cc_configured_3"
+ "cc_configured_4"
+ "cc_configured_5"
+ "cc_configured_6"
+ "cc_configured_7"
+ "cc_configured_8"
+ "cc_configured_9"
+ "config"
+ "ftD1"
+ "getBUIVisitsLastHour"
+ "getBUIVisitsToday"
+ "getBUIVisitsTotal"
+ "sleep"
+ "totalLogDuration"

```
