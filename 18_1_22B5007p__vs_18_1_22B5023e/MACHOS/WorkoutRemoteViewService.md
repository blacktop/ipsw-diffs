## WorkoutRemoteViewService

> `/Applications/WorkoutRemoteViewService.app/WorkoutRemoteViewService`

```diff

-889.0.0.0.0
+901.0.0.0.0
   __TEXT.__text: 0x384c
   __TEXT.__auth_stubs: 0x6e0
   __TEXT.__objc_stubs: 0x120

   __DATA_CONST.__auth_got: 0x378
   __DATA_CONST.__got: 0x110
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0x300
+  __DATA_CONST.__const: 0x340
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftWebKit.dylib
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
   Functions: 94
-  Symbols:   189
+  Symbols:   197
   CStrings:  281
 
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
