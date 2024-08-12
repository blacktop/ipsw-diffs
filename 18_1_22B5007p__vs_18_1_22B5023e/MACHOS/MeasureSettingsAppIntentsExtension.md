## MeasureSettingsAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/MeasureSettingsAppIntentsExtension.appex/MeasureSettingsAppIntentsExtension`

```diff

-175.0.4.0.0
+175.0.6.0.0
   __TEXT.__text: 0x38f0
   __TEXT.__auth_stubs: 0x3b0
   __TEXT.__const: 0x63c

   __DATA_CONST.__auth_got: 0x1d8
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__auth_ptr: 0x350
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
   Functions: 122
-  Symbols:   40
+  Symbols:   48
   CStrings:  21
 
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
