## WebUI

> `/System/Library/PrivateFrameworks/WebUI.framework/WebUI`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-625.1.24.10.1
-  __TEXT.__text: 0x33094
+625.1.29.10.3
+  __TEXT.__text: 0x33438
   __TEXT.__objc_methlist: 0x14b4
   __TEXT.__const: 0xd40
-  __TEXT.__gcc_except_tab: 0x5a0
+  __TEXT.__gcc_except_tab: 0x5b0
   __TEXT.__cstring: 0x16b6
   __TEXT.__oslogstring: 0x5ad
   __TEXT.__ustring: 0x9a6

   __TEXT.__swift_as_entry: 0xb8
   __TEXT.__swift_as_ret: 0x114
   __TEXT.__swift_as_cont: 0x178
-  __TEXT.__unwind_info: 0xe30
+  __TEXT.__unwind_info: 0xe40
   __TEXT.__eh_frame: 0x1960
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xfc0
+  __DATA_CONST.__const: 0xfe8
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x70

   __DATA_CONST.__got: 0x5f0
   __AUTH_CONST.__const: 0xd10
   __AUTH_CONST.__cfstring: 0xe80
-  __AUTH_CONST.__objc_const: 0x1f68
+  __AUTH_CONST.__objc_const: 0x1f88
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__auth_got: 0x960
   __AUTH.__objc_data: 0x90
   __AUTH.__data: 0x1d8
-  __DATA.__objc_ivar: 0x118
+  __DATA.__objc_ivar: 0x11c
   __DATA.__data: 0x658
   __DATA.__bss: 0xbe0
   __DATA_DIRTY.__objc_data: 0x6e8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 994
-  Symbols:   1859
+  Functions: 999
+  Symbols:   1866
   CStrings:  185
 
Symbols:
+ GCC_except_table109
+ GCC_except_table113
+ GCC_except_table127
+ GCC_except_table148
+ GCC_except_table151
+ GCC_except_table166
+ GCC_except_table167
+ GCC_except_table168
+ GCC_except_table189
+ GCC_except_table20
+ _OBJC_IVAR_$_WBUFormDataController._passwordSavingManagerLock
+ ___118-[WBUFormDataController _continueUpdatingCredentialsForForm:inWebView:frame:newUsername:newGeneratedPassword:context:]_block_invoke_3
+ ___145-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:formUniqueID:promptingPolicy:webView:completionHandler:]_block_invoke_9
+ ___194-[WBUFormDataController _webView:saveUsernameAndPasswordForURL:formType:formUniqueID:inFrame:username:password:isGeneratedPassword:confirmOverwritingCurrentPassword:inContext:submissionHandler:]_block_invoke_2
+ ___262-[WBUGeneratedPasswordCredentialUpdater updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:savedAccountContext:shouldSaveNewCredential:shouldSaveExistingCredential:associatedDomainsManager:completionHandler:]_block_invoke_6
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
- GCC_except_table108
- GCC_except_table112
- GCC_except_table125
- GCC_except_table146
- GCC_except_table149
- GCC_except_table163
- GCC_except_table164
- GCC_except_table165
- GCC_except_table185
Functions:
~ -[WBUFormDataController passwordSavingManager] : 268 -> 324
~ ___194-[WBUFormDataController _webView:saveUsernameAndPasswordForURL:formType:formUniqueID:inFrame:username:password:isGeneratedPassword:confirmOverwritingCurrentPassword:inContext:submissionHandler:]_block_invoke : 88 -> 184
+ ___194-[WBUFormDataController _webView:saveUsernameAndPasswordForURL:formType:formUniqueID:inFrame:username:password:isGeneratedPassword:confirmOverwritingCurrentPassword:inContext:submissionHandler:]_block_invoke_2
~ ___145-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:formUniqueID:promptingPolicy:webView:completionHandler:]_block_invoke : 88 -> 184
~ ___145-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:formUniqueID:promptingPolicy:webView:completionHandler:]_block_invoke_2 : 120 -> 88
~ ___145-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:formUniqueID:promptingPolicy:webView:completionHandler:]_block_invoke_3 : 4 -> 120
~ ___145-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:formUniqueID:promptingPolicy:webView:completionHandler:]_block_invoke_4 : 232 -> 4
~ ___145-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:formUniqueID:promptingPolicy:webView:completionHandler:]_block_invoke_5 : 860 -> 232
~ ___145-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:formUniqueID:promptingPolicy:webView:completionHandler:]_block_invoke_6 : 620 -> 860
~ ___145-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:formUniqueID:promptingPolicy:webView:completionHandler:]_block_invoke_7 : 8 -> 620
~ ___145-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:formUniqueID:promptingPolicy:webView:completionHandler:]_block_invoke_8 : 180 -> 8
+ ___145-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:formUniqueID:promptingPolicy:webView:completionHandler:]_block_invoke_9
~ ___144-[WBUFormDataController _webView:saveCredentialsForURL:formSubmission:formWithMetadata:fromFrame:username:password:inContext:submissionHandler:]_block_invoke : 96 -> 192
+ ___144-[WBUFormDataController _webView:saveCredentialsForURL:formSubmission:formWithMetadata:fromFrame:username:password:inContext:submissionHandler:]_block_invoke_2
~ ___118-[WBUFormDataController _continueUpdatingCredentialsForForm:inWebView:frame:newUsername:newGeneratedPassword:context:]_block_invoke : 20 -> 156
~ ___118-[WBUFormDataController _continueUpdatingCredentialsForForm:inWebView:frame:newUsername:newGeneratedPassword:context:]_block_invoke_2 : 120 -> 20
+ ___118-[WBUFormDataController _continueUpdatingCredentialsForForm:inWebView:frame:newUsername:newGeneratedPassword:context:]_block_invoke_3
~ ___262-[WBUGeneratedPasswordCredentialUpdater updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:savedAccountContext:shouldSaveNewCredential:shouldSaveExistingCredential:associatedDomainsManager:completionHandler:]_block_invoke_5 : 128 -> 204
+ ___262-[WBUGeneratedPasswordCredentialUpdater updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:savedAccountContext:shouldSaveNewCredential:shouldSaveExistingCredential:associatedDomainsManager:completionHandler:]_block_invoke_6
```
