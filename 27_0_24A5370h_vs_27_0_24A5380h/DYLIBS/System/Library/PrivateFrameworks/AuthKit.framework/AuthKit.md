## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-  __TEXT.__text: 0x19f4d0
-  __TEXT.__objc_methlist: 0x1049c
+  __TEXT.__text: 0x1a1494
+  __TEXT.__objc_methlist: 0x104fc
   __TEXT.__const: 0xd30
-  __TEXT.__cstring: 0x12f02
-  __TEXT.__oslogstring: 0x158a1
-  __TEXT.__gcc_except_tab: 0x65c4
+  __TEXT.__cstring: 0x12f76
+  __TEXT.__oslogstring: 0x15c80
+  __TEXT.__gcc_except_tab: 0x6694
   __TEXT.__dlopen_cstrs: 0x267
   __TEXT.__ustring: 0x34a
-  __TEXT.__unwind_info: 0x4830
+  __TEXT.__unwind_info: 0x4870
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x78a8
+  __DATA_CONST.__const: 0x78d8
   __DATA_CONST.__objc_classlist: 0x7d0
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8178
+  __DATA_CONST.__objc_selrefs: 0x81a0
   __DATA_CONST.__objc_protorefs: 0xf0
   __DATA_CONST.__objc_superrefs: 0x4c8
   __DATA_CONST.__objc_arraydata: 0x358
-  __DATA_CONST.__got: 0xbc0
+  __DATA_CONST.__got: 0xbc8
   __AUTH_CONST.__const: 0x13e0
-  __AUTH_CONST.__cfstring: 0x13f20
-  __AUTH_CONST.__objc_const: 0x2e488
+  __AUTH_CONST.__cfstring: 0x13fa0
+  __AUTH_CONST.__objc_const: 0x2e4b0
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_dictobj: 0x410
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__auth_got: 0x518
-  __AUTH.__objc_data: 0x34d0
+  __AUTH.__objc_data: 0x3890
   __DATA.__objc_ivar: 0x123c
   __DATA.__data: 0x1b70
   __DATA.__bss: 0x6d0
-  __DATA_DIRTY.__objc_data: 0x1950
+  __DATA_DIRTY.__objc_data: 0x1590
   __DATA_DIRTY.__bss: 0x2f0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6091
-  Symbols:   23093
-  CStrings:  7152
+  Functions: 6103
+  Symbols:   23126
+  CStrings:  7178
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__dlopen_cstrs : content changed
~ __TEXT.__ustring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __DATA.__objc_ivar : content changed
~ __DATA.__data : content changed
Symbols:
+ -[AKAccountRecoveryStepLocalAuthentication _isPushStyleResponse:]
+ -[AKAnisetteProvisioningController fetchSignedDeviceInfoHeadersWithCompletion:]
+ -[AKAppleIDPasskeyController configureRemoteInterface:]
+ -[AKAppleIDPasskeyController requestPasskeyChallengeWithContext:completion:]
+ -[AKAppleIDPasskeyController submitPasskeyCredentialWithContext:credential:completion:]
+ -[AKDevice hardwareModel]
+ ___76-[AKAppleIDPasskeyController requestPasskeyChallengeWithContext:completion:]_block_invoke
+ ___79-[AKAnisetteProvisioningController fetchSignedDeviceInfoHeadersWithCompletion:]_block_invoke
+ ___79-[AKAnisetteProvisioningController fetchSignedDeviceInfoHeadersWithCompletion:]_block_invoke_2
+ ___87-[AKAppleIDPasskeyController submitPasskeyCredentialWithContext:credential:completion:]_block_invoke
+ ___block_descriptor_56_e8_32bs_e62_v24?0"AKAppleIDPasskeyCredentialRequestContext"8"NSError"16ls32l8
+ _objc_msgSend$_isPushStyleResponse:
+ _objc_msgSend$fetchSignedDeviceInfoHeadersWithCompletion:
+ _objc_msgSend$hardwareModel
+ _objc_msgSend$queryItems
+ _objc_msgSend$requestPasskeyChallengeWithContext:completion:
+ _objc_msgSend$submitPasskeyCredentialWithContext:credential:completion:
- +[AKDevice _hardwareModel]
- _objc_msgSend$_hardwareModel
CStrings:
+ "AppleID passkey challenge request failed with error: %@"
+ "AppleID passkey credential submission failed with error: %@"
+ "AppleIDPasskey/requestPasskeyChallenge"
+ "AppleIDPasskey/submitPasskeyCredential"
+ "AppleIDPasskeyRequestChallenge"
+ "AppleIDPasskeySubmitCredential"
+ "BEGIN [%lld]: AppleIDPasskeyRequestChallenge  enableTelemetry=YES "
+ "BEGIN [%lld]: AppleIDPasskeySubmitCredential  enableTelemetry=YES "
+ "Completed AppleID passkey challenge request successfully"
+ "Completed AppleID passkey credential submission successfully"
+ "CustodianInstructionNTOMacOS"
+ "END [%lld] %fs:AppleIDPasskeyRequestChallenge  Error=%{public,signpost.telemetry:number2,name=Error}d "
+ "END [%lld] %fs:AppleIDPasskeySubmitCredential  Error=%{public,signpost.telemetry:number2,name=Error}d "
+ "FetchSignedDeviceInfo: Remote Anisette service returned an error: %@"
+ "FetchSignedDeviceInfo: Remote Anisette service successfully signed data."
+ "Local authentication: using push-style URL %@"
+ "MLBSerialNumber"
+ "URL matches Chromazone internal host, treating as third-party"
+ "authkit/signed-device-info"
+ "push"
+ "v24@?0@\"AKAppleIDPasskeyCredentialRequestContext\"8@\"NSError\"16"
+ "xa"

```
