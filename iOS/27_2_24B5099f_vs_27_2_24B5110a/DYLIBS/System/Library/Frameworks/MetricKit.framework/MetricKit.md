## MetricKit

> `/System/Library/Frameworks/MetricKit.framework/MetricKit`

```diff

-369.40.1.0.0
-  __TEXT.__text: 0x82bf8
-  __TEXT.__objc_methlist: 0x290c
-  __TEXT.__const: 0x94b6
-  __TEXT.__cstring: 0x1ed2
+369.40.2.0.0
+  __TEXT.__text: 0x83480
+  __TEXT.__objc_methlist: 0x293c
+  __TEXT.__const: 0x94e6
+  __TEXT.__cstring: 0x1f82
   __TEXT.__gcc_except_tab: 0x18
   __TEXT.__oslogstring: 0x349
-  __TEXT.__swift5_typeref: 0x1938
+  __TEXT.__swift5_typeref: 0x1990
   __TEXT.__swift5_reflstr: 0x1183
   __TEXT.__swift5_assocty: 0x4b0
   __TEXT.__constg_swiftt: 0x143c

   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_proto: 0x94c
   __TEXT.__swift5_types: 0x218
+  __TEXT.__swift5_capture: 0x20
   __TEXT.__swift_as_entry: 0x4
   __TEXT.__swift_as_ret: 0x4
   __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0x2ef0
+  __TEXT.__unwind_info: 0x2f20
   __TEXT.__eh_frame: 0x27e0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x148
+  __DATA_CONST.__const: 0x170
   __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1220
+  __DATA_CONST.__objc_selrefs: 0x1240
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__got: 0x498
-  __AUTH_CONST.__const: 0x4681
-  __AUTH_CONST.__cfstring: 0x1ba0
-  __AUTH_CONST.__objc_const: 0x67f0
-  __AUTH_CONST.__auth_got: 0xa20
+  __AUTH_CONST.__const: 0x4719
+  __AUTH_CONST.__cfstring: 0x1c00
+  __AUTH_CONST.__objc_const: 0x6820
+  __AUTH_CONST.__auth_got: 0xa58
   __AUTH.__objc_data: 0x188
   __AUTH.__data: 0x1c0
-  __DATA.__objc_ivar: 0x43c
-  __DATA.__data: 0x13c0
+  __DATA.__objc_ivar: 0x440
+  __DATA.__data: 0x13d0
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x11b0
   __DATA_DIRTY.__data: 0x1298

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3495
-  Symbols:   2461
-  CStrings:  355
+  Functions: 3509
+  Symbols:   2482
+  CStrings:  360
 
Symbols:
+ -[MXMetricManager _memoryExceptionDiagnosticCountForPayloads:]
+ -[MXMetricManager _reportMemoryDiagnosticsDeliveredForPayloads:]
+ -[MXMetricManager setStateAware:]
+ -[MXMetricManager stateAware]
+ _OBJC_IVAR_$_MXMetricManager._stateAware
+ __Block_copy
+ __Block_release
+ ___33-[MXMetricManager addSubscriber:]_block_invoke_2
+ ___64-[MXMetricManager _reportMemoryDiagnosticsDeliveredForPayloads:]_block_invoke
+ ___block_descriptor_40_e8_32s_e19_"NSDictionary"8?0ls32l8
+ ___swift_closure_destructor
+ _block_copy_helper
+ _block_descriptor
+ _block_destroy_helper
+ _swift_deallocObject
+ _swift_initStackObject
+ _swift_retain_x2
+ _symbolic SDySSSo8NSObjectCGIego_
+ _symbolic SS_So8NSObjectCt
+ _symbolic _____ySSSo8NSObjectCG s18_DictionaryStorageC
+ _symbolic _____ySS_So8NSObjectCtG s23_ContiguousArrayStorageC
CStrings:
+ "com.apple.metrickit.legacyManagerAdopted"
+ "com.apple.metrickit.memoryDiagnosticsDelivered"
+ "com.apple.metrickit.swiftManagerAdopted"
+ "stateReportingDomainCount"
+ "unknown"
```
