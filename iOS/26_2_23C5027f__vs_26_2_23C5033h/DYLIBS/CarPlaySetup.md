## CarPlaySetup

> `/System/Library/PrivateFrameworks/CarPlaySetup.framework/CarPlaySetup`

```diff

-746.17.0.0.0
+746.20.0.0.0
   __TEXT.__text: 0xb8c0
   __TEXT.__auth_stubs: 0x460
   __TEXT.__objc_methlist: 0x9a4

   __TEXT.__gcc_except_tab: 0x278
   __TEXT.__unwind_info: 0x2d8
   __TEXT.__objc_classname: 0x1b0
-  __TEXT.__objc_methname: 0x2286
+  __TEXT.__objc_methname: 0x2282
   __TEXT.__objc_methtype: 0x485
   __TEXT.__objc_stubs: 0x1fe0
   __DATA_CONST.__got: 0x218

   - /System/Library/PrivateFrameworks/ProxCardKit.framework/ProxCardKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 840C013D-EFB0-3732-90BD-0D79DD974271
+  UUID: D080B338-E937-3CA9-AD26-D06E490F1FE7
   Functions: 217
   Symbols:   1024
   CStrings:  859
Symbols:
+ +[CARSetupPrompts routeSharingInfoPromptForBrand:reason:responseHandler:]
+ -[CARSetupRouteSharingPermissionViewController initWithVehicleName:brand:responseHandler:]
+ ___73+[CARSetupPrompts routeSharingInfoPromptForBrand:reason:responseHandler:]_block_invoke
+ ___73+[CARSetupPrompts routeSharingInfoPromptForBrand:reason:responseHandler:]_block_invoke_2
+ ___73+[CARSetupPrompts routeSharingInfoPromptForBrand:reason:responseHandler:]_block_invoke_3
- +[CARSetupPrompts routeSharingInfoPromptForOEMName:reason:responseHandler:]
- -[CARSetupRouteSharingPermissionViewController initWithVehicleName:oemName:responseHandler:]
- ___75+[CARSetupPrompts routeSharingInfoPromptForOEMName:reason:responseHandler:]_block_invoke
- ___75+[CARSetupPrompts routeSharingInfoPromptForOEMName:reason:responseHandler:]_block_invoke_2
- ___75+[CARSetupPrompts routeSharingInfoPromptForOEMName:reason:responseHandler:]_block_invoke_3
CStrings:
+ "initWithVehicleName:brand:responseHandler:"
+ "routeSharingInfoPromptForBrand:reason:responseHandler:"
- "initWithVehicleName:oemName:responseHandler:"
- "routeSharingInfoPromptForOEMName:reason:responseHandler:"

```
