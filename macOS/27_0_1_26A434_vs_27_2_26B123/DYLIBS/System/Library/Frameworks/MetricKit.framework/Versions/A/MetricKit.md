## MetricKit

> `/System/Library/Frameworks/MetricKit.framework/Versions/A/MetricKit`

```diff

-367.0.0.0.0
-  __TEXT.__text: 0x7be8c
-  __TEXT.__objc_methlist: 0x290c
-  __TEXT.__const: 0x8d66
-  __TEXT.__cstring: 0x1ec2
+369.40.2.0.0
+  __TEXT.__text: 0x869cc
+  __TEXT.__objc_methlist: 0x293c
+  __TEXT.__const: 0x94d6
+  __TEXT.__cstring: 0x1f82
   __TEXT.__gcc_except_tab: 0x18
   __TEXT.__oslogstring: 0x349
-  __TEXT.__swift5_typeref: 0x1822
+  __TEXT.__swift5_typeref: 0x192e
   __TEXT.__swift5_reflstr: 0x1183
   __TEXT.__swift5_assocty: 0x4b0
   __TEXT.__constg_swiftt: 0x143c
   __TEXT.__swift5_fieldmd: 0x1c30
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_proto: 0x8c4
+  __TEXT.__swift5_proto: 0x94c
   __TEXT.__swift5_types: 0x218
+  __TEXT.__swift5_capture: 0x20
   __TEXT.__swift_as_entry: 0x4
   __TEXT.__swift_as_ret: 0x4
   __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0x2340
-  __TEXT.__eh_frame: 0x27b8
+  __TEXT.__unwind_info: 0x2558
+  __TEXT.__eh_frame: 0x27e0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1220
+  __DATA_CONST.__objc_selrefs: 0x1240
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x178
-  __DATA_CONST.__got: 0x480
-  __AUTH_CONST.__const: 0x46e1
-  __AUTH_CONST.__cfstring: 0x1ba0
-  __AUTH_CONST.__objc_const: 0x6738
-  __AUTH_CONST.__auth_got: 0x888
+  __DATA_CONST.__got: 0x498
+  __AUTH_CONST.__const: 0x47a9
+  __AUTH_CONST.__cfstring: 0x1c00
+  __AUTH_CONST.__objc_const: 0x6768
+  __AUTH_CONST.__auth_got: 0x8e0
   __AUTH_CONST.__auth_ptr: 0x5d0
   __AUTH.__objc_data: 0x188
   __AUTH.__data: 0x1c0
-  __DATA.__objc_ivar: 0x43c
-  __DATA.__data: 0x1190
-  __DATA.__bss: 0x12720
+  __DATA.__objc_ivar: 0x440
+  __DATA.__data: 0x13a0
+  __DATA.__bss: 0x13820
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x11b0
   __DATA_DIRTY.__data: 0x1280

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3311
-  Symbols:   2754
-  CStrings:  354
+  Functions: 3511
+  Symbols:   2802
+  CStrings:  360
 
Symbols:
+ -[MXMetricManager _memoryExceptionDiagnosticCountForPayloads:]
+ -[MXMetricManager _reportMemoryDiagnosticsDeliveredForPayloads:]
+ -[MXMetricManager setStateAware:]
+ -[MXMetricManager stateAware]
+ OBJC_IVAR_$_MXMetricManager._stateAware
+ __Block_copy
+ __Block_release
+ ___33-[MXMetricManager addSubscriber:]_block_invoke_2
+ ___64-[MXMetricManager _reportMemoryDiagnosticsDeliveredForPayloads:]_block_invoke
+ ___block_descriptor_40_e8_32s_e19_"NSDictionary"8?0l
+ ___copy_helper_block_e8_32s
+ ___destroy_helper_block_e8_32s
+ ___swift_closure_destructor
+ __swift_closure_destructor
+ _associated conformance 9MetricKit0A6ReportV10StateEntryVSHAASQ
+ _associated conformance 9MetricKit0A6ReportV11EnvironmentVSHAASQ
+ _associated conformance 9MetricKit0A6ReportV13IntervalEntryVSHAASQ
+ _associated conformance 9MetricKit0A6ReportVSHAASQ
+ _associated conformance 9MetricKit0A6ResultOSHAASQ
+ _associated conformance 9MetricKit14HangDiagnosticVSHAASQ
+ _associated conformance 9MetricKit14SignpostRecordVSHAASQ
+ _associated conformance 9MetricKit15CrashDiagnosticV25ObjectiveCExceptionReasonVSHAASQ
+ _associated conformance 9MetricKit15CrashDiagnosticVSHAASQ
+ _associated conformance 9MetricKit16DiagnosticReportV11EnvironmentVSHAASQ
+ _associated conformance 9MetricKit16DiagnosticReportVSHAASQ
+ _associated conformance 9MetricKit16DiagnosticResultOSHAASQ
+ _associated conformance 9MetricKit19AppLaunchDiagnosticVSHAASQ
+ _associated conformance 9MetricKit22CPUExceptionDiagnosticVSHAASQ
+ _associated conformance 9MetricKit25MemoryExceptionDiagnosticVSHAASQ
+ _associated conformance 9MetricKit28DiskWriteExceptionDiagnosticVSHAASQ
+ _associated conformance 9MetricKit9OSVersionVSHAASQ
+ _block_copy_helper
+ _block_descriptor
+ _block_destroy_helper
+ _objc_msgSend$_memoryExceptionDiagnosticCountForPayloads:
+ _objc_msgSend$_reportMemoryDiagnosticsDeliveredForPayloads:
+ _objc_msgSend$stateAware
+ _swift_deallocObject
+ _swift_getTupleTypeMetadata2
+ _swift_initStackObject
+ _symbolic SDySSSo8NSObjectCGIego_
+ _symbolic SS_So8NSObjectCt
+ _symbolic _____Sg_ABt 9MetricKit0A6ReportV11EnvironmentV
+ _symbolic _____Sg_ABt 9MetricKit15CrashDiagnosticV25ObjectiveCExceptionReasonV
+ _symbolic ______AAt 9MetricKit0A6ResultO
+ _symbolic ______AAt 9MetricKit16DiagnosticResultO
+ _symbolic _____ySSSo8NSObjectCG s18_DictionaryStorageC
+ _symbolic _____ySS_So8NSObjectCtG s23_ContiguousArrayStorageC
CStrings:
+ "com.apple.metrickit.legacyManagerAdopted"
+ "com.apple.metrickit.memoryDiagnosticsDelivered"
+ "com.apple.metrickit.swiftManagerAdopted"
+ "key value "
+ "stateReportingDomainCount"
+ "unknown"
```
