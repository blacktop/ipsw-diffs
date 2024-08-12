## LegacyPoster

> `/System/Library/ExtensionKit/Extensions/LegacyPoster.appex/LegacyPoster`

```diff

-214.1.0.0.0
+221.0.0.0.0
   __TEXT.__text: 0x193c
   __TEXT.__auth_stubs: 0x400
   __TEXT.__objc_stubs: 0x780

   __DATA_CONST.__auth_got: 0x208
   __DATA_CONST.__got: 0xa8
   __DATA_CONST.__auth_ptr: 0x50
-  __DATA_CONST.__const: 0x160
+  __DATA_CONST.__const: 0x1a0
   __DATA_CONST.__cfstring: 0xe0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20

   - /usr/lib/swift/libswiftSpatial.dylib
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
   Functions: 47
-  Symbols:   97
+  Symbols:   105
   CStrings:  220
 
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
