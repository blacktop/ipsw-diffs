## WebUI

> `/System/iOSSupport/System/Library/PrivateFrameworks/WebUI.framework/Versions/A/WebUI`

```diff

-620.2.4.11.6
-  __TEXT.__text: 0xec34
-  __TEXT.__auth_stubs: 0x570
-  __TEXT.__objc_methlist: 0xae0
+621.1.15.11.10
+  __TEXT.__text: 0xf51c
+  __TEXT.__auth_stubs: 0x5b0
+  __TEXT.__objc_methlist: 0x105c
   __TEXT.__const: 0x40
-  __TEXT.__gcc_except_tab: 0x4bc
-  __TEXT.__cstring: 0xbb6
-  __TEXT.__oslogstring: 0x41f
-  __TEXT.__ustring: 0x746
-  __TEXT.__unwind_info: 0x448
+  __TEXT.__gcc_except_tab: 0x4f4
+  __TEXT.__cstring: 0xcf8
+  __TEXT.__oslogstring: 0x3c5
+  __TEXT.__ustring: 0x6a0
+  __TEXT.__unwind_info: 0x468
   __TEXT.__objc_classname: 0x20a
-  __TEXT.__objc_methname: 0x5763
-  __TEXT.__objc_methtype: 0x101c
-  __TEXT.__objc_stubs: 0x3160
-  __DATA_CONST.__got: 0x330
-  __DATA_CONST.__const: 0x990
+  __TEXT.__objc_methname: 0x58f3
+  __TEXT.__objc_methtype: 0x102b
+  __TEXT.__objc_stubs: 0x3200
+  __DATA_CONST.__got: 0x338
+  __DATA_CONST.__const: 0xa80
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf00
+  __DATA_CONST.__objc_selrefs: 0x1220
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x2c8
+  __AUTH_CONST.__auth_got: 0x2e8
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0xa80
-  __AUTH_CONST.__objc_const: 0x21d0
+  __AUTH_CONST.__cfstring: 0xb00
+  __AUTH_CONST.__objc_const: 0x1790
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH.__objc_data: 0x410

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FA36F4C8-AC82-3AB3-97E4-B4356DCA506F
-  Functions: 315
-  Symbols:   1216
-  CStrings:  1051
+  UUID: 2CB63986-9A7A-371E-B3EA-9D52884892B9
+  Functions: 332
+  Symbols:   1253
+  CStrings:  1066
 
Symbols:
+ +[NSUserDefaults(WebUIExtras) webui_defaults].cold.1
+ +[WBUFeatureManager accessLevel].cold.1
+ +[WBUFeatureManager webui_sharedFeatureManager].cold.1
+ +[WBUFormAutoFillWhiteList sharedAutoFillWhiteList].cold.1
+ +[WBUGeneratedPasswordCredentialUpdater sharedUpdater].cold.1
+ -[WBUFormDataController _showPromptToUpdateCreditCardExpirationDateForWebView:cardNumber:expirationDate:completionHandler:]
+ -[WBUFormDataController completionDBPath].cold.1
+ -[WBUGeneratedPasswordCredentialUpdater _performRequest:completionHandler:]
+ -[WBUGeneratedPasswordCredentialUpdater _saveNewAccountWithRequest:completionHandler:]
+ -[WBUGeneratedPasswordCredentialUpdater _updateExistingSavedAccount:withNewGeneratedPassword:completionHandler:]
+ GCC_except_table111
+ GCC_except_table119
+ GCC_except_table120
+ GCC_except_table121
+ GCC_except_table130
+ GCC_except_table74
+ GCC_except_table80
+ GCC_except_table84
+ GCC_except_table88
+ WBS_LOG_CHANNEL_PREFIXAutoFill.cold.1
+ WBS_LOG_CHANNEL_PREFIXCrowdsourcedAutoFill.cold.1
+ _WBSOngoingSharingGroupIDNone
+ __132-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:promptingPolicy:webView:completionHandler:]_block_invoke.212
+ __132-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:promptingPolicy:webView:completionHandler:]_block_invoke.213
+ __132-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:promptingPolicy:webView:completionHandler:]_block_invoke_2.214
+ __132-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:promptingPolicy:webView:completionHandler:]_block_invoke_3.216
+ __99-[WBUFormDataController _warnAboutWeakPasswordIfNecessaryWithWebView:savedAccount:protectionSpace:]_block_invoke.270
+ __99-[WBUFormDataController _warnAboutWeakPasswordIfNecessaryWithWebView:savedAccount:protectionSpace:]_block_invoke.282
+ __99-[WBUFormDataController _warnAboutWeakPasswordIfNecessaryWithWebView:savedAccount:protectionSpace:]_block_invoke_2.285
+ ___101-[WBUFormDataController _webView:willSubmitFormContainingCreditCardData:fromFrame:submissionHandler:]_block_invoke_5
+ ___112-[WBUGeneratedPasswordCredentialUpdater _updateExistingSavedAccount:withNewGeneratedPassword:completionHandler:]_block_invoke
+ ___123-[WBUFormDataController _showPromptToUpdateCreditCardExpirationDateForWebView:cardNumber:expirationDate:completionHandler:]_block_invoke
+ ___132-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:promptingPolicy:webView:completionHandler:]_block_invoke_10
+ ___188-[WBUGeneratedPasswordCredentialUpdater updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:completionHandler:]_block_invoke_3
+ ___75-[WBUGeneratedPasswordCredentialUpdater _performRequest:completionHandler:]_block_invoke
+ ___86-[WBUGeneratedPasswordCredentialUpdater _saveNewAccountWithRequest:completionHandler:]_block_invoke
+ ___86-[WBUGeneratedPasswordCredentialUpdater _saveNewAccountWithRequest:completionHandler:]_block_invoke_2
+ ___block_descriptor_105_e8_32s40s48s56s64s72s80bs88bs96r_e8_v16?0Q8ls32l8r96l8s40l8s48l8s56l8s80l8s64l8s72l8s88l8
+ ___block_descriptor_113_e8_32s40s48s56s64s72s80s88s96s104bs_e18_v16?0"NSString"8ls32l8s40l8s48l8s56l8s64l8s72l8s104l8s80l8s88l8s96l8
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32s40s48bs_e25_v16?0"WBSSavedAccount"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e36_v16?0"WBSSavedAccountMatchResult"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e25_v16?0"WBSSavedAccount"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56bs64r_e5_v8?0ls56l8r64l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56bs64r_e8_v16?0Q8ls32l8s40l8s48l8r64l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e8_v12?0B8ls32l8s40l8s48l8s64l8s56l8
+ ___block_descriptor_97_e8_32s40s48s56s64s72s80s88bs_e18_v16?0"NSString"8ls32l8s40l8s48l8s88l8s56l8s64l8s72l8s80l8
+ __block_literal_global.514
+ __block_literal_global.535
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_notify
+ _objc_msgSend$_performRequest:completionHandler:
+ _objc_msgSend$_saveNewAccountWithRequest:completionHandler:
+ _objc_msgSend$_showPromptToUpdateCreditCardExpirationDateForWebView:cardNumber:expirationDate:completionHandler:
+ _objc_msgSend$_updateExistingSavedAccount:withNewGeneratedPassword:completionHandler:
+ _objc_msgSend$changeSavedAccountWithRequest:completionHandler:
+ _objc_msgSend$creditCardDataByMergingOtherAttributesBesidesCardNumberFromCard:mergeSecurityCode:updateExpirationDate:
+ _objc_msgSend$expirationDate
+ _objc_msgSend$expirationYearIsOlderThan:
+ _objc_msgSend$removeCredentialTypes:forSavedAccount:completionHandler:
+ _objc_msgSend$saveUser:password:forUserTypedSite:groupID:completionHandler:
+ _objc_msgSend$sharedGroupID
- -[WBUGeneratedPasswordCredentialUpdater _performRequest:]
- GCC_except_table106
- GCC_except_table109
- GCC_except_table115
- GCC_except_table116
- GCC_except_table125
- GCC_except_table77
- GCC_except_table81
- GCC_except_table85
- __132-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:promptingPolicy:webView:completionHandler:]_block_invoke.188
- __132-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:promptingPolicy:webView:completionHandler:]_block_invoke_2.189
- __132-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:promptingPolicy:webView:completionHandler:]_block_invoke_3.191
- __99-[WBUFormDataController _warnAboutWeakPasswordIfNecessaryWithWebView:savedAccount:protectionSpace:]_block_invoke.245
- __99-[WBUFormDataController _warnAboutWeakPasswordIfNecessaryWithWebView:savedAccount:protectionSpace:]_block_invoke.257
- __99-[WBUFormDataController _warnAboutWeakPasswordIfNecessaryWithWebView:savedAccount:protectionSpace:]_block_invoke_2.260
- ___block_descriptor_113_e8_32s40s48s56s64s72s80s88s96s104bs_e18_v16?0"NSString"8ls32l8s40l8s48l8s56l8s104l8s64l8s72l8s80l8s88l8s96l8
- ___block_descriptor_80_e8_32s40s48s56s64bs72r_e5_v8?0ls32l8s40l8s64l8r72l8s48l8s56l8
- ___block_descriptor_89_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s80l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_89_e8_32s40s48s56s64s72s80bs_e8_v12?0B8ls32l8s40l8s48l8s80l8s56l8s64l8s72l8
- ___block_descriptor_97_e8_32s40s48s56s64s72s80s88bs_e18_v16?0"NSString"8ls88l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8
- __block_literal_global.488
- __block_literal_global.506
- _objc_msgSend$_performRequest:
- _objc_msgSend$allValues
- _objc_msgSend$credentialsForProtectionSpace:
- _objc_msgSend$creditCardDataByMergingOtherAttributesBesidesCardNumberFromCard:mergeSecurityCode:
- _objc_msgSend$lastGeneratedPassword
- _objc_msgSend$removeCredentialTypes:forSavedAccount:
CStrings:
+ "Keychain credit card update (save security code data sheet)"
+ "Keychain credit card update (update expiration date data sheet)"
+ "Not Now (update credit card expiration date data sheet)"
+ "Update (update credit card expiration date data sheet)"
+ "Would you like Safari to update the expiration date for this credit card?"
+ "_performRequest:completionHandler:"
+ "_saveNewAccountWithRequest:completionHandler:"
+ "_showPromptToUpdateCreditCardExpirationDateForWebView:cardNumber:expirationDate:completionHandler:"
+ "_updateExistingSavedAccount:withNewGeneratedPassword:completionHandler:"
+ "changeSavedAccountWithRequest:completionHandler:"
+ "creditCardDataByMergingOtherAttributesBesidesCardNumberFromCard:mergeSecurityCode:updateExpirationDate:"
+ "expirationDate"
+ "expirationYearIsOlderThan:"
+ "iCloud keychain credit card update (save security code data sheet)"
+ "iCloud keychain credit card update (update expiration date data sheet)"
+ "removeCredentialTypes:forSavedAccount:completionHandler:"
+ "saveUser:password:forUserTypedSite:groupID:completionHandler:"
+ "sharedGroupID"
+ "v32@0:8@16@?24"
- "Safari will update the credit card saved in your Keychain."
- "Safari will update the credit card saved in your iCloud Keychain."
- "Using NSURLCredentialStorage to remove credential for user %{sensitive}@ on %{sensitive}@"
- "_performRequest:"
- "allValues"
- "credentialsForProtectionSpace:"
- "creditCardDataByMergingOtherAttributesBesidesCardNumberFromCard:mergeSecurityCode:"
- "removeCredentialTypes:forSavedAccount:"

```
