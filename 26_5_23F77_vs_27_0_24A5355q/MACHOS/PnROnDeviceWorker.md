## PnROnDeviceWorker

> `/System/Library/ExtensionKit/Extensions/PnROnDeviceWorker.appex/PnROnDeviceWorker`

```diff

-3525.5.1.0.0
-  __TEXT.__text: 0x29a8
-  __TEXT.__auth_stubs: 0x540
-  __TEXT.__const: 0x15a
+3600.17.3.0.0
+  __TEXT.__text: 0x49e0
+  __TEXT.__auth_stubs: 0xa50
+  __TEXT.__const: 0x1da
   __TEXT.__swift5_entry: 0x8
   __TEXT.__objc_classname: 0x2b
-  __TEXT.__constg_swiftt: 0x68
-  __TEXT.__swift5_typeref: 0x73
-  __TEXT.__swift5_fieldmd: 0x10
-  __TEXT.__swift5_reflstr: 0xe
+  __TEXT.__objc_methname: 0x1a
+  __TEXT.__objc_methtype: 0x1
+  __TEXT.__constg_swiftt: 0x88
+  __TEXT.__swift5_typeref: 0xb7
+  __TEXT.__swift5_reflstr: 0x28
+  __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__oslogstring: 0x139
-  __TEXT.__cstring: 0x5f
+  __TEXT.__oslogstring: 0x47f
+  __TEXT.__cstring: 0xaf
+  __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x4
-  __TEXT.__swift_as_entry: 0x14
-  __TEXT.__swift_as_ret: 0x10
-  __TEXT.__unwind_info: 0x100
-  __TEXT.__eh_frame: 0x140
-  __DATA_CONST.__auth_got: 0x2a0
-  __DATA_CONST.__got: 0x60
-  __DATA_CONST.__auth_ptr: 0x90
-  __DATA_CONST.__const: 0xa8
+  __TEXT.__swift_as_entry: 0x20
+  __TEXT.__swift_as_ret: 0x1c
+  __TEXT.__swift_as_cont: 0x24
+  __TEXT.__unwind_info: 0x158
+  __TEXT.__eh_frame: 0x288
+  __DATA_CONST.__const: 0xf8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x90
-  __DATA.__data: 0xe8
+  __DATA_CONST.__auth_got: 0x528
+  __DATA_CONST.__got: 0x70
+  __DATA_CONST.__auth_ptr: 0xa0
+  __DATA.__objc_const: 0xb8
+  __DATA.__data: 0x130
   __DATA.__bss: 0x108
   __DATA.__common: 0x18
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/AIMLInstrumentationStreams.framework/AIMLInstrumentationStreams
   - /System/Library/PrivateFrameworks/LighthouseBackground.framework/LighthouseBackground
   - /System/Library/PrivateFrameworks/PnROnDeviceFramework.framework/PnROnDeviceFramework
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D86A6C6F-B908-3D9F-BB21-C43D185E6027
-  Functions: 39
-  Symbols:   68
-  CStrings:  11
+  UUID: B64CD164-4094-33E1-9D11-26C69BB51343
+  Functions: 54
+  Symbols:   83
+  CStrings:  28
 
Symbols:
+ _OBJC_CLASS_$_OS_os_log
+ _objc_release_x27
+ _objc_retain_x21
+ _swift_bridgeObjectRelease_n
+ _swift_deallocObject
+ _swift_getObjCClassMetadata
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x24
+ _swift_release_x8
+ _swift_release_x9
+ _swift_retain_x19
+ _swift_retain_x24
+ _swift_retain_x8
+ _swift_task_create
+ _swift_unknownObjectRelease
- _objc_retain_x19
CStrings:
+ "%s"
+ "All component invocation metric processing failed: %ld upload failures, %ld provider errors"
+ "Component invocation had %ld provider errors, triggering ABC"
+ "Component invocation had %ld upload errors, triggering ABC"
+ "Component invocation metrics processing complete with %ld upload failures, %ld provider errors"
+ "Finished processing %ld Providers for turn %s"
+ "PNRODComponentInvocation"
+ "Partial success: %ld uploaded, %ld upload failures, %ld provider errors"
+ "Processing turn %ld/%ld, turnId: %s"
+ "Received %ld turns for component invocation processing"
+ "Running tasks for provider"
+ "Starting component invocation metrics processing"
+ "Task cancelled while processing turn %ld"
+ "TaskId: %s, TaskName: %s: Component invocation task cancelled"
+ "Using %ld component metric providers"
+ "componentMetricsProviders"
+ "doWorkComponentInvocationMetrics"

```
