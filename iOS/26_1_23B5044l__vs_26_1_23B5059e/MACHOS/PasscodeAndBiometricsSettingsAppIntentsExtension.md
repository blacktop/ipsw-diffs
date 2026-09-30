## PasscodeAndBiometricsSettingsAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/PasscodeAndBiometricsSettingsAppIntentsExtension.appex/PasscodeAndBiometricsSettingsAppIntentsExtension`

```diff

-15.0.0.0.0
-  __TEXT.__text: 0x6cbc
-  __TEXT.__auth_stubs: 0x840
-  __TEXT.__objc_stubs: 0x120
-  __TEXT.__objc_methlist: 0x50
-  __TEXT.__const: 0xae2
-  __TEXT.__gcc_except_tab: 0x48
-  __TEXT.__cstring: 0x1992
-  __TEXT.__objc_classname: 0x21
-  __TEXT.__oslogstring: 0x32
-  __TEXT.__objc_methname: 0x1ac
-  __TEXT.__objc_methtype: 0x14
-  __TEXT.__dlopen_cstrs: 0xe6
-  __TEXT.__constg_swiftt: 0x118
-  __TEXT.__swift5_typeref: 0x387
-  __TEXT.__swift5_fieldmd: 0x154
+17.0.0.0.0
+  __TEXT.__text: 0x6fc0
+  __TEXT.__auth_stubs: 0x7b0
+  __TEXT.__objc_methlist: 0x14
+  __TEXT.__const: 0xac2
+  __TEXT.__cstring: 0x1962
+  __TEXT.__objc_methname: 0xfc
+  __TEXT.__constg_swiftt: 0x170
+  __TEXT.__swift5_typeref: 0x39b
+  __TEXT.__swift5_reflstr: 0x2ab
+  __TEXT.__swift5_fieldmd: 0x178
   __TEXT.__swift5_types: 0x1c
   __TEXT.__swift_as_entry: 0x34
   __TEXT.__swift_as_ret: 0x28
   __TEXT.__swift5_proto: 0x84
-  __TEXT.__swift5_reflstr: 0x22b
+  __TEXT.__oslogstring: 0x1c
   __TEXT.__swift5_assocty: 0x120
-  __TEXT.__unwind_info: 0x328
-  __TEXT.__eh_frame: 0x288
-  __DATA_CONST.__auth_got: 0x430
-  __DATA_CONST.__got: 0xd8
+  __TEXT.__unwind_info: 0x2f8
+  __TEXT.__eh_frame: 0x2c8
+  __DATA_CONST.__auth_got: 0x3d8
+  __DATA_CONST.__got: 0xf8
   __DATA_CONST.__auth_ptr: 0x478
-  __DATA_CONST.__const: 0x588
-  __DATA_CONST.__objc_classlist: 0x10
+  __DATA_CONST.__const: 0x4a8
+  __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0xd8
-  __DATA.__objc_selrefs: 0x98
-  __DATA.__objc_data: 0x108
-  __DATA.__data: 0x1d8
-  __DATA.__bss: 0x10e0
+  __DATA.__objc_const: 0xb0
+  __DATA.__objc_selrefs: 0x58
+  __DATA.__objc_data: 0x128
+  __DATA.__data: 0x218
+  __DATA.__bss: 0x1080
   __DATA.__common: 0x30
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
-  - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/PasscodeAndBiometricsSettings.framework/PasscodeAndBiometricsSettings
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: ECC2C296-05EC-3E02-98E9-A42F53274861
-  Functions: 219
-  Symbols:   102
-  CStrings:  136
+  UUID: 468D5209-725E-3662-AB08-DD07DFC2332F
+  Functions: 207
+  Symbols:   82
+  CStrings:  112
 
Symbols:
+ _MobileGestalt_get_touchIDCapability
+ _OBJC_CLASS_$_PABSUnlockWithAppleWatchManager
+ __os_log_impl
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreMedia
+ __swift_FORCE_LOAD_$_swiftSpatial
+ _objc_release
+ _swift_arrayDestroy
+ _swift_deletedMethodError
+ _swift_getObjectType
+ _swift_slowDealloc
+ _swift_unknownObjectRetain
- _MobileGestalt_get_hasMesa
- _OBJC_CLASS_$_NSNumber
- _PSIsPearlAvailable
- _PSSupportsMesa
- __Block_object_dispose
- __NSConcreteGlobalBlock
- __Unwind_Resume
- ___assert_rtn
- ___objc_personality_v0
- ___stack_chk_fail
- ___stack_chk_guard
- __dispatch_main_q
- __os_log_error_impl
- __sl_dlopen
- _abort_report_np
- _dispatch_once
- _dlerror
- _dlsym
- _objc_alloc
- _objc_alloc_init
- _objc_claimAutoreleasedReturnValue
- _objc_getClass
- _objc_opt_class
- _objc_release_x1
- _objc_retainAutorelease
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x19
- _objc_retain_x2
- _objc_retain_x20
- _os_log_create
- _swift_deletedAsyncMethodErrorTu
CStrings:
+ "$__lazy_storage_$_isFaceIDAvailable"
+ "$__lazy_storage_$_isSDPAvailable"
+ "$__lazy_storage_$_isTouchIDAvailable"
+ "%{public}s:%ld - %{public}s"
+ "PasscodeAndBiometricsSettingsAppIntentsExtension"
+ "availabilityState(for:)"
- "%s"
- "IDSDefaultPairedDevice"
- "NRPairedDeviceRegistry"
- "PABSLogForCategory"
- "PABSLogging.m"
- "PABSUnlockWithAppleWatchManager"
- "Passcode"
- "PasscodeAndBiometricsSettings"
- "SFAuthenticationManager"
- "SFUnlockManager"
- "Unable to find class %s"
- "Unlock using Vision: %@"
- "Unlock using watch: %@ %@"
- "category < PABSLoggingCategoryCount"
- "count"
- "initWithQueue:"
- "isPaired"
- "isSupportedForType:"
- "listCandidateDevicesForType:completionHandler:"
- "numberWithBool:"
- "sharedUnlockManager"
- "softlink:r:path:/System/Library/PrivateFrameworks/IDS.framework/IDS"
- "softlink:r:path:/System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry"
- "softlink:r:path:/System/Library/PrivateFrameworks/Sharing.framework/Sharing"
- "unlockEnabledWithDevice:completionHandler:"
- "v20@?0B8@\"NSError\"12"
- "v24@0:8@?16"
- "v24@?0@\"NSSet\"8@\"NSError\"16"
- "v8@?0"

```
