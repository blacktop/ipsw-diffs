## Diagnostic-0001

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-0001.appex/Diagnostic-0001`

```diff

-795.0.0.0.0
+815.0.0.0.0
   __TEXT.__text: 0x648
   __TEXT.__auth_stubs: 0x160
   __TEXT.__objc_methlist: 0x38

   __DATA_CONST.__auth_got: 0xb0
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x88
+  __DATA_CONST.__const: 0xc8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x48

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
   Functions: 16
-  Symbols:   41
+  Symbols:   49
   CStrings:  12
 
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
