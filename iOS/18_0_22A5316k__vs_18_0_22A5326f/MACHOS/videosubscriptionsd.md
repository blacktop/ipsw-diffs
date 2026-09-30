## videosubscriptionsd

> `/usr/libexec/videosubscriptionsd`

```diff

-561.0.4.0.0
+561.0.7.0.0
   __TEXT.__text: 0xd094
   __TEXT.__auth_stubs: 0x6e0
   __TEXT.__objc_stubs: 0x23c0

   __TEXT.__unwind_info: 0x370
   __DATA_CONST.__auth_got: 0x380
   __DATA_CONST.__got: 0x2b0
-  __DATA_CONST.__const: 0x838
+  __DATA_CONST.__const: 0x878
   __DATA_CONST.__cfstring: 0x420
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x40

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
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
   Functions: 298
-  Symbols:   222
+  Symbols:   230
   CStrings:  713
 
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
