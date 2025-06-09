## MetricMeasurement

> `/System/Library/PrivateFrameworks/MetricMeasurement.framework/MetricMeasurement`

```diff

-261.0.0.0.0
-  __TEXT.__text: 0x1a000
-  __TEXT.__auth_stubs: 0x880
-  __TEXT.__objc_methlist: 0x267c
+291.0.0.0.1
+  __TEXT.__text: 0x1b270
+  __TEXT.__auth_stubs: 0x8a0
+  __TEXT.__objc_methlist: 0x26fc
   __TEXT.__const: 0x268
-  __TEXT.__cstring: 0x1fdd
-  __TEXT.__gcc_except_tab: 0x4b0
-  __TEXT.__oslogstring: 0x76d
+  __TEXT.__cstring: 0x2255
+  __TEXT.__gcc_except_tab: 0x5b4
+  __TEXT.__oslogstring: 0x77e
   __TEXT.__ustring: 0x34
-  __TEXT.__unwind_info: 0x8b0
-  __TEXT.__objc_classname: 0x571
-  __TEXT.__objc_methname: 0x448e
-  __TEXT.__objc_methtype: 0xf87
-  __TEXT.__objc_stubs: 0x3c40
-  __DATA_CONST.__got: 0x268
-  __DATA_CONST.__const: 0x4c8
+  __TEXT.__unwind_info: 0x8f8
+  __TEXT.__objc_classname: 0x594
+  __TEXT.__objc_methname: 0x471e
+  __TEXT.__objc_methtype: 0xfe9
+  __TEXT.__objc_stubs: 0x3dc0
+  __DATA_CONST.__got: 0x270
+  __DATA_CONST.__const: 0x5d0
   __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_nlclslist: 0x8
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0xa0
+  __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13d8
+  __DATA_CONST.__objc_selrefs: 0x1448
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x100
-  __AUTH_CONST.__auth_got: 0x450
-  __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x2280
-  __AUTH_CONST.__objc_const: 0x55b8
+  __AUTH_CONST.__auth_got: 0x460
+  __AUTH_CONST.__const: 0x140
+  __AUTH_CONST.__cfstring: 0x2380
+  __AUTH_CONST.__objc_const: 0x5678
   __AUTH_CONST.__objc_intobj: 0xa8
-  __DATA.__objc_ivar: 0x164
-  __DATA.__data: 0x780
+  __AUTH.__objc_data: 0xcd0
+  __DATA.__objc_ivar: 0x16c
+  __DATA.__data: 0x7e0
   __DATA.__bss: 0x2b0
-  __DATA_DIRTY.__objc_data: 0xdc0
+  __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
+  - /System/Library/PrivateFrameworks/FunctionCoverage.framework/FunctionCoverage
   - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
   - /System/Library/PrivateFrameworks/PerformanceTrace.framework/PerformanceTrace
   - /System/Library/PrivateFrameworks/SignpostCollection.framework/SignpostCollection

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpmsample.dylib
   - /usr/lib/libsysmon.dylib
-  UUID: A824B48E-273F-32E2-8714-6B3166873BF1
-  Functions: 799
-  Symbols:   3016
-  CStrings:  1713
+  UUID: BAF2CFC7-388B-3B70-B6BA-B54CBD477198
+  Functions: 816
+  Symbols:   3078
+  CStrings:  1754
 
Symbols:
+ +[MXMOSSignpostSampleTag animationPerAppNonFirstFrameGlitchTimeRatioAdjusted]
+ +[MXMOSSignpostSampleTag animationPerAppNonFirstFrameGlitchesTotalDuration]
+ +[MXMOSSignpostSampleTag animationPerAppNonFirstFrameNumberOfGlitches]
+ +[MXMProxyServiceManager shared].cold.1
+ -[MXMInstrument functionCoverageFileURL]
+ -[MXMOSSignpostMetric initWithSubsystem:category:name:processName:]
+ -[MXMOSSignpostMetric processName]
+ -[MXMProxyServiceManager _startFunctionCoverageCollection:response:]
+ -[MXMProxyServiceManager _stopFunctionCoverageCollection:]
+ GCC_except_table11
+ GCC_except_table13
+ GCC_except_table17
+ GCC_except_table21
+ GCC_except_table23
+ GCC_except_table28
+ GCC_except_table44
+ _MXMAttributeNameOSSignpostAnimationContributingProcessName
+ _MXMInstrumentOptionFunctionCoverageConfiguration
+ _MXMInstrumentOptionFunctionCoverageEnabled
+ _OBJC_CLASS_$_SignpostAnimationOverrunQuery
+ _OBJC_IVAR_$_MXMInstrument._functionCoverageFileURL
+ _OBJC_IVAR_$_MXMOSSignpostMetric._processName
+ _SignpostSupportTotalDurationNsForIntervals
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MXMSProxyFunctionCoverage_Internal
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MXMSProxyFunctionCoverage_Internal
+ __OBJC_$_PROTOCOL_REFS_MXMSProxyFunctionCoverage_Internal
+ __OBJC_LABEL_PROTOCOL_$_MXMSProxyFunctionCoverage_Internal
+ __OBJC_PROTOCOL_$_MXMSProxyFunctionCoverage_Internal
+ ___32+[MXMProxyServiceManager shared]_block_invoke
+ ___58-[MXMProxyServiceManager _stopFunctionCoverageCollection:]_block_invoke
+ ___68-[MXMProxyServiceManager _startFunctionCoverageCollection:response:]_block_invoke
+ ___87-[MXMOSSignpostProbe _addAnimationGlitchTimeRatioToData:fromSignpostAnimationInterval:]_block_invoke
+ ___88-[MXMOSSignpostProbe _addAnimationNumberOfGlitchesToData:fromSignpostAnimationInterval:]_block_invoke
+ ___93-[MXMOSSignpostProbe _addAnimationGlitchesTotalDurationToData:fromSignpostAnimationInterval:]_block_invoke
+ ___MXMStartFunctionCoverageCollection_block_invoke
+ ___MXMStopFunctionCoverageCollection_block_invoke
+ ___block_descriptor_40_e8_32r_e32_v28?0B8"NSError"12"NSError"20lr32l8
+ ___block_descriptor_48_e8_32r40r_e17_v16?0"NSError"8lr32l8r40l8
+ ___block_descriptor_48_e8_32r40r_e27_v24?0"NSURL"8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e12_v24?0Q8^B16ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e12_v24?0Q8^B16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e27_v24?0"NSURL"8"NSError"16ls32l8r40l8r48l8
+ ___block_literal_global.275
+ ___block_literal_global.75
+ _objc_msgSend$_startFunctionCoverageCollection:response:
+ _objc_msgSend$_startFunctionCoverageCollectionHelper:response:
+ _objc_msgSend$_stopFunctionCoverageCollection:
+ _objc_msgSend$_stopFunctionCoverageCollectionHelper:
+ _objc_msgSend$animationPerAppNonFirstFrameGlitchTimeRatioAdjusted
+ _objc_msgSend$animationPerAppNonFirstFrameGlitchesTotalDuration
+ _objc_msgSend$animationPerAppNonFirstFrameNumberOfGlitches
+ _objc_msgSend$contributingPidsForProcessName:
+ _objc_msgSend$endMachContinuousTime
+ _objc_msgSend$enumerateIndexesUsingBlock:
+ _objc_msgSend$initWithSubsystem:category:name:processName:
+ _objc_msgSend$nonFirstFrameContributedGlitches:
+ _objc_msgSend$overrunIntervals:
+ _objc_msgSend$timeRatioMSPerSForOverrunIntervals:applyPerceptionAdjustments:
+ _objc_retain_x9
+ _shared._shared
- GCC_except_table12
- GCC_except_table14
- GCC_except_table16
- GCC_except_table18
- GCC_except_table25
- GCC_except_table4
- ___block_literal_global.265
- __shared
- _objc_msgSend$initWithSubsystem:category:name:
- _objc_msgSend$timeRecordedMachContinuousTime
CStrings:
+ "@40@0:8Q16r^{?=QQIQBQQQQ^v^v{?=QQ}{?=QQ}Q^v^v^v^^vB^vdd^v^vB^v}24@32"
+ "MXMSProxyFunctionCoverage_Internal"
+ "T@\"NSString\",R,N,V_processName"
+ "T@\"NSURL\",R,V_functionCoverageFileURL"
+ "T^{?=QQIQBQQQQ^v^v{?=QQ}{?=QQ}Q^v^v^v^^vB^vdd^v^vB^v},V_currentIteration"
+ "Unable to start function coverage collection. See error logs for more detail."
+ "Unable to stop and post process function coverage. See error logs for more detail. %d"
+ "^{?=QQIQBQQQQ^v^v{?=QQ}{?=QQ}Q^v^v^v^^vB^vdd^v^vB^v}"
+ "^{?=QQIQBQQQQ^v^v{?=QQ}{?=QQ}Q^v^v^v^^vB^vdd^v^vB^v}16@0:8"
+ "_functionCoverageFileURL"
+ "_processName"
+ "_startFunctionCoverageCollection:response:"
+ "_startFunctionCoverageCollectionHelper:response:"
+ "_stopFunctionCoverageCollection:"
+ "_stopFunctionCoverageCollectionHelper:"
+ "animationPerAppNonFirstFrameGlitchTimeRatioAdjusted"
+ "animationPerAppNonFirstFrameGlitchesTotalDuration"
+ "animationPerAppNonFirstFrameNumberOfGlitches"
+ "com.apple.metricmeasurement.instrument.options.FunctionCoverageConfiguration"
+ "com.apple.metricmeasurement.instrument.options.FunctionCoverageEnabled"
+ "contributingPidsForProcessName:"
+ "endMachContinuousTime"
+ "enumerateIndexesUsingBlock:"
+ "functionCoverageFileURL"
+ "initWithSubsystem:category:name:processName:"
+ "isAnimation=YES "
+ "nonFirstFrameContributedGlitches:"
+ "os_signpost animation contributing process name"
+ "os_signpost.animation.hitch.per_app.non_first_frame.number"
+ "os_signpost.animation.hitch.per_app.non_first_frame.time.ratio.adjusted"
+ "os_signpost.animation.hitch.per_app.non_first_frame.total.duration"
+ "overrunIntervals:"
+ "timeRatioMSPerSForOverrunIntervals:applyPerceptionAdjustments:"
+ "v24@0:8@?<v@?@\"NSURL\"@\"NSError\">16"
+ "v24@0:8^{?=QQIQBQQQQ^v^v{?=QQ}{?=QQ}Q^v^v^v^^vB^vdd^v^vB^v}16"
+ "v24@?0@\"NSURL\"8@\"NSError\"16"
+ "v24@?0Q8^B16"
+ "v28@?0B8@\"NSError\"12@\"NSError\"20"
+ "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24"
+ "v40@0:8@16Q24^{vm_statistics64=IIIIQQQQQQQQQIIQQQQIIIIQQ}32"
+ "v48@0:8^{?=QQIQBQQQQ^v^v{?=QQ}{?=QQ}Q^v^v^v^^vB^vdd^v^vB^v}16@24@32@40"
+ "v52@0:8^{?=QQIQBQQQQ^v^v{?=QQ}{?=QQ}Q^v^v^v^^vB^vdd^v^vB^v}16B24^{_opaque_pthread_attr_t=q[56c]}28^^{_opaque_pthread_t}36^Q44"
- "@40@0:8Q16r^{?=QQIQBQQQQ^v^v{?=QQ}{?=QQ}Q^v^v^v^^vB^vdd^v^v}24@32"
- "T^{?=QQIQBQQQQ^v^v{?=QQ}{?=QQ}Q^v^v^v^^vB^vdd^v^v},V_currentIteration"
- "^{?=QQIQBQQQQ^v^v{?=QQ}{?=QQ}Q^v^v^v^^vB^vdd^v^v}"
- "^{?=QQIQBQQQQ^v^v{?=QQ}{?=QQ}Q^v^v^v^^vB^vdd^v^v}16@0:8"
- "timeRecordedMachContinuousTime"
- "v24@0:8^{?=QQIQBQQQQ^v^v{?=QQ}{?=QQ}Q^v^v^v^^vB^vdd^v^v}16"
- "v40@0:8@16Q24^{vm_statistics64=IIIIQQQQQQQQQIIQQQQIIIIQ}32"
- "v48@0:8^{?=QQIQBQQQQ^v^v{?=QQ}{?=QQ}Q^v^v^v^^vB^vdd^v^v}16@24@32@40"
- "v52@0:8^{?=QQIQBQQQQ^v^v{?=QQ}{?=QQ}Q^v^v^v^^vB^vdd^v^v}16B24^{_opaque_pthread_attr_t=q[56c]}28^^{_opaque_pthread_t}36^Q44"

```
