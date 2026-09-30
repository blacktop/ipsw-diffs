## SwiftUI

> `/System/Library/Trace/Providers/SwiftUI.bundle/SwiftUI`

```diff

-75.0.0.0.0
-  __TEXT.__text: 0xb8c
-  __TEXT.__auth_stubs: 0x300
-  __TEXT.__objc_methlist: 0x180
+79.0.0.0.0
+  __TEXT.__text: 0xae8
+  __TEXT.__auth_stubs: 0x2e0
+  __TEXT.__objc_stubs: 0x20
+  __TEXT.__objc_methlist: 0x19c
+  __TEXT.__objc_classname: 0x30
+  __TEXT.__objc_methname: 0x1e6
+  __TEXT.__objc_methtype: 0x209
   __TEXT.__const: 0x3a
-  __TEXT.__objc_methname: 0x1a3
-  __TEXT.__cstring: 0xfb
   __TEXT.__constg_swiftt: 0x44
   __TEXT.__swift5_typeref: 0x4c
   __TEXT.__swift5_reflstr: 0x15
   __TEXT.__swift5_fieldmd: 0x34
+  __TEXT.__cstring: 0x2b
   __TEXT.__swift5_types: 0x4
-  __TEXT.__objc_classname: 0x20
-  __TEXT.__objc_methtype: 0x17a
   __TEXT.__unwind_info: 0xa0
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__auth_got: 0x180
-  __DATA_CONST.__got: 0x28
+  __DATA_CONST.__auth_got: 0x178
+  __DATA_CONST.__got: 0x20
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x98
+  __DATA_CONST.__const: 0x90
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA.__objc_const: 0x150
-  __DATA.__objc_selrefs: 0x90
+  __DATA.__objc_const: 0x160
+  __DATA.__objc_selrefs: 0xa0
   __DATA.__objc_data: 0xd0
   __DATA.__data: 0xf8
   __DATA.__bss: 0x20

   - /System/Library/PrivateFrameworks/SwiftUITracingSupport.framework/SwiftUITracingSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1F175D0A-1AC6-3102-AEBC-7B611895DE45
+  UUID: B14D8924-B47A-36D9-8C94-CBDCE61BD584
   Functions: 20
-  Symbols:   290
-  CStrings:  45
+  Symbols:   286
+  CStrings:  46
 
Symbols:
+ /Library/Caches/com.apple.xbs/15D4ADCF-C2CE-4215-A198-100241EB4B96/TemporaryDirectory.BZzj3M/Binaries/SwiftUITracingSupport/install/TempContent/Objects/SwiftUITracingSupport.build/SwiftUITraceProvider.build/Objects-normal/arm64e/SwiftUIProvider.swiftmodule
+ /Library/Caches/com.apple.xbs/15D4ADCF-C2CE-4215-A198-100241EB4B96/TemporaryDirectory.BZzj3M/Binaries/SwiftUITracingSupport/install/TempContent/Objects/SwiftUITracingSupport.build/SwiftUITraceProvider.build/Objects-normal/arm64e/SwiftUITraceProvider.o
+ /Library/Caches/com.apple.xbs/15D4ADCF-C2CE-4215-A198-100241EB4B96/TemporaryDirectory.BZzj3M/Sources/SwiftUITracingSupport/SwiftUITraceProvider/
+ _objc_msgSend$warnWithMessage:
+ _objc_release_x24
+ _objc_retain_x24
- /Library/Caches/com.apple.xbs/Binaries/SwiftUITracingSupport/install/TempContent/Objects/SwiftUITracingSupport.build/SwiftUITraceProvider.build/Objects-normal/arm64e/SwiftUIProvider.swiftmodule
- /Library/Caches/com.apple.xbs/Binaries/SwiftUITracingSupport/install/TempContent/Objects/SwiftUITracingSupport.build/SwiftUITraceProvider.build/Objects-normal/arm64e/SwiftUITraceProvider.o
- /Library/Caches/com.apple.xbs/Sources/SwiftUITracingSupport/SwiftUITraceProvider/
- _$s21SwiftUITracingSupport11TraceConfigV7VersionO2v1yA2EmFWC
- __swift_FORCE_LOAD_$_swiftAccelerate
- __swift_FORCE_LOAD_$_swiftAccelerate_$_SwiftUIProvider
- _objc_release_x23
- _objc_release_x27
- _objc_retain_x23
Functions:
~ _$s15SwiftUIProviderAACfETo : 140 -> 132
~ _$s15SwiftUIProviderAAC18shouldStartTracing13configurationys13OpaquePointerV_tKFTf4dn_n : 828 -> 696
~ _$s15SwiftUIProviderAAC10willFinish7catalog4fileys13OpaquePointerV_AGSgtFTf4dnn_n : 604 -> 580
CStrings:
+ "B32@0:8^{ktrace_target_process=i}16^@24"
+ "SwiftUIProvider"
+ "informWithMessage:"
+ "shouldTargetProcess:error:"
- "while v1 are the future, they're backwards compatible only to V30"

```
