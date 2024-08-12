## SafetySessionFlowPlugin

> `/System/Library/Assistant/FlowDelegatePlugins/SafetySessionFlowPlugin.bundle/SafetySessionFlowPlugin`

```diff

-3400.100.1.0.0
+3401.4.1.0.0
   __TEXT.__text: 0x323c
   __TEXT.__auth_stubs: 0x480
   __TEXT.__const: 0x480

   __DATA_CONST.__auth_got: 0x240
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__auth_ptr: 0x210
-  __DATA_CONST.__const: 0x2a0
+  __DATA_CONST.__const: 0x2e0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x380

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
   Functions: 149
-  Symbols:   67
+  Symbols:   75
   CStrings:  16
 
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
