## XOJIT

> `/System/Library/PrivateFrameworks/XOJIT.framework/XOJIT`

```diff

-44.0.0.0.0
-  __TEXT.__text: 0x257ed8
-  __TEXT.__auth_stubs: 0x11a0
+47.0.0.0.0
+  __TEXT.__text: 0x258600
+  __TEXT.__auth_stubs: 0x1230
   __TEXT.__init_offsets: 0x118
   __TEXT.__const: 0x1dfac
-  __TEXT.__swift5_typeref: 0x260
+  __TEXT.__cstring: 0x7b309
+  __TEXT.__swift5_typeref: 0x258
   __TEXT.__swift5_capture: 0x54
-  __TEXT.__cstring: 0x7b199
+  __TEXT.__oslogstring: 0x11b
   __TEXT.__swift5_reflstr: 0x1fb
   __TEXT.__swift5_assocty: 0x28
   __TEXT.__constg_swiftt: 0x5a8

   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_proto: 0x64
   __TEXT.__swift5_types: 0x84
-  __TEXT.__oslogstring: 0xe4
   __TEXT.__orc_runtime: 0x7eb920
-  __TEXT.__unwind_info: 0x5348
-  __TEXT.__eh_frame: 0x910
+  __TEXT.__unwind_info: 0x5350
+  __TEXT.__eh_frame: 0x8d8
   __TEXT.__objc_methname: 0x36
   __DATA_CONST.__got: 0x100
-  __DATA_CONST.__const: 0x1ec50
+  __DATA_CONST.__const: 0x1eca0
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x8d0
+  __AUTH_CONST.__auth_got: 0x918
   __AUTH_CONST.__auth_ptr: 0x118
   __AUTH_CONST.__const: 0x8750
   __AUTH_CONST.__objc_const: 0x770
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0xbd8
-  __DATA.__data: 0xb00
+  __DATA.__data: 0xaf8
   __DATA.__bss: 0x82a8
   __DATA.__common: 0x15c0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  Functions: 8435
-  Symbols:   8897
-  CStrings:  19780
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 8444
+  Symbols:   8909
+  CStrings:  19789
 
Symbols:
+ __os_log_impl
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _objc_release_x21
+ _objc_release_x23
+ _objc_release_x24
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _sysconf
- __ZNSt3__16thread20hardware_concurrencyEv
- _objc_release_x19
- _objc_release_x20
- _swift_continuation_await
- _swift_continuation_init
CStrings:
+ "Fatal error"
+ "Negative value is not representable"
+ "Not enough bits to represent the passed value"
+ "Swift/Integers.swift"
+ "Swift/UnsafePointer.swift"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "failed to determine cpu count; limiting to %!l(MISSING)d threads"

```
