## com.apple.weather.appremoval

> `/System/Library/AppRemovalServices/com.apple.weather.appremoval.xpc/com.apple.weather.appremoval`

```diff

-771.11.0.0.0
+779.0.0.0.0
   __TEXT.__text: 0x1a68
   __TEXT.__auth_stubs: 0x390
   __TEXT.__objc_stubs: 0x4c0

   __DATA_CONST.__auth_got: 0x1d0
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1a0
+  __DATA_CONST.__const: 0x1e0
   __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18

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
   Functions: 35
-  Symbols:   103
+  Symbols:   111
   CStrings:  131
 
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
