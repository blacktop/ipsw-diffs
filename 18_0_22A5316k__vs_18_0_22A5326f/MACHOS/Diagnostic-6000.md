## Diagnostic-6000

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6000.appex/Diagnostic-6000`

```diff

-795.0.0.0.0
+815.0.0.0.0
   __TEXT.__text: 0x1c70
   __TEXT.__auth_stubs: 0x370
   __TEXT.__objc_methlist: 0x7c

   __DATA_CONST.__auth_got: 0x1b8
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0xd8
+  __DATA_CONST.__const: 0x118
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
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
   Functions: 42
-  Symbols:   65
+  Symbols:   73
   CStrings:  76
 
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
