## BarcodeSupport

> `/System/Library/PrivateFrameworks/BarcodeSupport.framework/BarcodeSupport`

```diff

-1014.1.0.0.0
-  __TEXT.__text: 0x34d18
-  __TEXT.__auth_stubs: 0x720
+1015.3.0.0.0
+  __TEXT.__text: 0x34db0
+  __TEXT.__auth_stubs: 0x740
   __TEXT.__objc_methlist: 0x2574
-  __TEXT.__cstring: 0x4077
+  __TEXT.__cstring: 0x406c
   __TEXT.__const: 0xb8
   __TEXT.__gcc_except_tab: 0x9ec
-  __TEXT.__oslogstring: 0x3883
+  __TEXT.__oslogstring: 0x3865
   __TEXT.__dlopen_cstrs: 0x82b
   __TEXT.__ustring: 0x11e
-  __TEXT.__unwind_info: 0x1160
+  __TEXT.__unwind_info: 0x1168
   __TEXT.__objc_classname: 0x784
-  __TEXT.__objc_methname: 0x64a9
-  __TEXT.__objc_methtype: 0xffa
+  __TEXT.__objc_methname: 0x64b7
+  __TEXT.__objc_methtype: 0xfef
   __TEXT.__objc_stubs: 0x59e0
-  __DATA_CONST.__got: 0xe8
+  __DATA_CONST.__got: 0xf0
   __DATA_CONST.__const: 0x10c8
   __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_catlist: 0x40

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x44a0
   __DATA_CONST.__objc_selrefs: 0x19c0
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_classrefs: 0x328
+  __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__cfstring: 0x30c0
   __AUTH_CONST.__objc_const: 0x1880
-  __AUTH_CONST.__const: 0x340
+  __AUTH_CONST.__const: 0x360
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x3a8
+  __AUTH_CONST.__auth_got: 0x3b8
   __AUTH.__objc_data: 0x1220
-  __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x328
-  __DATA.__objc_superrefs: 0x138
   __DATA.__objc_ivar: 0x258
   __DATA.__data: 0x850
-  __DATA.__bss: 0x4e8
+  __DATA.__bss: 0x4f8
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
+  - /System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport
   - /System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/ClipServices.framework/ClipServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 85FA92C8-70F6-30F1-BE37-4D59E63C5DD4
-  Functions: 1415
-  Symbols:   4854
-  CStrings:  2608
+  UUID: 3A5553D5-17FC-3DC3-9FD0-08E3CE83AD59
+  Functions: 1416
+  Symbols:   4863
+  CStrings:  2609
 
Symbols:
+ _APSRemoteConfigGetBooleanIfPresent
+ _APSRemoteConfigGetShared
+ __OBJC_$_PROP_LIST_BCSAction.304
+ ____bcs_airplayInWifiEnabled_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e48_v24?0"CTCellularPlanQRCodeAction"8"NSError"16ls40l8s32l8
+ ___block_literal_global.32
+ __bcs_airplayInWifiEnabled.onceToken
+ __bcs_airplayInWifiEnabled.remoteConfigAvailable
+ __bcs_airplayInWifiEnabled.remoteConfigValue
+ _kAPSRemoteConfigKey_AirPlaySetupAssistantAndBrokeredDiscovery
+ _objc_msgSend$getActionForCardData:completionHandler:
- __OBJC_$_PROP_LIST_BCSAction.303
- ___block_descriptor_48_e8_32s40bs_e59_v24?0"CTCellularPlanManagerCameraScanAction"8"NSError"16ls40l8s32l8
- _objc_msgSend$getCameraScanInfoForCardData:completionHandler:
CStrings:
+ "@\"CTCellularPlanQRCodeAction\""
+ "BCSURLAction: -[CoreTelephonyClient getActionForCardData]-->completionHandler"
+ "BCSURLAction: error getting CTCellularPlanQRCodeAction: %{public}@"
+ "BCSURLAction: got CTCellularPlanQRCodeAction %{private}@"
+ "T@\"NSString\",?,R,C"
+ "getActionForCardData:completionHandler:"
+ "v24@?0@\"CTCellularPlanQRCodeAction\"8@\"NSError\"16"
- "@\"CTCellularPlanManagerCameraScanAction\""
- "BCSURLAction: -[CoreTelephonyClient getCameraScanInfoForCardData]-->completionHandler"
- "BCSURLAction: error getting CTCellularPlanManagerCameraScanAction: %{public}@"
- "BCSURLAction: got CTCellularPlanManagerCameraScanAction %{private}@"
- "getCameraScanInfoForCardData:completionHandler:"
- "v24@?0@\"CTCellularPlanManagerCameraScanAction\"8@\"NSError\"16"

```
