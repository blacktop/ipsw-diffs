## SettingsSOSAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/SettingsSOSAppIntentsExtension.appex/SettingsSOSAppIntentsExtension`

```diff

-537.100.11.0.0
-  __TEXT.__text: 0x41b0
+630.200.11.0.0
+  __TEXT.__text: 0x4198
   __TEXT.__auth_stubs: 0x460
   __TEXT.__const: 0x7c2
   __TEXT.__cstring: 0x4fd

   __DATA_CONST.__auth_got: 0x230
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__auth_ptr: 0x440
-  __DATA_CONST.__const: 0x320
+  __DATA_CONST.__const: 0x360
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x20
   __DATA.__data: 0x1d8

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
   Functions: 162
-  Symbols:   52
+  Symbols:   60
   CStrings:  25
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "/"
- "root"

```