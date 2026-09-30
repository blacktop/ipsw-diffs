## Stateful

> `/System/Library/PrivateFrameworks/Stateful.framework/Stateful`

```diff

-175.0.4.0.0
+175.0.6.0.0
   __TEXT.__text: 0xd5cc
   __TEXT.__auth_stubs: 0x900
   __TEXT.__objc_methlist: 0x20

   __TEXT.__unwind_info: 0x438
   __TEXT.__objc_methname: 0x37
   __DATA_CONST.__got: 0x138
-  __DATA_CONST.__const: 0x190
+  __DATA_CONST.__const: 0x1d0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x28
   __AUTH_CONST.__auth_got: 0x480

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
   Functions: 381
-  Symbols:   109
+  Symbols:   117
   CStrings:  41
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd

```
