## PnROnDeviceWorker

> `/System/Library/ExtensionKit/Extensions/PnROnDeviceWorker.appex/PnROnDeviceWorker`

```diff

-3400.20.1.0.0
-  __TEXT.__text: 0x2218
-  __TEXT.__auth_stubs: 0x500
-  __TEXT.__const: 0xf6
+3402.20.1.0.0
+  __TEXT.__text: 0x38d0
+  __TEXT.__auth_stubs: 0x6c0
+  __TEXT.__const: 0x116
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__cstring: 0x2f0
-  __TEXT.__constg_swiftt: 0x70
-  __TEXT.__swift5_typeref: 0x5b
+  __TEXT.__cstring: 0x3d0
+  __TEXT.__constg_swiftt: 0x68
+  __TEXT.__swift5_typeref: 0xa1
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_reflstr: 0xe
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__oslogstring: 0x1b9
+  __TEXT.__oslogstring: 0x1f9
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0xe8
-  __TEXT.__eh_frame: 0x130
-  __DATA_CONST.__auth_got: 0x280
-  __DATA_CONST.__got: 0x30
-  __DATA_CONST.__auth_ptr: 0x78
+  __TEXT.__unwind_info: 0x118
+  __TEXT.__eh_frame: 0x1a8
+  __DATA_CONST.__auth_got: 0x360
+  __DATA_CONST.__got: 0xb8
+  __DATA_CONST.__auth_ptr: 0xa0
   __DATA_CONST.__const: 0xd0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90
-  __DATA.__data: 0x108
+  __DATA.__data: 0x138
   __DATA.__bss: 0x110
   __DATA.__common: 0x18
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/LighthouseBackground.framework/LighthouseBackground
+  - /System/Library/PrivateFrameworks/LighthouseDataProcessor.framework/LighthouseDataProcessor
   - /System/Library/PrivateFrameworks/PnROnDeviceFramework.framework/PnROnDeviceFramework
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 36
-  Symbols:   74
-  CStrings:  27
+  Functions: 47
+  Symbols:   83
+  CStrings:  32
 
Symbols:
+ ___chkstk_darwin
+ _objc_release_x23
+ _objc_release_x28
+ _objc_release_x8
+ _objc_retain_x20
+ _objc_retain_x21
+ _swift_allocBox
+ _swift_arrayInitWithCopy
+ _swift_beginAccess
CStrings:
+ "IEActionGrain SELF Upload Failed"
+ "IEPlannerGrain SELF Upload Failed"
+ "IERequestGrain SELF Upload Failed"
+ "No Session objects buildable from Biome"
+ "PnROnDeviceWorker doWork end %!@(MISSING)"
+ "PnROnDeviceWorker doWork start"
+ "PnROnDeviceWorker init"
+ "PnROnDeviceWorker retrieving sessionized data for IE metrics"
+ "Use platform managed bookmark with unique PnRMetricsWorker domain"
- "PnROnDeviceWoker"
- "PnROnDeviceWorker starts doing work"
- "Start init()"
- "com.apple.lighthouse.pnr"

```
