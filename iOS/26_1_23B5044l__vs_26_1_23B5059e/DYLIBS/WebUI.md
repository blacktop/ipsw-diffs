## WebUI

> `/System/Library/PrivateFrameworks/WebUI.framework/WebUI`

```diff

-622.2.5.10.3
-  __TEXT.__text: 0x12e04
-  __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_methlist: 0x1180
+622.2.9.10.3
+  __TEXT.__text: 0x13314
+  __TEXT.__auth_stubs: 0x600
+  __TEXT.__objc_methlist: 0x1198
   __TEXT.__const: 0x40
-  __TEXT.__gcc_except_tab: 0x674
+  __TEXT.__gcc_except_tab: 0x694
   __TEXT.__cstring: 0x1426
   __TEXT.__oslogstring: 0x445
   __TEXT.__ustring: 0x774
-  __TEXT.__unwind_info: 0x580
-  __TEXT.__objc_classname: 0x204
-  __TEXT.__objc_methname: 0x651d
-  __TEXT.__objc_methtype: 0xf7e
-  __TEXT.__objc_stubs: 0x3aa0
+  __TEXT.__unwind_info: 0x590
+  __TEXT.__objc_classname: 0x206
+  __TEXT.__objc_methname: 0x66af
+  __TEXT.__objc_methtype: 0xfcb
+  __TEXT.__objc_stubs: 0x3ac0
   __DATA_CONST.__got: 0x3f0
   __DATA_CONST.__const: 0xd70
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1480
+  __DATA_CONST.__objc_selrefs: 0x1488
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x318
-  __AUTH_CONST.__const: 0x1e0
+  __AUTH_CONST.__auth_got: 0x310
+  __AUTH_CONST.__const: 0x240
   __AUTH_CONST.__cfstring: 0xdc0
-  __AUTH_CONST.__objc_const: 0x19f0
+  __AUTH_CONST.__objc_const: 0x1a50
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0xf8
+  __DATA.__objc_ivar: 0x100
   __DATA.__data: 0x2b0
-  __DATA.__bss: 0x88
+  __DATA.__bss: 0x78
   __DATA_DIRTY.__objc_data: 0x460
-  __DATA_DIRTY.__bss: 0x40
+  __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B0604A26-DE3B-351B-A26C-A1E3551266F2
-  Functions: 389
-  Symbols:   1848
-  CStrings:  1214
+  UUID: 5A60AC3C-5EF9-395F-8426-4FBFBFB7DF3B
+  Functions: 395
+  Symbols:   1865
+  CStrings:  1221
 
Symbols:
+ +[WBUGeneratedPasswordCredentialUpdateRequest requestWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:savedAccountContext:shouldSaveNewCredential:shouldSaveExistingCredential:associatedDomainsManager:]
+ -[WBUGeneratedPasswordCredentialUpdateRequest _initRequestWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:savedAccountContext:shouldSaveNewCredential:shouldSaveExistingCredential:associatedDomainsManager:]
+ -[WBUGeneratedPasswordCredentialUpdateRequest associatedDomainsManager]
+ -[WBUGeneratedPasswordCredentialUpdateRequest savedAccountContext]
+ -[WBUGeneratedPasswordCredentialUpdater updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:savedAccountContext:shouldSaveNewCredential:shouldSaveExistingCredential:associatedDomainsManager:completionHandler:]
+ GCC_except_table100
+ GCC_except_table104
+ GCC_except_table109
+ GCC_except_table134
+ GCC_except_table137
+ GCC_except_table149
+ GCC_except_table150
+ GCC_except_table151
+ GCC_except_table161
+ GCC_except_table83
+ GCC_except_table96
+ _OBJC_IVAR_$_WBUGeneratedPasswordCredentialUpdateRequest._associatedDomainsManager
+ _OBJC_IVAR_$_WBUGeneratedPasswordCredentialUpdateRequest._savedAccountContext
+ ___132-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:promptingPolicy:webView:completionHandler:]_block_invoke.296
+ ___132-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:promptingPolicy:webView:completionHandler:]_block_invoke.298
+ ___132-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:promptingPolicy:webView:completionHandler:]_block_invoke_2.297
+ ___132-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:promptingPolicy:webView:completionHandler:]_block_invoke_2.299
+ ___132-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:promptingPolicy:webView:completionHandler:]_block_invoke_3.300
+ ___132-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:promptingPolicy:webView:completionHandler:]_block_invoke_4.301
+ ___144-[WBUFormDataController _webView:saveCredentialsForURL:formSubmission:formWithMetadata:fromFrame:username:password:inContext:submissionHandler:]_block_invoke_8
+ ___262-[WBUGeneratedPasswordCredentialUpdater updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:savedAccountContext:shouldSaveNewCredential:shouldSaveExistingCredential:associatedDomainsManager:completionHandler:]_block_invoke
+ ___262-[WBUGeneratedPasswordCredentialUpdater updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:savedAccountContext:shouldSaveNewCredential:shouldSaveExistingCredential:associatedDomainsManager:completionHandler:]_block_invoke_2
+ ___262-[WBUGeneratedPasswordCredentialUpdater updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:savedAccountContext:shouldSaveNewCredential:shouldSaveExistingCredential:associatedDomainsManager:completionHandler:]_block_invoke_3
+ ___262-[WBUGeneratedPasswordCredentialUpdater updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:savedAccountContext:shouldSaveNewCredential:shouldSaveExistingCredential:associatedDomainsManager:completionHandler:]_block_invoke_4
+ ___262-[WBUGeneratedPasswordCredentialUpdater updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:savedAccountContext:shouldSaveNewCredential:shouldSaveExistingCredential:associatedDomainsManager:completionHandler:]_block_invoke_5
+ ___86-[WBUGeneratedPasswordCredentialUpdater _saveNewAccountWithRequest:completionHandler:]_block_invoke_3
+ ___93-[WBUFormDataController saveUnsubmittedGeneratedPasswordInFrame:form:context:closingWebView:]_block_invoke_2
+ ___99-[WBUFormDataController _warnAboutWeakPasswordIfNecessaryWithWebView:savedAccount:protectionSpace:]_block_invoke.380
+ ___99-[WBUFormDataController _warnAboutWeakPasswordIfNecessaryWithWebView:savedAccount:protectionSpace:]_block_invoke.392
+ ___99-[WBUFormDataController _warnAboutWeakPasswordIfNecessaryWithWebView:savedAccount:protectionSpace:]_block_invoke_2.396
+ ___block_descriptor_106_e8_32s40s48s56s64s72s80s88s96bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_113_e8_32s40s48s56s64s72s80s88s96bs104bs_e8_v16?0q8ls96l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s104l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e25_v16?0"WBSSavedAccount"8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs72r_e36_v16?0"WBSSavedAccountMatchResult"8ls32l8s64l8r72l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs72r_e5_v8?0ls64l8r72l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_88_e8_32s40s48s56s64bs72bs80r_e8_v12?0B8ls64l8r80l8s32l8s40l8s48l8s56l8s72l8
+ ___block_descriptor_88_e8_32s40s48s56s64bs72r80r_e8_v12?0B8lr72l8s32l8s40l8s48l8s56l8r80l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_literal_global.280
+ ___block_literal_global.287
+ ___block_literal_global.318
+ ___block_literal_global.360
+ ___block_literal_global.362
+ ___block_literal_global.404
+ ___block_literal_global.644
+ ___block_literal_global.665
+ _objc_msgSend$_initRequestWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:savedAccountContext:shouldSaveNewCredential:shouldSaveExistingCredential:associatedDomainsManager:
+ _objc_msgSend$requestWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:savedAccountContext:shouldSaveNewCredential:shouldSaveExistingCredential:associatedDomainsManager:
+ _objc_msgSend$savedAccountContext
+ _objc_msgSend$setSavedAccountAsDefault:forProtectionSpace:context:associatedDomainsManager:
+ _objc_msgSend$setSavedAccountAsDefault:forProtectionSpace:context:associatedDomainsManager:completionHandler:
+ _objc_msgSend$updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:savedAccountContext:shouldSaveNewCredential:shouldSaveExistingCredential:associatedDomainsManager:completionHandler:
- +[WBUGeneratedPasswordCredentialUpdateRequest requestWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:shouldSaveExistingCredential:]
- -[WBUGeneratedPasswordCredentialUpdateRequest _initRequestWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:shouldSaveExistingCredential:]
- -[WBUGeneratedPasswordCredentialUpdater updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:shouldSaveExistingCredential:completionHandler:]
- GCC_except_table103
- GCC_except_table107
- GCC_except_table132
- GCC_except_table135
- GCC_except_table146
- GCC_except_table147
- GCC_except_table148
- GCC_except_table158
- GCC_except_table82
- GCC_except_table95
- GCC_except_table99
- ___132-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:promptingPolicy:webView:completionHandler:]_block_invoke.292
- ___132-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:promptingPolicy:webView:completionHandler:]_block_invoke.294
- ___132-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:promptingPolicy:webView:completionHandler:]_block_invoke_2.293
- ___132-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:promptingPolicy:webView:completionHandler:]_block_invoke_2.295
- ___132-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:promptingPolicy:webView:completionHandler:]_block_invoke_3.296
- ___217-[WBUGeneratedPasswordCredentialUpdater updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:shouldSaveExistingCredential:completionHandler:]_block_invoke
- ___217-[WBUGeneratedPasswordCredentialUpdater updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:shouldSaveExistingCredential:completionHandler:]_block_invoke_2
- ___217-[WBUGeneratedPasswordCredentialUpdater updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:shouldSaveExistingCredential:completionHandler:]_block_invoke_3
- ___217-[WBUGeneratedPasswordCredentialUpdater updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:shouldSaveExistingCredential:completionHandler:]_block_invoke_4
- ___217-[WBUGeneratedPasswordCredentialUpdater updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:shouldSaveExistingCredential:completionHandler:]_block_invoke_5
- ___99-[WBUFormDataController _warnAboutWeakPasswordIfNecessaryWithWebView:savedAccount:protectionSpace:]_block_invoke.373
- ___99-[WBUFormDataController _warnAboutWeakPasswordIfNecessaryWithWebView:savedAccount:protectionSpace:]_block_invoke.385
- ___99-[WBUFormDataController _warnAboutWeakPasswordIfNecessaryWithWebView:savedAccount:protectionSpace:]_block_invoke_2.389
- ___block_descriptor_105_e8_32s40s48s56s64s72s80s88bs96bs_e8_v16?0q8ls88l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s96l8
- ___block_descriptor_64_e8_32s40s48s56bs_e25_v16?0"WBSSavedAccount"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56bs64r_e36_v16?0"WBSSavedAccountMatchResult"8ls32l8s56l8r64l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56bs64r_e5_v8?0ls56l8r64l8s32l8s40l8s48l8
- ___block_descriptor_80_e8_32s40s48s56bs64bs72r_e8_v12?0B8ls56l8r72l8s32l8s40l8s48l8s64l8
- ___block_descriptor_80_e8_32s40s48s56bs64r72r_e8_v12?0B8lr64l8s32l8s40l8s48l8r72l8s56l8
- ___block_descriptor_90_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_literal_global.313
- ___block_literal_global.355
- ___block_literal_global.397
- ___block_literal_global.627
- ___block_literal_global.648
- _objc_msgSend$_initRequestWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:shouldSaveExistingCredential:
- _objc_msgSend$requestWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:shouldSaveExistingCredential:
- _objc_msgSend$setSavedAccountAsDefault:forProtectionSpace:
- _objc_msgSend$setSavedAccountAsDefault:forProtectionSpace:context:
- _objc_msgSend$updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:shouldSaveExistingCredential:completionHandler:
- _objc_retain_x6
CStrings:
+ "@\"WBSAutoFillAssociatedDomainsManager\""
+ "@\"WBSSavedAccountContext\""
+ "@80@0:8@16@24@32@40@48@56B64B68@72"
+ "T@\"WBSAutoFillAssociatedDomainsManager\",R,N,V_associatedDomainsManager"
+ "T@\"WBSSavedAccountContext\",R,N,V_savedAccountContext"
+ "_associatedDomainsManager"
+ "_initRequestWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:savedAccountContext:shouldSaveNewCredential:shouldSaveExistingCredential:associatedDomainsManager:"
+ "_savedAccountContext"
+ "requestWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:savedAccountContext:shouldSaveNewCredential:shouldSaveExistingCredential:associatedDomainsManager:"
+ "savedAccountContext"
+ "setSavedAccountAsDefault:forProtectionSpace:context:associatedDomainsManager:"
+ "setSavedAccountAsDefault:forProtectionSpace:context:associatedDomainsManager:completionHandler:"
+ "updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:savedAccountContext:shouldSaveNewCredential:shouldSaveExistingCredential:associatedDomainsManager:completionHandler:"
+ "v88@0:8@16@24@32@40@48@56B64B68@72@?80"
- "@64@0:8@16@24@32@40@48B56B60"
- "_initRequestWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:shouldSaveExistingCredential:"
- "requestWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:shouldSaveExistingCredential:"
- "setSavedAccountAsDefault:forProtectionSpace:"
- "setSavedAccountAsDefault:forProtectionSpace:context:"
- "updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:shouldSaveNewCredential:shouldSaveExistingCredential:completionHandler:"
- "v72@0:8@16@24@32@40@48B56B60@?64"

```
