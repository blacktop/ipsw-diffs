## CoreRepairUI

> `/System/Library/PrivateFrameworks/CoreRepairUI.framework/CoreRepairUI`

```diff

-921.60.26.0.0
-  __TEXT.__text: 0x19d40
-  __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_methlist: 0x137c
-  __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0x2f14
-  __TEXT.__gcc_except_tab: 0x458
-  __TEXT.__oslogstring: 0xc94
-  __TEXT.__unwind_info: 0x478
+921.80.167.0.0
+  __TEXT.__text: 0x19284
+  __TEXT.__auth_stubs: 0x680
+  __TEXT.__objc_methlist: 0x1334
+  __TEXT.__const: 0xb8
+  __TEXT.__cstring: 0x2e4b
+  __TEXT.__oslogstring: 0xc5d
+  __TEXT.__gcc_except_tab: 0x404
+  __TEXT.__unwind_info: 0x448
   __TEXT.__objc_classname: 0x685
-  __TEXT.__objc_methname: 0x3486
-  __TEXT.__objc_methtype: 0x3b2
-  __TEXT.__objc_stubs: 0x2f80
-  __DATA_CONST.__got: 0x470
-  __DATA_CONST.__const: 0x428
+  __TEXT.__objc_methname: 0x3309
+  __TEXT.__objc_methtype: 0x3a1
+  __TEXT.__objc_stubs: 0x2d20
+  __DATA_CONST.__got: 0x450
+  __DATA_CONST.__const: 0x3e0
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdd8
+  __DATA_CONST.__objc_selrefs: 0xd68
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1a8
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x358
-  __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x3b00
+  __AUTH_CONST.__auth_got: 0x350
+  __AUTH_CONST.__const: 0x100
+  __AUTH_CONST.__cfstring: 0x3a00
   __AUTH_CONST.__objc_const: 0x2ef0
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 31108C4D-741B-38D0-906A-16BB30D2670A
-  Functions: 445
-  Symbols:   2016
-  CStrings:  1721
+  UUID: 81D28597-0402-3E44-B9EA-9B85BA086FF6
+  Functions: 433
+  Symbols:   1963
+  CStrings:  1687
 
Symbols:
+ ___56-[SystemHealthUI getCurrentDetailsWithPrivacySpecifier:]_block_invoke.251
+ ___56-[SystemHealthUI getCurrentDetailsWithPrivacySpecifier:]_block_invoke.276
+ ___56-[SystemHealthUI updateSpecifiersWithCompletionHandler:]_block_invoke.308
+ _objc_msgSend$integerValue
- -[SystemHealthUI configureSpin:ofCellForSpecifier:setEnabled:]
- -[SystemHealthUI getNetworkAlert]
- -[SystemHealthUI getOSUpdateAlert]
- -[SystemHealthUI getPreFlightFailedAlert]
- -[SystemHealthUI performInteractivePreflightWithSpecifier:]
- -[SystemHealthUI showActionSheets:]
- GCC_except_table14
- _OBJC_CLASS_$_UIActivityIndicatorView
- _OBJC_CLASS_$_UIAlertAction
- _OBJC_CLASS_$_UIAlertController
- _PSTableCellKey
- ___33-[SystemHealthUI getNetworkAlert]_block_invoke
- ___34-[SystemHealthUI getOSUpdateAlert]_block_invoke
- ___35-[SystemHealthUI showActionSheets:]_block_invoke
- ___35-[SystemHealthUI showActionSheets:]_block_invoke.75
- ___56-[SystemHealthUI getCurrentDetailsWithPrivacySpecifier:]_block_invoke.304
- ___56-[SystemHealthUI getCurrentDetailsWithPrivacySpecifier:]_block_invoke.310
- ___56-[SystemHealthUI updateSpecifiersWithCompletionHandler:]_block_invoke.354
- ___59-[SystemHealthUI performInteractivePreflightWithSpecifier:]_block_invoke
- ___59-[SystemHealthUI performInteractivePreflightWithSpecifier:]_block_invoke_2
- ___block_descriptor_32_e23_v16?0"UIAlertAction"8l
- ___block_descriptor_48_e8_32s40s_e23_v16?0"UIAlertAction"8ls32l8s40l8
- ___block_literal_global.40
- ___block_literal_global.68
- _objc_msgSend$actionWithTitle:style:handler:
- _objc_msgSend$addAction:
- _objc_msgSend$alertControllerWithTitle:message:preferredStyle:
- _objc_msgSend$configureSpin:ofCellForSpecifier:setEnabled:
- _objc_msgSend$getNetworkAlert
- _objc_msgSend$getOSUpdateAlert
- _objc_msgSend$getPreFlightFailedAlert
- _objc_msgSend$getRepairTicket
- _objc_msgSend$hasConnectivity
- _objc_msgSend$initWithActivityIndicatorStyle:
- _objc_msgSend$isPreflightSuccessful
- _objc_msgSend$isbatteryLevelBelowThreshold
- _objc_msgSend$performInteractiveMiniPreflightWith:
- _objc_msgSend$performInteractivePreflightWithSpecifier:
- _objc_msgSend$presentViewController:animated:completion:
- _objc_msgSend$setAccessoryView:
- _objc_msgSend$setBootIntentAndReboot
- _objc_msgSend$setButtonAction:
- _objc_msgSend$setCellEnabled:
- _objc_msgSend$startAnimating
- _objc_retain_x9
CStrings:
+ "ClaimCount%ld"
+ "ClaimCountAbove10"
+ "ClaimCountAbove100"
+ "ClaimCountAbove1000"
+ "ClaimCountAbove6"
+ "ClaimCountInvalid"
+ "SEED_BUILDS_NOT_SUPPORTED"
+ "SEED_BUILDS_NOT_SUPPORTED_IPAD"
+ "integerValue"
- "BATTERY_ERROR"
- "BATTERY_ERROR_IPAD"
- "CANCEL"
- "NETWORK_CONNECTION_DESC"
- "NETWORK_CONNECTION_DESC_IPAD"
- "NETWORK_CONNECTION_REQUIRED"
- "NOT_AVAILABLE"
- "NOT_NOW"
- "Network is not reachable"
- "OS Update required to proceed"
- "RESTART_AND_FINISH_REPAIR"
- "RestartInitiated"
- "SOFTWARE_UPDATE"
- "SOFTWARE_UPDATE_DESC"
- "SOFTWARE_UPDATE_DESC_IPAD"
- "SOFTWARE_UPDATE_REQUIRED"
- "TRY_AGAIN_LATER_DESC"
- "actionWithTitle:style:handler:"
- "addAction:"
- "alertControllerWithTitle:message:preferredStyle:"
- "configureSpin:ofCellForSpecifier:setEnabled:"
- "getNetworkAlert"
- "getOSUpdateAlert"
- "getPreFlightFailedAlert"
- "initWithActivityIndicatorStyle:"
- "performInteractivePreflightWithSpecifier:"
- "prefs:root=General&path=SOFTWARE_UPDATE_LINK"
- "presentViewController:animated:completion:"
- "setAccessoryView:"
- "setButtonAction:"
- "setCellEnabled:"
- "showActionSheets:"
- "startAnimating"
- "v16@?0@\"UIAlertAction\"8"
- "v32@0:8B16@20B28"

```
