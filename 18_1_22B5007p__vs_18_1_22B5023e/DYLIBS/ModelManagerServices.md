## ModelManagerServices

> `/System/Library/PrivateFrameworks/ModelManagerServices.framework/ModelManagerServices`

```diff

-121.0.0.0.0
-  __TEXT.__text: 0x102150
-  __TEXT.__auth_stubs: 0x1750
+122.40.6.0.0
+  __TEXT.__text: 0x109eb4
+  __TEXT.__auth_stubs: 0x1760
   __TEXT.__objc_methlist: 0x44
-  __TEXT.__const: 0xf1f8
-  __TEXT.__cstring: 0x2406
-  __TEXT.__oslogstring: 0x1674
-  __TEXT.__swift5_typeref: 0x42f4
-  __TEXT.__swift5_capture: 0x780
-  __TEXT.__swift5_fieldmd: 0x3360
-  __TEXT.__constg_swiftt: 0x3700
-  __TEXT.__swift5_reflstr: 0x1b55
+  __TEXT.__const: 0xff78
+  __TEXT.__cstring: 0x2646
+  __TEXT.__oslogstring: 0x17c4
+  __TEXT.__swift5_typeref: 0x4684
+  __TEXT.__swift5_capture: 0x784
+  __TEXT.__swift5_fieldmd: 0x360c
+  __TEXT.__constg_swiftt: 0x3a10
+  __TEXT.__swift5_reflstr: 0x1ce5
   __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_protos: 0x5c
-  __TEXT.__swift5_proto: 0x101c
-  __TEXT.__swift5_types: 0x46c
+  __TEXT.__swift5_protos: 0x60
+  __TEXT.__swift5_proto: 0x10fc
+  __TEXT.__swift5_types: 0x4b0
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__swift5_assocty: 0x6d8
-  __TEXT.__unwind_info: 0x5a98
-  __TEXT.__eh_frame: 0xd2b8
+  __TEXT.__swift5_assocty: 0x760
+  __TEXT.__unwind_info: 0x5ef8
+  __TEXT.__eh_frame: 0xda20
   __TEXT.__objc_classname: 0x18
   __TEXT.__objc_methname: 0x234
   __TEXT.__objc_methtype: 0xad
-  __DATA_CONST.__got: 0x3c8
-  __DATA_CONST.__const: 0x1a8
-  __DATA_CONST.__objc_classlist: 0x90
+  __DATA_CONST.__got: 0x3f8
+  __DATA_CONST.__const: 0x1e8
+  __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x68
   __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0xba8
-  __AUTH_CONST.__auth_ptr: 0x830
-  __AUTH_CONST.__const: 0x7718
-  __AUTH_CONST.__objc_const: 0x16d0
-  __AUTH.__data: 0x578
-  __DATA.__data: 0x4270
-  __DATA.__bss: 0x1c720
+  __AUTH_CONST.__auth_got: 0xbb0
+  __AUTH_CONST.__auth_ptr: 0x870
+  __AUTH_CONST.__const: 0x7c50
+  __AUTH_CONST.__objc_const: 0x18b8
+  __AUTH.__objc_data: 0x50
+  __AUTH.__data: 0x308
+  __DATA.__data: 0x3b98
+  __DATA.__bss: 0x18f20
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x250
-  __DATA_DIRTY.__data: 0x2fe8
-  __DATA_DIRTY.__common: 0x30
-  __DATA_DIRTY.__bss: 0x3380
+  __DATA_DIRTY.__data: 0x3fa8
+  __DATA_DIRTY.__common: 0x48
+  __DATA_DIRTY.__bss: 0x8700
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CollectionsInternal.framework/CollectionsInternal

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 7609
-  Symbols:   1864
-  CStrings:  430
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 7893
+  Symbols:   1862
+  CStrings:  453
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- _swift_continuation_await
- _swift_continuation_init
CStrings:
+ ", try again later"
+ "Can't retry modelmanagerd connection. Inference monitor cannot be restored."
+ "Failed to restore inference monitor: %!@(MISSING)"
+ "InferenceMonitor received event: %!s(MISSING)"
+ "InferenceMonitor received unexpected incoming XPC request: %!@(MISSING)"
+ "Inferences Not Running"
+ "Inferences Running"
+ "Not executed due to current system state "
+ "Stream found to be cancelled due to policy change. Throwing deniedDueToSpecifiedSystemState."
+ "_TtCV20ModelManagerServices16InferenceMonitor13AsyncIterator"
+ "_TtCVV20ModelManagerServices16InferenceMonitor17DaemonEventSource7Handler"
+ "assetVersionMismatch"
+ "continuation"
+ "deniedDueToSpecifiedSystemState"
+ "endpoint"
+ "inferencesNotRunning"
+ "inferencesRunning"
+ "invalidator"
+ "lastEvent"
+ "source"
+ "specificPolicyChange"
+ "startMonitoringInferences"
+ "xpc session cache eviction"

```
