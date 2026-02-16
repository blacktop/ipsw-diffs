## CoreRepairUI

> `/System/Library/PrivateFrameworks/CoreRepairUI.framework/CoreRepairUI`

```diff

-921.80.171.0.1
-  __TEXT.__text: 0x19dcc
-  __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_methlist: 0x137c
+921.100.255.0.0
+  __TEXT.__text: 0x1b764
+  __TEXT.__auth_stubs: 0x680
+  __TEXT.__objc_methlist: 0x1364
   __TEXT.__const: 0xb8
-  __TEXT.__cstring: 0x2f7e
-  __TEXT.__gcc_except_tab: 0x458
-  __TEXT.__oslogstring: 0xc94
-  __TEXT.__unwind_info: 0x478
-  __TEXT.__objc_classname: 0x685
-  __TEXT.__objc_methname: 0x3493
-  __TEXT.__objc_methtype: 0x3b2
-  __TEXT.__objc_stubs: 0x2fa0
-  __DATA_CONST.__got: 0x470
-  __DATA_CONST.__const: 0x428
-  __DATA_CONST.__objc_classlist: 0x1c0
+  __TEXT.__cstring: 0x2e7f
+  __TEXT.__oslogstring: 0xcf3
+  __TEXT.__gcc_except_tab: 0x400
+  __TEXT.__unwind_info: 0x558
+  __TEXT.__objc_classname: 0x6a7
+  __TEXT.__objc_methname: 0x3325
+  __TEXT.__objc_methtype: 0x3a1
+  __TEXT.__objc_stubs: 0x2d40
+  __DATA_CONST.__got: 0x450
+  __DATA_CONST.__const: 0x3e0
+  __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xde0
+  __DATA_CONST.__objc_selrefs: 0xd70
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x1a8
+  __DATA_CONST.__objc_superrefs: 0x1b0
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x358
-  __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x3bc0
-  __AUTH_CONST.__objc_const: 0x2ef0
+  __AUTH_CONST.__auth_got: 0x350
+  __AUTH_CONST.__const: 0x100
+  __AUTH_CONST.__cfstring: 0x3a60
+  __AUTH_CONST.__objc_const: 0x2f80
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x1180
+  __AUTH.__objc_data: 0x11d0
   __DATA.__objc_ivar: 0x138
   __DATA.__data: 0xc0
   __DATA.__bss: 0x128

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3C29DA68-E216-3DA8-B287-B8C2681C7745
-  Functions: 445
-  Symbols:   2017
-  CStrings:  1734
+  UUID: 3C655319-D4FB-3117-80D7-658FF0D30313
+  Functions: 446
+  Symbols:   1995
+  CStrings:  1701
 
Symbols:
+ -[CRDetailViewComponentMtubSalvaged init]
+ -[CRDetailViewComponentMtubSalvaged specifiers]
+ -[CoreRepairUIUtils setupCAARetry:].cold.1
+ -[SystemHealthUI valueForSpecifierUnverified]
+ _OBJC_CLASS_$_CRDetailViewComponentMtubSalvaged
+ _OBJC_METACLASS_$_CRDetailViewComponentMtubSalvaged
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ __OBJC_$_INSTANCE_METHODS_CRDetailViewComponentMtubSalvaged
+ __OBJC_CLASS_RO_$_CRDetailViewComponentMtubSalvaged
+ __OBJC_METACLASS_RO_$_CRDetailViewComponentMtubSalvaged
+ ___56-[SystemHealthUI getCurrentDetailsWithPrivacySpecifier:]_block_invoke.255
+ ___56-[SystemHealthUI getCurrentDetailsWithPrivacySpecifier:]_block_invoke.280
+ ___56-[SystemHealthUI updateSpecifiersWithCompletionHandler:]_block_invoke.312
+ _objc_msgSend$valueForSpecifierUnverified
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x27
+ _objc_retain_x28
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
- ___56-[SystemHealthUI getCurrentDetailsWithPrivacySpecifier:]_block_invoke.329
- ___56-[SystemHealthUI updateSpecifiersWithCompletionHandler:]_block_invoke.372
- ___59-[SystemHealthUI performInteractivePreflightWithSpecifier:]_block_invoke
- ___59-[SystemHealthUI performInteractivePreflightWithSpecifier:]_block_invoke_2
- ___block_descriptor_32_e23_v16?0"UIAlertAction"8l
- ___block_descriptor_48_e8_32s40s_e23_v16?0"UIAlertAction"8ls32l8s40l8
- ___block_literal_global.40
- ___block_literal_global.68
- _objc_claimAutoreleasedReturnValue
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
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x9
CStrings:
+ "CAA repairHistory from cache: %@"
+ "CAA repairHistory: %@ error: %@"
+ "CRDetailViewComponentMtubSalvaged"
+ "Has invalid RCHL: %d"
+ "Missing parameter"
+ "No detail views"
+ "PART_UNVERIFIED"
+ "Preflight results from cache: %@"
+ "RCHL device: %d"
+ "SEED_BUILDS_NOT_SUPPORTED"
+ "SEED_BUILDS_NOT_SUPPORTED_IPAD"
+ "Sealing Manifest DC signed: %d"
+ "UNVERIFIED_MLB_DESC"
+ "UNVERIFIED_PART"
+ "valueForSpecifierUnverified"
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
- "repairHistory: %@ error: %@"
- "repairHistoryItems:%@"
- "setAccessoryView:"
- "setButtonAction:"
- "setCellEnabled:"
- "showActionSheets:"
- "startAnimating"
- "v16@?0@\"UIAlertAction\"8"
- "v32@0:8B16@20B28"

```
