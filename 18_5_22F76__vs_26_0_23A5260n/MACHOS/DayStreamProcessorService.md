## DayStreamProcessorService

> `/System/Library/PrivateFrameworks/HealthAlgorithms.framework/XPCServices/DayStreamProcessorService.xpc/DayStreamProcessorService`

```diff

-122.0.0.0.0
-  __TEXT.__text: 0x1040
-  __TEXT.__auth_stubs: 0x200
+131.0.0.0.0
+  __TEXT.__text: 0xdc4
+  __TEXT.__auth_stubs: 0x210
   __TEXT.__objc_stubs: 0x4a0
-  __TEXT.__objc_methlist: 0x21c
+  __TEXT.__objc_methlist: 0x214
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x204
+  __TEXT.__cstring: 0x15f
   __TEXT.__objc_classname: 0x95
-  __TEXT.__objc_methname: 0x5b4
-  __TEXT.__objc_methtype: 0x207
-  __TEXT.__gcc_except_tab: 0x48
-  __TEXT.__oslogstring: 0xbd
-  __TEXT.__unwind_info: 0xb0
-  __DATA_CONST.__auth_got: 0x110
-  __DATA_CONST.__got: 0x68
+  __TEXT.__objc_methname: 0x57a
+  __TEXT.__objc_methtype: 0x1d6
+  __TEXT.__gcc_except_tab: 0x80
+  __TEXT.__oslogstring: 0x134
+  __TEXT.__unwind_info: 0xa0
+  __DATA_CONST.__auth_got: 0x118
+  __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x40
-  __DATA_CONST.__cfstring: 0x120
+  __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA.__objc_const: 0x360
+  __DATA.__objc_const: 0x380
   __DATA.__objc_selrefs: 0x1f0
-  __DATA.__objc_ivar: 0x8
+  __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x180
   __DATA.__bss: 0x10

   - /System/Library/PrivateFrameworks/MenstrualAlgorithmsInternal.framework/MenstrualAlgorithmsInternal
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 13997EAB-C00F-344F-9B3B-3D987731F4AE
-  Functions: 26
-  Symbols:   62
-  CStrings:  131
+  UUID: B34FFEDB-70E2-392E-A3E8-33516E6296C7
+  Functions: 22
+  Symbols:   60
+  CStrings:  121
 
Symbols:
+ __os_signpost_emit_with_name_impl
+ _objc_retain
+ _os_signpost_enabled
+ _os_signpost_id_make_with_pointer
- _OBJC_CLASS_$_NSDictionary
- _OBJC_CLASS_$_NSNumber
- _clock_gettime_nsec_np
- _ha_get_log
- _objc_autoreleaseReturnValue
- _objc_release_x25
CStrings:
+ "DayStreamProcessorAnalysisDuration"
+ "Q"
+ "_signpostID"
+ "count"
+ "day_stream_processor_service"
+ "firstObject"
+ "isOngoingMenstruation"
+ "menstrualPredictionFirstPrimarySource=%{signpost.telemetry:number1}f fertilityPredictionFirstPrimarySource=%{signpost.telemetry:number2}f enableTelemetry=YES "
+ "objectAtIndexedSubscript:"
- "@40@0:8r^{MAIDayStreamProcessorOutput=@@@}16Q24Q32"
- "HAMenstrualAlgorithmsPredictionPrimarySource has the unexpected index: %hhu"
- "com.apple.hid.cycle_tracking.day_stream_analysis_latency"
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
