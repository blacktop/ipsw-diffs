## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-520.0.0.0.0
-  __TEXT.__text: 0x173728
+521.1.1.0.0
+  __TEXT.__text: 0x174aac
   __TEXT.__auth_stubs: 0xb90
-  __TEXT.__objc_methlist: 0xd8f4
-  __TEXT.__const: 0x69c0
-  __TEXT.__cstring: 0xf1c6
-  __TEXT.__oslogstring: 0x11539
-  __TEXT.__gcc_except_tab: 0x9af0
+  __TEXT.__objc_methlist: 0xd944
+  __TEXT.__const: 0x69c8
+  __TEXT.__cstring: 0xf1f4
+  __TEXT.__oslogstring: 0x1175a
+  __TEXT.__gcc_except_tab: 0x9b20
   __TEXT.__dlopen_cstrs: 0x305
   __TEXT.__ustring: 0x1b8
-  __TEXT.__unwind_info: 0x4018
+  __TEXT.__unwind_info: 0x4038
   __TEXT.__objc_classname: 0x1c15
-  __TEXT.__objc_methname: 0x21c83
+  __TEXT.__objc_methname: 0x21cf2
   __TEXT.__objc_methtype: 0x45bb
-  __TEXT.__objc_stubs: 0xefc0
+  __TEXT.__objc_stubs: 0xf040
   __DATA_CONST.__got: 0xa38
-  __DATA_CONST.__const: 0xa0a8
+  __DATA_CONST.__const: 0xa0c8
   __DATA_CONST.__objc_classlist: 0x620
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6e60
+  __DATA_CONST.__objc_selrefs: 0x6e80
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x3d8
   __DATA_CONST.__objc_arraydata: 0x2c8
   __AUTH_CONST.__auth_got: 0x5d8
-  __AUTH_CONST.__const: 0x11e0
-  __AUTH_CONST.__cfstring: 0xf940
-  __AUTH_CONST.__objc_const: 0x25218
-  __AUTH_CONST.__objc_intobj: 0x2b8
+  __AUTH_CONST.__const: 0x1200
+  __AUTH_CONST.__cfstring: 0xf9a0
+  __AUTH_CONST.__objc_const: 0x25230
+  __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x3e8
   __AUTH.__objc_data: 0x2620

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2AA3C586-7242-3CF4-939B-3AAA102043FA
-  Functions: 5269
-  Symbols:   20019
-  CStrings:  11635
+  UUID: 7214E9F3-9B34-3935-83F7-3AF8F64232E0
+  Functions: 5280
+  Symbols:   20051
+  CStrings:  11654
 
