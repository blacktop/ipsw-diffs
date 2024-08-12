## textcontextd

> `/usr/libexec/textcontextd`

```diff

 14.0.0.0.0
-  __TEXT.__text: 0x4844
-  __TEXT.__auth_stubs: 0x650
+  __TEXT.__text: 0x481c
+  __TEXT.__auth_stubs: 0x640
   __TEXT.__objc_methlist: 0xc0
   __TEXT.__const: 0xfa
   __TEXT.__objc_methname: 0x32c

   __TEXT.__constg_swiftt: 0x13c
   __TEXT.__swift5_types: 0x10
   __TEXT.__cstring: 0x527
-  __TEXT.__swift5_typeref: 0x100
+  __TEXT.__swift5_typeref: 0xfe
   __TEXT.__swift5_reflstr: 0x39
   __TEXT.__swift5_fieldmd: 0x6c
   __TEXT.__oslogstring: 0x144
   __TEXT.__objc_classname: 0x1f
   __TEXT.__objc_methtype: 0xe9
-  __TEXT.__swift5_capture: 0x118
+  __TEXT.__swift5_capture: 0x168
   __TEXT.__unwind_info: 0x228
   __TEXT.__eh_frame: 0x360
-  __DATA_CONST.__auth_got: 0x328
+  __DATA_CONST.__auth_got: 0x320
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__auth_ptr: 0x50
-  __DATA_CONST.__const: 0x478
+  __DATA_CONST.__const: 0x558
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_const: 0x918
   __DATA.__objc_selrefs: 0xa8
   __DATA.__objc_data: 0x330
-  __DATA.__data: 0x250
+  __DATA.__data: 0x270
   __DATA.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftWebKit.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 115
-  Symbols:   158
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 117
+  Symbols:   165
   CStrings:  96
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- _objc_retain_x23

```
