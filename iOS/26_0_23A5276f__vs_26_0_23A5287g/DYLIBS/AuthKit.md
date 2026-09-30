## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-514.2.0.0.0
-  __TEXT.__text: 0xd9b14
+517.0.0.0.0
+  __TEXT.__text: 0xda1ac
   __TEXT.__auth_stubs: 0xdd0
-  __TEXT.__objc_methlist: 0xd764
+  __TEXT.__objc_methlist: 0xd7ac
   __TEXT.__const: 0x6af0
-  __TEXT.__cstring: 0xe985
-  __TEXT.__oslogstring: 0x112b4
-  __TEXT.__gcc_except_tab: 0x5790
+  __TEXT.__cstring: 0xe9d6
+  __TEXT.__oslogstring: 0x113b2
+  __TEXT.__gcc_except_tab: 0x5798
   __TEXT.__ustring: 0x1b8
   __TEXT.__dlopen_cstrs: 0x16c
-  __TEXT.__unwind_info: 0x4018
+  __TEXT.__unwind_info: 0x4028
   __TEXT.__objc_classname: 0x1c02
-  __TEXT.__objc_methname: 0x2175f
-  __TEXT.__objc_methtype: 0x4529
-  __TEXT.__objc_stubs: 0xed20
+  __TEXT.__objc_methname: 0x2185e
+  __TEXT.__objc_methtype: 0x452a
+  __TEXT.__objc_stubs: 0xede0
   __DATA_CONST.__got: 0xa08
-  __DATA_CONST.__const: 0x7ed8
+  __DATA_CONST.__const: 0x7ee8
   __DATA_CONST.__objc_classlist: 0x618
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6d68
+  __DATA_CONST.__objc_selrefs: 0x6da8
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x3d8
-  __DATA_CONST.__objc_arraydata: 0x1c8
+  __DATA_CONST.__objc_arraydata: 0x1d8
   __AUTH_CONST.__auth_got: 0x6f8
-  __AUTH_CONST.__const: 0x1170
-  __AUTH_CONST.__cfstring: 0xf140
-  __AUTH_CONST.__objc_const: 0x25080
-  __AUTH_CONST.__objc_intobj: 0x270
-  __AUTH_CONST.__objc_arrayobj: 0x60
+  __AUTH_CONST.__const: 0x11b0
+  __AUTH_CONST.__cfstring: 0xf1a0
+  __AUTH_CONST.__objc_const: 0x250c0
+  __AUTH_CONST.__objc_intobj: 0x2a0
+  __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x280
   __AUTH.__objc_data: 0x2530
-  __DATA.__objc_ivar: 0xfc0
+  __DATA.__objc_ivar: 0xfc4
   __DATA.__data: 0x18a0
-  __DATA.__bss: 0x640
+  __DATA.__bss: 0x650
   __DATA_DIRTY.__objc_data: 0x17c0
   __DATA_DIRTY.__bss: 0x278
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5AF83EA5-6324-3A00-ACC2-E2EE233D844A
-  Functions: 6140
-  Symbols:   21407
-  CStrings:  11429
+  UUID: F81FA263-6AB6-38BC-B11D-B59E38BA06B5
+  Functions: 6152
+  Symbols:   21437
+  CStrings:  11454
 
