## osanalyticshelper

> `/System/Library/CoreServices/osanalyticshelper`

```diff

-726.0.9.0.0
+726.0.13.0.0
   __TEXT.__text: 0x11c5c
   __TEXT.__auth_stubs: 0xcc0
   __TEXT.__objc_stubs: 0x2400

   __DATA_CONST.__auth_got: 0x678
   __DATA_CONST.__got: 0x480
   __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0x8a0
+  __DATA_CONST.__const: 0x8e0
   __DATA_CONST.__cfstring: 0x1820
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x18

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
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
   Functions: 272
-  Symbols:   371
+  Symbols:   379
   CStrings:  899
 
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
