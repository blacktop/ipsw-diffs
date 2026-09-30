## AppInstallationSettings

> `/System/Library/PreferenceBundles/AppInstallationSettings.bundle/AppInstallationSettings`

```diff

-2.2.25.0.0
-  __TEXT.__text: 0x15340
-  __TEXT.__auth_stubs: 0xc20
-  __TEXT.__objc_methlist: 0x2b0
-  __TEXT.__const: 0x1f8
-  __TEXT.__cstring: 0x1081
-  __TEXT.__objc_methname: 0xc60
-  __TEXT.__constg_swiftt: 0x3bc
-  __TEXT.__swift5_typeref: 0x1f5
-  __TEXT.__swift5_fieldmd: 0x148
-  __TEXT.__swift5_capture: 0x14c
+2.2.29.0.0
+  __TEXT.__text: 0x1bfb0
+  __TEXT.__auth_stubs: 0xc90
+  __TEXT.__objc_methlist: 0x29c
+  __TEXT.__const: 0x252
+  __TEXT.__cstring: 0x1151
+  __TEXT.__objc_methname: 0xc56
+  __TEXT.__constg_swiftt: 0x3e0
+  __TEXT.__swift5_typeref: 0x2ff
+  __TEXT.__swift5_fieldmd: 0x158
+  __TEXT.__swift5_capture: 0x184
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_types: 0x1c
   __TEXT.__oslogstring: 0x28
-  __TEXT.__unwind_info: 0x418
-  __TEXT.__eh_frame: 0x400
-  __DATA_CONST.__auth_got: 0x610
-  __DATA_CONST.__got: 0x1f8
-  __DATA_CONST.__auth_ptr: 0xb0
-  __DATA_CONST.__const: 0x648
+  __TEXT.__swift5_proto: 0x8
+  __TEXT.__swift5_protos: 0x4
+  __TEXT.__unwind_info: 0x4e8
+  __TEXT.__eh_frame: 0x718
+  __DATA_CONST.__auth_got: 0x648
+  __DATA_CONST.__got: 0x210
+  __DATA_CONST.__auth_ptr: 0xc8
+  __DATA_CONST.__const: 0x660
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x3e8
   __DATA.__objc_selrefs: 0x420
-  __DATA.__objc_data: 0x700
-  __DATA.__data: 0x2f0
+  __DATA.__objc_data: 0x6f8
+  __DATA.__data: 0x390
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
+  - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/ManagedAppDistribution.framework/ManagedAppDistribution
   - /System/Library/Frameworks/MarketplaceKit.framework/MarketplaceKit
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon
+  - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
+  - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/CoreFollowUpUI.framework/CoreFollowUpUI
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration

   - /System/Library/PrivateFrameworks/StoreServices.framework/StoreServices
   - /System/Library/PrivateFrameworks/ThirdPartyApplicationSettings.framework/ThirdPartyApplicationSettings
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
-  - /System/Library/PrivateFrameworks/iTunesStore.framework/iTunesStore
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 316
-  Symbols:   181
-  CStrings:  247
+  Functions: 346
+  Symbols:   188
+  CStrings:  251
 
Symbols:
+ _AMSNetworkTypeCellular
+ _MobileGestalt_get_current_device
+ _MobileGestalt_get_wifiCapability
+ _OBJC_CLASS_$_AMSBag
+ _OBJC_CLASS_$_AMSNetworkConstraints
+ _OBJC_CLASS_$_BSProcessHandle
+ _OBJC_CLASS_$_CTBundle
+ _OBJC_CLASS_$_CTXPCServiceSubscriptionContext
+ _OBJC_CLASS_$_CoreTelephonyClient
+ _swift_allocBox
+ _swift_bridgeObjectRelease_n
+ _swift_dynamicCastObjCClass
+ _swift_once
+ _swift_task_isCurrentExecutor
+ _swift_task_reportUnexpectedExecutor
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
- _OBJC_CLASS_$_ISNetworkObserver
- _OBJC_CLASS_$_ISURLBagCache
- _OBJC_CLASS_$_SSDevice
- _OBJC_CLASS_$_SSURLBagContext
- _objc_release_x28
- _objc_retain_x1
- _objc_retain_x28
- _objc_retain_x3
- _swift_allocError
- _swift_continuation_throwingResume
- _swift_continuation_throwingResumeWithError
CStrings:
+ "AllowAutoDownloadOnCellular"
+ "AppInstallationSettings/ApprovedDevelopersController.swift"
+ "AppInstallationSettings/DefaultAppMarketplaceViewWrapper.swift"
+ "AppInstallationSettings/LocalizedString.swift"
+ "ShowiTunesStoreAutoDownloadOverCellularSwitch"
+ "_createCheckedThrowingContinuation(_:)"
+ "addSpecifiersFromArray:"
+ "bagForProfile:profileVersion:"
+ "copyCarrierBundleValue:key:bundleType:error:"
+ "getSubscriptionInfoWithError:"
+ "initWithBundleType:"
+ "initWithQueue:"
+ "networkConstraintsForMediaType:withBag:"
+ "removeObserver:"
+ "resultWithCompletion:"
+ "setDelegate:"
+ "slotID"
+ "subscriptions"
+ "telephonyClient"
+ "v24@?0@\"AMSNetworkConstraints\"8@\"NSError\"16"
- "AppInstallationSettings.AppInstallationSettingsController"
- "AppInstallationSettings.CellularLimitsController"
- "URLBagForContext:"
- "contextWithBagType:"
- "default_cellular_limit"
- "getCellularNetworkingAllowedWithBlock:"
- "init"
- "integerForKey:"
- "networkConstraintsForDownloadKind:"
- "removeObserver:name:object:"
- "setCellularNetworkingAllowed:"
- "sharedCache"
- "sharedInstance"
- "shouldShowCellularAutomaticDownloadsSwitch"
- "supportsDeviceCapability:"
- "v12@?0B8"

```
