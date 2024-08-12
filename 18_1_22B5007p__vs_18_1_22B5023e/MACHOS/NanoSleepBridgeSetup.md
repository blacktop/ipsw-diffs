## NanoSleepBridgeSetup

> `/System/Library/NanoPreferenceBundles/SetupBundles/NanoSleepBridgeSetup.bundle/NanoSleepBridgeSetup`

```diff

-5132.0.0.0.0
+5200.1.3.0.0
   __TEXT.__text: 0x2524
   __TEXT.__auth_stubs: 0x590
   __TEXT.__objc_methlist: 0x90

   __DATA_CONST.__auth_got: 0x2c8
   __DATA_CONST.__got: 0xa8
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x180
+  __DATA_CONST.__const: 0x1c0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30

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
   Functions: 50
-  Symbols:   97
+  Symbols:   105
   CStrings:  95
 
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
