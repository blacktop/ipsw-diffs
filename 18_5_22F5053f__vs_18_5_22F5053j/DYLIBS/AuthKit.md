## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-493.462.0.0.0
-  __TEXT.__text: 0xd22e8
+493.463.1.0.0
+  __TEXT.__text: 0xd2a68
   __TEXT.__auth_stubs: 0xdb0
-  __TEXT.__objc_methlist: 0xcfd4
+  __TEXT.__objc_methlist: 0xd08c
   __TEXT.__const: 0x2871
-  __TEXT.__cstring: 0xe291
-  __TEXT.__oslogstring: 0x106a4
+  __TEXT.__cstring: 0xe2de
+  __TEXT.__oslogstring: 0x106e4
   __TEXT.__gcc_except_tab: 0x5480
   __TEXT.__ustring: 0x1b8
   __TEXT.__dlopen_cstrs: 0x16c
-  __TEXT.__unwind_info: 0x3d88
-  __TEXT.__objc_classname: 0x1aba
-  __TEXT.__objc_methname: 0x20646
+  __TEXT.__unwind_info: 0x3db0
+  __TEXT.__objc_classname: 0x1ad4
+  __TEXT.__objc_methname: 0x20712
   __TEXT.__objc_methtype: 0x43ca
-  __TEXT.__objc_stubs: 0xe5c0
-  __DATA_CONST.__got: 0x9b8
-  __DATA_CONST.__const: 0x5c90
-  __DATA_CONST.__objc_classlist: 0x5d0
+  __TEXT.__objc_stubs: 0xe640
+  __DATA_CONST.__got: 0x9c0
+  __DATA_CONST.__const: 0x5ca0
+  __DATA_CONST.__objc_classlist: 0x5d8
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x1e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6a88
+  __DATA_CONST.__objc_selrefs: 0x6ab0
   __DATA_CONST.__objc_protorefs: 0xd8
   __DATA_CONST.__objc_superrefs: 0x3a0
   __DATA_CONST.__objc_arraydata: 0x1c8
   __AUTH_CONST.__auth_got: 0x6e8
   __AUTH_CONST.__auth_ptr: 0x20
   __AUTH_CONST.__const: 0x10f0
-  __AUTH_CONST.__cfstring: 0xe9a0
-  __AUTH_CONST.__objc_const: 0x23748
+  __AUTH_CONST.__cfstring: 0xea20
+  __AUTH_CONST.__objc_const: 0x23958
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x280
-  __AUTH.__objc_data: 0x22b0
-  __DATA.__objc_ivar: 0xf40
+  __AUTH.__objc_data: 0x2300
+  __DATA.__objc_ivar: 0xf48
   __DATA.__data: 0x1720
   __DATA.__bss: 0x640
   __DATA_DIRTY.__objc_data: 0x1770

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5928
-  Symbols:   20514
-  CStrings:  9229
+  Functions: 5945
+  Symbols:   20573
+  CStrings:  9243
 
