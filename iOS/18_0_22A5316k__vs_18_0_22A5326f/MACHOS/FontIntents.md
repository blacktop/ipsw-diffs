## FontIntents

> `/System/Library/ExtensionKit/Extensions/FontIntents.appex/FontIntents`

```diff

-134.0.0.0.0
+136.0.0.0.0
   __TEXT.__text: 0x21a4
   __TEXT.__auth_stubs: 0x320
   __TEXT.__const: 0x592

   __DATA_CONST.__auth_got: 0x190
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__auth_ptr: 0x328
-  __DATA_CONST.__const: 0x1d8
+  __DATA_CONST.__const: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x138
   __DATA.__bss: 0xb20

   - /usr/lib/swift/libswiftQuartzCore.dylib
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
   Functions: 105
-  Symbols:   40
+  Symbols:   48
   CStrings:  5
 
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
