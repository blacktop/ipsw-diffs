## healthrecordsd

> `/System/Library/PrivateFrameworks/HealthRecordServices.framework/healthrecordsd`

```diff

-5132.0.0.0.0
+5200.1.3.0.0
   __TEXT.__text: 0x6c
   __TEXT.__auth_stubs: 0x80
   __TEXT.__cstring: 0x19

   __TEXT.__unwind_info: 0x58
   __DATA_CONST.__auth_got: 0x40
   __DATA_CONST.__got: 0x8
-  __DATA_CONST.__const: 0x68
+  __DATA_CONST.__const: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__common: 0x8
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 1
-  Symbols:   24
+  Symbols:   32
   CStrings:  1
 
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