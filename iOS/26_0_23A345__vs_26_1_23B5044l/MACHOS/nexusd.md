## nexusd

> `/usr/libexec/nexusd`

```diff

-800.15.0.0.0
-  __TEXT.__text: 0x76c
-  __TEXT.__auth_stubs: 0x2e0
-  __TEXT.__cstring: 0x44
+810.16.0.0.0
+  __TEXT.__text: 0x644
+  __TEXT.__auth_stubs: 0x240
+  __TEXT.__cstring: 0x1d
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x18
+  __TEXT.__const: 0xe
   __TEXT.__constg_swiftt: 0x28
   __TEXT.__swift5_typeref: 0x10
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__oslogstring: 0x60
-  __TEXT.__unwind_info: 0x88
-  __DATA_CONST.__auth_got: 0x170
-  __DATA_CONST.__got: 0x40
+  __TEXT.__unwind_info: 0x78
+  __DATA_CONST.__auth_got: 0x120
+  __DATA_CONST.__got: 0x30
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0xa8
+  __DATA_CONST.__const: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x20
-  __DATA.__bss: 0x10
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
+  - /System/Library/PrivateFrameworks/CoreUtilsSwift.framework/CoreUtilsSwift
   - /System/Library/PrivateFrameworks/Nexus.framework/Nexus
   - /System/Library/PrivateFrameworks/NexusDaemon.framework/NexusDaemon
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 339031CA-D53C-3BC5-8A7E-86BC84244B7E
-  Functions: 12
-  Symbols:   69
-  CStrings:  7
+  UUID: 8FD6C1F4-5C74-3529-84C4-E16D4DB76298
+  Functions: 8
+  Symbols:   55
+  CStrings:  2
 
Symbols:
+ _$s11NexusDaemon8NXDaemonC13dispatchQueue11environmentACSo03OS_D6_queueC_14CoreUtilsSwift19CUEnvironmentValuesVtcfc
+ _$s14CoreUtilsSwift19CUEnvironmentValuesV13dispatchQueueSo03OS_F13_queue_serialCvg
+ _$s14CoreUtilsSwift19CUEnvironmentValuesV13dispatchQueueSo03OS_F13_queue_serialCvs
+ _$s14CoreUtilsSwift19CUEnvironmentValuesVACycfC
+ _$s14CoreUtilsSwift19CUEnvironmentValuesVMa
+ _$s5Nexus11NXConstantsO12logSubsystemSSvgZ
+ _$s5Nexus11NXConstantsO14daemonBundleIDSSvgZ
+ _$sSS11utf8CStrings15ContiguousArrayVys4Int8VGvg
+ _$sSo24OS_dispatch_queue_serialC8DispatchE10AttributesVMa
+ _$sSo24OS_dispatch_queue_serialC8DispatchE10AttributesVMn
+ _$sSo24OS_dispatch_queue_serialC8DispatchE10AttributesVs10SetAlgebraACMc
+ _$sSo24OS_dispatch_queue_serialC8DispatchE5label3qos10attributes20autoreleaseFrequency6targetABSS_AC0E3QoSVAbCE10AttributesVSo0a1_b1_C0CACE011AutoreleaseJ0OANSgtcfC
+ _CUEnterSandbox
+ _OBJC_CLASS_$_OS_dispatch_queue_serial
+ _swift_bridgeObjectRelease
- _$s11NexusDaemon25NXDaemonEnvironmentDarwinVAA0cD0AAWP
- _$s11NexusDaemon25NXDaemonEnvironmentDarwinVACycfC
- _$s11NexusDaemon25NXDaemonEnvironmentDarwinVMa
- _$s11NexusDaemon8NXDaemonC13dispatchQueue11environmentACSo03OS_D6_queueC_AA0C11Environment_ptcfc
- _$sSo17OS_dispatch_queueC8DispatchE10AttributesVMa
- _$sSo17OS_dispatch_queueC8DispatchE10AttributesVMn
- _$sSo17OS_dispatch_queueC8DispatchE10AttributesVs10SetAlgebraACMc
- _$sSo17OS_dispatch_queueC8DispatchE5label3qos10attributes20autoreleaseFrequency6targetABSS_AC0D3QoSVAbCE10AttributesVAbCE011AutoreleaseI0OABSgtcfC
- _OBJC_CLASS_$_OS_dispatch_queue
- __NSConcreteGlobalBlock
- ___error
- ___stack_chk_fail
- ___stack_chk_guard
- __os_log_error_impl
- __set_user_dir_suffix
- __swift_FORCE_LOAD_$_swiftOSLog
- _bzero
- _confstr
- _dispatch_once
- _objc_claimAutoreleasedReturnValue
- _objc_release_x1
- _objc_release_x19
- _objc_release_x20
- _objc_release_x23
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x20
- _os_log_create
- _os_log_type_enabled
- _swift_allocBox
CStrings:
- "### _set_user_dir_suffix failed: %{darwin.errno}d"
- "### confstr temp dir failed: %{darwin.errno}d"
- "com.apple.nexus"
- "com.apple.nexusd"
- "v8@?0"

```