Symbols:
+ -[AKAnisetteProvisioningController _setTimeAdjustmentWithServerTime:completion:]
+ -[AKAnisetteProvisioningController setTimeSetOperationResult:]
+ -[AKAnisetteProvisioningController timeSetOperationResult]
+ -[AKConfiguration _clearGlobalConfigValues]
+ -[AKConfiguration baaTimeDelta]
+ -[AKConfiguration configurationValueForKey:useDomain:]
+ -[AKConfiguration configurationValueForKey:useDomain:].cold.1
+ -[AKConfiguration setBaaTimeDelta:]
+ -[AKConfiguration setDomainConfigurationValue:forKey:]
+ -[AKConfiguration setDomainConfigurationValue:forKey:].cold.1
+ _OBJC_IVAR_$_AKAnisetteProvisioningController._timeSetOperationResult
+ __AKLogNto
+ __AKLogNto.cold.1
+ __AKLogNto.log
+ __AKLogNto.onceToken
+ ___43-[AKConfiguration _clearGlobalConfigValues]_block_invoke
+ ___54-[AKConfiguration configurationValueForKey:useDomain:]_block_invoke
+ ___54-[AKConfiguration configurationValueForKey:useDomain:]_block_invoke_2
+ ___72-[AKAnisetteProvisioningController postAttestationAnalytics:completion:]_block_invoke.36
+ ___72-[AKAnisetteProvisioningController postAttestationAnalytics:completion:]_block_invoke.36.cold.1
+ ___72-[AKAnisetteProvisioningController postAttestationAnalytics:completion:]_block_invoke.36.cold.2
+ ___73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.66
+ ___73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.66.cold.1
+ ___73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.67
+ ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.78
+ ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.78.cold.1
+ ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.78.cold.2
+ ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.80
+ ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.80.cold.1
+ ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.81
+ ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.81.cold.1
+ ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.81.cold.2
+ ___80-[AKAnisetteProvisioningController _setTimeAdjustmentWithServerTime:completion:]_block_invoke
+ ___80-[AKAnisetteProvisioningController _setTimeAdjustmentWithServerTime:completion:]_block_invoke.34
+ ___80-[AKAnisetteProvisioningController _setTimeAdjustmentWithServerTime:completion:]_block_invoke.34.cold.1
+ ___80-[AKAnisetteProvisioningController _setTimeAdjustmentWithServerTime:completion:]_block_invoke.34.cold.2
+ ___80-[AKAnisetteProvisioningController _setTimeAdjustmentWithServerTime:completion:]_block_invoke_2
+ ___80-[AKAnisetteProvisioningController _setTimeAdjustmentWithServerTime:completion:]_block_invoke_2.cold.1
+ ___83-[AKAppleIDSession URLSession:task:getAppleIDHeadersForResponse:completionHandler:]_block_invoke.58
+ ___83-[AKAppleIDSession URLSession:task:getAppleIDHeadersForResponse:completionHandler:]_block_invoke.58.cold.1
+ ___83-[AKAppleIDSession URLSession:task:getAppleIDHeadersForResponse:completionHandler:]_block_invoke.59
+ ___91-[AKAppleIDSession _handleAnisetteReprovisionWithRequestURL:anisetteController:completion:]_block_invoke.85
+ ___91-[AKAppleIDSession _handleAnisetteReprovisionWithRequestURL:anisetteController:completion:]_block_invoke.85.cold.1
+ ___91-[AKAppleIDSession _handleAnisetteReprovisionWithRequestURL:anisetteController:completion:]_block_invoke.85.cold.2
+ ___92-[AKAppleIDSession URLSession:task:getAppleIDRequestOrHeadersForResponse:completionHandler:]_block_invoke.54
+ ___92-[AKAppleIDSession URLSession:task:getAppleIDRequestOrHeadersForResponse:completionHandler:]_block_invoke.54.cold.1
+ ___92-[AKAppleIDSession URLSession:task:getAppleIDRequestOrHeadersForResponse:completionHandler:]_block_invoke.55
+ ____AKLogNto_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e20_v24?0Q8"NSError"16ls32l8s40l8
+ ___block_literal_global.34
+ ___block_literal_global.93
+ _objc_msgSend$_clearGlobalConfigValues
+ _objc_msgSend$_setTimeAdjustmentWithServerTime:completion:
+ _objc_msgSend$configurationValueForKey:useDomain:
+ _objc_msgSend$setDomainConfigurationValue:forKey:
+ _objc_msgSend$setTimeSetOperationResult:
+ _objc_msgSend$synchronize
+ _objc_msgSend$timeSetOperationResult
- -[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:].cold.8
- -[AKAppleIDSession _handleServerTimeAdjustmentWithTime:completion:]
- -[AKConfiguration configurationValueForKey:].cold.1
- _AKRequestHeaderDebugErrorKey
- ___44-[AKConfiguration configurationValueForKey:]_block_invoke
- ___44-[AKConfiguration configurationValueForKey:]_block_invoke_2
- ___72-[AKAnisetteProvisioningController postAttestationAnalytics:completion:]_block_invoke.35
- ___72-[AKAnisetteProvisioningController postAttestationAnalytics:completion:]_block_invoke.35.cold.1
- ___72-[AKAnisetteProvisioningController postAttestationAnalytics:completion:]_block_invoke.35.cold.2
- ___73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.62
- ___73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.62.cold.1
- ___73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.63
- ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.74
- ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.74.cold.1
- ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.75
- ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.75.cold.1
- ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.75.cold.2
- ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.77
- ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.77.cold.1
- ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.77.cold.2
- ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.cold.1
- ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.cold.2
- ___79-[AKAnisetteProvisioningController setTimeAdjustmentWithServerTime:completion:]_block_invoke
- ___79-[AKAnisetteProvisioningController setTimeAdjustmentWithServerTime:completion:]_block_invoke.34
- ___79-[AKAnisetteProvisioningController setTimeAdjustmentWithServerTime:completion:]_block_invoke.34.cold.1
- ___79-[AKAnisetteProvisioningController setTimeAdjustmentWithServerTime:completion:]_block_invoke.34.cold.2
- ___79-[AKAnisetteProvisioningController setTimeAdjustmentWithServerTime:completion:]_block_invoke_2
- ___79-[AKAnisetteProvisioningController setTimeAdjustmentWithServerTime:completion:]_block_invoke_2.cold.1
- ___83-[AKAppleIDSession URLSession:task:getAppleIDHeadersForResponse:completionHandler:]_block_invoke.54
- ___83-[AKAppleIDSession URLSession:task:getAppleIDHeadersForResponse:completionHandler:]_block_invoke.54.cold.1
- ___83-[AKAppleIDSession URLSession:task:getAppleIDHeadersForResponse:completionHandler:]_block_invoke.55
- ___91-[AKAppleIDSession _handleAnisetteReprovisionWithRequestURL:anisetteController:completion:]_block_invoke.81
- ___91-[AKAppleIDSession _handleAnisetteReprovisionWithRequestURL:anisetteController:completion:]_block_invoke.81.cold.1
- ___91-[AKAppleIDSession _handleAnisetteReprovisionWithRequestURL:anisetteController:completion:]_block_invoke.81.cold.2
- ___92-[AKAppleIDSession URLSession:task:getAppleIDRequestOrHeadersForResponse:completionHandler:]_block_invoke.50
- ___92-[AKAppleIDSession URLSession:task:getAppleIDRequestOrHeadersForResponse:completionHandler:]_block_invoke.50.cold.1
- ___92-[AKAppleIDSession URLSession:task:getAppleIDRequestOrHeadersForResponse:completionHandler:]_block_invoke.51
- _objc_msgSend$_handleServerTimeAdjustmentWithTime:completion:
CStrings:
+ "AKLastCheckInAttemptDate"
+ "AKLastCheckInSuccessDate"
+ "Calling akd with server time - %@"
+ "Nil key while getting config!"
+ "Nil key while setting config!"
+ "Nil key while setting domain config!"
+ "T@\"NSNumber\",&,N"
+ "TQ,V_timeSetOperationResult"
+ "Time adjustment information found in non-443 status."
+ "Time adjustment information found with status 443."
+ "Time has been set already. Doing an early return."
+ "Time updated with error - %@"
+ "Vv32@0:8@\"NSString\"16@?<v@?Q@\"NSError\">24"
+ "_AKServerTimeAdjustmentKey"
+ "_clearGlobalConfigValues"
+ "_setTimeAdjustmentWithServerTime:completion:"
+ "_timeSetOperationResult"
+ "baaTimeDelta"
+ "configurationValueForKey:useDomain:"
+ "nto"
+ "setBaaTimeDelta:"
+ "setDomainConfigurationValue:forKey:"
+ "setTimeSetOperationResult:"
+ "synchronize"
+ "timeSetOperationResult"
- "Could not set server adjusted time. Error: %@, not retrying"
- "Vv32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "_handleServerTimeAdjustmentWithTime:completion:"

```
