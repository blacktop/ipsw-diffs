## CoreRepairUI

> `/System/Library/PrivateFrameworks/CoreRepairUI.framework/CoreRepairUI`

```diff

 921.0.120.0.0
-  __TEXT.__text: 0x1b72c
-  __TEXT.__auth_stubs: 0xa30
-  __TEXT.__objc_methlist: 0x136c
+  __TEXT.__text: 0x1c274
+  __TEXT.__auth_stubs: 0xa40
+  __TEXT.__objc_methlist: 0x13b4
   __TEXT.__const: 0x2b6
-  __TEXT.__cstring: 0x2f29
-  __TEXT.__oslogstring: 0xc5d
-  __TEXT.__gcc_except_tab: 0x404
+  __TEXT.__cstring: 0x3059
+  __TEXT.__gcc_except_tab: 0x458
+  __TEXT.__oslogstring: 0xc94
   __TEXT.__constg_swiftt: 0x70
   __TEXT.__swift5_typeref: 0x133
   __TEXT.__swift5_fieldmd: 0x2c

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x4d8
+  __TEXT.__unwind_info: 0x508
   __TEXT.__objc_classname: 0x685
-  __TEXT.__objc_methname: 0x33c0
-  __TEXT.__objc_methtype: 0x3a1
-  __TEXT.__objc_stubs: 0x2cc0
-  __DATA_CONST.__got: 0x4c0
-  __DATA_CONST.__const: 0x488
+  __TEXT.__objc_methname: 0x354a
+  __TEXT.__objc_methtype: 0x3b2
+  __TEXT.__objc_stubs: 0x2f40
+  __DATA_CONST.__got: 0x4e0
+  __DATA_CONST.__const: 0x4d0
   __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdc8
+  __DATA_CONST.__objc_selrefs: 0xe40
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1a8
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x528
-  __AUTH_CONST.__const: 0x218
-  __AUTH_CONST.__cfstring: 0x38e0
+  __AUTH_CONST.__auth_got: 0x530
+  __AUTH_CONST.__const: 0x258
+  __AUTH_CONST.__cfstring: 0x3aa0
   __AUTH_CONST.__objc_const: 0x2f38
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5464AA36-20F9-36AB-993C-638171535C7E
-  Functions: 486
-  Symbols:   2076
-  CStrings:  1692
+  UUID: 16215B13-D59B-3195-A2CF-229C810B9415
+  Functions: 498
+  Symbols:   2130
+  CStrings:  1739
 
Symbols:
+ -[SystemHealthUI configureSpin:ofCellForSpecifier:setEnabled:]
+ -[SystemHealthUI getNetworkAlert]
+ -[SystemHealthUI getOSUpdateAlert]
+ -[SystemHealthUI getPreFlightFailedAlert]
+ -[SystemHealthUI performInteractivePreflightWithSpecifier:]
+ -[SystemHealthUI showActionSheets:]
+ GCC_except_table14
+ _OBJC_CLASS_$_UIActivityIndicatorView
+ _OBJC_CLASS_$_UIAlertAction
+ _OBJC_CLASS_$_UIAlertController
+ _PSTableCellKey
+ ___33-[SystemHealthUI getNetworkAlert]_block_invoke
+ ___34-[SystemHealthUI getOSUpdateAlert]_block_invoke
+ ___35-[SystemHealthUI showActionSheets:]_block_invoke
+ ___35-[SystemHealthUI showActionSheets:]_block_invoke.75
+ ___56-[SystemHealthUI getCurrentDetailsWithPrivacySpecifier:]_block_invoke.304
+ ___56-[SystemHealthUI getCurrentDetailsWithPrivacySpecifier:]_block_invoke.310
+ ___56-[SystemHealthUI updateSpecifiersWithCompletionHandler:]_block_invoke.354
+ ___59-[SystemHealthUI performInteractivePreflightWithSpecifier:]_block_invoke
+ ___59-[SystemHealthUI performInteractivePreflightWithSpecifier:]_block_invoke_2
+ ___block_descriptor_32_e23_v16?0"UIAlertAction"8l
+ ___block_descriptor_48_e8_32s40s_e23_v16?0"UIAlertAction"8ls32l8s40l8
+ ___block_literal_global.40
+ ___block_literal_global.68
+ _objc_msgSend$actionWithTitle:style:handler:
+ _objc_msgSend$addAction:
+ _objc_msgSend$alertControllerWithTitle:message:preferredStyle:
+ _objc_msgSend$configureSpin:ofCellForSpecifier:setEnabled:
+ _objc_msgSend$getNetworkAlert
+ _objc_msgSend$getOSUpdateAlert
+ _objc_msgSend$getPreFlightFailedAlert
+ _objc_msgSend$getRepairTicket
+ _objc_msgSend$hasConnectivity
+ _objc_msgSend$initWithActivityIndicatorStyle:
+ _objc_msgSend$isPreflightSuccessful
+ _objc_msgSend$isbatteryLevelBelowThreshold
+ _objc_msgSend$performInteractiveMiniPreflightWith:
+ _objc_msgSend$performInteractivePreflightWithSpecifier:
+ _objc_msgSend$presentViewController:animated:completion:
+ _objc_msgSend$setAccessoryView:
+ _objc_msgSend$setBootIntentAndReboot
+ _objc_msgSend$setButtonAction:
+ _objc_msgSend$setCellEnabled:
+ _objc_msgSend$startAnimating
+ _objc_retain_x9
- ___56-[SystemHealthUI getCurrentDetailsWithPrivacySpecifier:]_block_invoke.251
- ___56-[SystemHealthUI getCurrentDetailsWithPrivacySpecifier:]_block_invoke.257
- ___56-[SystemHealthUI updateSpecifiersWithCompletionHandler:]_block_invoke.290
CStrings:
+ "BATTERY_ERROR"
+ "BATTERY_ERROR_IPAD"
+ "CANCEL"
+ "NETWORK_CONNECTION_DESC"
+ "NETWORK_CONNECTION_DESC_IPAD"
+ "NETWORK_CONNECTION_REQUIRED"
+ "NOT_AVAILABLE"
+ "NOT_NOW"
+ "Network is not reachable"
+ "OS Update required to proceed"
+ "RESTART_AND_FINISH_REPAIR"
+ "RestartInitiated"
+ "SOFTWARE_UPDATE"
+ "SOFTWARE_UPDATE_DESC"
+ "SOFTWARE_UPDATE_DESC_IPAD"
+ "SOFTWARE_UPDATE_REQUIRED"
+ "TRY_AGAIN_LATER_DESC"
+ "actionWithTitle:style:handler:"
+ "addAction:"
+ "alertControllerWithTitle:message:preferredStyle:"
+ "configureSpin:ofCellForSpecifier:setEnabled:"
+ "getNetworkAlert"
+ "getOSUpdateAlert"
+ "getPreFlightFailedAlert"
+ "initWithActivityIndicatorStyle:"
+ "performInteractivePreflightWithSpecifier:"
+ "prefs:root=General&path=SOFTWARE_UPDATE_LINK"
+ "presentViewController:animated:completion:"
+ "setAccessoryView:"
+ "setButtonAction:"
+ "setCellEnabled:"
+ "showActionSheets:"
+ "startAnimating"
+ "v16@?0@\"UIAlertAction\"8"
+ "v32@0:8B16@20B28"
- "SEED_BUILDS_NOT_SUPPORTED"
- "SEED_BUILDS_NOT_SUPPORTED_IPAD"

```
