## DocumentAppShortcuts

> `/System/Library/ExtensionKit/Extensions/DocumentAppShortcuts.appex/DocumentAppShortcuts`

```diff

-332.0.0.0.0
+335.1.0.0.0
   __TEXT.__text: 0x195c
   __TEXT.__auth_stubs: 0x2d0
   __TEXT.__const: 0x2ae

   __DATA_CONST.__auth_got: 0x168
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__auth_ptr: 0x160
-  __DATA_CONST.__const: 0x140
+  __DATA_CONST.__const: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0xb0
   __DATA.__common: 0x50

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
   Functions: 42
-  Symbols:   44
+  Symbols:   52
   CStrings:  10
 
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
