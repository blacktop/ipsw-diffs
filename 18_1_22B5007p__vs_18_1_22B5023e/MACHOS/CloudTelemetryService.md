## CloudTelemetryService

> `/System/Library/PrivateFrameworks/CloudTelemetry.framework/XPCServices/CloudTelemetryService.xpc/CloudTelemetryService`

```diff

-2200.142.0.0.0
-  __TEXT.__text: 0x804f4
-  __TEXT.__auth_stubs: 0x2230
-  __TEXT.__objc_stubs: 0x300
+2200.144.0.0.0
+  __TEXT.__text: 0x881c0
+  __TEXT.__auth_stubs: 0x2220
+  __TEXT.__objc_stubs: 0x320
   __TEXT.__objc_methlist: 0x44
-  __TEXT.__const: 0x3adc
+  __TEXT.__const: 0x3bac
   __TEXT.__gcc_except_tab: 0x80
-  __TEXT.__cstring: 0x3145
+  __TEXT.__cstring: 0x30e5
   __TEXT.__objc_classname: 0x82
-  __TEXT.__objc_methname: 0x909
+  __TEXT.__objc_methname: 0x931
   __TEXT.__objc_methtype: 0x220
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__oslogstring: 0x18b7
-  __TEXT.__swift5_typeref: 0x11ff
-  __TEXT.__constg_swiftt: 0x16a8
-  __TEXT.__swift5_reflstr: 0xe65
-  __TEXT.__swift5_fieldmd: 0x18dc
-  __TEXT.__swift5_capture: 0x31c
+  __TEXT.__oslogstring: 0x19d7
+  __TEXT.__swift5_typeref: 0x1287
+  __TEXT.__constg_swiftt: 0x16d0
+  __TEXT.__swift5_reflstr: 0xef5
+  __TEXT.__swift5_fieldmd: 0x1928
+  __TEXT.__swift5_capture: 0xa80
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_assocty: 0x128
-  __TEXT.__swift5_proto: 0x3bc
-  __TEXT.__swift5_types: 0x1ec
+  __TEXT.__swift5_proto: 0x3c4
+  __TEXT.__swift5_types: 0x1f4
   __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x2180
-  __TEXT.__eh_frame: 0x4b7c
-  __DATA_CONST.__auth_got: 0x1128
+  __TEXT.__unwind_info: 0x2240
+  __TEXT.__eh_frame: 0x4d24
+  __DATA_CONST.__auth_got: 0x1120
   __DATA_CONST.__got: 0x4e0
-  __DATA_CONST.__auth_ptr: 0x5b0
-  __DATA_CONST.__const: 0x3860
-  __DATA_CONST.__cfstring: 0x100
+  __DATA_CONST.__auth_ptr: 0x578
+  __DATA_CONST.__const: 0x4bc8
+  __DATA_CONST.__cfstring: 0x120
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA.__objc_const: 0x1d10
-  __DATA.__objc_selrefs: 0x258
+  __DATA.__objc_selrefs: 0x260
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x230
-  __DATA.__data: 0x2770
-  __DATA.__bss: 0x61e8
-  __DATA.__common: 0x268
+  __DATA.__data: 0x27f0
+  __DATA.__bss: 0x62f8
+  __DATA.__common: 0x270
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2313
-  Symbols:   336
-  CStrings:  584
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 2478
+  Symbols:   342
+  CStrings:  587
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- _swift_taskGroup_destroy
- _swift_taskGroup_initialize
CStrings:
+ "failed writing sendOneMessage to transparency log %!{(MISSING)public}s:%!{(MISSING)public}s for backend %!{(MISSING)public}s with error %!{(MISSING)public}s"
+ "mock error"
+ "reporting disabled due to failure setting up session coordinator. %!{(MISSING)public}s"
+ "reporting disabled due to startup failure."
+ "setApplicationBundleIdentifierOverride:"
+ "unable to register: %!s(MISSING), nil bundleIdentifier"
+ "writing sendOneMessage to transparency log %!{(MISSING)public}s:%!{(MISSING)public}s for backend %!{(MISSING)public}s"
- "CloudTelemetryService/StorebagCache.swift"
- "mockSubdirectoryCacheWithNameCrash"
- "reporting disabled due to startup failure"
- "writing sendOneMessage to transparency log %!{(MISSING)public}s:%!{(MISSING)public}s"

```
