## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-525.475.19.0.0
-  __TEXT.__text: 0x1978e0
+525.575.4.0.0
+  __TEXT.__text: 0x19b818
   __TEXT.__auth_stubs: 0xc80
-  __TEXT.__objc_methlist: 0xf00c
+  __TEXT.__objc_methlist: 0xf1d4
   __TEXT.__const: 0x6a48
-  __TEXT.__cstring: 0x107db
-  __TEXT.__gcc_except_tab: 0xa7f4
-  __TEXT.__oslogstring: 0x13e9f
+  __TEXT.__cstring: 0x109a0
+  __TEXT.__gcc_except_tab: 0xaa8c
+  __TEXT.__oslogstring: 0x14556
   __TEXT.__dlopen_cstrs: 0x305
   __TEXT.__ustring: 0x300
-  __TEXT.__unwind_info: 0x4558
-  __TEXT.__objc_classname: 0x1e34
-  __TEXT.__objc_methname: 0x2528b
-  __TEXT.__objc_methtype: 0x49aa
-  __TEXT.__objc_stubs: 0x10bc0
-  __DATA_CONST.__got: 0xad0
-  __DATA_CONST.__const: 0xa6e8
-  __DATA_CONST.__objc_classlist: 0x6b8
+  __TEXT.__unwind_info: 0x45f8
+  __TEXT.__objc_classname: 0x1e5f
+  __TEXT.__objc_methname: 0x255d4
+  __TEXT.__objc_methtype: 0x4a55
+  __TEXT.__objc_stubs: 0x10c80
+  __DATA_CONST.__got: 0xad8
+  __DATA_CONST.__const: 0xa778
+  __DATA_CONST.__objc_classlist: 0x6c8
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x78f8
+  __DATA_CONST.__objc_selrefs: 0x7988
   __DATA_CONST.__objc_protorefs: 0xe0
-  __DATA_CONST.__objc_superrefs: 0x438
+  __DATA_CONST.__objc_superrefs: 0x448
   __DATA_CONST.__objc_arraydata: 0x2e8
   __AUTH_CONST.__auth_got: 0x650
   __AUTH_CONST.__const: 0x1410
-  __AUTH_CONST.__cfstring: 0x115a0
-  __AUTH_CONST.__objc_const: 0x282e0
+  __AUTH_CONST.__cfstring: 0x116a0
+  __AUTH_CONST.__objc_const: 0x28660
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x410
-  __AUTH.__objc_data: 0x2ad0
-  __DATA.__objc_ivar: 0x1160
+  __AUTH.__objc_data: 0x2b70
+  __DATA.__objc_ivar: 0x117c
   __DATA.__data: 0x1900
   __DATA.__bss: 0x6f8
   __DATA_DIRTY.__objc_data: 0x1860

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D49721BC-E5DA-3E57-BD0F-C526874C77B2
-  Functions: 5777
-  Symbols:   21858
-  CStrings:  12843
+  UUID: C8F74100-EDBD-3DAD-AC20-76DFFC24DAD4
+  Functions: 5821
+  Symbols:   21996
+  CStrings:  12926
 
