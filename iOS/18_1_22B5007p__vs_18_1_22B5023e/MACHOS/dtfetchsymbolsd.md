## dtfetchsymbolsd

> `/usr/libexec/dtfetchsymbolsd`

```diff

 34.0.0.0.0
-  __TEXT.__text: 0x6210
-  __TEXT.__auth_stubs: 0x790
+  __TEXT.__text: 0x6140
+  __TEXT.__auth_stubs: 0x780
   __TEXT.__const: 0x20e
   __TEXT.__cstring: 0x2d0
   __TEXT.__swift5_typeref: 0x10d

   __TEXT.__swift5_types: 0xc
   __TEXT.__unwind_info: 0x1b0
   __TEXT.__eh_frame: 0x118
-  __DATA_CONST.__auth_got: 0x3c8
+  __DATA_CONST.__auth_got: 0x3c0
   __DATA_CONST.__got: 0xb8
   __DATA_CONST.__auth_ptr: 0x120
-  __DATA_CONST.__const: 0x258
+  __DATA_CONST.__const: 0x298
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0xc0
   __DATA.__common: 0xc0

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 122
-  Symbols:   186
+  Symbols:   193
   CStrings:  32
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- _objc_release_x21

```
