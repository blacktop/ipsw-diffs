## AnnounceDaemon

> `/System/Library/PrivateFrameworks/AnnounceDaemon.framework/AnnounceDaemon`

```diff

-234.0.5.0.0
-  __TEXT.__text: 0x54938
-  __TEXT.__auth_stubs: 0x1290
-  __TEXT.__objc_methlist: 0x2e7c
+234.10.2.0.0
+  __TEXT.__text: 0x55004
+  __TEXT.__auth_stubs: 0x1270
+  __TEXT.__objc_methlist: 0x2ed4
   __TEXT.__const: 0x41c
-  __TEXT.__cstring: 0x27d2
-  __TEXT.__oslogstring: 0x5a18
-  __TEXT.__gcc_except_tab: 0x102c
-  __TEXT.__swift5_typeref: 0x3cf
+  __TEXT.__cstring: 0x2802
+  __TEXT.__oslogstring: 0x5b98
+  __TEXT.__gcc_except_tab: 0x1074
+  __TEXT.__swift5_typeref: 0x3c5
   __TEXT.__swift5_capture: 0xd0
   __TEXT.__constg_swiftt: 0x1d8
   __TEXT.__swift5_reflstr: 0x141

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_proto: 0x1c
-  __TEXT.__unwind_info: 0x13e8
+  __TEXT.__unwind_info: 0x1418
   __TEXT.__eh_frame: 0x340
-  __TEXT.__objc_classname: 0x9d2
-  __TEXT.__objc_methname: 0xb74c
-  __TEXT.__objc_methtype: 0x28fb
-  __TEXT.__objc_stubs: 0x88a0
-  __DATA_CONST.__got: 0x8d8
-  __DATA_CONST.__const: 0x1618
-  __DATA_CONST.__objc_classlist: 0x150
-  __DATA_CONST.__objc_catlist: 0x88
+  __TEXT.__objc_classname: 0x9ef
+  __TEXT.__objc_methname: 0xb814
+  __TEXT.__objc_methtype: 0x291c
+  __TEXT.__objc_stubs: 0x8960
+  __DATA_CONST.__got: 0x8f0
+  __DATA_CONST.__const: 0x16a8
+  __DATA_CONST.__objc_classlist: 0x158
+  __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2648
+  __DATA_CONST.__objc_selrefs: 0x2678
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x108
-  __AUTH_CONST.__auth_got: 0x958
+  __AUTH_CONST.__auth_got: 0x948
   __AUTH_CONST.__auth_ptr: 0x118
-  __AUTH_CONST.__const: 0xa38
-  __AUTH_CONST.__cfstring: 0x1320
-  __AUTH_CONST.__objc_const: 0x7a30
+  __AUTH_CONST.__const: 0xa58
+  __AUTH_CONST.__cfstring: 0x1360
+  __AUTH_CONST.__objc_const: 0x7b20
   __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH.__objc_data: 0x600
+  __AUTH.__objc_data: 0x650
   __AUTH.__data: 0x68
   __DATA.__objc_ivar: 0x294
-  __DATA.__data: 0x13d0
-  __DATA.__bss: 0x480
+  __DATA.__data: 0x13b8
+  __DATA.__bss: 0x490
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x948
-  __DATA_DIRTY.__data: 0x90
+  __DATA_DIRTY.__data: 0x98
   __DATA_DIRTY.__bss: 0x100
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

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
-  Functions: 1572
-  Symbols:   1907
-  CStrings:  3009
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 1587
+  Symbols:   1930
+  CStrings:  3032
 
Symbols:
+ _ANAnnounceErrorDomain
+ _ANDefaultHomeKitRefreshTimeout
+ _OBJC_CLASS_$_ANValidationHelper
+ _OBJC_METACLASS_$_ANValidationHelper
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- _swift_continuation_await
- _swift_continuation_init
CStrings:
+ "%!@(MISSING)Home manager refresh %!@(MISSING)"
+ "%!@(MISSING)Home manager refresh start (%!f(MISSING)s timeout)"
+ "%!@(MISSING)Starting validation check (is retry = %!d(MISSING))"
+ "%!@(MISSING)Validation check failed - HomeManager refresh error"
+ "%!@(MISSING)Validation check failed with Home error - requesting HomeManager refresh"
+ "%!@(MISSING)Validation check success"
+ "@\"NSError\"8@?0"
+ "@28@0:8@?16B24"
+ "ANValidationHelper"
+ "Checking if best device to alert"
+ "Home is nil for sendAnnouncement, refreshing Home Manager and retrying"
+ "HomeError"
+ "Info dictionary: %!s(MISSING)"
+ "ValidationHelper"
+ "_refreshBeforeDate:completionHandler:"
+ "_runValidationCheck:isRetry:"
+ "domain"
+ "failure"
+ "home:didUpdateDismissedWalletKeyUWBUnlockOnboarding:"
+ "isHomeError"
+ "refreshHomeSynchronous"
+ "sendAnnouncement:isRetry:sentHandler:"
+ "success"
+ "v36@0:8@16B24@?28"
- "Info dctionary: %!s(MISSING)"

```
