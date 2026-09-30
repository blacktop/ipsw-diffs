## securityresearchdevice-init

> `/usr/libexec/securityresearchdevice-init`

```diff

-221.0.27.0.0
-  __TEXT.__text: 0x19a84
-  __TEXT.__auth_stubs: 0xe70
-  __TEXT.__const: 0x818
+221.40.5.0.0
+  __TEXT.__text: 0x1a770
+  __TEXT.__auth_stubs: 0xfe0
+  __TEXT.__const: 0x808
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__cstring: 0x70c
+  __TEXT.__cstring: 0x73c
   __TEXT.__swift_as_entry: 0x6c
   __TEXT.__swift_as_ret: 0xa0
-  __TEXT.__oslogstring: 0x82c
-  __TEXT.__swift5_typeref: 0x158
+  __TEXT.__oslogstring: 0x9bc
+  __TEXT.__swift5_typeref: 0x188
   __TEXT.__constg_swiftt: 0x21c
-  __TEXT.__swift5_reflstr: 0x534
-  __TEXT.__swift5_fieldmd: 0x340
+  __TEXT.__swift5_reflstr: 0x554
+  __TEXT.__swift5_fieldmd: 0x34c
   __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_mpenum: 0x28
   __TEXT.__objc_methname: 0x29a
+  __TEXT.__swift5_capture: 0x44
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x2c
   __TEXT.__swift5_types: 0x30
-  __TEXT.__swift5_capture: 0x20
-  __TEXT.__unwind_info: 0x650
-  __TEXT.__eh_frame: 0x16a8
-  __DATA_CONST.__auth_got: 0x738
-  __DATA_CONST.__got: 0x1e8
-  __DATA_CONST.__auth_ptr: 0xd0
-  __DATA_CONST.__const: 0x560
+  __TEXT.__unwind_info: 0x680
+  __TEXT.__eh_frame: 0x16b8
+  __DATA_CONST.__auth_got: 0x7f0
+  __DATA_CONST.__got: 0x200
+  __DATA_CONST.__auth_ptr: 0xd8
+  __DATA_CONST.__const: 0x5d8
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0xb8
   __DATA.__objc_selrefs: 0xd0
-  __DATA.__data: 0x4f0
+  __DATA.__data: 0x518
   __DATA.__bss: 0x5a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Network.framework/Network
+  - /System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore
   - /System/Library/PrivateFrameworks/CryptexKit.framework/CryptexKit
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 54832F57-0BE0-386E-97E4-D9CF767E1E57
-  Functions: 343
-  Symbols:   337
-  CStrings:  125
+  UUID: 5A43FC63-E735-3DCB-8347-4F96E0FEAF48
+  Functions: 356
+  Symbols:   363
+  CStrings:  135
 
Symbols:
+ _$s13AppleKeyStore11AKSIdentityV16getIdentityStateAC0G0VyKF
+ _$s13AppleKeyStore11AKSIdentityV5StateV5stateAeDVSgvg
+ _$s13AppleKeyStore11AKSIdentityV5StateVADV12beenUnlockedAFvgZ
+ _$s13AppleKeyStore11AKSIdentityV5StateVADVMa
+ _$s13AppleKeyStore11AKSIdentityV5StateVADVMn
+ _$s13AppleKeyStore11AKSIdentityV5StateVADVs10SetAlgebraAAMc
+ _$s13AppleKeyStore11AKSIdentityV5StateVMa
+ _$s13AppleKeyStore11AKSIdentityVMa
+ _$s13AppleKeyStore11AKSIdentityVyAcA9AKSHandleVcfC
+ _$s13AppleKeyStore9AKSHandleV7sessionACvgZ
+ _$s13AppleKeyStore9AKSHandleVMa
+ _$s8Dispatch0A3QoSV0B6SClassO7defaultyA2EmFWC
+ _$s8Dispatch0A3QoSV0B6SClassOMa
+ _$sSo17OS_dispatch_groupC8DispatchE4waityyF
+ _$sSo17OS_dispatch_queueC8DispatchE6global3qosAbC0D3QoSV0G6SClassO_tFZ
+ _$ss10SetAlgebraP10isSuperset2ofSbx_tFTj
+ _MASetPallasUrlForType
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _notify_cancel
+ _notify_register_dispatch
+ _objc_retain_x26
+ _swift_beginAccess
+ _swift_endAccess
CStrings:
+ "AKSIdentity.State.state appears nil, device appears to have never been unlocked"
+ "Pallas URL override set: %s"
+ "com.apple.mobile.keybagd.lock_status"
+ "com.apple.security-research-device"
+ "device appears before first unlock even after notification"
+ "failed to get lock state: %@"
+ "failed to register for lock status notification"
+ "mobileAssetDownload(assetType:audienceId:pallasURLOverride:compatibilityVersion:)"
+ "received lock status notification"
+ "returning after validating device has been through first unlock"
+ "srd-prov-asset-pallas-url"
+ "v12@?0i8"
+ "waiting for first unlock"
- "com.apple.research.securityresearchdeviceinit"
- "com.apple.research.securityresearchdeviceinit.core"
- "mobileAssetDownload(assetType:audienceId:compatibilityVersion:)"

```
