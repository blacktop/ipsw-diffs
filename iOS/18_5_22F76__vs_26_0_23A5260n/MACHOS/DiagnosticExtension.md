## DiagnosticExtension

> `/System/Library/PrivateFrameworks/IntelligencePlatform.framework/PlugIns/DiagnosticExtension.appex/DiagnosticExtension`

```diff

-124.19.0.1.0
-  __TEXT.__text: 0x1bdc
-  __TEXT.__auth_stubs: 0x400
+146.101.0.0.0
+  __TEXT.__text: 0x1b04
+  __TEXT.__auth_stubs: 0x3d0
   __TEXT.__objc_stubs: 0x60
   __TEXT.__objc_methlist: 0x68
-  __TEXT.__const: 0xc8
+  __TEXT.__const: 0xc0
   __TEXT.__cstring: 0x9f
-  __TEXT.__objc_methname: 0x137
+  __TEXT.__objc_methname: 0x156
   __TEXT.__constg_swiftt: 0x6c
   __TEXT.__swift5_typeref: 0x2e
   __TEXT.__swift5_fieldmd: 0x20
-  __TEXT.__oslogstring: 0x1f4
+  __TEXT.__oslogstring: 0x284
   __TEXT.__swift5_types: 0x8
   __TEXT.__objc_classname: 0x2c
   __TEXT.__objc_methtype: 0x36
-  __TEXT.__unwind_info: 0xf0
-  __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0x208
+  __TEXT.__unwind_info: 0xf8
+  __TEXT.__eh_frame: 0x58
+  __DATA_CONST.__auth_got: 0x1f0
   __DATA_CONST.__got: 0x58
-  __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x148
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__const: 0x158
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0x100
-  __DATA.__objc_selrefs: 0x58
+  __DATA.__objc_selrefs: 0x60
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x110
   __DATA.__data: 0x48

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
+  - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 33D0CA63-4729-3650-BB6D-EDE375A9FA16
-  Functions: 53
-  Symbols:   93
-  CStrings:  32
+  UUID: 61DD67D6-809B-3F20-9F06-33795614D262
+  Functions: 64
+  Symbols:   87
+  CStrings:  35
 
Symbols:
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftMLCompute
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- ___chkstk_darwin
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _objc_release_x24
- _objc_release_x25
- _objc_release_x26
CStrings:
+ "Failed to collect event view diagnostic data: %s"
+ "Skipping collection of event view diagnostic data because user did not consent"
+ "eventViewDiagnosticsWithError:"

```
