## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/Versions/A/AuthKit`

```diff

-  __TEXT.__text: 0x2c6b0c
-  __TEXT.__objc_methlist: 0x10254
+  __TEXT.__text: 0x2c8aac
+  __TEXT.__objc_methlist: 0x102a4
   __TEXT.__const: 0x3ac40
-  __TEXT.__cstring: 0x1291a
-  __TEXT.__oslogstring: 0x1539d
-  __TEXT.__gcc_except_tab: 0x6560
+  __TEXT.__cstring: 0x1297e
+  __TEXT.__oslogstring: 0x1577c
+  __TEXT.__gcc_except_tab: 0x6630
   __TEXT.__dlopen_cstrs: 0x250
   __TEXT.__ustring: 0x34a
-  __TEXT.__unwind_info: 0x4968
+  __TEXT.__unwind_info: 0x49a8
   __TEXT.__eh_frame: 0xc0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7ec0
+  __DATA_CONST.__objc_selrefs: 0x7ee8
   __DATA_CONST.__objc_protorefs: 0xf0
   __DATA_CONST.__objc_superrefs: 0x4c8
   __DATA_CONST.__objc_arraydata: 0x368
-  __DATA_CONST.__got: 0xa58
-  __AUTH_CONST.__const: 0xb680
-  __AUTH_CONST.__cfstring: 0x13ba0
-  __AUTH_CONST.__objc_const: 0x2dd18
+  __DATA_CONST.__got: 0xa60
+  __AUTH_CONST.__const: 0xb6b0
+  __AUTH_CONST.__cfstring: 0x13c00
+  __AUTH_CONST.__objc_const: 0x2dd40
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0x438
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__auth_got: 0x558
-  __AUTH.__objc_data: 0x3340
+  __AUTH.__objc_data: 0x3750
   __DATA.__objc_ivar: 0x121c
   __DATA.__data: 0x1f18
   __DATA.__bss: 0x640
   __DATA.__common: 0xa18
-  __DATA_DIRTY.__objc_data: 0x19a0
+  __DATA_DIRTY.__objc_data: 0x1590
   __DATA_DIRTY.__bss: 0x320
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6162
-  Symbols:   16869
-  CStrings:  7050
+  Functions: 6174
+  Symbols:   16891
+  CStrings:  7074
 
Sections:
~ __TEXT.__dlopen_cstrs : content changed
~ __TEXT.__ustring : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
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
+ __76-[AKAppleIDPasskeyController requestPasskeyChallengeWithContext:completion:]_block_invoke
+ __79-[AKAnisetteProvisioningController fetchSignedDeviceInfoHeadersWithCompletion:]_block_invoke
+ __87-[AKAppleIDPasskeyController submitPasskeyCredentialWithContext:credential:completion:]_block_invoke
+ ___76-[AKAppleIDPasskeyController requestPasskeyChallengeWithContext:completion:]_block_invoke
+ ___79-[AKAnisetteProvisioningController fetchSignedDeviceInfoHeadersWithCompletion:]_block_invoke
+ ___87-[AKAppleIDPasskeyController submitPasskeyCredentialWithContext:credential:completion:]_block_invoke
+ ___block_descriptor_56_e8_32bs_e62_v24?0"AKAppleIDPasskeyCredentialRequestContext"8"NSError"16l
+ _objc_msgSend$_isPushStyleResponse:
+ _objc_msgSend$fetchSignedDeviceInfoHeadersWithCompletion:
+ _objc_msgSend$hardwareModel
+ _objc_msgSend$queryItems
+ _objc_msgSend$requestPasskeyChallengeWithContext:completion:
+ _objc_msgSend$submitPasskeyCredentialWithContext:credential:completion:
+ _objc_msgSend$value
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
+ "URL matches Chromazone internal host, treating as third-party"
+ "authkit/signed-device-info"
+ "push"
+ "v24@?0@\"AKAppleIDPasskeyCredentialRequestContext\"8@\"NSError\"16"
+ "xa"

```
