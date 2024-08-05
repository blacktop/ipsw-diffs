## AmbientSettingsAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/AmbientSettingsAppIntentsExtension.appex/AmbientSettingsAppIntentsExtension`

```diff

-72.0.0.0.0
+74.0.0.0.0
   __TEXT.__text: 0x2e20
   __TEXT.__auth_stubs: 0x360
   __TEXT.__const: 0x66a

   __DATA_CONST.__auth_got: 0x1b0
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__auth_ptr: 0x360
-  __DATA_CONST.__const: 0x220
+  __DATA_CONST.__const: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x168
   __DATA.__bss: 0xb80

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
   Functions: 125
-  Symbols:   42
+  Symbols:   50
   CStrings:  20
 
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
