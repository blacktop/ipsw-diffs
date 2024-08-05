## DoNotDisturbAppIntents

> `/System/Library/ExtensionKit/Extensions/DoNotDisturbAppIntents.appex/DoNotDisturbAppIntents`

```diff

-429.0.0.0.0
+431.1.3.0.0
   __TEXT.__text: 0xce44
   __TEXT.__auth_stubs: 0xb30
   __TEXT.__const: 0xe8c

   __DATA_CONST.__auth_got: 0x598
   __DATA_CONST.__got: 0x158
   __DATA_CONST.__auth_ptr: 0x530
-  __DATA_CONST.__const: 0x418
+  __DATA_CONST.__const: 0x458
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x80
   __DATA.__data: 0x3c0

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
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
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 325
-  Symbols:   107
+  Symbols:   115
   CStrings:  73
 
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