Symbols:
+ -[AKAnisetteProvisioningController refreshBAADeviceTokenWithCompletion:]
+ -[AKAppleIDAuthenticationController fetchBAADeviceTokenWithCompletion:]
+ -[AKAppleIDAuthenticationController refreshBAADeviceTokenWithCompletion:]
+ _AKCarrierBundleResultKeySimType
+ _AKURLBagKeyBAAFetchDeviceToken
+ _AKURLBagKeySendBAACertsWithToken
+ _CTOidAppleMacPlatformQA
+ ___71-[AKAppleIDAuthenticationController fetchBAADeviceTokenWithCompletion:]_block_invoke
+ ___71-[AKAppleIDAuthenticationController fetchBAADeviceTokenWithCompletion:]_block_invoke.356
+ ___72-[AKAnisetteProvisioningController postAttestationAnalytics:completion:]_block_invoke.37
+ ___72-[AKAnisetteProvisioningController refreshBAADeviceTokenWithCompletion:]_block_invoke
+ ___72-[AKAnisetteProvisioningController refreshBAADeviceTokenWithCompletion:]_block_invoke.34
+ ___72-[AKAnisetteProvisioningController refreshBAADeviceTokenWithCompletion:]_block_invoke_2
+ ___72-[AKAppleIDAuthenticationController fetchBirthdayForAltDSID:completion:]_block_invoke.366
+ ___72-[AKAppleIDAuthenticationController shieldSignInOrCreateFlowsWithError:]_block_invoke.360
+ ___73-[AKAppleIDAuthenticationController refreshBAADeviceTokenWithCompletion:]_block_invoke
+ ___73-[AKAppleIDAuthenticationController refreshBAADeviceTokenWithCompletion:]_block_invoke.355
+ ___73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.68
+ ___73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.69
+ ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.82
+ ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.83
+ ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.84
+ ___74-[AKAppleIDAuthenticationController performEdpMigrationWithAltDSID:error:]_block_invoke.357
+ ___76-[AKAppleIDAuthenticationController performRemoveEdpTokenWithAltDSID:error:]_block_invoke.359
+ ___80-[AKAnisetteProvisioningController _setTimeAdjustmentWithServerTime:completion:]_block_invoke.35
+ ___80-[AKAppleIDAuthenticationController performEdpCompleteKeyDropWithAltDSID:error:]_block_invoke.358
+ ___83-[AKAppleIDSession URLSession:task:getAppleIDHeadersForResponse:completionHandler:]_block_invoke.60
+ ___83-[AKAppleIDSession URLSession:task:getAppleIDHeadersForResponse:completionHandler:]_block_invoke.61
+ ___91-[AKAppleIDSession _handleAnisetteReprovisionWithRequestURL:anisetteController:completion:]_block_invoke.90
+ ___92-[AKAppleIDSession URLSession:task:getAppleIDRequestOrHeadersForResponse:completionHandler:]_block_invoke.56
+ ___92-[AKAppleIDSession URLSession:task:getAppleIDRequestOrHeadersForResponse:completionHandler:]_block_invoke.57
+ ___block_literal_global.430
+ ___block_literal_global.86
+ ___block_literal_global.98
+ _objc_msgSend$fetchBAADeviceTokenWithCompletion:
+ _objc_msgSend$getSimHardwareInfo:error:
+ _objc_msgSend$hardwareType
+ _objc_msgSend$refreshBAADeviceTokenWithCompletion:
- ___72-[AKAnisetteProvisioningController postAttestationAnalytics:completion:]_block_invoke.36
- ___72-[AKAppleIDAuthenticationController fetchBirthdayForAltDSID:completion:]_block_invoke.364
- ___72-[AKAppleIDAuthenticationController shieldSignInOrCreateFlowsWithError:]_block_invoke.358
- ___73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.66
- ___73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.67
- ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.78
- ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.81
- ___74-[AKAppleIDAuthenticationController performEdpMigrationWithAltDSID:error:]_block_invoke.355
- ___76-[AKAppleIDAuthenticationController performRemoveEdpTokenWithAltDSID:error:]_block_invoke.357
- ___80-[AKAnisetteProvisioningController _setTimeAdjustmentWithServerTime:completion:]_block_invoke.34
- ___80-[AKAppleIDAuthenticationController performEdpCompleteKeyDropWithAltDSID:error:]_block_invoke.356
- ___83-[AKAppleIDSession URLSession:task:getAppleIDHeadersForResponse:completionHandler:]_block_invoke.58
- ___83-[AKAppleIDSession URLSession:task:getAppleIDHeadersForResponse:completionHandler:]_block_invoke.59
- ___91-[AKAppleIDSession _handleAnisetteReprovisionWithRequestURL:anisetteController:completion:]_block_invoke.85
- ___92-[AKAppleIDSession URLSession:task:getAppleIDRequestOrHeadersForResponse:completionHandler:]_block_invoke.54
- ___92-[AKAppleIDSession URLSession:task:getAppleIDRequestOrHeadersForResponse:completionHandler:]_block_invoke.55
- ___block_literal_global.424
- ___block_literal_global.93
CStrings:
+ "Calling out to remote auth service to fetch BAA Device Token"
+ "Calling out to remote auth service to refresh BAA Device Token"
+ "Error fetching SIM hardware info: %@"
+ "Remote Anisette service renewed BAA device token successfully."
+ "Remote Anisette service returned an error during renew BAA device token: %@"
+ "Result of fetch BAA Device Token remote call result: %@ and error: %@"
+ "Result of refresh BAA Device Token remote call result: %d and error: %@"
+ "The BAA device token is invalid. It needs to be renewed asynchronously."
+ "authkit/renew-baa-device-token"
+ "fetchBAADeviceTokenWithCompletion:"
+ "fetchDeviceToken"
+ "getSimHardwareInfo:error:"
+ "hardwareType"
+ "refreshBAADeviceTokenWithCompletion:"
+ "sendBAACertWithToken"
+ "simType"

```
