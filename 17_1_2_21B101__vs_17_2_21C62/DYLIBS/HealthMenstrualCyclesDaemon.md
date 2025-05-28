## HealthMenstrualCyclesDaemon

> `/System/Library/PrivateFrameworks/HealthMenstrualCyclesDaemon.framework/HealthMenstrualCyclesDaemon`

```diff

-4146.1.11.3.0
-  __TEXT.__text: 0x3d770
+4146.2.12.1.3
+  __TEXT.__text: 0x3ddc4
   __TEXT.__auth_stubs: 0xad0
-  __TEXT.__objc_methlist: 0x26b4
+  __TEXT.__objc_methlist: 0x272c
   __TEXT.__const: 0xd8
   __TEXT.__cstring: 0x29ba
   __TEXT.__gcc_except_tab: 0x9e8
-  __TEXT.__oslogstring: 0x4bdd
-  __TEXT.__unwind_info: 0xbc4
-  __TEXT.__objc_classname: 0x9e0
-  __TEXT.__objc_methname: 0xf748
+  __TEXT.__oslogstring: 0x4ccf
+  __TEXT.__unwind_info: 0xbd4
+  __TEXT.__objc_classname: 0x9e1
+  __TEXT.__objc_methname: 0xf976
   __TEXT.__objc_methtype: 0x1354
-  __TEXT.__objc_stubs: 0x90a0
-  __DATA_CONST.__got: 0x3a0
+  __TEXT.__objc_stubs: 0x9220
+  __DATA_CONST.__got: 0x3c0
   __DATA_CONST.__const: 0xed0
   __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4970
-  __DATA_CONST.__objc_selrefs: 0x26f8
+  __DATA_CONST.__objc_const: 0x4a60
+  __DATA_CONST.__objc_selrefs: 0x2758
   __DATA_CONST.__objc_arraydata: 0xb0
-  __AUTH_CONST.__objc_intobj: 0x2b8
+  __AUTH_CONST.__objc_intobj: 0x318
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__cfstring: 0x20c0
   __AUTH_CONST.__objc_const: 0x14b0

   __AUTH.__objc_data: 0x140
   __DATA.__objc_classrefs: 0x4e8
   __DATA.__objc_superrefs: 0x140
-  __DATA.__objc_ivar: 0x470
+  __DATA.__objc_ivar: 0x484
   __DATA.__data: 0x9c0
   __DATA_DIRTY.__objc_data: 0xc30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1140
-  Symbols:   4785
-  CStrings:  2542
+  Functions: 1155
+  Symbols:   4836
+  CStrings:  2567
 
Symbols:
+ -[HDMCDailyAnalytics _collectSensitiveFieldsForMetric:settingsManager:menstrualCyclesSettings:heartRateInputFeatureStatus:deviationDetectionSettings:wristTemperatureInputFeatureStatus:gregorianCalendar:error:].cold.18
+ -[HDMCDailyAnalytics _collectSensitiveFieldsForMetric:settingsManager:menstrualCyclesSettings:heartRateInputFeatureStatus:deviationDetectionSettings:wristTemperatureInputFeatureStatus:gregorianCalendar:error:].cold.19
+ -[HDMCDailyAnalytics _collectSensitiveFieldsForMetric:settingsManager:menstrualCyclesSettings:heartRateInputFeatureStatus:deviationDetectionSettings:wristTemperatureInputFeatureStatus:gregorianCalendar:error:].cold.20
+ -[HDMCDailyMetric countPairedWatch]
+ -[HDMCDailyMetric countPairediPad]
+ -[HDMCDailyMetric countPairediPhone]
+ -[HDMCDailyMetric isSleepScheduleEnabled]
+ -[HDMCDailyMetric isSleepScreenEnabled]
+ -[HDMCDailyMetric setCountPairedWatch:]
+ -[HDMCDailyMetric setCountPairediPad:]
+ -[HDMCDailyMetric setCountPairediPhone:]
+ -[HDMCDailyMetric setIsSleepScheduleEnabled:]
+ -[HDMCDailyMetric setIsSleepScreenEnabled:]
+ _HKAnalyticsPropertyNameDeviceContextCountPhone
+ _HKAnalyticsPropertyNameDeviceContextCountWatch
+ _HKAnalyticsPropertyNameDeviceContextCountiPad
+ _HKLogSync
+ _OBJC_IVAR_$_HDMCDailyMetric._countPairedWatch
+ _OBJC_IVAR_$_HDMCDailyMetric._countPairediPad
+ _OBJC_IVAR_$_HDMCDailyMetric._countPairediPhone
+ _OBJC_IVAR_$_HDMCDailyMetric._isSleepScheduleEnabled
+ _OBJC_IVAR_$_HDMCDailyMetric._isSleepScreenEnabled
+ _objc_msgSend$countPairedWatch
+ _objc_msgSend$countPairediPad
+ _objc_msgSend$countPairediPhone
+ _objc_msgSend$deviceContextManager
+ _objc_msgSend$isSleepScheduleEnabled
+ _objc_msgSend$isSleepScreenEnabled
+ _objc_msgSend$numberOfDeviceContextsPerDeviceType:
+ _objc_msgSend$setCountPairedWatch:
+ _objc_msgSend$setCountPairediPad:
+ _objc_msgSend$setCountPairediPhone:
+ _objc_msgSend$setIsSleepScheduleEnabled:
+ _objc_msgSend$setIsSleepScreenEnabled:
CStrings:
+ "\x1f\x0f\x0f\x0f\x0f\x0f\x05"
+ "%{public}@: Failed to get device contexts dictionary for HealthMenstrualCycles daily analytics: %{public}@"
+ "T@\"NSNumber\",&,N,V_countPairedWatch"
+ "T@\"NSNumber\",&,N,V_countPairediPad"
+ "T@\"NSNumber\",&,N,V_countPairediPhone"
+ "T@\"NSNumber\",&,N,V_isSleepScheduleEnabled"
+ "T@\"NSNumber\",&,N,V_isSleepScreenEnabled"
+ "[%{public}@] Error retrieving current sleep settings: %{public}@"
+ "[%{public}@] Error retrieving sleep screen enabled status: %{public}@"
+ "_countPairedWatch"
+ "_countPairediPad"
+ "_countPairediPhone"
+ "_isSleepScheduleEnabled"
+ "_isSleepScreenEnabled"
+ "countPairedWatch"
+ "countPairediPad"
+ "countPairediPhone"
+ "deviceContextManager"
+ "numberOfDeviceContextsPerDeviceType:"
+ "setCountPairedWatch:"
+ "setCountPairediPad:"
+ "setCountPairediPhone:"
+ "setIsSleepScheduleEnabled:"
+ "setIsSleepScreenEnabled:"
- "\x1f\x0f\x0f\x0f\x0f\x0f"

```
