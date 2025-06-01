## SignpostSupport

> `/System/Library/PrivateFrameworks/SignpostSupport.framework/SignpostSupport`

```diff

-119.0.0.0.0
-  __TEXT.__text: 0x30fc8
+121.0.0.0.0
+  __TEXT.__text: 0x31ae0
   __TEXT.__auth_stubs: 0x520
-  __TEXT.__objc_methlist: 0x3c8c
+  __TEXT.__objc_methlist: 0x3d24
   __TEXT.__const: 0x114
-  __TEXT.__cstring: 0x15189
+  __TEXT.__cstring: 0x15244
   __TEXT.__oslogstring: 0xd2e
   __TEXT.__gcc_except_tab: 0x148
   __TEXT.__ustring: 0x3e
-  __TEXT.__unwind_info: 0xc94
+  __TEXT.__unwind_info: 0xca0
   __TEXT.__objc_classname: 0x9be
-  __TEXT.__objc_methname: 0xa717
-  __TEXT.__objc_methtype: 0xc11
-  __TEXT.__objc_stubs: 0x6280
+  __TEXT.__objc_methname: 0xa965
+  __TEXT.__objc_methtype: 0xc2b
+  __TEXT.__objc_stubs: 0x6440
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0x728
   __DATA_CONST.__objc_classlist: 0x230
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6f10
-  __DATA_CONST.__objc_selrefs: 0x1da8
+  __DATA_CONST.__objc_const: 0x6f90
+  __DATA_CONST.__objc_selrefs: 0x1e10
   __DATA_CONST.__objc_arraydata: 0x4e58
-  __AUTH_CONST.__cfstring: 0x15c40
+  __AUTH_CONST.__cfstring: 0x15d40
   __AUTH_CONST.__objc_arrayobj: 0x2e8
-  __AUTH_CONST.__const: 0x20
+  __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__objc_const: 0x0
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__auth_got: 0x2a0
   __DATA.__objc_classrefs: 0x218
   __DATA.__objc_superrefs: 0x1d8
-  __DATA.__objc_ivar: 0x5d8
+  __DATA.__objc_ivar: 0x5e0
   __DATA.__data: 0x2c8
   __DATA.__bss: 0x308
-  __DATA_DIRTY.__const: 0x760
+  __DATA_DIRTY.__const: 0x720
   __DATA_DIRTY.__objc_const: 0x19d8
   __DATA_DIRTY.__objc_data: 0x15e0
   __DATA_DIRTY.__bss: 0x20

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E60A3C5A-E5A4-3070-A411-0C37F292ECB5
-  Functions: 1507
-  Symbols:   5028
-  CStrings:  7612
+  UUID: C2CBED2C-876C-3FC2-BF6F-AAC71DACD043
+  Functions: 1519
+  Symbols:   5068
+  CStrings:  7646
 
Symbols:
+ +[SignpostAggregationGroupDuration _combinedStdDevFromDuration0:duration1:]
+ +[SignpostAggregationGroupDuration _combinedStdDevNsFromCount0:totalDurationNs0:stdDevNs0:count1:totalDurationNs1:stdDevNs1:]
+ -[SignpostAggregation _groupToTypeToDurationStdDevNs]
+ -[SignpostAggregation _groupToTypeToMaxDurationNs]
+ -[SignpostAggregation _groupToTypeToMinDurationNs]
+ -[SignpostAggregation _handleDurationStdDevSegment:]
+ -[SignpostAggregation set_groupToTypeToDurationStdDevNs:]
+ -[SignpostAggregation set_groupToTypeToMaxDurationNs:]
+ -[SignpostAggregation set_groupToTypeToMinDurationNs:]
+ -[SignpostAggregationGroupDuration _coreAnalyticsDurationStdDevFieldName]
+ -[SignpostAggregationGroupDuration _coreAnalyticsMaxDurationFieldName]
+ -[SignpostAggregationGroupDuration _coreAnalyticsMinDurationFieldName]
+ -[SignpostAggregationGroupDuration _coreAnalyticsTotalDurationFieldName]
+ -[SignpostAggregationGroupDuration _initializeAsSumOfDuration1:duration2:]
+ -[SignpostAggregationGroupDuration setStdDevNs:]
+ -[SignpostAggregationGroupDuration stdDevMs]
+ -[SignpostAggregationGroupDuration stdDevNs]
+ -[SignpostAggregationGroupDuration stdDevSeconds]
+ _OBJC_IVAR_$_SignpostAggregation.__groupToTypeToDurationStdDevNs
+ _OBJC_IVAR_$_SignpostAggregation.__groupToTypeToMaxDurationNs
+ _OBJC_IVAR_$_SignpostAggregation.__groupToTypeToMinDurationNs
+ _OBJC_IVAR_$_SignpostAggregationGroupDuration._stdDevNs
+ ___block_literal_global.578
+ ___block_literal_global.587
+ _objc_msgSend$_combinedStdDevFromDuration0:duration1:
+ _objc_msgSend$_combinedStdDevNsFromCount0:totalDurationNs0:stdDevNs0:count1:totalDurationNs1:stdDevNs1:
+ _objc_msgSend$_coreAnalyticsDurationStdDevFieldName
+ _objc_msgSend$_coreAnalyticsMaxDurationFieldName
+ _objc_msgSend$_coreAnalyticsMinDurationFieldName
+ _objc_msgSend$_coreAnalyticsTotalDurationFieldName
+ _objc_msgSend$_groupToTypeToDurationStdDevNs
+ _objc_msgSend$_groupToTypeToMaxDurationNs
+ _objc_msgSend$_groupToTypeToMinDurationNs
+ _objc_msgSend$_handleDurationStdDevSegment:
+ _objc_msgSend$_initializeAsSumOfDuration1:duration2:
+ _objc_msgSend$maxDurationSeconds
+ _objc_msgSend$minDurationSeconds
+ _objc_msgSend$setStdDevNs:
+ _objc_msgSend$set_groupToTypeToDurationStdDevNs:
+ _objc_msgSend$set_groupToTypeToMaxDurationNs:
+ _objc_msgSend$set_groupToTypeToMinDurationNs:
+ _objc_msgSend$stdDevNs
+ _objc_msgSend$stdDevSeconds
- -[SignpostAggregation _groupToTypeToMaxDuration]
- -[SignpostAggregation _groupToTypeToMinDuration]
- -[SignpostAggregation set_groupToTypeToMaxDuration:]
- -[SignpostAggregation set_groupToTypeToMinDuration:]
- -[SignpostAggregationGroupDuration _addDuration:]
- -[SignpostAggregationGroupDuration _coreAnalyticsFieldName]
- _OBJC_IVAR_$_SignpostAggregation.__groupToTypeToMaxDuration
- _OBJC_IVAR_$_SignpostAggregation.__groupToTypeToMinDuration
- ___block_literal_global.531
- ___block_literal_global.540
- _objc_msgSend$_addDuration:
- _objc_msgSend$_groupToTypeToMaxDuration
- _objc_msgSend$_groupToTypeToMinDuration
- _objc_msgSend$set_groupToTypeToMaxDuration:
- _objc_msgSend$set_groupToTypeToMinDuration:
CStrings:
+ "\x05\x17"
+ "\x12\x13"
+ "%@__%@__DurationStdDev"
+ "%@__%@__MaxDuration"
+ "%@__%@__MinDuration"
+ "@64@0:8Q16Q24d32Q40Q48d56"
+ "Cannot add durations with and without duration stddev value"
+ "DurationStdDevNs"
+ "MaxDurationNs"
+ "MinDurationNs"
+ "T@\"NSMutableDictionary\",&,N,V__groupToTypeToDurationStdDevNs"
+ "T@\"NSMutableDictionary\",&,N,V__groupToTypeToMaxDurationNs"
+ "T@\"NSMutableDictionary\",&,N,V__groupToTypeToMinDurationNs"
+ "T@\"NSNumber\",&,N,V_stdDevNs"
+ "__groupToTypeToDurationStdDevNs"
+ "__groupToTypeToMaxDurationNs"
+ "__groupToTypeToMinDurationNs"
+ "_combinedStdDevFromDuration0:duration1:"
+ "_combinedStdDevNsFromCount0:totalDurationNs0:stdDevNs0:count1:totalDurationNs1:stdDevNs1:"
+ "_coreAnalyticsDurationStdDevFieldName"
+ "_coreAnalyticsMaxDurationFieldName"
+ "_coreAnalyticsMinDurationFieldName"
+ "_coreAnalyticsTotalDurationFieldName"
+ "_groupToTypeToDurationStdDevNs"
+ "_groupToTypeToMaxDurationNs"
+ "_groupToTypeToMinDurationNs"
+ "_handleDurationStdDevSegment:"
+ "_initializeAsSumOfDuration1:duration2:"
+ "_stdDevNs"
+ "duration_stddev_ns"
+ "setStdDevNs:"
+ "set_groupToTypeToDurationStdDevNs:"
+ "set_groupToTypeToMaxDurationNs:"
+ "set_groupToTypeToMinDurationNs:"
+ "stdDevMs"
+ "stdDevNs"
+ "stdDevSeconds"
- "\x05\x16"
- "\x12\x12"
- "T@\"NSMutableDictionary\",&,N,V__groupToTypeToMaxDuration"
- "T@\"NSMutableDictionary\",&,N,V__groupToTypeToMinDuration"
- "__groupToTypeToMaxDuration"
- "__groupToTypeToMinDuration"
- "_addDuration:"
- "_groupToTypeToMaxDuration"
- "_groupToTypeToMinDuration"
- "a"
- "set_groupToTypeToMaxDuration:"
- "set_groupToTypeToMinDuration:"

```
