## MetricKit

> `/System/Library/Frameworks/MetricKit.framework/MetricKit`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_DIRTY.__objc_data`

```diff

-361.0.0.0.0
-  __TEXT.__text: 0x7cf4c
-  __TEXT.__objc_methlist: 0x2894
-  __TEXT.__const: 0x8f06
+367.0.0.0.0
+  __TEXT.__text: 0x7c148
+  __TEXT.__objc_methlist: 0x290c
+  __TEXT.__const: 0x8d76
   __TEXT.__cstring: 0x1ec2
   __TEXT.__gcc_except_tab: 0x18
   __TEXT.__oslogstring: 0x349
-  __TEXT.__swift5_typeref: 0x18b4
-  __TEXT.__swift5_reflstr: 0x11b1
-  __TEXT.__swift5_assocty: 0x4c8
-  __TEXT.__constg_swiftt: 0x145c
-  __TEXT.__swift5_fieldmd: 0x1c88
+  __TEXT.__swift5_typeref: 0x1884
+  __TEXT.__swift5_reflstr: 0x1183
+  __TEXT.__swift5_assocty: 0x4b0
+  __TEXT.__constg_swiftt: 0x143c
+  __TEXT.__swift5_fieldmd: 0x1c30
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_proto: 0x8dc
-  __TEXT.__swift5_types: 0x21c
+  __TEXT.__swift5_proto: 0x8c4
+  __TEXT.__swift5_types: 0x218
   __TEXT.__swift_as_entry: 0x4
   __TEXT.__swift_as_ret: 0x4
   __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0x23c0
-  __TEXT.__eh_frame: 0x2838
+  __TEXT.__unwind_info: 0x2390
+  __TEXT.__eh_frame: 0x27b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x108
-  __DATA_CONST.__objc_classlist: 0x1b0
+  __DATA_CONST.__const: 0x148
+  __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1228
+  __DATA_CONST.__objc_selrefs: 0x1220
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x178
-  __DATA_CONST.__got: 0x490
-  __AUTH_CONST.__const: 0x4779
-  __AUTH_CONST.__cfstring: 0x1b60
-  __AUTH_CONST.__objc_const: 0x6718
-  __AUTH_CONST.__auth_got: 0x9e8
-  __AUTH.__objc_data: 0xd8
-  __AUTH.__data: 0x198
-  __DATA.__objc_ivar: 0x430
-  __DATA.__data: 0x11d0
-  __DATA.__bss: 0x12a50
+  __DATA_CONST.__got: 0x480
+  __AUTH_CONST.__const: 0x4681
+  __AUTH_CONST.__cfstring: 0x1ba0
+  __AUTH_CONST.__objc_const: 0x67f0
+  __AUTH_CONST.__auth_got: 0x9f0
+  __AUTH.__objc_data: 0x188
+  __AUTH.__data: 0x1c0
+  __DATA.__objc_ivar: 0x43c
+  __DATA.__data: 0x11c0
+  __DATA.__bss: 0x12720
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x11b0
-  __DATA_DIRTY.__data: 0x1328
-  __DATA_DIRTY.__bss: 0x3a0
+  __DATA_DIRTY.__data: 0x1298
+  __DATA_DIRTY.__bss: 0x390
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3325
-  Symbols:   2819
-  CStrings:  352
+  Functions: 3311
+  Symbols:   2820
+  CStrings:  354
 
