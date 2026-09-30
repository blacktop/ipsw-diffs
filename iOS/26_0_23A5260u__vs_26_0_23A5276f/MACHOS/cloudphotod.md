## cloudphotod

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/Support/cloudphotod`

```diff

-800.14.111.0.0
-  __TEXT.__text: 0x1c3188
+800.20.101.0.0
+  __TEXT.__text: 0x1c3a64
   __TEXT.__auth_stubs: 0x1ac0
-  __TEXT.__objc_stubs: 0x1b9c0
-  __TEXT.__objc_methlist: 0xfd5c
-  __TEXT.__cstring: 0x1b05c
-  __TEXT.__objc_classname: 0x2882
-  __TEXT.__objc_methname: 0x28609
-  __TEXT.__objc_methtype: 0x84d3
+  __TEXT.__objc_stubs: 0x1bac0
+  __TEXT.__objc_methlist: 0xfd64
+  __TEXT.__cstring: 0x1b0f6
+  __TEXT.__objc_classname: 0x2880
+  __TEXT.__objc_methname: 0x28765
+  __TEXT.__objc_methtype: 0x84e4
   __TEXT.__const: 0x7890
   __TEXT.__gcc_except_tab: 0x33cc
-  __TEXT.__oslogstring: 0x10715
+  __TEXT.__oslogstring: 0x107bc
   __TEXT.__swift5_typeref: 0x182f
   __TEXT.__swift5_reflstr: 0x1f67
   __TEXT.__swift5_assocty: 0x378

   __TEXT.__swift5_types: 0x158
   __TEXT.__swift5_capture: 0x348
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__unwind_info: 0x6db8
+  __TEXT.__unwind_info: 0x6dd8
   __TEXT.__eh_frame: 0x1668
   __DATA_CONST.__auth_got: 0xd70
-  __DATA_CONST.__got: 0xc50
+  __DATA_CONST.__got: 0xc58
   __DATA_CONST.__auth_ptr: 0x398
-  __DATA_CONST.__const: 0xa220
-  __DATA_CONST.__cfstring: 0x11880
+  __DATA_CONST.__const: 0xa250
+  __DATA_CONST.__cfstring: 0x118e0
   __DATA_CONST.__objc_classlist: 0x6a0
   __DATA_CONST.__objc_catlist: 0x190
   __DATA_CONST.__objc_protolist: 0x448

   __DATA_CONST.__objc_floatobj: 0x60
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x1c5a8
-  __DATA.__objc_selrefs: 0x86b0
-  __DATA.__objc_ivar: 0x122c
+  __DATA.__objc_const: 0x1c5e8
+  __DATA.__objc_selrefs: 0x86f8
+  __DATA.__objc_ivar: 0x1234
   __DATA.__objc_data: 0x43e8
   __DATA.__data: 0x6b98
-  __DATA.__bss: 0xddf0
+  __DATA.__bss: 0xde00
   __DATA.__common: 0x6f0
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6D39FA46-0074-3F02-B11B-EA97366DB742
-  Functions: 9928
-  Symbols:   957
-  CStrings:  13753
+  UUID: 378697AA-B93F-3A78-BE5E-E2F72B4E5C93
+  Functions: 9935
+  Symbols:   954
+  CStrings:  13775
 
Symbols:
+ _OBJC_CLASS_$_BGSystemTaskThroughputMetrics
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
CStrings:
+ "'%@' task finished work, started: %@, itemCount: %lu"
+ "'%@': %@, Can't register throughput tracking"
+ "'%@': %@, Couldn't deregister metrics"
+ "CloudKit operation has been cancelled by caller"
+ "CloudKit operation has been deferred by system"
+ "Unexpected error domain for %@"
+ "_activeThroughputMetrics"
+ "_sessionIsNonDiscretionary"
+ "addItemCount:"
+ "daemon.cloudkitrescheduler.bgst.activity"
+ "deregisterThroughputTrackingFor:withEndTime:error:"
+ "initWithIdentifier:qos:workloadCategory:expectedMetricValue:"
+ "metricsIdentifier"
+ "mingled, scopeIndex, transientType"
+ "no throughput"
+ "numberWithUnsignedInt:"
+ "performanceMetricIdentifier"
+ "registerThroughputTrackingFor:withStartTime:error:"
+ "reportThroughputWorkForMetrics:itemCount:done:"
+ "scopeIndex = %ld AND identifier = %@ AND +mingled = %i"
+ "scopeIndex, mingled, class, transientType"
+ "startTime"
+ "v36@0:8@16Q24B32"
- "CloudKit operation has been cancelled by user"
- "mingled, scopeIndex"
- "scopeIndex = %ld AND identifier = %@ AND mingled = %i"
- "shouldBeDiscretionary"
- "transientType, mingled, class, scopeIndex"

```
