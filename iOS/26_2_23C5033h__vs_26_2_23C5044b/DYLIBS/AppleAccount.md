## AppleAccount

> `/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount`

```diff

-1037.250.2.0.0
-  __TEXT.__text: 0xeb548
+1037.250.4.0.0
+  __TEXT.__text: 0xeb984
   __TEXT.__auth_stubs: 0x1180
-  __TEXT.__objc_methlist: 0xae94
+  __TEXT.__objc_methlist: 0xaeec
   __TEXT.__const: 0x23e0
   __TEXT.__gcc_except_tab: 0x24cc
-  __TEXT.__oslogstring: 0xff6d
-  __TEXT.__cstring: 0xf1dc
+  __TEXT.__oslogstring: 0xffad
+  __TEXT.__cstring: 0xf27c
   __TEXT.__dlopen_cstrs: 0x325
   __TEXT.__constg_swiftt: 0x2d8
   __TEXT.__swift5_typeref: 0x2ed

   __TEXT.__swift5_capture: 0x90
   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x14
-  __TEXT.__unwind_info: 0x2f80
+  __TEXT.__unwind_info: 0x2fa0
   __TEXT.__eh_frame: 0x3e8
   __TEXT.__objc_classname: 0x1fc6
-  __TEXT.__objc_methname: 0x15c68
+  __TEXT.__objc_methname: 0x15e0a
   __TEXT.__objc_methtype: 0x30f8
-  __TEXT.__objc_stubs: 0xc380
+  __TEXT.__objc_stubs: 0xc440
   __DATA_CONST.__got: 0xd80
-  __DATA_CONST.__const: 0x3aa8
+  __DATA_CONST.__const: 0x3ab8
   __DATA_CONST.__objc_classlist: 0x7f8
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x1e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4ea0
+  __DATA_CONST.__objc_selrefs: 0x4ee8
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x578
   __DATA_CONST.__objc_arraydata: 0xe0
   __AUTH_CONST.__auth_got: 0x8d0
   __AUTH_CONST.__const: 0x7160
-  __AUTH_CONST.__cfstring: 0xcee0
+  __AUTH_CONST.__cfstring: 0xcf40
   __AUTH_CONST.__objc_const: 0x23890
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 295EBE0B-1987-31EF-B6AA-A0F6300531D7
-  Functions: 4939
-  Symbols:   16319
-  CStrings:  8994
+  UUID: 3BBC7F0D-AAD0-3501-ADC3-766F1973234C
+  Functions: 4946
+  Symbols:   16340
+  CStrings:  9010
 
Symbols:
+ -[AARequest performRequestWithSession:withFlowID:withHandler:]
+ -[AARequest performSignedRequestWithFlowID:completionHandler:]
+ -[AAURLSession _enqueueRequest:withFlowID:completion:]
+ -[AAURLSession _enqueueRequest:withFlowID:completion:].cold.1
+ -[AAURLSession _enqueueRequest:withFlowID:completion:].cold.2
+ -[AAURLSession dataTaskWithRequest:withFlowID:completion:]
+ -[AAURLSession dataTaskWithRequest:withFlowID:completion:].cold.1
+ -[AAURLSession dataTaskWithRequest:withFlowID:completion:].cold.2
+ -[AAURLSessionContext _additionalAbsintheHeadersForData:withFlowID:completion:]
+ -[AAURLSessionContext _additionalHeadersForRequest:withFlowID:completion:]
+ -[AAURLSessionContext _additionalHeadersForRequest:withFlowID:completion:].cold.1
+ -[AAURLSessionContext _sendEventForAddAbsintheHeaderWithFlowID:absintheError:]
+ -[AAiCloudLoginAccountRequester loginWithAccount:withFlowID:forDelegates:completion:]
+ -[ACAccountStore(AppleAccount) aa_loginAndUpdateiCloudAccount:flowID:delegateParams:withCompletion:]
+ -[ACAccountStore(AppleAccount) aa_loginAndUpdateiCloudAccount:flowID:delegateParams:withCompletion:].cold.1
+ -[ACAccountStore(AppleAccount) aa_loginAndUpdateiCloudAccount:flowID:delegateParams:withCompletion:].cold.2
+ ___100-[ACAccountStore(AppleAccount) aa_loginAndUpdateiCloudAccount:flowID:delegateParams:withCompletion:]_block_invoke
+ ___100-[ACAccountStore(AppleAccount) aa_loginAndUpdateiCloudAccount:flowID:delegateParams:withCompletion:]_block_invoke.cold.1
+ ___54-[AAURLSession _enqueueRequest:withFlowID:completion:]_block_invoke
+ ___62-[AARequest performRequestWithSession:withFlowID:withHandler:]_block_invoke
+ ___62-[AARequest performRequestWithSession:withFlowID:withHandler:]_block_invoke.86
+ ___62-[AARequest performRequestWithSession:withFlowID:withHandler:]_block_invoke.cold.1
+ ___62-[AARequest performRequestWithSession:withFlowID:withHandler:]_block_invoke.cold.2
+ ___74-[AAURLSessionContext _additionalHeadersForRequest:withFlowID:completion:]_block_invoke
+ ___74-[AAURLSessionContext _additionalHeadersForRequest:withFlowID:completion:]_block_invoke.cold.1
+ ___74-[AAURLSessionContext _additionalHeadersForRequest:withFlowID:completion:]_block_invoke_2
+ ___74-[AAURLSessionContext _additionalHeadersForRequest:withFlowID:completion:]_block_invoke_3
+ ___74-[AAURLSessionContext _additionalHeadersForRequest:withFlowID:completion:]_block_invoke_4
+ ___79-[AAURLSessionContext _additionalAbsintheHeadersForData:withFlowID:completion:]_block_invoke
+ ___85-[AAiCloudLoginAccountRequester loginWithAccount:withFlowID:forDelegates:completion:]_block_invoke
+ ___block_descriptor_56_e8_32s40s48bs_e28_v24?0"NSData"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s56l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e40_v24?0"AAURLConfiguration"8"NSError"16ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.180
+ ___block_literal_global.187
+ ___block_literal_global.257
+ _kAAAnalyticsEventSignInAddAbsintheHeader
+ _objc_msgSend$_additionalAbsintheHeadersForData:withFlowID:completion:
+ _objc_msgSend$_additionalHeadersForRequest:withFlowID:completion:
+ _objc_msgSend$_enqueueRequest:withFlowID:completion:
+ _objc_msgSend$_sendEventForAddAbsintheHeaderWithFlowID:absintheError:
+ _objc_msgSend$aa_loginAndUpdateiCloudAccount:flowID:delegateParams:withCompletion:
+ _objc_msgSend$dataTaskWithRequest:withFlowID:completion:
+ _objc_msgSend$loginWithAccount:withFlowID:forDelegates:completion:
+ _objc_msgSend$performRequestWithSession:withFlowID:withHandler:
+ _objc_msgSend$performSignedRequestWithFlowID:completionHandler:
+ _objc_msgSend$setTaskDescription:
+ _objc_msgSend$taskDescription
- -[AAURLSession _enqueueRequest:completion:].cold.1
- -[AAURLSession _enqueueRequest:completion:].cold.2
- -[AAURLSession dataTaskWithRequest:completion:].cold.1
- -[AAURLSession dataTaskWithRequest:completion:].cold.2
- -[AAURLSessionContext _additionalAbsintheHeadersForData:completion:]
- -[AAURLSessionContext _additionalHeadersForRequest:completion:]
- -[AAURLSessionContext _additionalHeadersForRequest:completion:].cold.1
- -[ACAccountStore(AppleAccount) aa_loginAndUpdateiCloudAccount:delegateParams:withCompletion:].cold.1
- -[ACAccountStore(AppleAccount) aa_loginAndUpdateiCloudAccount:delegateParams:withCompletion:].cold.2
- GCC_except_table108
- ___43-[AAURLSession _enqueueRequest:completion:]_block_invoke
- ___51-[AARequest performRequestWithSession:withHandler:]_block_invoke
- ___51-[AARequest performRequestWithSession:withHandler:]_block_invoke.86
- ___51-[AARequest performRequestWithSession:withHandler:]_block_invoke.cold.1
- ___51-[AARequest performRequestWithSession:withHandler:]_block_invoke.cold.2
- ___63-[AAURLSessionContext _additionalHeadersForRequest:completion:]_block_invoke
- ___63-[AAURLSessionContext _additionalHeadersForRequest:completion:]_block_invoke.cold.1
- ___63-[AAURLSessionContext _additionalHeadersForRequest:completion:]_block_invoke_2
- ___63-[AAURLSessionContext _additionalHeadersForRequest:completion:]_block_invoke_3
- ___63-[AAURLSessionContext _additionalHeadersForRequest:completion:]_block_invoke_4
- ___68-[AAURLSessionContext _additionalAbsintheHeadersForData:completion:]_block_invoke
- ___74-[AAiCloudLoginAccountRequester loginWithAccount:forDelegates:completion:]_block_invoke
- ___93-[ACAccountStore(AppleAccount) aa_loginAndUpdateiCloudAccount:delegateParams:withCompletion:]_block_invoke
- ___93-[ACAccountStore(AppleAccount) aa_loginAndUpdateiCloudAccount:delegateParams:withCompletion:]_block_invoke.cold.1
- ___block_descriptor_40_e8_32bs_e28_v24?0"NSData"8"NSError"16ls32l8
- ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e40_v24?0"AAURLConfiguration"8"NSError"16ls32l8s40l8s48l8s56l8
- ___block_literal_global.169
- ___block_literal_global.176
- ___block_literal_global.254
- _objc_msgSend$_additionalAbsintheHeadersForData:completion:
- _objc_msgSend$_additionalHeadersForRequest:completion:
- _objc_msgSend$_enqueueRequest:completion:
- _objc_msgSend$loginWithAccount:forDelegates:completion:
- _objc_msgSend$performSignedRequestWithHandler:
CStrings:
+ "Managed Apple Account not supported for the Apple Account About Text Re-prompt"
+ "Privacy Re-prompt should not display for Managed Apple Accounts"
+ "_additionalAbsintheHeadersForData:withFlowID:completion:"
+ "_additionalHeadersForRequest:withFlowID:completion:"
+ "_enqueueRequest:withFlowID:completion:"
+ "_sendEventForAddAbsintheHeaderWithFlowID:absintheError:"
+ "aa_loginAndUpdateiCloudAccount:flowID:delegateParams:withCompletion:"
+ "com.apple.AAAbsintheErrorDomain"
+ "com.apple.appleaccount.addAbsintheHeader"
+ "dataTaskWithRequest:withFlowID:completion:"
+ "loginWithAccount:withFlowID:forDelegates:completion:"
+ "performRequestWithSession:withFlowID:withHandler:"
+ "performSignedRequestWithFlowID:completionHandler:"
+ "setTaskDescription:"
+ "taskDescription"
- "_additionalAbsintheHeadersForData:completion:"
- "_additionalHeadersForRequest:completion:"

```