Symbols:
+ +[MXCrashDiagnostic _terminationCategoryForNamespace:code:signal:]
+ -[MXCrashDiagnostic initWithMetaData:applicationVersion:signpostData:reportedStateData:pid:terminationReason:applicationSpecificInfo:virtualMemoryRegionInfo:exceptionType:exceptionCode:exceptionReason:signal:terminationNamespace:terminationCode:stackTrace:]
+ -[MXCrashDiagnostic terminationCode]
+ -[MXCrashDiagnostic terminationNamespace]
+ -[MXLocationActivityMetric cumulativeReducedAccuracyTime]
+ -[MXLocationActivityMetric initWithCumulativeBestAccuracyTimeMeasurement:cumulativeBestAccuracyForNavigationTimeMeasurement:nearestTenMetersAccuracyTimeMeasurement:hundredMetersAccuracyTimeMeasurement:kilometerAccuracyTimeMeasurement:threeKilometerAccuracyTimeMeasurement:reducedAccuracyTimeMeasurement:]
+ _OBJC_CLASS_$__TtC9MetricKit14HitchTimeRatio
+ _OBJC_IVAR_$_MXCrashDiagnostic._terminationCode
+ _OBJC_IVAR_$_MXCrashDiagnostic._terminationNamespace
+ _OBJC_IVAR_$_MXLocationActivityMetric._cumulativeReducedAccuracyTime
+ _OBJC_METACLASS_$__TtC9MetricKit14HitchTimeRatio
+ __CLASS_METHODS__TtC9MetricKit14HitchTimeRatio
+ __DATA__TtC9MetricKit14HitchTimeRatio
+ __INSTANCE_METHODS__TtC9MetricKit14HitchTimeRatio
+ __METACLASS_DATA__TtC9MetricKit14HitchTimeRatio
+ _associated conformance 9MetricKit09HitchTimeA0V10CodingKeys33_FD315CFDC4824D66A6FC5270D3174733LLOSHAASQ
+ _associated conformance 9MetricKit09HitchTimeA0V10CodingKeys33_FD315CFDC4824D66A6FC5270D3174733LLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 9MetricKit09HitchTimeA0V10CodingKeys33_FD315CFDC4824D66A6FC5270D3174733LLOs0E3KeyAAs28CustomDebugStringConvertible
+ _objc_msgSend$_terminationCategoryForNamespace:code:signal:
+ _objc_msgSend$cumulativeReducedAccuracyTime
+ _objc_msgSend$decodeInt64ForKey:
+ _objc_msgSend$encodeInt64:forKey:
+ _objc_msgSend$initWithCumulativeBestAccuracyTimeMeasurement:cumulativeBestAccuracyForNavigationTimeMeasurement:nearestTenMetersAccuracyTimeMeasurement:hundredMetersAccuracyTimeMeasurement:kilometerAccuracyTimeMeasurement:threeKilometerAccuracyTimeMeasurement:
+ _objc_msgSend$initWithMetaData:applicationVersion:signpostData:reportedStateData:pid:terminationReason:applicationSpecificInfo:virtualMemoryRegionInfo:exceptionType:exceptionCode:exceptionReason:signal:terminationNamespace:terminationCode:stackTrace:
+ _objc_retain_x4
+ _symbolic _____ 9MetricKit09HitchTimeA0V10CodingKeys33_FD315CFDC4824D66A6FC5270D3174733LLO
+ _symbolic _____ 9MetricKit14HitchTimeRatioC
+ _symbolic _____y_____G 10Foundation11MeasurementV 9MetricKit14HitchTimeRatioC
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit09HitchTimeD0V10CodingKeys33_FD315CFDC4824D66A6FC5270D3174733LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit09HitchTimeD0V10CodingKeys33_FD315CFDC4824D66A6FC5270D3174733LLO
+ _symbolic _____y_____GSg 10Foundation11MeasurementV 9MetricKit14HitchTimeRatioC
+ _symbolic _____y_____GSg_ADt 10Foundation11MeasurementV 9MetricKit14HitchTimeRatioC
- +[MXCrashDiagnostic _resolveTerminationCategoryWithSignal:terminationReason:]
- _OBJC_CLASS_$_NSRegularExpression
- _OBJC_CLASS_$_NSScanner
- _associated conformance 9MetricKit015ScrollHitchTimeA0V10CodingKeys33_03245610228668DEF28556E7C33FDCA3LLOSHAASQ
- _associated conformance 9MetricKit015ScrollHitchTimeA0V10CodingKeys33_03245610228668DEF28556E7C33FDCA3LLOs0F3KeyAAs23CustomStringConvertible
- _associated conformance 9MetricKit015ScrollHitchTimeA0V10CodingKeys33_03245610228668DEF28556E7C33FDCA3LLOs0F3KeyAAs28CustomDebugStringConvertible
- _associated conformance 9MetricKit015ScrollHitchTimeA0VSHAASQ
- _associated conformance 9MetricKit09HitchTimeA0V10CodingKeys011_2B5C7FD179G20A6A18C2E25E0EB7EAAA5LLOSHAASQ
- _associated conformance 9MetricKit09HitchTimeA0V10CodingKeys011_2B5C7FD179G20A6A18C2E25E0EB7EAAA5LLOs0E3KeyAAs23CustomStringConvertible
- _associated conformance 9MetricKit09HitchTimeA0V10CodingKeys011_2B5C7FD179G20A6A18C2E25E0EB7EAAA5LLOs0E3KeyAAs28CustomDebugStringConvertible
- _objc_msgSend$_resolveTerminationCategoryWithSignal:terminationReason:
- _objc_msgSend$firstMatchInString:options:range:
- _objc_msgSend$length
- _objc_msgSend$numberOfRanges
- _objc_msgSend$rangeAtIndex:
- _objc_msgSend$regularExpressionWithPattern:options:error:
- _objc_msgSend$scanHexLongLong:
- _objc_msgSend$scannerWithString:
- _objc_msgSend$scrollHitchTimeRatio
- _objc_msgSend$substringWithRange:
- _objc_msgSend$totalScrollHitchTime
- _objc_msgSend$totalScrollTime
- _symbolic _____ 9MetricKit015ScrollHitchTimeA0V
- _symbolic _____ 9MetricKit015ScrollHitchTimeA0V10CodingKeys33_03245610228668DEF28556E7C33FDCA3LLO
- _symbolic _____ 9MetricKit09HitchTimeA0V10CodingKeys011_2B5C7FD179G20A6A18C2E25E0EB7EAAA5LLO
- _symbolic _____Sg 9MetricKit015ScrollHitchTimeA0V
- _symbolic _____ySo6NSUnitCGSg_AEt 10Foundation11MeasurementV
- _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit015ScrollHitchTimeD0V10CodingKeys33_03245610228668DEF28556E7C33FDCA3LLO
- _symbolic _____y_____G s22KeyedDecodingContainerV 9MetricKit09HitchTimeD0V10CodingKeys011_2B5C7FD179J20A6A18C2E25E0EB7EAAA5LLO
- _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit015ScrollHitchTimeD0V10CodingKeys33_03245610228668DEF28556E7C33FDCA3LLO
- _symbolic _____y_____G s22KeyedEncodingContainerV 9MetricKit09HitchTimeD0V10CodingKeys011_2B5C7FD179J20A6A18C2E25E0EB7EAAA5LLO
CStrings:
+ "cumulativeReducedAccuracyTime"
+ "reducedAccuracy"
+ "terminationCode"
+ "terminationNamespace"
- "domain:(\\d+)\\s+code:0x([0-9A-Fa-f]+)"
- "scrollHitchTimeMetric"
```
