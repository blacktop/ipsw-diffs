## signpost_reporter

> `/usr/libexec/signpost_reporter`

```diff

-121.0.0.0.0
-  __TEXT.__text: 0x8930
-  __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_stubs: 0x1660
+125.0.0.0.0
+  __TEXT.__text: 0x8260
+  __TEXT.__auth_stubs: 0x5a0
+  __TEXT.__objc_stubs: 0x1580
   __TEXT.__objc_methlist: 0x5b8
-  __TEXT.__const: 0x38
-  __TEXT.__objc_methname: 0x18e0
-  __TEXT.__cstring: 0x12eb
+  __TEXT.__const: 0x30
+  __TEXT.__objc_methname: 0x1868
+  __TEXT.__cstring: 0x120c
   __TEXT.__objc_classname: 0x17d
   __TEXT.__objc_methtype: 0x226
-  __TEXT.__oslogstring: 0xb15
+  __TEXT.__oslogstring: 0xb88
   __TEXT.__gcc_except_tab: 0x284
-  __TEXT.__unwind_info: 0x258
-  __DATA_CONST.__auth_got: 0x2e8
+  __TEXT.__unwind_info: 0x244
+  __DATA_CONST.__auth_got: 0x2e0
   __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0x668
-  __DATA_CONST.__cfstring: 0x1780
+  __DATA_CONST.__const: 0x5f8
+  __DATA_CONST.__cfstring: 0x1640
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x110
+  __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_arraydata: 0x378
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA.__objc_const: 0xfa0
-  __DATA.__objc_selrefs: 0x5e8
-  __DATA.__objc_classrefs: 0x108
-  __DATA.__objc_superrefs: 0x70
+  __DATA.__objc_selrefs: 0x5b0
   __DATA.__objc_ivar: 0x80
   __DATA.__objc_data: 0x410
   __DATA.__data: 0x110
-  __DATA.__common: 0x8
-  __DATA.__bss: 0x150
+  __DATA.__bss: 0x140
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /System/Library/PrivateFrameworks/WorkflowResponsiveness.framework/WorkflowResponsiveness
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 233
+  Functions: 228
   Symbols:   131
-  CStrings:  577
+  CStrings:  561
 
Symbols:
+ _OBJC_CLASS_$_SignpostAggregationAccumulator
+ _OBJC_CLASS_$_SignpostSupportSubsystemCategoryAllowlist
- _OBJC_CLASS_$_NSCharacterSet
- _objc_retain_x5
CStrings:
+ "%@ is not telemetry enabled"
+ "Accumulated information on %llu aggregations"
+ "Could not generate telemetry payload for %@"
+ "Submitting CA event payload for %@"
+ "_coreAnalyticsEventName"
+ "_coreAnalyticsEventPayloadDictionary"
+ "accumulatedAggregation"
+ "addSubsystem:category:"
+ "aggregationSignature"
+ "allValues"
+ "allowListForAllSignposts"
+ "com.apple.Telemetry.PeriodicAggregations"
+ "generateTelemetry"
+ "handleInterval:"
+ "initForReadbackWithWorkflow:eventCompletionCallback:"
+ "initWithIncludeRawIntervals:"
+ "signatureToAccumulatorEntry"
+ "v16@?0@\"WRWorkflowEventTracker\"8"
- "%@_%@"
- "%@_count"
- "%@_delaySec"
- "%@_durationSec"
- "%@_env_%@"
- ".,:-_'\""
- "Bailing since we have no work to do."
- "UNKNOWN"
- "addCharactersInString:"
- "allSignpostTrackers"
- "allowList"
- "com.apple.%@"
- "componentsSeparatedByCharactersInSet:"
- "endSignpost"
- "endSignpostGroups"
- "enumerateKeysAndObjectsUsingBlock:"
- "environment"
- "individuationFieldName"
- "individuationIdentifier"
- "initWithFormat:"
- "initWithWorkflow:eventCompletionCallback:"
- "machContTimeNs"
- "mutableCopy"
- "numberWithInt:"
- "overallDurationSeconds"
- "startSignpost"
- "startSignposts"
- "timeUntilFirstSignpostNanoseconds"
- "totalDurationNanoseconds"
- "v16@?0@\"WRSignpostTracker\"8"
- "v32@?0@\"NSString\"8@16^B24"
- "v48@?0@\"WRWorkflowEventTracker\"8@\"WRTimestampAndThread\"16@\"WRTimestampAndThread\"24@\"WRSignpost\"32@\"WRSignpost\"40"
- "whitespaceAndNewlineCharacterSet"

```
