## SleepHealth

> `/System/Library/PrivateFrameworks/SleepHealth.framework/SleepHealth`

```diff

-5200.5.1.0.0
-  __TEXT.__text: 0x4fb8
+6074.1.2.4.0
+  __TEXT.__text: 0x5178
   __TEXT.__auth_stubs: 0x330
-  __TEXT.__objc_methlist: 0x61c
-  __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x83c
-  __TEXT.__gcc_except_tab: 0x11c
-  __TEXT.__oslogstring: 0x3a3
-  __TEXT.__unwind_info: 0x190
+  __TEXT.__objc_methlist: 0x624
+  __TEXT.__const: 0x88
+  __TEXT.__cstring: 0x812
+  __TEXT.__gcc_except_tab: 0x124
+  __TEXT.__oslogstring: 0x36c
+  __TEXT.__unwind_info: 0x198
   __TEXT.__objc_classname: 0x14e
-  __TEXT.__objc_methname: 0x1d01
-  __TEXT.__objc_methtype: 0x3ca
-  __TEXT.__objc_stubs: 0x1060
-  __DATA_CONST.__got: 0x168
+  __TEXT.__objc_methname: 0x1e33
+  __TEXT.__objc_methtype: 0x3d1
+  __TEXT.__objc_stubs: 0x1160
+  __DATA_CONST.__got: 0x170
   __DATA_CONST.__const: 0x238
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x650
+  __DATA_CONST.__objc_selrefs: 0x690
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x1a8
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x7c0
+  __AUTH_CONST.__cfstring: 0x7a0
   __AUTH_CONST.__objc_const: 0xc58
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x50
+  __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x80
-  __DATA.__data: 0x368
-  __DATA_DIRTY.__objc_data: 0x140
+  __DATA.__data: 0x360
+  __DATA_DIRTY.__objc_data: 0xf0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit

   - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D37783DD-ED07-3F28-AB6C-B3E2C4E9F003
+  UUID: 68F7E50B-D7BD-311F-B3A1-93CD7BCA3C82
   Functions: 105
-  Symbols:   598
-  CStrings:  477
+  Symbols:   607
+  CStrings:  482
 
Symbols:
+ +[HKSHSleepMetricsEngine _generateConsiderationIntervalFromDaySummaries:morningIndexRange:]
+ +[HKSHSleepMetricsEngine _generateStrategyWithSleepDayInterval:considerationInterval:]
+ _OBJC_CLASS_$_HKSleepDaySummaryDurationStrategy
+ ___block_literal_global.297
+ _objc_msgSend$_generateConsiderationIntervalFromDaySummaries:morningIndexRange:
+ _objc_msgSend$_generateStrategyWithSleepDayInterval:considerationInterval:
+ _objc_msgSend$bestFitDurationStrategyForSleepDayInterval:considerationInterval:
+ _objc_msgSend$distantFuture
+ _objc_msgSend$distantPast
+ _objc_msgSend$durationsForStrategy:
+ _objc_msgSend$earlierDate:
+ _objc_msgSend$hasNonZeroSleepDurationGoal
+ _objc_msgSend$hk_sleepDayIntervalForMorningIndexRange:calendar:
+ _objc_msgSend$laterDate:
+ _objc_msgSend$remote_getBreathingDisturbanceSamplesInDateInterval:includeTimeZones:completion:
- +[HKSleepHealthStore _areAllSamples:containedInDateInterval:]
- ___61+[HKSleepHealthStore _areAllSamples:containedInDateInterval:]_block_invoke
- ___block_literal_global.294
- _objc_msgSend$_areAllSamples:containedInDateInterval:
- _objc_msgSend$containsDate:
- _objc_msgSend$remote_getBreathingDisturbanceSamplesInDateInterval:completion:
CStrings:
+ "_generateConsiderationIntervalFromDaySummaries:morningIndexRange:"
+ "_generateStrategyWithSleepDayInterval:considerationInterval:"
+ "bestFitDurationStrategyForSleepDayInterval:considerationInterval:"
+ "distantFuture"
+ "distantPast"
+ "durationsForStrategy:"
+ "earlierDate:"
+ "hasNonZeroSleepDurationGoal"
+ "hk_sleepDayIntervalForMorningIndexRange:calendar:"
+ "laterDate:"
+ "remote_getBreathingDisturbanceSamplesInDateInterval:includeTimeZones:completion:"
+ "v36@0:8@\"NSDateInterval\"16B24@?<v@?@\"NSArray\">28"
+ "v36@0:8@16B24@?28"
- "B32@0:8@16@24"
- "[%{public}@] dateInterval does not contain all samples"
- "_areAllSamples:containedInDateInterval:"
- "containsDate:"
- "dateInterval does not contain all samples"
- "remote_getBreathingDisturbanceSamplesInDateInterval:completion:"
- "v32@0:8@\"NSDateInterval\"16@?<v@?@\"NSArray\">24"

```
