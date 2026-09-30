## OSIntelligence

> `/System/Library/PrivateFrameworks/OSIntelligence.framework/OSIntelligence`

```diff

-234.60.4.0.0
-  __TEXT.__text: 0x18ed8
-  __TEXT.__auth_stubs: 0x5e0
-  __TEXT.__objc_methlist: 0x20e0
+234.60.6.0.0
+  __TEXT.__text: 0x19498
+  __TEXT.__auth_stubs: 0x5f0
+  __TEXT.__objc_methlist: 0x2138
   __TEXT.__const: 0x1a0
-  __TEXT.__cstring: 0x1819
+  __TEXT.__cstring: 0x18ad
   __TEXT.__gcc_except_tab: 0x634
-  __TEXT.__oslogstring: 0x1be8
-  __TEXT.__unwind_info: 0x908
+  __TEXT.__oslogstring: 0x1ce2
+  __TEXT.__unwind_info: 0x920
   __TEXT.__objc_classname: 0x455
-  __TEXT.__objc_methname: 0x3fdd
-  __TEXT.__objc_methtype: 0xbc5
-  __TEXT.__objc_stubs: 0x2da0
-  __DATA_CONST.__got: 0x1e0
-  __DATA_CONST.__const: 0x808
+  __TEXT.__objc_methname: 0x419d
+  __TEXT.__objc_methtype: 0xbf8
+  __TEXT.__objc_stubs: 0x2e20
+  __DATA_CONST.__got: 0x1e8
+  __DATA_CONST.__const: 0x828
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10e0
+  __DATA_CONST.__objc_selrefs: 0x1120
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x300
+  __AUTH_CONST.__auth_got: 0x308
   __AUTH_CONST.__const: 0x780
-  __AUTH_CONST.__cfstring: 0x1400
-  __AUTH_CONST.__objc_const: 0x2ef0
+  __AUTH_CONST.__cfstring: 0x1440
+  __AUTH_CONST.__objc_const: 0x2f50
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x1b0
+  __DATA.__objc_ivar: 0x1b8
   __DATA.__data: 0x5a0
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x690

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CAA4487F-C103-3D0B-93C4-495DFBC3CFE9
-  Functions: 867
-  Symbols:   2921
-  CStrings:  1380
+  UUID: 7C283524-9943-3C29-8123-A937EBAABA20
+  Functions: 874
+  Symbols:   2943
+  CStrings:  1406
 
Symbols:
+ +[OSIUtilities daysCrossingDailyDrainThreshold:overPastDays:fromDate:]
+ +[OSIUtilities drainPerDayFromDate:forNumberOfDays:]
+ +[OSIUtilities drainPerDayFromDate:forNumberOfDays:].cold.1
+ +[OSIUtilities logCompletion:]
+ +[OSIUtilities logCompletion:].cold.1
+ +[OSIUtilities logCompletion:].cold.2
+ +[_OSITimeSeriesUtilities resampleTimeSeries:withStartDate:withEndDate:withFrequency:]
+ +[_OSITimeSeriesUtilities sortedVerifiedDatesFrom:withStartDate:withEndDate:]
+ -[_OSIBLManager evaluateForHighDailyDrainInPastOnDate:overPastDays:]
+ -[_OSIBLManager hasHighDailyDrainBehavior]
+ -[_OSIBLManager hasHighDailyDrain]
+ -[_OSIBLManager lastEvaluationDateForHighDailyDrain]
+ -[_OSIBLManager setHasHighDailyDrain:]
+ -[_OSIBLManager setLastEvaluationDateForHighDailyDrain:]
+ GCC_except_table14
+ GCC_except_table9
+ _OBJC_IVAR_$__OSIBLManager._hasHighDailyDrain
+ _OBJC_IVAR_$__OSIBLManager._lastEvaluationDateForHighDailyDrain
+ ___21-[_OSIBLManager init]_block_invoke.92
+ ___21-[_OSIBLManager init]_block_invoke_2.94
+ ___22-[_OSIBLManager start]_block_invoke.115
+ ___22-[_OSIBLManager start]_block_invoke.118
+ ___41-[_OSIBLManager updateTrialOSIParameters]_block_invoke.103
+ ___48-[_OSBatteryDrainPredictor lastBatteryLevelDate]_block_invoke.52
+ ___49-[_OSBatteryDrainPredictor firstBatteryLevelDate]_block_invoke.56
+ ___49-[_OSBatteryDrainPredictor lastBatteryLevelValue]_block_invoke.57
+ ___52+[OSIUtilities drainPerDayFromDate:forNumberOfDays:]_block_invoke
+ ___52+[OSIUtilities drainPerDayFromDate:forNumberOfDays:]_block_invoke_2
+ ___52+[OSIUtilities drainPerDayFromDate:forNumberOfDays:]_block_invoke_3
+ ___block_descriptor_40_e23_v16?0"BPSCompletion"8l
+ ___block_literal_global.55
+ _objc_msgSend$daysCrossingDailyDrainThreshold:overPastDays:fromDate:
+ _objc_msgSend$evaluateForHighDailyDrainInPastOnDate:overPastDays:
+ _objc_msgSend$hasHighDailyDrainBehavior
+ _objc_msgSend$sortedVerifiedDatesFrom:withStartDate:withEndDate:
+ _objc_retain_x27
+ _objc_retain_x4
- +[_OSITimeSeriesUtilities resampleTimeSeries:withMaxDays:withFrequency:]
- -[_OSBatteryDrainPredictor drainPerDayFromDate:forNumberOfDays:]
- -[_OSBatteryDrainPredictor drainPerDayFromDate:forNumberOfDays:].cold.1
- -[_OSBatteryDrainPredictor logCompletion:]
- -[_OSBatteryDrainPredictor logCompletion:].cold.1
- -[_OSBatteryDrainPredictor logCompletion:].cold.2
- ___21-[_OSIBLManager init]_block_invoke.86
- ___21-[_OSIBLManager init]_block_invoke_2.88
- ___22-[_OSIBLManager start]_block_invoke.109
- ___22-[_OSIBLManager start]_block_invoke.112
- ___41-[_OSIBLManager updateTrialOSIParameters]_block_invoke.97
- ___48-[_OSBatteryDrainPredictor lastBatteryLevelDate]_block_invoke.58
- ___49-[_OSBatteryDrainPredictor firstBatteryLevelDate]_block_invoke.61
- ___49-[_OSBatteryDrainPredictor lastBatteryLevelValue]_block_invoke.62
- ___64-[_OSBatteryDrainPredictor drainPerDayFromDate:forNumberOfDays:]_block_invoke
- ___64-[_OSBatteryDrainPredictor drainPerDayFromDate:forNumberOfDays:]_block_invoke_2
- ___64-[_OSBatteryDrainPredictor drainPerDayFromDate:forNumberOfDays:]_block_invoke_3
- ___block_literal_global.60
- _objc_retain_x24
CStrings:
+ ":\"4"
+ "@40@0:8@16@24@32"
+ "@48@0:8@16@24@32d40"
+ "B28@0:8@16i24"
+ "High daily drain in history has been identified. Skipping evaluation"
+ "Is High Daily Drain User: %{public}d"
+ "Number of days that cross the threshold %u"
+ "Number of days that cross the threshold to classify as high drain user: %ld"
+ "Q36@0:8Q16i24@28"
+ "T@\"NSDate\",&,N,V_lastEvaluationDateForHighDailyDrain"
+ "TB,N,V_hasHighDailyDrain"
+ "Using cached result for high daily drain classification: %{public}d"
+ "_hasHighDailyDrain"
+ "_lastEvaluationDateForHighDailyDrain"
+ "daysCrossingDailyDrainThreshold:overPastDays:fromDate:"
+ "evaluateForHighDailyDrainInPastOnDate:overPastDays:"
+ "hasHighDailyDrain"
+ "hasHighDailyDrainBehavior"
+ "kIsHighDailyDrainBehavior"
+ "kLastCheckForHighDailyDrain"
+ "lastEvaluationDateForHighDailyDrain"
+ "osiutilities.drainCrossingThreshold"
+ "osiutilities.drainPerDayInPast"
+ "osiutilities.logCompletion"
+ "resampleTimeSeries:withStartDate:withEndDate:withFrequency:"
+ "setHasHighDailyDrain:"
+ "setLastEvaluationDateForHighDailyDrain:"
+ "sortedVerifiedDatesFrom:withStartDate:withEndDate:"
- ":\"3"
- "@40@0:8@16q24d32"
- "Number of days that cross the threshold %d"
- "resampleTimeSeries:withMaxDays:withFrequency:"

```
