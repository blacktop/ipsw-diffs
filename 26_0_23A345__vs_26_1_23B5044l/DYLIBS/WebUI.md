## WebUI

> `/System/Library/PrivateFrameworks/WebUI.framework/WebUI`

```diff

-622.1.22.10.9
-  __TEXT.__text: 0x127d4
-  __TEXT.__auth_stubs: 0x5e0
-  __TEXT.__objc_methlist: 0x1140
+622.2.5.10.3
+  __TEXT.__text: 0x12e04
+  __TEXT.__auth_stubs: 0x610
+  __TEXT.__objc_methlist: 0x1180
   __TEXT.__const: 0x40
-  __TEXT.__gcc_except_tab: 0x608
+  __TEXT.__gcc_except_tab: 0x674
   __TEXT.__cstring: 0x1426
-  __TEXT.__oslogstring: 0x46c
+  __TEXT.__oslogstring: 0x445
   __TEXT.__ustring: 0x774
-  __TEXT.__unwind_info: 0x530
-  __TEXT.__objc_classname: 0x1ec
-  __TEXT.__objc_methname: 0x64d7
-  __TEXT.__objc_methtype: 0xf63
-  __TEXT.__objc_stubs: 0x3b20
-  __DATA_CONST.__got: 0x3e8
-  __DATA_CONST.__const: 0xcf8
-  __DATA_CONST.__objc_classlist: 0x70
+  __TEXT.__unwind_info: 0x580
+  __TEXT.__objc_classname: 0x204
+  __TEXT.__objc_methname: 0x651d
+  __TEXT.__objc_methtype: 0xf7e
+  __TEXT.__objc_stubs: 0x3aa0
+  __DATA_CONST.__got: 0x3f0
+  __DATA_CONST.__const: 0xd70
+  __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1498
-  __DATA_CONST.__objc_superrefs: 0x50
+  __DATA_CONST.__objc_selrefs: 0x1480
+  __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x300
+  __AUTH_CONST.__auth_got: 0x318
   __AUTH_CONST.__const: 0x1e0
   __AUTH_CONST.__cfstring: 0xdc0
-  __AUTH_CONST.__objc_const: 0x1920
+  __AUTH_CONST.__objc_const: 0x19f0
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __DATA.__objc_ivar: 0xf4
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0xf8
   __DATA.__data: 0x2b0
   __DATA.__bss: 0x88
   __DATA_DIRTY.__objc_data: 0x460

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CDB725DB-5E1C-3E0F-B7F5-4609D25FEF19
-  Functions: 380
-  Symbols:   1814
+  UUID: B0604A26-DE3B-351B-A26C-A1E3551266F2
+  Functions: 389
+  Symbols:   1848
   CStrings:  1214
 
Symbols:
+ +[WBUFormAutoFillPrompt showAutoFillPromptForAppleCashLowBalanceInWebView:title:message:chooseDifferentCardButtonTitle:addMoneyButtonTitle:completionHandler:]
+ -[WBUAlertController dealloc]
+ -[WBUAlertController deallocationHandler]
+ -[WBUAlertController setDeallocationHandler:]
+ -[WBUSheetAlertController .cxx_destruct]
+ -[WBUSheetAlertController _setUpAlert]
+ -[WBUSheetAlertController initWithAlert:automaticallyDismiss:completionHandler:]
+ -[WBUSheetAlertController tableView:cellForRowAtIndexPath:]
+ -[WBUSheetAlertController tableView:didSelectRowAtIndexPath:]
+ -[WBUSheetAlertController tableView:numberOfRowsInSection:]
+ GCC_except_table16
+ GCC_except_table17
+ GCC_except_table4
+ GCC_except_table5
+ GCC_except_table6
+ _OBJC_CLASS_$_WBUSheetAlertController
+ _OBJC_IVAR_$_WBUAlertController._deallocationHandler
+ _OBJC_IVAR_$_WBUSheetAlertController._alert
+ _OBJC_IVAR_$_WBUSheetAlertController._automaticallyDismiss
+ _OBJC_IVAR_$_WBUSheetAlertController._handler
+ _OBJC_IVAR_$_WBUSheetAlertController._tableView
+ _OBJC_METACLASS_$_WBUSheetAlertController
+ __OBJC_$_INSTANCE_METHODS_WBUSheetAlertController
+ __OBJC_$_INSTANCE_VARIABLES_WBUSheetAlertController
+ __OBJC_$_PROP_LIST_WBUSheetAlertController
+ __OBJC_CLASS_PROTOCOLS_$_WBUSheetAlertController
+ __OBJC_CLASS_RO_$_WBUSheetAlertController
+ __OBJC_METACLASS_RO_$_WBUSheetAlertController
+ __WBSRunOnceImpl
+ ___147-[WBUFormAutoFillPrompt showAutoFillPromptForUsernameInWebView:url:title:message:suggestedUsername:password:isGeneratedPassword:completionHandler:]_block_invoke_5
+ ___147-[WBUFormAutoFillPrompt showAutoFillPromptForUsernameInWebView:url:title:message:suggestedUsername:password:isGeneratedPassword:completionHandler:]_block_invoke_6
+ ___158+[WBUFormAutoFillPrompt showAutoFillPromptForAppleCashLowBalanceInWebView:title:message:chooseDifferentCardButtonTitle:addMoneyButtonTitle:completionHandler:]_block_invoke
+ ___158+[WBUFormAutoFillPrompt showAutoFillPromptForAppleCashLowBalanceInWebView:title:message:chooseDifferentCardButtonTitle:addMoneyButtonTitle:completionHandler:]_block_invoke_2
+ ___203+[WBUFormAutoFillPrompt showAutoFillPromptInWebView:title:message:cancelButtonTitle:otherButtonTitles:cancelWhenAppEntersBackground:makeFirstButtonSuggestedAction:headerViewController:completionHandler:]_block_invoke_6
+ ___203+[WBUFormAutoFillPrompt showAutoFillPromptInWebView:title:message:cancelButtonTitle:otherButtonTitles:cancelWhenAppEntersBackground:makeFirstButtonSuggestedAction:headerViewController:completionHandler:]_block_invoke_7
+ ___38-[WBUSheetAlertController _setUpAlert]_block_invoke
+ ___38-[WBUSheetAlertController _setUpAlert]_block_invoke_2
+ ___38-[WBUSheetAlertController _setUpAlert]_block_invoke_3
+ ___61-[WBUSheetAlertController tableView:didSelectRowAtIndexPath:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e23_v16?0"UIAlertAction"8ls32l8
+ ___block_descriptor_48_e8_32bs40bs_e18_v16?0"NSString"8ls32l8s40l8
+ ___block_descriptor_48_e8_32bs40bs_e8_v16?0q8ls32l8s40l8
+ ___block_descriptor_48_e8_32bs_e23_v16?0"UIAlertAction"8ls32l8
+ ___block_descriptor_56_e8_32s40s48bs_e23_v16?0"UIAlertAction"8ls32l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40s48s56bs_e25_v32?0"NSString"8Q16^B24ls56l8s32l8s40l8s48l8
+ _objc_msgSend$setDeallocationHandler:
+ _objc_sync_enter
+ _objc_sync_exit
- -[WBUAlertController _setUpAlert]
- -[WBUAlertController initWithAlert:automaticallyDismiss:completionHandler:]
- -[WBUAlertController tableView:cellForRowAtIndexPath:]
- -[WBUAlertController tableView:didSelectRowAtIndexPath:]
- -[WBUAlertController tableView:numberOfRowsInSection:]
- -[WBUFormAutoFillPrompt showAutoFillPromptForUsernameInWebView:url:title:message:suggestedUsername:password:isGeneratedPassword:completionHandler:].cold.1
- -[WBUHistory historyStoreDidFailDatabaseIntegrityCheck:]
- _OBJC_IVAR_$_WBUAlertController._alert
- _OBJC_IVAR_$_WBUAlertController._automaticallyDismiss
- _OBJC_IVAR_$_WBUAlertController._handler
- _OBJC_IVAR_$_WBUAlertController._tableView
- __OBJC_CLASS_PROTOCOLS_$_WBUAlertController
- ___33-[WBUAlertController _setUpAlert]_block_invoke
- ___33-[WBUAlertController _setUpAlert]_block_invoke_2
- ___33-[WBUAlertController _setUpAlert]_block_invoke_3
- ___56-[WBUAlertController tableView:didSelectRowAtIndexPath:]_block_invoke
- ___block_descriptor_56_e8_32bs40bs_e23_v16?0"UIAlertAction"8ls32l8s40l8
- ___block_descriptor_64_e8_32s40s48bs56bs_e23_v16?0"UIAlertAction"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_73_e8_32s40s48s56bs64bs_e25_v32?0"NSString"8Q16^B24ls56l8s64l8s32l8s40l8s48l8
- _objc_msgSend$historyDatabaseURL
- _objc_msgSend$historyDatabaseWriteAheadLogURL
- _objc_msgSend$isBeingPresented
- _objc_msgSend$presentingViewController
- _objc_msgSend$removeItemAtURL:error:
CStrings:
+ "T@?,C,N,V_deallocationHandler"
+ "WBUSheetAlertController"
+ "_deallocationHandler"
+ "deallocationHandler"
+ "setDeallocationHandler:"
+ "showAutoFillPromptForAppleCashLowBalanceInWebView:title:message:chooseDifferentCardButtonTitle:addMoneyButtonTitle:completionHandler:"
+ "v64@0:8@16@24@32@40@48@?56"
- "Failed to present prompt for username."
- "historyDatabaseURL"
- "historyDatabaseWriteAheadLogURL"
- "historyStoreDidFailDatabaseIntegrityCheck:"
- "isBeingPresented"
- "presentingViewController"
- "removeItemAtURL:error:"

```
