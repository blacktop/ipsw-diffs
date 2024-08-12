## applicensedeliveryd

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/applicensedeliveryd`

```diff

-2.0.37.0.0
+2.0.42.0.0
   __TEXT.__text: 0xe04
   __TEXT.__auth_stubs: 0x2d0
   __TEXT.__objc_stubs: 0x120

   __TEXT.__unwind_info: 0xa0
   __DATA_CONST.__auth_got: 0x170
   __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0xe8
+  __DATA_CONST.__const: 0x128
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

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
   Functions: 20
-  Symbols:   70
+  Symbols:   78
   CStrings:  59
 
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
