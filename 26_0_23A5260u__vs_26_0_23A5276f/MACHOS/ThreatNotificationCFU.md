## ThreatNotificationCFU

> `/System/Library/PrivateFrameworks/ThreatNotificationUI.framework/Extensions/ThreatNotificationCFU.appex/ThreatNotificationCFU`

```diff

-24.0.1.0.0
-  __TEXT.__text: 0x2108
-  __TEXT.__auth_stubs: 0x520
+24.0.5.0.0
+  __TEXT.__text: 0x2638
+  __TEXT.__auth_stubs: 0x560
   __TEXT.__objc_methlist: 0x50
   __TEXT.__const: 0xa6
-  __TEXT.__objc_methname: 0x1f5
-  __TEXT.__oslogstring: 0x153
+  __TEXT.__objc_methname: 0x25f
+  __TEXT.__oslogstring: 0x213
   __TEXT.__swift5_typeref: 0x82
   __TEXT.__swift5_capture: 0x30
   __TEXT.__cstring: 0xb5

   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x8
   __TEXT.__unwind_info: 0xf8
-  __DATA_CONST.__auth_got: 0x290
-  __DATA_CONST.__got: 0x58
+  __DATA_CONST.__auth_got: 0x2b0
+  __DATA_CONST.__got: 0x70
   __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0x198
+  __DATA_CONST.__const: 0x180
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0xa8
+  __DATA.__objc_selrefs: 0xd8
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x60
   __DATA.__bss: 0x80
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/CoreFollowUpUI.framework/CoreFollowUpUI
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/ThreatNotification.framework/ThreatNotification

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8A26B024-6AFD-349A-8E2C-B5D847F404D7
+  UUID: 08EE1D8B-CF2E-3836-ADE9-0D701FE93656
   Functions: 46
-  Symbols:   495
-  CStrings:  40
+  Symbols:   493
+  CStrings:  51
 
Symbols:
+ _$s10Foundation22_convertErrorToNSErrorySo0E0Cs0C0_pF
+ _$s22ThreatNotificationCore12TNCKVStorageC5clearyyFTj
+ _$s22ThreatNotificationCore12TNCKVStorageCACycfc
+ _$s22ThreatNotificationCore12TNCKVStorageCMa
+ _AKAppleIDAuthenticationErrorDomain
+ _OBJC_CLASS_$_AKFollowUpProviderFactory
+ _OBJC_CLASS_$_AKFollowUpSynchronizer
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCompression_$_ThreatNotificationCFU
+ _swift_unknownObjectRelease
- _$s20ThreatNotificationUI13TNUIAnalyticsC10clearCacheyyFZ
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_ThreatNotificationCFU
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_ThreatNotificationCFU
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_ThreatNotificationCFU
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_ThreatNotificationCFU
Functions:
~ _$s21ThreatNotificationCFU0aB14ViewControllerC21followUpPerformUpdate17completionHandleryySo14FLUpdateResultVcSg_tFTf4nd_n : 1080 -> 2408
CStrings:
+ "AK follow-ups synchronization was cancelled"
+ "Cleared storage"
+ "Did synchronize AK follow-ups"
+ "Synchronization of AK follow-ups failed with error: %@"
+ "Will perform CFU update"
+ "code"
+ "domain"
+ "init"
+ "setFollowupProvider:"
+ "sharedAuthKitFollowupProvider"
+ "synchronizeFollowUpsForAccount:error:"

```
