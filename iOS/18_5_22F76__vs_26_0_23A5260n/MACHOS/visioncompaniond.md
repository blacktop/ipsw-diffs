## visioncompaniond

> `/usr/libexec/visioncompaniond`

```diff

-16.120.1.0.0
-  __TEXT.__text: 0x1968
-  __TEXT.__auth_stubs: 0x380
-  __TEXT.__const: 0x42
+17.0.22.0.0
+  __TEXT.__text: 0x1054
+  __TEXT.__auth_stubs: 0x1b0
+  __TEXT.__const: 0x5a
   __TEXT.__swift5_typeref: 0x27
-  __TEXT.__objc_methname: 0x7b
+  __TEXT.__objc_methname: 0x10
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__cstring: 0x13b
-  __TEXT.__oslogstring: 0x24
   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
-  __TEXT.__unwind_info: 0xe0
-  __TEXT.__eh_frame: 0x118
-  __DATA_CONST.__auth_got: 0x1c0
-  __DATA_CONST.__got: 0x48
+  __TEXT.__unwind_info: 0xc0
+  __TEXT.__eh_frame: 0x110
+  __DATA_CONST.__auth_got: 0xd8
+  __DATA_CONST.__got: 0x10
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x1e8
+  __DATA_CONST.__const: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x30
-  __DATA.__data: 0x48
-  __DATA.__common: 0x30
-  - /System/Library/Frameworks/Accounts.framework/Accounts
+  __DATA.__objc_selrefs: 0x10
+  __DATA.__data: 0x18
+  __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/VisionCompanion.framework/VisionCompanion
-  - /System/Library/PrivateFrameworks/VisionCompanionServices.framework/VisionCompanionServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 8FA159B5-08A1-3ECE-94C8-EC433C52A5F9
-  Functions: 33
-  Symbols:   100
-  CStrings:  15
+  UUID: 5CBFED58-2B82-3C0E-BF58-B789930F9795
+  Functions: 20
+  Symbols:   58
+  CStrings:  2
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- _$s10Foundation22_convertNSErrorToErrorys0E0_pSo0C0CSgF
- _$s23VisionCompanionServices0aB8FeaturesO6phase1yA2CmFWC
- _$s23VisionCompanionServices0aB8FeaturesO9isEnabledSbvg
- _$s23VisionCompanionServices0aB8FeaturesOMa
- _$s2os6LoggerV9logObjectSo03OS_a1_C0Cvg
- _$s2os6LoggerV9subsystem8categoryACSS_SStcfC
- _$s2os6LoggerVMa
- _$s8Dispatch0A3QoSV0B6SClassO7defaultyA2EmFWC
- _$s8Dispatch0A3QoSV0B6SClassOMa
- _$sSS10FoundationE19_bridgeToObjectiveCSo8NSStringCyF
- _$sSo13os_log_type_ta0A0E7defaultABvgZ
- _$sSo17OS_dispatch_queueC8DispatchE6global3qosAbC0D3QoSV0G6SClassO_tFZ
- _OBJC_CLASS_$_ACXPCEventSubscriber
- _OBJC_CLASS_$_BGSystemTaskScheduler
- _OBJC_CLASS_$_OS_dispatch_queue
- __Block_copy
- __Block_release
- __NSConcreteStackBlock
- ___stack_chk_fail
- ___stack_chk_guard
- __os_log_impl
- __swift_FORCE_LOAD_$_swiftCryptoTokenKit
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _exit
- _objc_release
- _objc_release_x19
- _objc_release_x20
- _objc_release_x22
- _objc_retain_x19
- _objc_retain_x20
- _os_log_type_enabled
- _swift_errorRelease
- _swift_getObjCClassMetadata
- _swift_once
- _swift_retain
- _swift_slowDealloc
- _swift_willThrow
- _xpc_set_event_stream_handler
CStrings:
- "Tetsuo phase 1 not enabled; exiting"
- "cancelTaskRequestWithIdentifier:error:"
- "com.apple.MobileGestalt.MobileGestaltEvents"
- "com.apple.distnoted.matching"
- "com.apple.notifyd.matching"
- "com.apple.visioncompaniond"
- "com.apple.visioncompaniond.AppInstallationRetryTask"
- "com.apple.visioncompaniond.PostInstall"
- "registerAccountChangeEventHandler:"
- "sharedScheduler"
- "sharedSubscriber"
- "v16@?0@\"<OS_xpc_object>\"8"
- "v20@?0@\"ACAccount\"8i16"

```
