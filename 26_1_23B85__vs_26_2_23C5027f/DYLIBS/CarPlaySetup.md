## CarPlaySetup

> `/System/Library/PrivateFrameworks/CarPlaySetup.framework/CarPlaySetup`

```diff

-746.11.0.0.0
-  __TEXT.__text: 0xb018
-  __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_methlist: 0x954
+746.17.0.0.0
+  __TEXT.__text: 0xb8c0
+  __TEXT.__auth_stubs: 0x460
+  __TEXT.__objc_methlist: 0x9a4
   __TEXT.__const: 0xa0
   __TEXT.__oslogstring: 0x4ab
-  __TEXT.__cstring: 0xda5
+  __TEXT.__cstring: 0xec1
   __TEXT.__gcc_except_tab: 0x278
-  __TEXT.__unwind_info: 0x2c8
-  __TEXT.__objc_classname: 0x183
-  __TEXT.__objc_methname: 0x2184
+  __TEXT.__unwind_info: 0x2d8
+  __TEXT.__objc_classname: 0x1b0
+  __TEXT.__objc_methname: 0x2286
   __TEXT.__objc_methtype: 0x485
-  __TEXT.__objc_stubs: 0x1f20
-  __DATA_CONST.__got: 0x210
+  __TEXT.__objc_stubs: 0x1fe0
+  __DATA_CONST.__got: 0x218
   __DATA_CONST.__const: 0x290
-  __DATA_CONST.__objc_classlist: 0x50
+  __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9d0
+  __DATA_CONST.__objc_selrefs: 0xa20
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0xb0
-  __AUTH_CONST.__auth_got: 0x238
+  __AUTH_CONST.__auth_got: 0x240
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x1420
-  __AUTH_CONST.__objc_const: 0x1298
+  __AUTH_CONST.__cfstring: 0x1540
+  __AUTH_CONST.__objc_const: 0x1368
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH.__objc_data: 0x320
-  __DATA.__objc_ivar: 0x98
+  __AUTH.__objc_data: 0x370
+  __DATA.__objc_ivar: 0x9c
   __DATA.__data: 0x180
   __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/BaseBoardUI.framework/BaseBoardUI
   - /System/Library/PrivateFrameworks/CarKit.framework/CarKit
+  - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/ProxCardKit.framework/ProxCardKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D51C1314-029C-3F20-891F-86533CE8274D
-  Functions: 208
-  Symbols:   988
-  CStrings:  830
+  UUID: 840C013D-EFB0-3732-90BD-0D79DD974271
+  Functions: 217
+  Symbols:   1024
+  CStrings:  859
 
Symbols:
+ +[CARSetupPrompts routeSharingInfoPromptForOEMName:reason:responseHandler:]
+ -[CARSetupRouteSharingPermissionViewController .cxx_destruct]
+ -[CARSetupRouteSharingPermissionViewController _handleAllow:]
+ -[CARSetupRouteSharingPermissionViewController _handleDontAllow:]
+ -[CARSetupRouteSharingPermissionViewController initWithVehicleName:oemName:responseHandler:]
+ -[CARSetupRouteSharingPermissionViewController responseHandler]
+ _OBJC_CLASS_$_CARSetupRouteSharingPermissionViewController
+ _OBJC_CLASS_$_OBLinkTrayButton
+ _OBJC_CLASS_$_OBWelcomeController
+ _OBJC_IVAR_$_CARSetupRouteSharingPermissionViewController._responseHandler
+ _OBJC_METACLASS_$_CARSetupRouteSharingPermissionViewController
+ _OBJC_METACLASS_$_OBWelcomeController
+ __OBJC_$_INSTANCE_METHODS_CARSetupRouteSharingPermissionViewController
+ __OBJC_$_INSTANCE_VARIABLES_CARSetupRouteSharingPermissionViewController
+ __OBJC_$_PROP_LIST_CARSetupRouteSharingPermissionViewController
+ __OBJC_CLASS_RO_$_CARSetupRouteSharingPermissionViewController
+ __OBJC_METACLASS_RO_$_CARSetupRouteSharingPermissionViewController
+ ___105+[CARSetupPrompts assetSupportingUseWirelessPromptWithWirelessEnablement:declineVariant:responseHandler:]_block_invoke.267
+ ___106+[CARSetupPrompts assetSupportingConnectPromptWithBluetoothOnlyOption:wirelessEnablement:responseHandler:]_block_invoke.244
+ ___106+[CARSetupPrompts assetSupportingConnectPromptWithBluetoothOnlyOption:wirelessEnablement:responseHandler:]_block_invoke.245
+ ___75+[CARSetupPrompts routeSharingInfoPromptForOEMName:reason:responseHandler:]_block_invoke
+ ___75+[CARSetupPrompts routeSharingInfoPromptForOEMName:reason:responseHandler:]_block_invoke_2
+ ___75+[CARSetupPrompts routeSharingInfoPromptForOEMName:reason:responseHandler:]_block_invoke_3
+ ___91+[CARSetupPrompts connectPromptWithBluetoothOnlyOption:wirelessEnablement:responseHandler:]_block_invoke.188
+ ___91+[CARSetupPrompts connectPromptWithBluetoothOnlyOption:wirelessEnablement:responseHandler:]_block_invoke.189
+ _objc_msgSend$addButton:
+ _objc_msgSend$addTarget:action:forControlEvents:
+ _objc_msgSend$buttonTray
+ _objc_msgSend$initWithTitle:detailText:symbolName:
+ _objc_msgSend$linkButton
+ _objc_msgSend$setTitle:forState:
+ _objc_retain_x25
- ___105+[CARSetupPrompts assetSupportingUseWirelessPromptWithWirelessEnablement:declineVariant:responseHandler:]_block_invoke.252
- ___106+[CARSetupPrompts assetSupportingConnectPromptWithBluetoothOnlyOption:wirelessEnablement:responseHandler:]_block_invoke.229
- ___106+[CARSetupPrompts assetSupportingConnectPromptWithBluetoothOnlyOption:wirelessEnablement:responseHandler:]_block_invoke.230
- ___91+[CARSetupPrompts connectPromptWithBluetoothOnlyOption:wirelessEnablement:responseHandler:]_block_invoke.171
- ___91+[CARSetupPrompts connectPromptWithBluetoothOnlyOption:wirelessEnablement:responseHandler:]_block_invoke.172
CStrings:
+ "ALLOW_ROUTE_SHARING_CARD_ALLOW"
+ "ALLOW_ROUTE_SHARING_CARD_DECLINE"
+ "ALLOW_ROUTE_SHARING_CARD_MESSAGE_%@_%@"
+ "ALLOW_ROUTE_SHARING_CARD_TITLE"
+ "CARSetupRouteSharingPermissionViewController"
+ "ROUTE_SHARING_PERMISSION_ALLOW"
+ "ROUTE_SHARING_PERMISSION_CARD_BODY_%@"
+ "ROUTE_SHARING_PERMISSION_CARD_TITLE_%@"
+ "ROUTE_SHARING_PERMISSION_DONT_ALLOW"
+ "_handleAllow:"
+ "_handleDontAllow:"
+ "addButton:"
+ "addTarget:action:forControlEvents:"
+ "buttonTray"
+ "initWithTitle:detailText:symbolName:"
+ "initWithVehicleName:oemName:responseHandler:"
+ "linkButton"
+ "route"
+ "routeSharingInfoPromptForOEMName:reason:responseHandler:"
+ "setTitle:forState:"

```
