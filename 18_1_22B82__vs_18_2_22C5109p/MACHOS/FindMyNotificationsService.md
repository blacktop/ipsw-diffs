## FindMyNotificationsService

> `/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyNotificationsService.appex/FindMyNotificationsService`

```diff

-412.31.8.11.4
-  __TEXT.__text: 0x15958
-  __TEXT.__auth_stubs: 0xd30
+415.32.7.8.25
+  __TEXT.__text: 0x1a1a4
+  __TEXT.__auth_stubs: 0xe50
   __TEXT.__objc_methlist: 0xc4
   __TEXT.__const: 0x7d0
-  __TEXT.__cstring: 0x7d0
-  __TEXT.__constg_swiftt: 0x334
-  __TEXT.__swift5_typeref: 0x358
-  __TEXT.__swift5_reflstr: 0x1ad
-  __TEXT.__swift5_fieldmd: 0x2ec
+  __TEXT.__cstring: 0x7f0
+  __TEXT.__constg_swiftt: 0x33c
+  __TEXT.__swift5_typeref: 0x382
+  __TEXT.__swift5_reflstr: 0x1b8
+  __TEXT.__swift5_fieldmd: 0x2f8
   __TEXT.__objc_methname: 0x8da
-  __TEXT.__oslogstring: 0x10bc
+  __TEXT.__oslogstring: 0x1104
   __TEXT.__swift5_capture: 0xb4
   __TEXT.__swift5_proto: 0x60
   __TEXT.__swift5_types: 0x30

   __TEXT.__objc_classname: 0x1c
   __TEXT.__objc_methtype: 0x204
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x568
-  __TEXT.__eh_frame: 0x690
-  __DATA_CONST.__auth_got: 0x698
-  __DATA_CONST.__got: 0x198
-  __DATA_CONST.__auth_ptr: 0x178
-  __DATA_CONST.__const: 0x8c8
+  __TEXT.__unwind_info: 0x5d0
+  __TEXT.__eh_frame: 0x870
+  __DATA_CONST.__auth_got: 0x728
+  __DATA_CONST.__got: 0x1e8
+  __DATA_CONST.__auth_ptr: 0x188
+  __DATA_CONST.__const: 0x8d0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA.__objc_const: 0xa60
+  __DATA.__objc_const: 0xa80
   __DATA.__objc_selrefs: 0x1d0
   __DATA.__objc_data: 0x258
-  __DATA.__data: 0x690
+  __DATA.__data: 0x6d8
   __DATA.__bss: 0xa80
   __DATA.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/CommunicationsFilter.framework/CommunicationsFilter
   - /System/Library/PrivateFrameworks/CorePhoneNumbers.framework/CorePhoneNumbers
   - /System/Library/PrivateFrameworks/FMF.framework/FMF
+  - /System/Library/PrivateFrameworks/FindMyBase.framework/FindMyBase
+  - /System/Library/PrivateFrameworks/FindMyLocate.framework/FindMyLocate
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/SPOwner.framework/SPOwner
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_stdio.dylib
   - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 384
-  Symbols:   329
-  CStrings:  253
+  Functions: 410
+  Symbols:   358
+  CStrings:  255
 
Symbols:
+ _$s10FindMyBase16isFeatureEnabledySb0E5Flags0eG3Key_pF
+ _$s10FindMyBase7FeatureO0aB0O0D5Flags0dE3KeyAAMc
+ _$s10FindMyBase7FeatureO0aB0O15fencesMigrationyA2EmFWC
+ _$s10FindMyBase7FeatureO0aB0OMa
+ _$s12FindMyLocate12ClientOriginO04findB3AppyA2CmFWC
+ _$s12FindMyLocate12ClientOriginOMa
+ _$s12FindMyLocate6FriendV6handleAA6HandleVvg
+ _$s12FindMyLocate6FriendVMa
+ _$s12FindMyLocate6HandleV10identifierSSvg
+ _$s12FindMyLocate6HandleV8serverIDSSSgvg
+ _$s12FindMyLocate6HandleVMa
+ _$s12FindMyLocate6HandleVMn
+ _$s12FindMyLocate6HandleVSHAAMc
+ _$s12FindMyLocate6HandleVSQAAMc
+ _$s12FindMyLocate7SessionC06sharedD06originAcA12ClientOriginO_tFZ
+ _$s12FindMyLocate7SessionC18forceRefreshClientyyYaKF
+ _$s12FindMyLocate7SessionC18forceRefreshClientyyYaKFTu
+ _$s12FindMyLocate7SessionC24friendsWithPendingOffersSayAA6FriendVGyYaKF
+ _$s12FindMyLocate7SessionC24friendsWithPendingOffersSayAA6FriendVGyYaKFTu
+ _$s12FindMyLocate7SessionC29friendsSharingLocationsWithMeSayAA6FriendVGyYaKF
+ _$s12FindMyLocate7SessionC29friendsSharingLocationsWithMeSayAA6FriendVGyYaKFTu
+ _$s12FindMyLocate7SessionCMa
+ _$s12FindMyLocate7SessionCMn
+ _$sSh15minimumCapacityShyxGSi_tcfC
+ __swift_FORCE_LOAD_$_swiftsimd
+ _swift_allocBox
+ _swift_arrayInitWithCopy
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
CStrings:
+ "LocationSharingContentService: Failed to force refresh FMF due to: %!{(MISSING)public}@"
+ "LocationSharingContentService: Failed to force refresh FML due to: %!{(MISSING)public}@"
+ "fmlSession"
- "LocationSharingContentService: Failed to force refresh FMF due to: %!@(MISSING) "

```
