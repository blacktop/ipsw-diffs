## remotectl

> `/usr/libexec/remotectl`

```diff

-163.0.0.0.0
-  __TEXT.__text: 0x1add8
+164.0.0.0.0
+  __TEXT.__text: 0x1ad78
   __TEXT.__auth_stubs: 0x1aa0
   __TEXT.__objc_stubs: 0xc0
   __TEXT.__const: 0x63c

   __DATA_CONST.__auth_got: 0xd60
   __DATA_CONST.__got: 0x260
   __DATA_CONST.__auth_ptr: 0x218
-  __DATA_CONST.__const: 0x6b0
+  __DATA_CONST.__const: 0x6f0
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftSystem.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 392
-  Symbols:   563
+  Symbols:   571
   CStrings:  462
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _objc_retain_x26
- _objc_retain_x27

```