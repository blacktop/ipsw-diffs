## HistoricalAnalyzerService

> `/System/Library/PrivateFrameworks/HealthAlgorithms.framework/XPCServices/HistoricalAnalyzerService.xpc/HistoricalAnalyzerService`

```diff

-122.0.0.0.0
-  __TEXT.__text: 0xe88
-  __TEXT.__auth_stubs: 0x1e0
-  __TEXT.__objc_stubs: 0x440
+131.0.0.0.0
+  __TEXT.__text: 0xd34
+  __TEXT.__auth_stubs: 0x1f0
+  __TEXT.__objc_stubs: 0x3e0
   __TEXT.__objc_methlist: 0x21c
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x19d
+  __TEXT.__cstring: 0xf7
   __TEXT.__objc_classname: 0x95
-  __TEXT.__objc_methname: 0x512
-  __TEXT.__objc_methtype: 0x1b1
-  __TEXT.__gcc_except_tab: 0x54
-  __TEXT.__oslogstring: 0xbc
-  __TEXT.__unwind_info: 0xb0
-  __DATA_CONST.__auth_got: 0x100
-  __DATA_CONST.__got: 0x68
+  __TEXT.__objc_methname: 0x4b3
+  __TEXT.__objc_methtype: 0x1ad
+  __TEXT.__gcc_except_tab: 0x60
+  __TEXT.__oslogstring: 0xe5
+  __TEXT.__unwind_info: 0xa8
+  __DATA_CONST.__auth_got: 0x108
+  __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x40
-  __DATA_CONST.__cfstring: 0x100
+  __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA.__objc_const: 0x360
-  __DATA.__objc_selrefs: 0x1d8
-  __DATA.__objc_ivar: 0x8
+  __DATA.__objc_const: 0x380
+  __DATA.__objc_selrefs: 0x1c0
+  __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x180
   __DATA.__bss: 0x10

   - /System/Library/PrivateFrameworks/MenstrualAlgorithmsInternal.framework/MenstrualAlgorithmsInternal
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C43ABFCD-A00A-3066-BC7A-EC27A30205BD
-  Functions: 23
-  Symbols:   60
-  CStrings:  125
+  UUID: 9A93CA48-AC47-38C8-982B-B5A09EF8412A
+  Functions: 22
+  Symbols:   58
+  CStrings:  113
 
Symbols:
+ __os_signpost_emit_with_name_impl
+ _os_signpost_enabled
+ _os_signpost_id_make_with_pointer
- _OBJC_CLASS_$_NSDictionary
- _OBJC_CLASS_$_NSNumber
- _clock_gettime_nsec_np
- _ha_get_log
- _objc_autoreleaseReturnValue
CStrings:
+ "HistoricalAnalyzerAnalysisDuration"
+ "Q"
+ "_signpostID"
+ "countPrimarySourceHeartRate:"
+ "historical_analyzer_service"
+ "i24@0:8r^{MAIHistoricalAnalyzerOutput=@@}16"
+ "primarySourceHeartRateCount=%{signpost.telemetry:number1}lf enableTelemetry=YES "
- "@40@0:8r^{MAIHistoricalAnalyzerOutput=@@}16Q24Q32"
- "HAMenstrualAlgorithmsPredictionPrimarySource has the unexpected index: %hhu"
- "com.apple.hid.cycle_tracking.historical_analysis_latency"
- "dictionaryWithObjects:forKeys:count:"
- "framework"
- "latencyCoreAnalytics:start_nanoseconds:end_nanoseconds:"
- "milliseconds"
- "numberWithInt:"
- "numberWithUnsignedLongLong:"
- "primarySourceCalendarMethod"
- "primarySourceHeartRate"
- "primarySourceOvulationTestResult"
- "primarySourceWristTemperature"

```
