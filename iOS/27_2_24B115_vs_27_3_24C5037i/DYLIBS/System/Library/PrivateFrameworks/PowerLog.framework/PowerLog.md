## PowerLog

> `/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog`

```diff

-3486.42.1.0.0
-  __TEXT.__text: 0x1e8b4
+3486.60.36.0.0
+  __TEXT.__text: 0x1eff0
   __TEXT.__objc_methlist: 0x150c
-  __TEXT.__const: 0xf78
+  __TEXT.__const: 0xfa0
   __TEXT.__gcc_except_tab: 0x6a0
-  __TEXT.__cstring: 0x2420
-  __TEXT.__oslogstring: 0x3a4a
-  __TEXT.__unwind_info: 0xaf0
+  __TEXT.__cstring: 0x24a8
+  __TEXT.__oslogstring: 0x3b06
+  __TEXT.__unwind_info: 0xb10
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_arraydata: 0x198
   __DATA_CONST.__got: 0x1c8
   __AUTH_CONST.__const: 0x560
-  __AUTH_CONST.__cfstring: 0x29e0
+  __AUTH_CONST.__cfstring: 0x2a60
   __AUTH_CONST.__objc_const: 0x22c8
   __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_arrayobj: 0x120

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 838
-  Symbols:   1233
-  CStrings:  689
+  Functions: 846
+  Symbols:   1239
+  CStrings:  697
 
Symbols:
+ _PLConfigureBUIQueryDailyDrainInformation
+ _PLConfigureBUIQueryHourlyChargingInformation
+ ___PLConfigureBUIQueryDailyDrainInformation_block_invoke
+ ___PLConfigureBUIQueryHourlyChargingInformation_block_invoke
+ _dailyDrainInformation
+ _hourlyChargingInformation
CStrings:
+ "MergedDailyDrainInformation"
+ "MergedHourlyChargingInformation"
+ "PLBatteryUIDailyDrainInformationKey"
+ "PLBatteryUIHourlyChargingInformationKey"
+ "invalid queryResult, no daily drain information"
+ "invalid queryResult, no hourly charging information"
+ "returning daily drain information=%@"
+ "returning hourly charging information for %lu days"
```
