## MobileMailUI

> `/System/Library/PrivateFrameworks/MobileMailUI.framework/MobileMailUI`

```diff

-3774.400.21.0.0
-  __TEXT.__text: 0x3a5e4
+3774.500.171.2.2
+  __TEXT.__text: 0x3b034
   __TEXT.__auth_stubs: 0x980
-  __TEXT.__objc_methlist: 0x3578
-  __TEXT.__gcc_except_tab: 0x8144
+  __TEXT.__objc_methlist: 0x35e0
+  __TEXT.__gcc_except_tab: 0x82f8
   __TEXT.__cstring: 0x2ba8
   __TEXT.__ustring: 0x318
   __TEXT.__const: 0x1546a
-  __TEXT.__oslogstring: 0x19d2
-  __TEXT.__unwind_info: 0x2360
-  __TEXT.__objc_classname: 0xa2f
-  __TEXT.__objc_methname: 0x10a38
-  __TEXT.__objc_methtype: 0x4058
-  __TEXT.__objc_stubs: 0xb540
+  __TEXT.__oslogstring: 0x1a39
+  __TEXT.__unwind_info: 0x23a0
+  __TEXT.__objc_classname: 0xa2d
+  __TEXT.__objc_methname: 0x10ba2
+  __TEXT.__objc_methtype: 0x4107
+  __TEXT.__objc_stubs: 0xb5e0
   __DATA_CONST.__got: 0x360
-  __DATA_CONST.__const: 0x11c8
+  __DATA_CONST.__const: 0x1218
   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x7ba8
-  __DATA_CONST.__objc_selrefs: 0x3608
+  __DATA_CONST.__objc_const: 0x7c70
+  __DATA_CONST.__objc_selrefs: 0x3630
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0x618
+  __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0x38
   __AUTH_CONST.__cfstring: 0x2de0
-  __AUTH_CONST.__objc_const: 0x1500
+  __AUTH_CONST.__objc_const: 0x1548
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__const: 0x400
   __AUTH_CONST.__objc_arrayobj: 0x30

   __AUTH_CONST.__auth_got: 0x4d0
   __AUTH.__objc_data: 0x550
   __AUTH.__data: 0x10
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x618
-  __DATA.__objc_superrefs: 0x130
-  __DATA.__objc_ivar: 0x444
+  __DATA.__objc_ivar: 0x44c
   __DATA.__data: 0xf90
   __DATA.__bss: 0x68
   __DATA_DIRTY.__objc_data: 0xaf0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 079FAA48-59B3-3D11-B5FA-1A91EAF0035E
-  Functions: 1321
-  Symbols:   6342
-  CStrings:  3921
+  UUID: 0A5AD19E-A058-3489-A809-80072B634497
+  Functions: 1331
+  Symbols:   6377
+  CStrings:  3938
 
Symbols:
+ +[MFAddressAtomStatusManager shouldDecorateAtomListForSender:replyTo:]
+ -[MFAddressAtomStatusManager replyToList]
+ -[MFAddressAtomStatusManager setReplyToList:]
+ -[MFAddressAtomStatusManager updateWithReplyToInformation:]
+ -[MFMessageContentView _updatedHeaderViewModelForMessage:replyToList:]
+ -[MessageHeaderViewModel replyToList]
+ -[MessageHeaderViewModel setReplyToList:]
+ GCC_except_table101
+ GCC_except_table119
+ GCC_except_table125
+ GCC_except_table132
+ GCC_except_table139
+ GCC_except_table150
+ GCC_except_table152
+ GCC_except_table156
+ GCC_except_table157
+ GCC_except_table170
+ GCC_except_table180
+ GCC_except_table192
+ GCC_except_table194
+ GCC_except_table202
+ GCC_except_table204
+ GCC_except_table206
+ GCC_except_table208
+ GCC_except_table212
+ GCC_except_table216
+ GCC_except_table220
+ GCC_except_table224
+ GCC_except_table225
+ GCC_except_table232
+ GCC_except_table242
+ GCC_except_table244
+ GCC_except_table249
+ GCC_except_table255
+ GCC_except_table259
+ GCC_except_table264
+ GCC_except_table266
+ GCC_except_table268
+ GCC_except_table340
+ GCC_except_table341
+ GCC_except_table348
+ GCC_except_table49
+ GCC_except_table57
+ GCC_except_table63
+ GCC_except_table67
+ GCC_except_table76
+ GCC_except_table82
+ GCC_except_table84
+ GCC_except_table96
+ GCC_except_table97
+ _OBJC_IVAR_$_MFAddressAtomStatusManager._replyToList
+ _OBJC_IVAR_$_MessageHeaderViewModel._replyToList
+ __OBJC_$_CLASS_METHODS_MFAddressAtomStatusManager
+ ___42-[MFMessageContentView setContentRequest:]_block_invoke.162
+ ___42-[MFMessageContentView setContentRequest:]_block_invoke.162.cold.1
+ ___42-[MFMessageContentView setContentRequest:]_block_invoke.164
+ ___42-[MFMessageContentView setContentRequest:]_block_invoke.165
+ ___59-[MFAddressAtomStatusManager updateWithReplyToInformation:]_block_invoke
+ ___60-[MFMessageContentView _webView:renderingProgressDidChange:]_block_invoke.369
+ ___60-[MFMessageContentView generateSnapshotImageWithCompletion:]_block_invoke.275
+ ___70-[MFMessageContentView _updatedHeaderViewModelForMessage:replyToList:]_block_invoke
+ ___71-[MessageContentItemsHelper startDownloadForContentItem:userInitiated:]_block_invoke.109
+ ___71-[MessageContentItemsHelper startDownloadForContentItem:userInitiated:]_block_invoke.122
+ ___73-[MFMessageContentView _webView:webContentProcessDidTerminateWithReason:]_block_invoke.370
+ ___block_descriptor_48_ea8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_64_ea8_32s40s48s56s_e41_v16?0"<MessageHeaderViewModelBuilder>"8ls32l8s40l8s48l8s56l8
+ ___block_literal_global.1441
+ ___block_literal_global.1448
+ ___block_literal_global.173
+ ___block_literal_global.176
+ ___block_literal_global.209
+ ___block_literal_global.256
+ __unnamed_array_storage.351
+ _objc_msgSend$_updatedHeaderViewModelForMessage:replyToList:
+ _objc_msgSend$replyToList
+ _objc_msgSend$setReplyToList:
+ _objc_msgSend$shouldDecorateAtomListForSender:replyTo:
+ _objc_msgSend$updateWithReplyToInformation:
- GCC_except_table100
- GCC_except_table107
- GCC_except_table122
- GCC_except_table128
- GCC_except_table142
- GCC_except_table147
- GCC_except_table153
- GCC_except_table155
- GCC_except_table160
- GCC_except_table162
- GCC_except_table173
- GCC_except_table186
- GCC_except_table197
- GCC_except_table201
- GCC_except_table205
- GCC_except_table209
- GCC_except_table210
- GCC_except_table211
- GCC_except_table221
- GCC_except_table222
- GCC_except_table223
- GCC_except_table228
- GCC_except_table230
- GCC_except_table235
- GCC_except_table245
- GCC_except_table252
- GCC_except_table253
- GCC_except_table258
- GCC_except_table265
- GCC_except_table337
- GCC_except_table338
- GCC_except_table345
- GCC_except_table48
- GCC_except_table52
- GCC_except_table60
- GCC_except_table70
- GCC_except_table79
- GCC_except_table88
- GCC_except_table93
- GCC_except_table99
- ___42-[MFMessageContentView setContentRequest:]_block_invoke.158
- ___42-[MFMessageContentView setContentRequest:]_block_invoke.163
- ___42-[MFMessageContentView setContentRequest:]_block_invoke.163.cold.1
- ___60-[MFMessageContentView _webView:renderingProgressDidChange:]_block_invoke.367
- ___60-[MFMessageContentView generateSnapshotImageWithCompletion:]_block_invoke.273
- ___71-[MessageContentItemsHelper startDownloadForContentItem:userInitiated:]_block_invoke.108
- ___71-[MessageContentItemsHelper startDownloadForContentItem:userInitiated:]_block_invoke.121
- ___73-[MFMessageContentView _webView:webContentProcessDidTerminateWithReason:]_block_invoke.368
- ___block_literal_global.1430
- ___block_literal_global.1437
- ___block_literal_global.167
- ___block_literal_global.174
- ___block_literal_global.208
- ___block_literal_global.254
- __unnamed_array_storage.349
CStrings:
+ "\f"
+ "<%{public}@: %p>: Failed to display message for header view model: %{public}@ due to error: %{public}@"
+ "@\"NSString\"24@0:8@\"WKWebView\"16"
+ "T@\"NSArray\",&,N,V_replyToList"
+ "T@\"NSArray\",C,N,V_replyToList"
+ "T@\"NSString\",?,R,C"
+ "_hostSceneBundleIdentifierForWebView:"
+ "_hostSceneIdentifierForWebView:"
+ "_replyToList"
+ "_updatedHeaderViewModelForMessage:replyToList:"
+ "_webView:didPromptForStorageAccess:forSubFrameDomain:forQuirk:"
+ "_webView:startXRSessionWithFeatures:completionHandler:"
+ "replyToList"
+ "setReplyToList:"
+ "shouldDecorateAtomListForSender:replyTo:"
+ "updateWithReplyToInformation:"
+ "v40@0:8@\"WKWebView\"16Q24@?<v@?@@\"UIViewController\">32"
+ "v40@0:8@16Q24@?32"
+ "v44@0:8@\"WKWebView\"16@\"NSString\"24@\"NSString\"32B40"
+ "v44@0:8@16@24@32B40"
- "\v"
- "$"
- "_webView:requestWebAuthenticationNoGestureForOrigin:completionHandler:"

```
