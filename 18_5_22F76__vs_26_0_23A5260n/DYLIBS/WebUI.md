## WebUI

> `/System/Library/PrivateFrameworks/WebUI.framework/WebUI`

```diff

-621.2.5.10.10
-  __TEXT.__text: 0x111b8
+622.1.14.10.4
+  __TEXT.__text: 0x12be0
   __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_methlist: 0x1164
+  __TEXT.__objc_methlist: 0x11d4
   __TEXT.__const: 0x40
-  __TEXT.__gcc_except_tab: 0x564
-  __TEXT.__cstring: 0xee7
-  __TEXT.__oslogstring: 0x564
+  __TEXT.__gcc_except_tab: 0x5dc
+  __TEXT.__cstring: 0x143b
+  __TEXT.__oslogstring: 0x5b4
   __TEXT.__ustring: 0x774
-  __TEXT.__unwind_info: 0x4d8
-  __TEXT.__objc_classname: 0x242
-  __TEXT.__objc_methname: 0x627e
-  __TEXT.__objc_methtype: 0x10c3
-  __TEXT.__objc_stubs: 0x3900
-  __DATA_CONST.__got: 0x400
-  __DATA_CONST.__const: 0xb90
+  __TEXT.__unwind_info: 0x528
+  __TEXT.__objc_classname: 0x244
+  __TEXT.__objc_methname: 0x6790
+  __TEXT.__objc_methtype: 0x110b
+  __TEXT.__objc_stubs: 0x3be0
+  __DATA_CONST.__got: 0x418
+  __DATA_CONST.__const: 0xcf8
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1428
+  __DATA_CONST.__objc_selrefs: 0x14f0
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__auth_got: 0x318
-  __AUTH_CONST.__const: 0x1c0
-  __AUTH_CONST.__cfstring: 0xc60
-  __AUTH_CONST.__objc_const: 0x1948
+  __AUTH_CONST.__const: 0x200
+  __AUTH_CONST.__cfstring: 0xdc0
+  __AUTH_CONST.__objc_const: 0x19c8
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __DATA.__objc_ivar: 0xf0
+  __DATA.__objc_ivar: 0xfc
   __DATA.__data: 0x370
-  __DATA.__bss: 0x78
+  __DATA.__bss: 0x88
   __DATA_DIRTY.__objc_data: 0x460
   __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 14F55723-1864-3E10-9334-52201D1E7E1F
-  Functions: 363
-  Symbols:   1766
-  CStrings:  1178
+  UUID: 4B70ABFA-052E-32CB-942C-CBCED9F18714
+  Functions: 391
+  Symbols:   1865
+  CStrings:  1239
 
Symbols:
+ +[WBUGeneratedPasswordCredentialUpdateRequest requestWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:shouldSaveExistingCredential:]
+ -[WBUCreditCardDataController shouldOfferVirtualCards]
+ -[WBUFeatureManager _determineIfContentFilteringEnabledOrManagedByParentWithCompletionHandler:]
+ -[WBUFeatureManager determineIfHistoryClearingIsAvailableWithCompletionHandler:]
+ -[WBUFeatureManager determineIfScreenTimePasscodeIsSetWithCompletionHandler:]
+ -[WBUFormAutoFillPrompt showAutoFillPromptForUsernameInWebView:url:title:message:suggestedUsername:password:isGeneratedPassword:completionHandler:]
+ -[WBUFormDataController _detailTextForPromptToSaveSecurityCode]
+ -[WBUFormDataController _detailTextForPromptToUpdateExpirationDate]
+ -[WBUFormDataController _silentlyUpdateCredentialsForSavedAccounts:withPassword:]
+ -[WBUFormDataController _silentlyUpdateSavedAccountsEquivalentToUserName:atURL:inContext:withPassword:]
+ -[WBUFormDataController lastFilledSavedAccount]
+ -[WBUFormDataController setLastFilledSavedAccount:]
+ -[WBUGeneratedPasswordCredentialUpdateRequest _initRequestWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:shouldSaveExistingCredential:]
+ -[WBUGeneratedPasswordCredentialUpdateRequest shouldSaveExistingCredential]
+ -[WBUGeneratedPasswordCredentialUpdater updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:shouldSaveExistingCredential:completionHandler:]
+ GCC_except_table100
+ GCC_except_table104
+ GCC_except_table129
+ GCC_except_table143
+ GCC_except_table144
+ GCC_except_table145
+ GCC_except_table155
+ GCC_except_table24
+ GCC_except_table79
+ GCC_except_table92
+ GCC_except_table96
+ _OBJC_CLASS_$_SFSuggestedUserProvider
+ _OBJC_CLASS_$_UITextSuggestion
+ _OBJC_CLASS_$_WBSSavedAccountMatchResult
+ _OBJC_IVAR_$_WBUFormAutoFillPrompt._url
+ _OBJC_IVAR_$_WBUFormDataController._lastFilledSavedAccount
+ _OBJC_IVAR_$_WBUGeneratedPasswordCredentialUpdateRequest._shouldSaveExistingCredential
+ _WBS_LOG_CHANNEL_PREFIXKeychain
+ _WBS_LOG_CHANNEL_PREFIXKeychain.cold.1
+ _WBS_LOG_CHANNEL_PREFIXKeychain.log
+ _WBS_LOG_CHANNEL_PREFIXKeychain.onceToken
+ ___101-[WBUFormDataController _webView:willSubmitFormContainingCreditCardData:fromFrame:submissionHandler:]_block_invoke_10
+ ___101-[WBUFormDataController _webView:willSubmitFormContainingCreditCardData:fromFrame:submissionHandler:]_block_invoke_11
+ ___101-[WBUFormDataController _webView:willSubmitFormContainingCreditCardData:fromFrame:submissionHandler:]_block_invoke_12
+ ___101-[WBUFormDataController _webView:willSubmitFormContainingCreditCardData:fromFrame:submissionHandler:]_block_invoke_6
+ ___101-[WBUFormDataController _webView:willSubmitFormContainingCreditCardData:fromFrame:submissionHandler:]_block_invoke_7
+ ___101-[WBUFormDataController _webView:willSubmitFormContainingCreditCardData:fromFrame:submissionHandler:]_block_invoke_8
+ ___101-[WBUFormDataController _webView:willSubmitFormContainingCreditCardData:fromFrame:submissionHandler:]_block_invoke_9
+ ___103-[WBUFormDataController _silentlyUpdateSavedAccountsEquivalentToUserName:atURL:inContext:withPassword:]_block_invoke
+ ___132-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:promptingPolicy:webView:completionHandler:]_block_invoke.291
+ ___132-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:promptingPolicy:webView:completionHandler:]_block_invoke.293
+ ___132-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:promptingPolicy:webView:completionHandler:]_block_invoke_2.292
+ ___132-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:promptingPolicy:webView:completionHandler:]_block_invoke_2.294
+ ___132-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:promptingPolicy:webView:completionHandler:]_block_invoke_3.296
+ ___147-[WBUFormAutoFillPrompt showAutoFillPromptForUsernameInWebView:url:title:message:suggestedUsername:password:isGeneratedPassword:completionHandler:]_block_invoke
+ ___147-[WBUFormAutoFillPrompt showAutoFillPromptForUsernameInWebView:url:title:message:suggestedUsername:password:isGeneratedPassword:completionHandler:]_block_invoke_2
+ ___147-[WBUFormAutoFillPrompt showAutoFillPromptForUsernameInWebView:url:title:message:suggestedUsername:password:isGeneratedPassword:completionHandler:]_block_invoke_3
+ ___147-[WBUFormAutoFillPrompt showAutoFillPromptForUsernameInWebView:url:title:message:suggestedUsername:password:isGeneratedPassword:completionHandler:]_block_invoke_4
+ ___217-[WBUGeneratedPasswordCredentialUpdater updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:shouldSaveExistingCredential:completionHandler:]_block_invoke
+ ___217-[WBUGeneratedPasswordCredentialUpdater updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:shouldSaveExistingCredential:completionHandler:]_block_invoke_2
+ ___217-[WBUGeneratedPasswordCredentialUpdater updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:shouldSaveExistingCredential:completionHandler:]_block_invoke_3
+ ___217-[WBUGeneratedPasswordCredentialUpdater updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:shouldSaveExistingCredential:completionHandler:]_block_invoke_4
+ ___217-[WBUGeneratedPasswordCredentialUpdater updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:shouldSaveExistingCredential:completionHandler:]_block_invoke_5
+ ___50-[WBUFormAutoFillPrompt _alertTextFieldDidChange:]_block_invoke
+ ___50-[WBUFormAutoFillPrompt _alertTextFieldDidChange:]_block_invoke_2
+ ___50-[WBUFormAutoFillPrompt _alertTextFieldDidChange:]_block_invoke_3
+ ___77-[WBUFeatureManager determineIfScreenTimePasscodeIsSetWithCompletionHandler:]_block_invoke
+ ___81-[WBUFormDataController _silentlyUpdateCredentialsForSavedAccounts:withPassword:]_block_invoke
+ ___95-[WBUFeatureManager _determineIfContentFilteringEnabledOrManagedByParentWithCompletionHandler:]_block_invoke
+ ___99-[WBUFormDataController _warnAboutWeakPasswordIfNecessaryWithWebView:savedAccount:protectionSpace:]_block_invoke.373
+ ___99-[WBUFormDataController _warnAboutWeakPasswordIfNecessaryWithWebView:savedAccount:protectionSpace:]_block_invoke.385
+ ___99-[WBUFormDataController _warnAboutWeakPasswordIfNecessaryWithWebView:savedAccount:protectionSpace:]_block_invoke_2.389
+ ___WBS_LOG_CHANNEL_PREFIXKeychain_block_invoke
+ ___block_descriptor_105_e8_32s40s48s56s64s72s80bs88bs96r_e8_v16?0Q8ls32l8s40l8r96l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_105_e8_32s40s48s56s64s72s80s88bs96r_e5_v8?0ls32l8s88l8s40l8s48l8s56l8r96l8s64l8s72l8s80l8
+ ___block_descriptor_40_e8_32bs_e25_v16?0"WBSSavedAccount"8ls32l8
+ ___block_descriptor_40_e8_32s_e43_"UITextSuggestion"16?0"SFSuggestedUser"8ls32l8
+ ___block_descriptor_40_e8_32s_e55_"WBSSavedAccountChangeRequest"16?0"WBSSavedAccount"8ls32l8
+ ___block_descriptor_48_e8_32bs40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSArray"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e25_v16?0"WBSSavedAccount"8ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56bs64r_e8_v16?0Q8ls32l8s40l8r64l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e8_v12?0B8ls32l8s40l8s48l8s72l8s56l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e30_v24?0Q8"WBSCreditCardData"16ls80l8s32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80r_e8_v12?0B8ls32l8r80l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_90_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80s88r_e9_B16?0^8lr88l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_literal_global.10
+ ___block_literal_global.313
+ ___block_literal_global.355
+ ___block_literal_global.397
+ ___block_literal_global.648
+ ___block_literal_global.669
+ _objc_msgSend$_alertTextFieldDidChange:
+ _objc_msgSend$_detailTextForPromptToSaveSecurityCode
+ _objc_msgSend$_detailTextForPromptToUpdateExpirationDate
+ _objc_msgSend$_initRequestWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:shouldSaveExistingCredential:
+ _objc_msgSend$_silentlyUpdateCredentialsForSavedAccounts:withPassword:
+ _objc_msgSend$_silentlyUpdateSavedAccountsEquivalentToUserName:atURL:inContext:withPassword:
+ _objc_msgSend$accountsToConsiderEquivalentForUserName:atURL:
+ _objc_msgSend$canSaveCardData:lastFilledCardData:completionHandler:
+ _objc_msgSend$changeSavedAccountsWithRequests:
+ _objc_msgSend$isHistoryClearingEnabled
+ _objc_msgSend$isKeychainCardsInWalletEnabled
+ _objc_msgSend$isPrivateBrowsingEnabled
+ _objc_msgSend$isRestrictionsPasscodeSet
+ _objc_msgSend$isVirtualCard:previouslyFilledVirtualCardNumbers:
+ _objc_msgSend$neverSaveCVVForCreditCardData:
+ _objc_msgSend$requestWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:shouldSaveExistingCredential:
+ _objc_msgSend$safari_isCaseInsensitiveEqualToString:
+ _objc_msgSend$saveCreditCardData:completionHandler:
+ _objc_msgSend$setSuggestions:
+ _objc_msgSend$sharedProvider
+ _objc_msgSend$shouldEvaluateAccountsToConsiderEquivalentForUserName:atURL:
+ _objc_msgSend$shouldSaveExistingCredential
+ _objc_msgSend$showAutoFillPromptForUsernameInWebView:url:title:message:suggestedUsername:password:isGeneratedPassword:completionHandler:
+ _objc_msgSend$stableIDString
+ _objc_msgSend$suggestedUsersPrioritizingExistingUsersForURL:matchingText:limitForUsersNotFromURL:completionHandler:
+ _objc_msgSend$textInputSuggestionDelegate
+ _objc_msgSend$textSuggestionWithInputText:searchText:
+ _objc_msgSend$updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:shouldSaveExistingCredential:completionHandler:
+ _objc_msgSend$updateCreditCardDataCreditCardData:
- +[WBUGeneratedPasswordCredentialUpdateRequest requestWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:]
- -[WBUCreditCardDataController _shouldOfferVirtualCards]
- -[WBUFormAutoFillPrompt showAutoFillPromptForUsernameInWebView:title:message:suggestedUsername:password:isGeneratedPassword:completionHandler:]
- -[WBUFormDataController saveUser:password:forURL:inContext:andPromptToUpdateRelatedCredentialsWithWebView:]
- -[WBUGeneratedPasswordCredentialUpdateRequest _initRequestWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:]
- -[WBUGeneratedPasswordCredentialUpdater updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:completionHandler:]
- GCC_except_table116
- GCC_except_table119
- GCC_except_table130
- GCC_except_table131
- GCC_except_table142
- GCC_except_table20
- GCC_except_table77
- GCC_except_table83
- GCC_except_table87
- GCC_except_table91
- ___132-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:promptingPolicy:webView:completionHandler:]_block_invoke.228
- ___132-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:promptingPolicy:webView:completionHandler:]_block_invoke.229
- ___132-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:promptingPolicy:webView:completionHandler:]_block_invoke_2.230
- ___132-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:promptingPolicy:webView:completionHandler:]_block_invoke_3.232
- ___143-[WBUFormAutoFillPrompt showAutoFillPromptForUsernameInWebView:title:message:suggestedUsername:password:isGeneratedPassword:completionHandler:]_block_invoke
- ___143-[WBUFormAutoFillPrompt showAutoFillPromptForUsernameInWebView:title:message:suggestedUsername:password:isGeneratedPassword:completionHandler:]_block_invoke_2
- ___143-[WBUFormAutoFillPrompt showAutoFillPromptForUsernameInWebView:title:message:suggestedUsername:password:isGeneratedPassword:completionHandler:]_block_invoke_3
- ___143-[WBUFormAutoFillPrompt showAutoFillPromptForUsernameInWebView:title:message:suggestedUsername:password:isGeneratedPassword:completionHandler:]_block_invoke_4
- ___188-[WBUGeneratedPasswordCredentialUpdater updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:completionHandler:]_block_invoke
- ___188-[WBUGeneratedPasswordCredentialUpdater updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:completionHandler:]_block_invoke_2
- ___188-[WBUGeneratedPasswordCredentialUpdater updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:completionHandler:]_block_invoke_3
- ___80-[WBUFeatureManager determineIfPrivateBrowsingIsAvailableWithCompletionHandler:]_block_invoke
- ___99-[WBUFormDataController _warnAboutWeakPasswordIfNecessaryWithWebView:savedAccount:protectionSpace:]_block_invoke.307
- ___99-[WBUFormDataController _warnAboutWeakPasswordIfNecessaryWithWebView:savedAccount:protectionSpace:]_block_invoke.319
- ___99-[WBUFormDataController _warnAboutWeakPasswordIfNecessaryWithWebView:savedAccount:protectionSpace:]_block_invoke_2.323
- ___block_descriptor_40_e8_32s_e25_v16?0"WBSSavedAccount"8ls32l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e8_v12?0B8ls32l8s40l8s48l8s64l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64r_e9_B16?0^8lr64l8s32l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32s40s48s56s64s72r_e8_v12?0B8lr72l8s32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_89_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_literal_global.289
- ___block_literal_global.331
- ___block_literal_global.570
- ___block_literal_global.591
- _objc_msgSend$_initRequestWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:
- _objc_msgSend$initWithData:encoding:
- _objc_msgSend$requestWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:
- _objc_msgSend$showAutoFillPromptForUsernameInWebView:title:message:suggestedUsername:password:isGeneratedPassword:completionHandler:
- _objc_msgSend$stableID
- _objc_msgSend$updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:completionHandler:
CStrings:
+ "@\"UITextSuggestion\"16@?0@\"SFSuggestedUser\"8"
+ "@\"WBSSavedAccountChangeRequest\"16@?0@\"WBSSavedAccount\"8"
+ "@64@0:8@16@24@32@40@48B56B60"
+ "Keychain"
+ "Keychain credit card update in Wallet (save security code data sheet)"
+ "Keychain credit card update in Wallet (update expiration date data sheet)"
+ "Silently updating %zu accounts"
+ "T@\"WBSSavedAccount\",&,N,V_lastFilledSavedAccount"
+ "TB,R,N,V_shouldSaveExistingCredential"
+ "Update existing saved account without a user name"
+ "Updating existing saved account to new password"
+ "Would you like Wallet to remember this credit card?"
+ "Would you like Wallet to save the security code for this credit card?"
+ "Would you like Wallet to update the expiration date for this credit card?"
+ "Your name, card number, and expiration date will be saved to your Keychain and can be used for AutoFill.\n\nYou can change this anytime in Wallet & Apple Pay settings."
+ "Your name, card number, and expiration date will be saved to your iCloud Keychain and can be used for AutoFill.\n\nYou can change this anytime in Wallet & Apple Pay settings."
+ "Your name, card number, expiration date, and security code will be saved to your Keychain and can be used for AutoFill.\n\nYou can change this anytime in Wallet & Apple Pay settings."
+ "Your name, card number, expiration date, and security code will be saved to your iCloud Keychain and can be used for AutoFill.\n\nYou can change this anytime in Wallet & Apple Pay settings."
+ "_detailTextForPromptToSaveSecurityCode"
+ "_detailTextForPromptToUpdateExpirationDate"
+ "_determineIfContentFilteringEnabledOrManagedByParentWithCompletionHandler:"
+ "_initRequestWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:shouldSaveExistingCredential:"
+ "_lastFilledSavedAccount"
+ "_shouldSaveExistingCredential"
+ "_silentlyUpdateCredentialsForSavedAccounts:withPassword:"
+ "_silentlyUpdateSavedAccountsEquivalentToUserName:atURL:inContext:withPassword:"
+ "_url"
+ "accountsToConsiderEquivalentForUserName:atURL:"
+ "canSaveCardData:lastFilledCardData:completionHandler:"
+ "changeSavedAccountsWithRequests:"
+ "determineIfHistoryClearingIsAvailableWithCompletionHandler:"
+ "determineIfScreenTimePasscodeIsSetWithCompletionHandler:"
+ "iCloud keychain credit card update in Wallet (save security code data sheet)"
+ "iCloud keychain credit card update in Wallet (update expiration date data sheet)"
+ "isHistoryClearingEnabled"
+ "isKeychainCardsInWalletEnabled"
+ "isPrivateBrowsingEnabled"
+ "isRestrictionsPasscodeSet"
+ "isVirtualCard:previouslyFilledVirtualCardNumbers:"
+ "lastFilledSavedAccount"
+ "neverSaveCVVForCreditCardData:"
+ "requestWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:shouldSaveExistingCredential:"
+ "safari_isCaseInsensitiveEqualToString:"
+ "saveCreditCardData:completionHandler:"
+ "setLastFilledSavedAccount:"
+ "setSuggestions:"
+ "sharedProvider"
+ "shouldEvaluateAccountsToConsiderEquivalentForUserName:atURL:"
+ "shouldSaveExistingCredential"
+ "showAutoFillPromptForUsernameInWebView:url:title:message:suggestedUsername:password:isGeneratedPassword:completionHandler:"
+ "stableIDString"
+ "suggestedUsersPrioritizingExistingUsersForURL:matchingText:limitForUsersNotFromURL:completionHandler:"
+ "textInputSuggestionDelegate"
+ "textSuggestionWithInputText:searchText:"
+ "updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:shouldSaveExistingCredential:completionHandler:"
+ "updateCreditCardDataCreditCardData:"
+ "v16@?0@\"NSArray\"8"
+ "v24@?0Q8@\"WBSCreditCardData\"16"
+ "v72@0:8@16@24@32@40@48B56B60@?64"
+ "v76@0:8@16@24@32@40@48@56B64@?68"
- "Update existing saved account without a password"
- "_initRequestWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:"
- "_shouldOfferVirtualCards"
- "initWithData:encoding:"
- "requestWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:"
- "saveUser:password:forURL:inContext:andPromptToUpdateRelatedCredentialsWithWebView:"
- "showAutoFillPromptForUsernameInWebView:title:message:suggestedUsername:password:isGeneratedPassword:completionHandler:"
- "stableID"
- "updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:completionHandler:"
- "v56@0:8@16@24@32@40@48"

```