Symbols:
+ +[AKAttestationResponseData supportsSecureCoding]
+ -[AKAnisetteProvisioningController handleAttestationResponseWithResponseData:completion:]
+ -[AKAnisetteProvisioningController handleAttestationResponseWithResponseData:completion:].cold.1
+ -[AKAnisetteProvisioningController handleAttestationResponseWithResponseData:completion:].cold.2
+ -[AKAnisetteProvisioningController handleAttestationResponseWithResponseData:completion:].cold.3
+ -[AKAttestationResponseData .cxx_destruct]
+ -[AKAttestationResponseData copyWithZone:]
+ -[AKAttestationResponseData description]
+ -[AKAttestationResponseData encodeWithCoder:]
+ -[AKAttestationResponseData headersFromServer]
+ -[AKAttestationResponseData initWithCoder:]
+ -[AKAttestationResponseData setHeadersFromServer:]
+ -[AKAttestationResponseData setStatus:]
+ -[AKAttestationResponseData status]
+ -[AKURLBag isIDSBAADisabled]
+ -[NSError(AuthKit) ak_errorsHeaderStringWithMessage]
+ _AKHTTPResponseHeaderServerTimeKey
+ _OBJC_CLASS_$_AKAttestationResponseData
+ _OBJC_IVAR_$_AKAttestationResponseData._headersFromServer
+ _OBJC_IVAR_$_AKAttestationResponseData._status
+ _OBJC_METACLASS_$_AKAttestationResponseData
+ __OBJC_$_CLASS_METHODS_AKAttestationResponseData
+ __OBJC_$_CLASS_PROP_LIST_AKAttestationResponseData
+ __OBJC_$_INSTANCE_METHODS_AKAttestationResponseData
+ __OBJC_$_INSTANCE_VARIABLES_AKAttestationResponseData
+ __OBJC_$_PROP_LIST_AKAttestationResponseData
+ __OBJC_CLASS_PROTOCOLS_$_AKAttestationResponseData
+ __OBJC_CLASS_RO_$_AKAttestationResponseData
+ __OBJC_METACLASS_RO_$_AKAttestationResponseData
+ ___52-[NSError(AuthKit) ak_errorsHeaderStringWithMessage]_block_invoke
+ ___73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.62
+ ___73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.62.cold.1
+ ___73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.63
+ ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.74
+ ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.74.cold.1
+ ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.75
+ ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.75.cold.1
+ ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.75.cold.2
+ ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.77.cold.2
+ ___83-[AKAppleIDSession URLSession:task:getAppleIDHeadersForResponse:completionHandler:]_block_invoke.54
+ ___83-[AKAppleIDSession URLSession:task:getAppleIDHeadersForResponse:completionHandler:]_block_invoke.54.cold.1
+ ___83-[AKAppleIDSession URLSession:task:getAppleIDHeadersForResponse:completionHandler:]_block_invoke.55
+ ___91-[AKAppleIDSession _handleAnisetteReprovisionWithRequestURL:anisetteController:completion:]_block_invoke.81
+ ___91-[AKAppleIDSession _handleAnisetteReprovisionWithRequestURL:anisetteController:completion:]_block_invoke.81.cold.1
+ ___91-[AKAppleIDSession _handleAnisetteReprovisionWithRequestURL:anisetteController:completion:]_block_invoke.81.cold.2
+ ___92-[AKAppleIDSession URLSession:task:getAppleIDRequestOrHeadersForResponse:completionHandler:]_block_invoke.50
+ ___92-[AKAppleIDSession URLSession:task:getAppleIDRequestOrHeadersForResponse:completionHandler:]_block_invoke.50.cold.1
+ ___92-[AKAppleIDSession URLSession:task:getAppleIDRequestOrHeadersForResponse:completionHandler:]_block_invoke.51
+ ___block_literal_global.412
+ _objc_msgSend$headersFromServer
+ _objc_msgSend$setHeadersFromServer:
+ _objc_msgSend$setStatus:
+ _objc_msgSend$status
- ___73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.65
- ___73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.65.cold.1
- ___73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.66
- ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.78
- ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.78.cold.1
- ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.78.cold.2
- ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.80
- ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.80.cold.1
- ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.80.cold.2
- ___83-[AKAppleIDSession URLSession:task:getAppleIDHeadersForResponse:completionHandler:]_block_invoke.57
- ___83-[AKAppleIDSession URLSession:task:getAppleIDHeadersForResponse:completionHandler:]_block_invoke.57.cold.1
- ___83-[AKAppleIDSession URLSession:task:getAppleIDHeadersForResponse:completionHandler:]_block_invoke.58
- ___91-[AKAppleIDSession _handleAnisetteReprovisionWithRequestURL:anisetteController:completion:]_block_invoke.84
- ___91-[AKAppleIDSession _handleAnisetteReprovisionWithRequestURL:anisetteController:completion:]_block_invoke.84.cold.1
- ___91-[AKAppleIDSession _handleAnisetteReprovisionWithRequestURL:anisetteController:completion:]_block_invoke.84.cold.2
- ___92-[AKAppleIDSession URLSession:task:getAppleIDRequestOrHeadersForResponse:completionHandler:]_block_invoke.53
- ___92-[AKAppleIDSession URLSession:task:getAppleIDRequestOrHeadersForResponse:completionHandler:]_block_invoke.53.cold.1
- ___92-[AKAppleIDSession URLSession:task:getAppleIDRequestOrHeadersForResponse:completionHandler:]_block_invoke.54
- ___block_literal_global.409
CStrings:
+ "%@:%ld:[%@]"
+ "<%@: %p> status: %li, headers:%@"
+ "AKAttestationResponseData"
+ "Handling attestation response - %@"
+ "T@\"NSDictionary\",&,N,V_headersFromServer"
+ "Unhandled status code (%ld)."
+ "_headersFromServer"
+ "ak_errorsHeaderStringWithMessage"
+ "disableIDSBAA"
+ "handleAttestationResponseWithResponseData:completion:"
+ "headersFromServer"
+ "isIDSBAADisabled"
+ "setHeadersFromServer:"

```
