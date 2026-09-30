## webinspectord

> `/usr/libexec/webinspectord`

```diff

-7621.2.5.10.10
-  __TEXT.__text: 0x998
-  __TEXT.__auth_stubs: 0x270
+7622.1.14.10.4
+  __TEXT.__text: 0x9c8
+  __TEXT.__auth_stubs: 0x290
   __TEXT.__objc_stubs: 0xa0
   __TEXT.__objc_methlist: 0x44
   __TEXT.__cstring: 0xb9

   __TEXT.__swift5_capture: 0x10
   __TEXT.__swift5_types: 0x4
   __TEXT.__unwind_info: 0xb0
-  __DATA_CONST.__auth_got: 0x140
+  __DATA_CONST.__auth_got: 0x150
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x138
+  __DATA_CONST.__const: 0x140
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
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
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 7B50E0E4-02BA-3781-9553-D66F41D4C4C6
-  Functions: 20
-  Symbols:   78
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: 6AB76B73-807E-357A-A44C-7104A9202E5D
+  Functions: 21
+  Symbols:   81
   CStrings:  23
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swiftsimd
+ _swift_deallocClassInstance
+ _swift_setDeallocating
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd

```
