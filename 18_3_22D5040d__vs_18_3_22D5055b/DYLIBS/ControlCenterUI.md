## ControlCenterUI

> `/System/Library/PrivateFrameworks/ControlCenterUI.framework/ControlCenterUI`

```diff

-600.3.2.0.0
-  __TEXT.__text: 0x9bf24
-  __TEXT.__auth_stubs: 0x22b0
+600.3.3.100.0
+  __TEXT.__text: 0x9d1cc
+  __TEXT.__auth_stubs: 0x23b0
   __TEXT.__objc_methlist: 0x6754
-  __TEXT.__const: 0x1e64
-  __TEXT.__cstring: 0x6b6f
+  __TEXT.__const: 0x1e74
+  __TEXT.__cstring: 0x6bef
   __TEXT.__gcc_except_tab: 0x7e8
-  __TEXT.__oslogstring: 0x2850
+  __TEXT.__oslogstring: 0x29e0
   __TEXT.__dlopen_cstrs: 0xe8
   __TEXT.__constg_swiftt: 0x1eb0
-  __TEXT.__swift5_typeref: 0x1ecc
+  __TEXT.__swift5_typeref: 0x1ef0
   __TEXT.__swift5_builtin: 0x154
-  __TEXT.__swift5_reflstr: 0x12e2
-  __TEXT.__swift5_fieldmd: 0xdb0
+  __TEXT.__swift5_reflstr: 0x1312
+  __TEXT.__swift5_fieldmd: 0xdbc
   __TEXT.__swift5_assocty: 0x180
   __TEXT.__swift5_proto: 0xc8
   __TEXT.__swift5_types: 0xf4
-  __TEXT.__swift5_capture: 0xa74
+  __TEXT.__swift5_capture: 0xa5c
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__unwind_info: 0x2818
+  __TEXT.__unwind_info: 0x2820
   __TEXT.__eh_frame: 0x508
   __TEXT.__objc_classname: 0x1501
   __TEXT.__objc_methname: 0x1ae06
   __TEXT.__objc_methtype: 0x77a2
   __TEXT.__objc_stubs: 0xbc60
-  __DATA_CONST.__got: 0xc20
+  __DATA_CONST.__got: 0xc30
   __DATA_CONST.__const: 0x1120
   __DATA_CONST.__objc_classlist: 0x368
   __DATA_CONST.__objc_catlist: 0x30

   __DATA_CONST.__objc_protorefs: 0x1d8
   __DATA_CONST.__objc_superrefs: 0x1d0
   __DATA_CONST.__objc_arraydata: 0x78
-  __AUTH_CONST.__auth_got: 0x1168
-  __AUTH_CONST.__auth_ptr: 0x698
-  __AUTH_CONST.__const: 0x3298
+  __AUTH_CONST.__auth_got: 0x11e8
+  __AUTH_CONST.__auth_ptr: 0x680
+  __AUTH_CONST.__const: 0x3260
   __AUTH_CONST.__cfstring: 0x24a0
   __AUTH_CONST.__objc_const: 0x14370
   __AUTH_CONST.__objc_arrayobj: 0xf0

   __AUTH.__objc_data: 0x18d0
   __AUTH.__data: 0x6b8
   __DATA.__objc_ivar: 0x69c
-  __DATA.__data: 0x3140
+  __DATA.__data: 0x3148
   __DATA.__bss: 0x1080
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x2a70
-  __DATA_DIRTY.__data: 0x9d0
+  __DATA_DIRTY.__data: 0x9e0
   __DATA_DIRTY.__bss: 0x9f0
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/Frameworks/WidgetKit.framework/WidgetKit
   - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection
   - /System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore
+  - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BaseBoardUI.framework/BaseBoardUI

   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/GamePolicy.framework/GamePolicy
+  - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/IconFoundation.framework/IconFoundation
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MaterialKit.framework/MaterialKit
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
+  - /System/Library/PrivateFrameworks/OSEligibility.framework/OSEligibility
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /System/Library/PrivateFrameworks/PrototypeTools.framework/PrototypeTools
   - /System/Library/PrivateFrameworks/Sharing.framework/Sharing

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 4124
-  Symbols:   3098
-  CStrings:  5738
+  Symbols:   3103
+  CStrings:  5747
 
Symbols:
+ _AFDeviceSupportsSAEByDeviceCapabilityAndFeatureFlags
+ _AFIsInternalInstall
+ _AFVisualIntelligenceCameraRestricted
+ _MobileGestalt_get_cameraButtonCapability
+ _MobileGestalt_get_current_device
+ _dispatch_semaphore_create
- _dispatch_sync
CStrings:
+ "Skipped device dependent module migration"
+ "Skipped visual intelligence control migration"
+ "Starting device dependent module migration..."
+ "Starting visual intelligence control migration..."
+ "com.apple.siri.TypeToSiriWidget"
+ "com.apple.siri.VisualIntelligenceWidget"
+ "hasCameraButton: %{bool}d"
+ "isAppleIntelligenceSupported: %{bool}d, AFDeviceSupportsSAEByDeviceCapabilityAndFeatureFlags: %{bool}d, AFVisualIntelligenceCameraRestricted: %{bool}d"
+ "visualIntelligenceControlMigrated"

```
