## ktrace

> `/System/Library/PrivateFrameworks/ktrace.framework/ktrace`

```diff

-629.0.1.0.0
-  __TEXT.__text: 0xbbfb8
+629.0.5.0.0
+  __TEXT.__text: 0xbb990
   __TEXT.__auth_stubs: 0x30b0
   __TEXT.__objc_methlist: 0x160
   __TEXT.__const: 0x32d1
-  __TEXT.__cstring: 0x63e6
+  __TEXT.__cstring: 0x63d6
   __TEXT.__oslogstring: 0x5215
   __TEXT.__gcc_except_tab: 0x10d0
   __TEXT.__swift5_typeref: 0x1042

   __TEXT.__swift5_types: 0x1e0
   __TEXT.__swift5_builtin: 0x208
   __TEXT.__swift5_mpenum: 0x50
-  __TEXT.__swift5_capture: 0x304
+  __TEXT.__swift5_capture: 0x308
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x2a50
+  __TEXT.__unwind_info: 0x2a48
   __TEXT.__eh_frame: 0x26f8
   __TEXT.__objc_classname: 0x9b
   __TEXT.__objc_methname: 0xc13
   __TEXT.__objc_methtype: 0xfea
   __TEXT.__objc_stubs: 0x7e0
   __DATA_CONST.__got: 0x508
-  __DATA_CONST.__const: 0x1bb0
+  __DATA_CONST.__const: 0x1bf0
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8

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
-  Functions: 3717
-  Symbols:   3484
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 3716
+  Symbols:   3492
   CStrings:  1572
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "TRACE_PLAN_PATH"
- "KTRACE_PLAN_PATH"

```
