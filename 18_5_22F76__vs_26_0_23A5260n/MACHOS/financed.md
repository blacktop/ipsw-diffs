## financed

> `/System/Library/Frameworks/FinanceKit.framework/financed`

```diff

-224.5.3.0.0
-  __TEXT.__text: 0x2238
-  __TEXT.__auth_stubs: 0x2e0
-  __TEXT.__const: 0x42
-  __TEXT.__cstring: 0x116
-  __TEXT.__oslogstring: 0x2ec
+291.1.0.0.0
+  __TEXT.__text: 0x1d3c
+  __TEXT.__auth_stubs: 0x2d0
+  __TEXT.__const: 0x3a
   __TEXT.__swift5_entry: 0x8
+  __TEXT.__cstring: 0x184
+  __TEXT.__oslogstring: 0x2bc
   __TEXT.__objc_methname: 0x4a
-  __TEXT.__unwind_info: 0xc0
+  __TEXT.__unwind_info: 0xc8
   __TEXT.__eh_frame: 0x50
-  __DATA_CONST.__auth_got: 0x170
-  __DATA_CONST.__got: 0x58
+  __DATA_CONST.__auth_got: 0x168
+  __DATA_CONST.__got: 0x40
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x168
+  __DATA_CONST.__const: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__linkguard: 0xe
   __DATA.__objc_selrefs: 0x20
-  __DATA.__data: 0xb8
-  __DATA.__common: 0x218
+  __DATA.__data: 0xd0
+  __DATA.__common: 0x260
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/FinanceKit.framework/FinanceKit
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /usr/appleinternal/lib/liblinkguard.dylib
   - /usr/lib/libSystem.B.dylib
-  - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: D592E2AF-0B94-36AB-AE77-6CAF9369B1F9
-  Functions: 89
-  Symbols:   91
-  CStrings:  27
+  UUID: 26D468FB-391E-319F-A8BD-C577EA5D64CD
+  Functions: 96
+  Symbols:   82
+  CStrings:  29
 
Symbols:
+ _$s13FinanceDaemon0B0C3runyyF
+ _$sScA15unownedExecutorScevgTj
+ _$sScM6sharedScMvgZ
+ _$sScMMa
+ _$sScMScAsWP
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _objc_release
+ _objc_release_x24
+ _objc_retain_x26
+ _swift_task_isCurrentExecutor
+ _swift_task_reportUnexpectedExecutor
- _$s13FinanceDaemon0B0C3runyyFTj
- __os_log_default
- __os_log_error_impl
- __swift_FORCE_LOAD_$_swiftCryptoTokenKit
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _malloc_create_zone
- _malloc_set_zone_name
- _malloc_zone_free
- _malloc_zone_malloc
- _malloc_zone_realloc
- _objc_release_x21
- _objc_release_x22
- _objc_retain
- _objc_retain_x22
- _objc_retain_x23
- _u_setMemoryFunctions
CStrings:
+ "BackgroundDelivery"
+ "DiagnosticExtension"
+ "com.apple.finance.FinanceDiagnosticExtension"
+ "financed/main.swift"
- "Could not set up ICU malloc zone, error %i"
- "ICU"

```
