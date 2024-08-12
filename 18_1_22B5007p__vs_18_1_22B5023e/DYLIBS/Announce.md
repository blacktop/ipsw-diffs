## Announce

> `/System/Library/PrivateFrameworks/Announce.framework/Announce`

```diff

-234.0.5.0.0
-  __TEXT.__text: 0x1c424
+234.10.2.0.0
+  __TEXT.__text: 0x1c1c4
   __TEXT.__auth_stubs: 0xad0
   __TEXT.__objc_methlist: 0x1c80
   __TEXT.__const: 0x272
-  __TEXT.__cstring: 0x3cd9
+  __TEXT.__cstring: 0x3d29
   __TEXT.__oslogstring: 0xb5a
   __TEXT.__gcc_except_tab: 0x288
-  __TEXT.__swift5_typeref: 0x1c5
+  __TEXT.__swift5_typeref: 0x1c3
   __TEXT.__swift5_capture: 0x64
   __TEXT.__swift5_fieldmd: 0xf8
   __TEXT.__constg_swiftt: 0x158

   __TEXT.__objc_methtype: 0xe24
   __TEXT.__objc_stubs: 0x3420
   __DATA_CONST.__got: 0x2a8
-  __DATA_CONST.__const: 0xad0
+  __DATA_CONST.__const: 0xb18
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xc0

   __AUTH_CONST.__auth_got: 0x578
   __AUTH_CONST.__auth_ptr: 0xb8
   __AUTH_CONST.__const: 0x480
-  __AUTH_CONST.__cfstring: 0x2d40
+  __AUTH_CONST.__cfstring: 0x2d80
   __AUTH_CONST.__objc_const: 0x46e8
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x110

   - /usr/lib/swift/libswiftQuartzCore.dylib
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
-  Functions: 793
-  Symbols:   1165
-  CStrings:  1576
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 792
+  Symbols:   1174
+  CStrings:  1578
 
Symbols:
+ _ANDefaultHomeKitRefreshTimeout
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "[Double] Duration to wait for HomeKit refresh in seconds"
+ "homekit_refresh_timeout"

```
