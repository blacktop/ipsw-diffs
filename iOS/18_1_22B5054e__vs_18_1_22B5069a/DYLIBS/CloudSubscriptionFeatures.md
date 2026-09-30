## CloudSubscriptionFeatures

> `/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures`

```diff

-301.22.1.8.0
-  __TEXT.__text: 0xafd14
-  __TEXT.__auth_stubs: 0x1c00
-  __TEXT.__objc_methlist: 0xaec
+301.22.1.9.2
+  __TEXT.__text: 0xb1254
+  __TEXT.__auth_stubs: 0x1cb0
+  __TEXT.__objc_methlist: 0xae4
   __TEXT.__const: 0x4f48
-  __TEXT.__gcc_except_tab: 0x178
-  __TEXT.__cstring: 0x4921
-  __TEXT.__oslogstring: 0x6fac
-  __TEXT.__dlopen_cstrs: 0x11e
-  __TEXT.__swift5_typeref: 0x1b28
-  __TEXT.__swift5_fieldmd: 0x1544
-  __TEXT.__constg_swiftt: 0x1b08
-  __TEXT.__swift5_reflstr: 0x10ad
+  __TEXT.__gcc_except_tab: 0x168
+  __TEXT.__cstring: 0x49d1
+  __TEXT.__oslogstring: 0x734c
+  __TEXT.__dlopen_cstrs: 0xc4
+  __TEXT.__swift5_typeref: 0x1b3a
+  __TEXT.__swift5_fieldmd: 0x1568
+  __TEXT.__constg_swiftt: 0x1b10
+  __TEXT.__swift5_reflstr: 0x111d
   __TEXT.__swift5_builtin: 0xc8
   __TEXT.__swift5_assocty: 0x2e8
   __TEXT.__swift5_capture: 0xc38

   __TEXT.__swift5_proto: 0x468
   __TEXT.__swift5_types: 0x1b8
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x2e20
-  __TEXT.__eh_frame: 0x6a18
-  __TEXT.__objc_classname: 0x140
-  __TEXT.__objc_methname: 0x1bef
+  __TEXT.__unwind_info: 0x2de0
+  __TEXT.__eh_frame: 0x6920
+  __TEXT.__objc_classname: 0x131
+  __TEXT.__objc_methname: 0x1bd4
   __TEXT.__objc_methtype: 0x28e
   __TEXT.__objc_stubs: 0xb80
-  __DATA_CONST.__got: 0x500
-  __DATA_CONST.__const: 0x5b0
+  __DATA_CONST.__got: 0x510
+  __DATA_CONST.__const: 0x5b8
   __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x820
+  __DATA_CONST.__objc_selrefs: 0x818
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0xe10
-  __AUTH_CONST.__auth_ptr: 0x780
-  __AUTH_CONST.__const: 0x4948
+  __AUTH_CONST.__auth_got: 0xe68
+  __AUTH_CONST.__auth_ptr: 0x750
+  __AUTH_CONST.__const: 0x49a0
   __AUTH_CONST.__cfstring: 0x440
-  __AUTH_CONST.__objc_const: 0x35a8
+  __AUTH_CONST.__objc_const: 0x35e8
   __AUTH.__objc_data: 0x228
   __AUTH.__data: 0xe8
   __DATA.__objc_ivar: 0x2c
-  __DATA.__data: 0x13d0
-  __DATA.__bss: 0x6330
+  __DATA.__data: 0x13f0
+  __DATA.__bss: 0x6320
   __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0x1150
+  __DATA_DIRTY.__objc_data: 0x1160
   __DATA_DIRTY.__data: 0x1b20
   __DATA_DIRTY.__bss: 0x1c40
   __DATA_DIRTY.__common: 0x48

   - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp
   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
+  - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels
   - /System/Library/PrivateFrameworks/GenerativeModelsFoundation.framework/GenerativeModelsFoundation
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3382
-  Symbols:   597
-  CStrings:  1365
+  Functions: 3387
+  Symbols:   594
+  CStrings:  1378
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit
+ _os_unfair_lock_trylock
+ _swift_runtimeSupportsNoncopyableTypes
- _dlerror
- _dlsym
CStrings:
+ "%!s(MISSING) Symbol `GenerativeModelsAvailability` is not available on this platform. Will return false."
+ "CFU posting was already in progess, not posting CFU"
+ "Determining if Siri assets are finished downloading."
+ "GenerativeModels are full available, Siri assets are finished downloading. Returning true"
+ "GenerativeModels are restricted and Siri assets are not finished downloading. Returning false."
+ "GenerativeModels are restricted but Siri assets are finished downloading. Returning true."
+ "GenerativeModels are unavailable and Siri asset status is unknown. Returning false."
+ "GenerativeModels are unavailable and Siri assets are not finished downloading. Returning false."
+ "GenerativeModels are unavailable but Siri assets are finished downloading. Returning true."
+ "Successfully cleared CFU on opt-in"
+ "Unable to clear CFU on opt-in. Error: %!{(MISSING)public}s"
+ "Unknown availabilty case when determining if Siri assets are downloaded."
+ "cfuLock"
+ "com.apple.SetupAssistant"
+ "com.apple.purplebuddy"
+ "getSiriAssetsFinishedDownloading"
+ "siriAssetsFinishedDownloading()"
+ "siriAssetsNotFinishedDownloading"
- "BYSetupAssistantNeedsToRun"
- "SetupAssistant"
- "User has not completed Buddy, will not post CFU."
- "softlink:r:path:/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant"

```
