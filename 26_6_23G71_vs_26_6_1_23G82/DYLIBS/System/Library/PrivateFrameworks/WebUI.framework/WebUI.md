## WebUI

> `/System/Library/PrivateFrameworks/WebUI.framework/WebUI`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_classname`

```diff

-624.4.5.10.5
-  __TEXT.__text: 0x33790
+624.5.1.10.1
+  __TEXT.__text: 0x33b20
   __TEXT.__auth_stubs: 0x1180
   __TEXT.__objc_methlist: 0x143c
   __TEXT.__const: 0xd00
-  __TEXT.__gcc_except_tab: 0x5a8
+  __TEXT.__gcc_except_tab: 0x5b8
   __TEXT.__cstring: 0x16a6
   __TEXT.__oslogstring: 0x53d
   __TEXT.__ustring: 0x9a6

   __TEXT.__swift5_capture: 0x3dc
   __TEXT.__swift_as_entry: 0xb0
   __TEXT.__swift_as_ret: 0x10c
-  __TEXT.__unwind_info: 0xe48
+  __TEXT.__unwind_info: 0xe50
   __TEXT.__eh_frame: 0x1950
   __TEXT.__objc_classname: 0x330
-  __TEXT.__objc_methname: 0x742d
-  __TEXT.__objc_methtype: 0x1679
+  __TEXT.__objc_methname: 0x744d
+  __TEXT.__objc_methtype: 0x16a9
   __TEXT.__objc_stubs: 0x4100
   __DATA_CONST.__got: 0x5d8
-  __DATA_CONST.__const: 0xf10
+  __DATA_CONST.__const: 0xf38
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x70

   __AUTH_CONST.__auth_got: 0x8d0
   __AUTH_CONST.__const: 0xcc0
   __AUTH_CONST.__cfstring: 0xe80
-  __AUTH_CONST.__objc_const: 0x1f08
+  __AUTH_CONST.__objc_const: 0x1f28
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH.__objc_data: 0x318
   __AUTH.__data: 0x250
-  __DATA.__objc_ivar: 0x110
+  __DATA.__objc_ivar: 0x114
   __DATA.__data: 0x688
   __DATA.__bss: 0xc00
   __DATA.__common: 0x18

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 980
-  Symbols:   1810
-  CStrings:  1252
+  Functions: 985
+  Symbols:   1817
+  CStrings:  1254
 
Symbols:
+ GCC_except_table104
+ GCC_except_table108
+ GCC_except_table122
+ GCC_except_table142
+ GCC_except_table145
+ GCC_except_table160
+ GCC_except_table161
+ GCC_except_table162
+ GCC_except_table177
+ GCC_except_table18
+ _OBJC_IVAR_$_WBUFormDataController._passwordSavingManagerLock
+ ___145-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:formUniqueID:promptingPolicy:webView:completionHandler:]_block_invoke_9
+ ___194-[WBUFormDataController _webView:saveUsernameAndPasswordForURL:formType:formUniqueID:inFrame:username:password:isGeneratedPassword:confirmOverwritingCurrentPassword:inContext:submissionHandler:]_block_invoke_2
+ ___262-[WBUGeneratedPasswordCredentialUpdater updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:savedAccountContext:shouldSaveNewCredential:shouldSaveExistingCredential:associatedDomainsManager:completionHandler:]_block_invoke_6
+ ___96-[WBUFormDataController _updateCredentialsWithGeneratedPasswordForForm:inWebView:frame:context:]_block_invoke_3
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
- GCC_except_table103
- GCC_except_table107
- GCC_except_table120
- GCC_except_table140
- GCC_except_table143
- GCC_except_table157
- GCC_except_table158
- GCC_except_table159
- GCC_except_table173
Functions:
~ -[WBUFormDataController passwordSavingManager] : 288 -> 332
~ ___194-[WBUFormDataController _webView:saveUsernameAndPasswordForURL:formType:formUniqueID:inFrame:username:password:isGeneratedPassword:confirmOverwritingCurrentPassword:inContext:submissionHandler:]_block_invoke : 88 -> 184
+ ___194-[WBUFormDataController _webView:saveUsernameAndPasswordForURL:formType:formUniqueID:inFrame:username:password:isGeneratedPassword:confirmOverwritingCurrentPassword:inContext:submissionHandler:]_block_invoke_2
~ ___145-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:formUniqueID:promptingPolicy:webView:completionHandler:]_block_invoke : 88 -> 184
~ ___145-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:formUniqueID:promptingPolicy:webView:completionHandler:]_block_invoke_2 : 132 -> 88
~ ___145-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:formUniqueID:promptingPolicy:webView:completionHandler:]_block_invoke_3 : 4 -> 132
~ ___145-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:formUniqueID:promptingPolicy:webView:completionHandler:]_block_invoke_4 : 244 -> 4
~ ___145-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:formUniqueID:promptingPolicy:webView:completionHandler:]_block_invoke_5 : 900 -> 244
~ ___145-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:formUniqueID:promptingPolicy:webView:completionHandler:]_block_invoke_6 : 628 -> 900
~ ___145-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:formUniqueID:promptingPolicy:webView:completionHandler:]_block_invoke_7 : 8 -> 628
~ ___145-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:formUniqueID:promptingPolicy:webView:completionHandler:]_block_invoke_8 : 196 -> 8
+ ___145-[WBUFormDataController _saveUser:password:isGeneratedPassword:forURL:inContext:formType:formUniqueID:promptingPolicy:webView:completionHandler:]_block_invoke_9
~ ___144-[WBUFormDataController _webView:saveCredentialsForURL:formSubmission:formWithMetadata:fromFrame:username:password:inContext:submissionHandler:]_block_invoke : 96 -> 192
+ ___144-[WBUFormDataController _webView:saveCredentialsForURL:formSubmission:formWithMetadata:fromFrame:username:password:inContext:submissionHandler:]_block_invoke_2
~ ___96-[WBUFormDataController _updateCredentialsWithGeneratedPasswordForForm:inWebView:frame:context:]_block_invoke : 76 -> 156
~ ___96-[WBUFormDataController _updateCredentialsWithGeneratedPasswordForForm:inWebView:frame:context:]_block_invoke_2 : 116 -> 76
+ ___96-[WBUFormDataController _updateCredentialsWithGeneratedPasswordForForm:inWebView:frame:context:]_block_invoke_3
~ ___262-[WBUGeneratedPasswordCredentialUpdater updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:savedAccountContext:shouldSaveNewCredential:shouldSaveExistingCredential:associatedDomainsManager:completionHandler:]_block_invoke_5 : 132 -> 200
+ ___262-[WBUGeneratedPasswordCredentialUpdater updateCredentialWithNewUsername:newGeneratedPassword:lastGeneratedPassword:credentialURL:protectionSpace:savedAccountContext:shouldSaveNewCredential:shouldSaveExistingCredential:associatedDomainsManager:completionHandler:]_block_invoke_6
CStrings:
+ "_passwordSavingManagerLock"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
```
