## KeyboardSettingsExtension

> `/System/Library/ExtensionKit/Extensions/KeyboardSettingsExtension.appex/KeyboardSettingsExtension`

```diff

-8100.0.101.0.0
+8103.1.0.0.0
   __TEXT.__text: 0x5208
   __TEXT.__auth_stubs: 0x490
   __TEXT.__cstring: 0x1cf7

   __DATA_CONST.__auth_got: 0x248
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__auth_ptr: 0x450
-  __DATA_CONST.__const: 0x498
+  __DATA_CONST.__const: 0x4d8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x10
   __DATA.__data: 0x1d0

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
   Functions: 151
-  Symbols:   53
+  Symbols:   61
   CStrings:  90
 
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