Symbols:
+ +[AKBasicServerRequest supportsSecureCoding]
+ +[AKBasicServerResponse supportsSecureCoding]
+ -[AKAppleIDAuthenticationController executeIDMSRequestWithContext:completion:]
+ -[AKAppleIDAuthenticationController failureInjectionHeadersForURL:error:]
+ -[AKAppleIDSession _authController]
+ -[AKBasicServerRequest .cxx_destruct]
+ -[AKBasicServerRequest description]
+ -[AKBasicServerRequest encodeWithCoder:]
+ -[AKBasicServerRequest expectedResponseFormat]
+ -[AKBasicServerRequest initWithAltDSID:urlBagKey:]
+ -[AKBasicServerRequest initWithCoder:]
+ -[AKBasicServerRequest requestBodyFormat]
+ -[AKBasicServerRequest requestBody]
+ -[AKBasicServerRequest setExpectedResponseFormat:]
+ -[AKBasicServerRequest setRequestBody:]
+ -[AKBasicServerRequest setRequestBodyFormat:]
+ -[AKBasicServerRequest setUrlBagKey:]
+ -[AKBasicServerRequest urlBagKey]
+ -[AKBasicServerResponse .cxx_destruct]
+ -[AKBasicServerResponse data]
+ -[AKBasicServerResponse description]
+ -[AKBasicServerResponse encodeWithCoder:]
+ -[AKBasicServerResponse httpResponse]
+ -[AKBasicServerResponse initWithCoder:]
+ -[AKBasicServerResponse initWithHTTPResponse:data:]
+ -[AKBasicServerResponse setData:]
+ -[AKBasicServerResponse setHttpResponse:]
+ -[AKFeatureManager isFailureInjectionHeaderEnabled]
+ -[AKWalrusController beginADPFlowWithID:altDSID:completion:]
+ -[AKWalrusController completeADPFlowWithID:success:completion:]
+ GCC_except_table151
+ GCC_except_table158
+ GCC_except_table169
+ GCC_except_table173
+ GCC_except_table176
+ GCC_except_table181
+ GCC_except_table186
+ GCC_except_table189
+ GCC_except_table190
+ GCC_except_table192
+ GCC_except_table196
+ GCC_except_table198
+ GCC_except_table200
+ GCC_except_table205
+ GCC_except_table213
+ GCC_except_table221
+ GCC_except_table233
+ GCC_except_table236
+ GCC_except_table238
+ GCC_except_table261
+ GCC_except_table263
+ GCC_except_table283
+ GCC_except_table302
+ GCC_except_table305
+ GCC_except_table308
+ GCC_except_table316
+ GCC_except_table357
+ GCC_except_table363
+ GCC_except_table379
+ _AKBasicServerResponseDataKey
+ _AKBasicServerResponseHTTPResponseKey
+ _AKURLBagKeyFetchUserEvents
+ _OBJC_CLASS_$_AKBasicServerRequest
+ _OBJC_CLASS_$_AKBasicServerResponse
+ _OBJC_IVAR_$_AKBasicServerRequest._expectedResponseFormat
+ _OBJC_IVAR_$_AKBasicServerRequest._requestBody
+ _OBJC_IVAR_$_AKBasicServerRequest._requestBodyFormat
+ _OBJC_IVAR_$_AKBasicServerRequest._urlBagKey
+ _OBJC_IVAR_$_AKBasicServerResponse._data
+ _OBJC_IVAR_$_AKBasicServerResponse._httpResponse
+ _OBJC_IVAR_$_AKFeatureManager._cachedFailureInjectionHeaderEnabled
+ _OBJC_METACLASS_$_AKBasicServerRequest
+ _OBJC_METACLASS_$_AKBasicServerResponse
+ __OBJC_$_CLASS_METHODS_AKBasicServerRequest
+ __OBJC_$_CLASS_METHODS_AKBasicServerResponse
+ __OBJC_$_CLASS_PROP_LIST_AKBasicServerResponse
+ __OBJC_$_INSTANCE_METHODS_AKBasicServerRequest
+ __OBJC_$_INSTANCE_METHODS_AKBasicServerResponse
+ __OBJC_$_INSTANCE_VARIABLES_AKBasicServerRequest
+ __OBJC_$_INSTANCE_VARIABLES_AKBasicServerResponse
+ __OBJC_$_PROP_LIST_AKBasicServerRequest
+ __OBJC_$_PROP_LIST_AKBasicServerResponse
+ __OBJC_CLASS_PROTOCOLS_$_AKBasicServerResponse
+ __OBJC_CLASS_RO_$_AKBasicServerRequest
+ __OBJC_CLASS_RO_$_AKBasicServerResponse
+ __OBJC_METACLASS_RO_$_AKBasicServerRequest
+ __OBJC_METACLASS_RO_$_AKBasicServerResponse
+ ___102-[AKWalrusController postWalrusStateUpdateToServerWithContext:urlBagKey:username:password:completion:]_block_invoke.85
+ ___102-[AKWalrusController postWalrusStateUpdateToServerWithContext:urlBagKey:username:password:completion:]_block_invoke.86
+ ___52-[AKAppleIDServerResourceLoadDelegate _signRequest:]_block_invoke.145
+ ___60-[AKWalrusController beginADPFlowWithID:altDSID:completion:]_block_invoke
+ ___60-[AKWalrusController beginADPFlowWithID:altDSID:completion:]_block_invoke.87
+ ___60-[AKWalrusController beginADPFlowWithID:altDSID:completion:]_block_invoke.88
+ ___63-[AKWalrusController completeADPFlowWithID:success:completion:]_block_invoke
+ ___63-[AKWalrusController completeADPFlowWithID:success:completion:]_block_invoke.95
+ ___63-[AKWalrusController completeADPFlowWithID:success:completion:]_block_invoke.96
+ ___66-[AKAppleIDServerResourceLoadDelegate _signRequestWithBAAHeaders:]_block_invoke.153
+ ___70-[AKWalrusController verifyEnableWalrusAllowedWithContext:completion:]_block_invoke.83
+ ___70-[AKWalrusController verifyEnableWalrusAllowedWithContext:completion:]_block_invoke.84
+ ___73-[AKAppleIDAuthenticationController failureInjectionHeadersForURL:error:]_block_invoke
+ ___73-[AKAppleIDAuthenticationController failureInjectionHeadersForURL:error:]_block_invoke_2
+ ___78-[AKAppleIDAuthenticationController executeIDMSRequestWithContext:completion:]_block_invoke
+ ___78-[AKAppleIDAuthenticationController executeIDMSRequestWithContext:completion:]_block_invoke.394
+ ___78-[AKAppleIDAuthenticationController executeIDMSRequestWithContext:completion:]_block_invoke.395
+ ___block_descriptor_40_e8_32bs_e43_v24?0"AKBasicServerResponse"8"NSError"16ls32l8
+ ___block_descriptor_64_e8_32bs40r_e43_v24?0"AKBasicServerResponse"8"NSError"16lr40l8s32l8
+ ___block_literal_global.460
+ ___os_log_helper_16_2_3_8_64_8_64_8_0
+ ___os_log_helper_16_2_4_8_64_8_112_8_64_8_0
+ ___os_log_helper_16_2_4_8_64_8_32_8_64_8_0
+ _kAKBasicServerRequestExpectedResponseFormat
+ _kAKBasicServerRequestRequestBody
+ _kAKBasicServerRequestRequestBodyFormat
+ _kAKBasicServerRequestURLBagKey
+ _objc_msgSend$beginADPFlowWithID:altDSID:completion:
+ _objc_msgSend$completeADPFlowWithID:success:completion:
+ _objc_msgSend$failureInjectionHeadersForURL:completion:
+ _objc_msgSend$failureInjectionHeadersForURL:error:
+ _objc_msgSend$initWithHTTPResponse:data:
+ _objc_msgSend$isFailureInjectionHeaderEnabled
+ _objc_msgSend$performBasicServerRequest:completion:
+ _objc_msgSend$urlBagKey
- GCC_except_table159
- GCC_except_table163
- GCC_except_table170
- GCC_except_table172
- GCC_except_table174
- GCC_except_table175
- GCC_except_table183
- GCC_except_table185
- GCC_except_table187
- GCC_except_table188
- GCC_except_table191
- GCC_except_table193
- GCC_except_table197
- GCC_except_table199
- GCC_except_table202
- GCC_except_table207
- GCC_except_table208
- GCC_except_table212
- GCC_except_table214
- GCC_except_table215
- GCC_except_table223
- GCC_except_table235
- GCC_except_table237
- GCC_except_table253
- GCC_except_table258
- GCC_except_table264
- GCC_except_table303
- GCC_except_table306
- GCC_except_table309
- GCC_except_table328
- GCC_except_table358
- GCC_except_table365
- ___102-[AKWalrusController postWalrusStateUpdateToServerWithContext:urlBagKey:username:password:completion:]_block_invoke.80
- ___102-[AKWalrusController postWalrusStateUpdateToServerWithContext:urlBagKey:username:password:completion:]_block_invoke.81
- ___52-[AKAppleIDServerResourceLoadDelegate _signRequest:]_block_invoke.146
- ___66-[AKAppleIDServerResourceLoadDelegate _signRequestWithBAAHeaders:]_block_invoke.154
- ___70-[AKWalrusController verifyEnableWalrusAllowedWithContext:completion:]_block_invoke.78
- ___70-[AKWalrusController verifyEnableWalrusAllowedWithContext:completion:]_block_invoke.79
- ___block_literal_global.457
- _objc_msgSend$failureInjectionConfig
- _objc_msgSend$headerRepresentationForRequestURL:
CStrings:
+ " URLBagKey=%{public,signpost.telemetry:string1,name=URLBagKey}@  enableTelemetry=YES "
+ "-[AKWalrusController beginADPFlowWithID:altDSID:completion:]_block_invoke"
+ "-[AKWalrusController completeADPFlowWithID:success:completion:]_block_invoke"
+ "<%@: %p; altDSID=%@, urlBagKey=%@, requestBody=%@, expectedResponseFormat=%lu, requestBodyFormat=%lu>"
+ "<%@: %p; statusCode=%ld; dataLength=%lu>"
+ "ADP Flow [CLIENT->DAEMON BEGIN]: flowID=%@, altDSID=%{mask.hash}@, xpcSession=%p"
+ "ADP Flow [CLIENT->DAEMON BEGIN_FAILED]: flowID=%@, error=%{public}@"
+ "ADP Flow [CLIENT->DAEMON BEGIN_SUCCESS]: flowID=%@, daemon acknowledged flow start"
+ "ADP Flow [CLIENT->DAEMON COMPLETE]: flowID=%@, success=%@, xpcSession=%p"
+ "ADP Flow [CLIENT->DAEMON COMPLETE_FAILED]: flowID=%@, error=%{public}@"
+ "ADP Flow [CLIENT->DAEMON COMPLETE_SENDING]: flowID=%@, obtained XPC proxy, sending completion to daemon"
+ "ADP Flow [CLIENT->DAEMON COMPLETE_SUCCESS]: flowID=%@, daemon acknowledged flow completion"
+ "ADP Flow [CLIENT->DAEMON SENDING]: flowID=%@, obtained XPC proxy, sending to daemon"
+ "ADP Flow [XPC_CONNECTION_ERROR]: flowID=%@, function=%s, error=%@, errorCode=%ld"
+ "AKBasicServerRequest"
+ "AKBasicServerResponse"
+ "Attaching failure injection headers: %@"
+ "BEGIN [%lld]: BasicServerRequest  URLBagKey=%{public,signpost.telemetry:string1,name=URLBagKey}@  enableTelemetry=YES "
+ "BasicServerRequest"
+ "Calling out to remote auth service to performBasicServerRequest with urlBagKey: %{public}@"
+ "END [%lld] %fs:BasicServerRequest "
+ "Failed to get failure injection headers with error: %@"
+ "FailureInjectionHeader"
+ "Feature FailureInjectionHeader enabled - %@"
+ "Invalid PDP state value: %lu (max: %lu)"
+ "Invalid pdpStateOverride value: %lu (max: %lu)"
+ "Out-of-range PDP state (%lu), treating as ineligible"
+ "Remote authentication service returned an error for executeIDMSRequestWithContext: %{public}@"
+ "Setting PDP state override to %lu"
+ "T@\"NSData\",C,N,V_data"
+ "T@\"NSDictionary\",C,N,V_requestBody"
+ "T@\"NSHTTPURLResponse\",&,N,V_httpResponse"
+ "T@\"NSString\",C,N,V_urlBagKey"
+ "TB,R,N,GisFailureInjectionHeaderEnabled"
+ "TQ,N,V_expectedResponseFormat"
+ "TQ,N,V_requestBodyFormat"
+ "_cachedFailureInjectionHeaderEnabled"
+ "_expectedResponseFormat"
+ "_requestBody"
+ "_requestBodyFormat"
+ "_urlBagKey"
+ "authkit/basic-server-request"
+ "beginADPFlowWithID:altDSID:completion:"
+ "completeADPFlowWithID:success:completion:"
+ "executeIDMSRequestWithContext: called with nil context"
+ "executeIDMSRequestWithContext:completion:"
+ "expectedResponseFormat"
+ "failureInjectionHeaderEnabled"
+ "failureInjectionHeadersForURL:completion:"
+ "failureInjectionHeadersForURL:error:"
+ "fetchUserEvents"
+ "initWithAltDSID:urlBagKey:"
+ "initWithHTTPResponse:data:"
+ "isFailureInjectionHeaderEnabled"
+ "performBasicServerRequest completed with response: %{public}@"
+ "performBasicServerRequest failed with error: %{public}@"
+ "performBasicServerRequest:completion:"
+ "requestBody"
+ "requestBodyFormat"
+ "setExpectedResponseFormat:"
+ "setHttpResponse:"
+ "setRequestBody:"
+ "setRequestBodyFormat:"
+ "setUrlBagKey:"
+ "urlBagKey"
+ "v24@?0@\"AKBasicServerResponse\"8@\"NSError\"16"
+ "v32@0:8@\"AKBasicServerRequest\"16@?<v@?@\"AKBasicServerResponse\"@\"NSError\">24"
+ "v32@0:8@\"NSURL\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
+ "v36@0:8@\"NSString\"16B24@?<v@?@\"NSError\">28"
+ "walrus-authkit/begin-adp-flow"
+ "walrus-authkit/complete-adp-flow"
- "Rejecting out-of-range PDP state (%@)."

```
