## SafariSharedUI

> `/System/Library/PrivateFrameworks/SafariSharedUI.framework/SafariSharedUI`

```diff

-618.1.15.10.15
-  __TEXT.__text: 0x16ff44
+618.2.12.10.9
+  __TEXT.__text: 0x170070
   __TEXT.__auth_stubs: 0x1450
-  __TEXT.__objc_methlist: 0xc744
-  __TEXT.__gcc_except_tab: 0x1e96c
-  __TEXT.__cstring: 0x17f82
+  __TEXT.__objc_methlist: 0xc734
+  __TEXT.__gcc_except_tab: 0x1e9b4
+  __TEXT.__cstring: 0x17f99
   __TEXT.__const: 0x26e0
-  __TEXT.__oslogstring: 0xade1
+  __TEXT.__oslogstring: 0xae31
   __TEXT.__ustring: 0x1f00
   __TEXT.__dlopen_cstrs: 0x3f8
-  __TEXT.__unwind_info: 0x9cc4
+  __TEXT.__unwind_info: 0x9c0c
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x27d3
-  __TEXT.__objc_methname: 0x31661
+  __TEXT.__objc_methname: 0x31647
   __TEXT.__objc_methtype: 0x78c9
-  __TEXT.__objc_stubs: 0x1cbe0
+  __TEXT.__objc_stubs: 0x1cb80
   __DATA_CONST.__got: 0x7b8
-  __DATA_CONST.__const: 0x74d0
+  __DATA_CONST.__const: 0x74f8
   __DATA_CONST.__objc_classlist: 0x7b0
   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x18688
-  __DATA_CONST.__objc_selrefs: 0x8da0
+  __DATA_CONST.__objc_const: 0x186a8
+  __DATA_CONST.__objc_selrefs: 0x8d88
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_classrefs: 0xc90
   __DATA_CONST.__objc_superrefs: 0x560

   __AUTH.__objc_data: 0x4920
   __AUTH.__data: 0x70
   __DATA.__got_weak: 0xd0
-  __DATA.__objc_ivar: 0x1318
+  __DATA.__objc_ivar: 0x131c
   __DATA.__data: 0x1f80
-  __DATA.__bss: 0x1068
+  __DATA.__bss: 0x1078
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x3c0
   __DATA_DIRTY.__bss: 0x30

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   Functions: 7534
-  Symbols:   27025
+  Symbols:   27026
   CStrings:  11760
 
Symbols:
+ -[WBSAppLink _getAppLinkForBanner:withCompletionHandler:]
+ -[WBSWebExtensionsController clearPermissionStateUsedToDetermineIfExtensionShouldBeDisabledOnUpgradeForExtension:]
+ GCC_except_table166
+ GCC_except_table209
+ GCC_except_table244
+ GCC_except_table247
+ GCC_except_table339
+ GCC_except_table385
+ GCC_except_table391
+ GCC_except_table393
+ GCC_except_table396
+ GCC_except_table400
+ GCC_except_table406
+ GCC_except_table412
+ GCC_except_table414
+ GCC_except_table418
+ _OBJC_IVAR_$_WBSParsecDFeedbackDispatcher._currentQueryForVisibleResultsFeedback
+ _OBJC_IVAR_$_WBSParsecDFeedbackDispatcher._previousQueryForVisibleResultsFeedback
+ __ZGVZ108-[WBSWebExtensionsController sendMessage:toApplicationWithID:fromExtensionWithIdentifier:completionHandler:]E35nativeMessagingActiveContextTracker
+ __ZZ108-[WBSWebExtensionsController sendMessage:toApplicationWithID:fromExtensionWithIdentifier:completionHandler:]E35nativeMessagingActiveContextTracker
+ ___108-[WBSWebExtensionsController sendMessage:toApplicationWithID:fromExtensionWithIdentifier:completionHandler:]_block_invoke.158
+ ___118-[WBSWebExtensionsController setKeyedData:inStorageOfType:forExtensionWithUniqueIdentifier:webView:completionHandler:]_block_invoke.347
+ ___57-[WBSAppLink _getAppLinkForBanner:withCompletionHandler:]_block_invoke
+ ___77-[WBSWebExtensionsController postMessage:fromPortWithID:fromExtensionWithID:]_block_invoke.302
+ ___79-[WBSWebExtensionsController _deleteStorageForExtensionWithComposedIdentifier:]_block_invoke.175
+ ___91-[WBSWebExtensionsController _loadPermissionsFromStorageForWebExtension:completionHandler:]_block_invoke.306
+ ___block_descriptor_40_ea8_32s_e23_B32?0"NSDate"8Q16^B24ls32l8
+ ___block_literal_global.245
+ ___block_literal_global.262
+ ___block_literal_global.304
+ ___block_literal_global.311
+ ___block_literal_global.317
+ ___block_literal_global.327
+ ___block_literal_global.332
+ ___block_literal_global.361
+ ___block_literal_global.467
+ ___block_literal_global.474
+ ___block_literal_global.65
+ __unnamed_array_storage.463
+ __unnamed_array_storage.510
+ _objc_msgSend$_getAppLinkForBanner:withCompletionHandler:
+ _objc_msgSend$clearPermissionStateUsedToDetermineIfExtensionShouldBeDisabledOnUpgradeForExtension:
+ _objc_msgSend$safari_isEarlierThanDate:
- -[WBSAppLink _getAppLinkWithCompletionHandler:]
- -[WBSParsecDFeedbackDispatcher _visibleResultsFeedback:isShallowEqual:]
- -[WBSWebExtensionsController clearPermissionStateUsedToDetermineIfExtensionShouldBeDisabledOnUpgradeForWebExtension:]
- GCC_except_table214
- GCC_except_table245
- GCC_except_table309
- GCC_except_table340
- GCC_except_table387
- GCC_except_table392
- GCC_except_table395
- GCC_except_table397
- GCC_except_table401
- GCC_except_table408
- GCC_except_table413
- GCC_except_table417
- _OBJC_IVAR_$_WBSParsecDFeedbackDispatcher._previousQuery
- ___118-[WBSWebExtensionsController setKeyedData:inStorageOfType:forExtensionWithUniqueIdentifier:webView:completionHandler:]_block_invoke.345
- ___47-[WBSAppLink _getAppLinkWithCompletionHandler:]_block_invoke
- ___77-[WBSWebExtensionsController postMessage:fromPortWithID:fromExtensionWithID:]_block_invoke.300
- ___79-[WBSWebExtensionsController _deleteStorageForExtensionWithComposedIdentifier:]_block_invoke.172
- ___91-[WBSWebExtensionsController _loadPermissionsFromStorageForWebExtension:completionHandler:]_block_invoke.304
- ___block_literal_global.201
- ___block_literal_global.212
- ___block_literal_global.243
- ___block_literal_global.260
- ___block_literal_global.302
- ___block_literal_global.309
- ___block_literal_global.315
- ___block_literal_global.325
- ___block_literal_global.330
- ___block_literal_global.359
- ___block_literal_global.465
- ___block_literal_global.472
- __unnamed_array_storage.431
- __unnamed_array_storage.461
- __unnamed_array_storage.508
- _objc_msgSend$_getAppLinkWithCompletionHandler:
- _objc_msgSend$_visibleResultsFeedback:isShallowEqual:
- _objc_msgSend$clearPermissionStateUsedToDetermineIfExtensionShouldBeDisabledOnUpgradeForWebExtension:
- _objc_msgSend$goTakeoverResult
- _objc_msgSend$uniqueIdentifiersOfVisibleCardSections
- _objc_msgSend$uniqueIdsOfVisibleButtons
CStrings:
+ "8618.2.12.10.9"
+ "B32@?0@\"NSDate\"8Q16^B24"
+ "Dropping native message from %{private}@ due to too many active native messages"
+ "_currentQueryForVisibleResultsFeedback"
+ "_getAppLinkForBanner:withCompletionHandler:"
+ "_previousQueryForVisibleResultsFeedback"
+ "clearPermissionStateUsedToDetermineIfExtensionShouldBeDisabledOnUpgradeForExtension:"
+ "safari_isEarlierThanDate:"
- "8618.1.15.10.15"
- "_getAppLinkWithCompletionHandler:"
- "_previousQuery"
- "_visibleResultsFeedback:isShallowEqual:"
- "clearPermissionStateUsedToDetermineIfExtensionShouldBeDisabledOnUpgradeForWebExtension:"
- "goTakeoverResult"
- "uniqueIdentifiersOfVisibleCardSections"
- "uniqueIdsOfVisibleButtons"

```
