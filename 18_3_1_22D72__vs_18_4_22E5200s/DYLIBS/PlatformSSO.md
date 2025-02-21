## PlatformSSO

> `/System/Library/PrivateFrameworks/PlatformSSO.framework/PlatformSSO`

```diff

-417.80.4.0.0
-  __TEXT.__text: 0x4d7c4
-  __TEXT.__auth_stubs: 0xa00
-  __TEXT.__objc_methlist: 0x2750
-  __TEXT.__const: 0x108
-  __TEXT.__cstring: 0x7a05
-  __TEXT.__oslogstring: 0x1c1a
-  __TEXT.__gcc_except_tab: 0x14e8
+417.100.33.0.0
+  __TEXT.__text: 0x4e650
+  __TEXT.__auth_stubs: 0xa20
+  __TEXT.__objc_methlist: 0x2d6c
+  __TEXT.__const: 0x110
+  __TEXT.__cstring: 0x7ac0
+  __TEXT.__oslogstring: 0x1ca9
+  __TEXT.__gcc_except_tab: 0x1508
   __TEXT.__dlopen_cstrs: 0x110
-  __TEXT.__unwind_info: 0x1150
+  __TEXT.__unwind_info: 0x11e0
   __TEXT.__objc_classname: 0x3ad
-  __TEXT.__objc_methname: 0x89c8
-  __TEXT.__objc_methtype: 0x13d7
-  __TEXT.__objc_stubs: 0x67e0
-  __DATA_CONST.__got: 0x3b0
-  __DATA_CONST.__const: 0xd58
+  __TEXT.__objc_methname: 0x8c27
+  __TEXT.__objc_methtype: 0x1407
+  __TEXT.__objc_stubs: 0x6940
+  __DATA_CONST.__got: 0x3b8
+  __DATA_CONST.__const: 0xd40
   __DATA_CONST.__objc_classlist: 0xf0
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e08
+  __DATA_CONST.__objc_selrefs: 0x1f28
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x510
+  __AUTH_CONST.__auth_got: 0x520
   __AUTH_CONST.__const: 0x720
-  __AUTH_CONST.__cfstring: 0x35c0
-  __AUTH_CONST.__objc_const: 0x7e38
+  __AUTH_CONST.__cfstring: 0x3640
+  __AUTH_CONST.__objc_const: 0x73d0
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x960
-  __DATA.__objc_ivar: 0x2d0
+  __DATA.__objc_ivar: 0x2d4
   __DATA.__data: 0x5a0
   __DATA.__bss: 0x230
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit
+  - /System/Library/Frameworks/DeviceCheck.framework/DeviceCheck
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/GSS.framework/GSS
   - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication

   - /System/Library/PrivateFrameworks/AppSSO.framework/AppSSO
   - /System/Library/PrivateFrameworks/AppSSOCore.framework/AppSSOCore
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
+  - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
   - /System/Library/PrivateFrameworks/Heimdal.framework/Heimdal
   - /System/Library/PrivateFrameworks/PlatformSSOCore.framework/PlatformSSOCore
   - /System/Library/PrivateFrameworks/SecurityFoundation.framework/SecurityFoundation

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1725
-  Symbols:   2600
-  CStrings:  2459
+  Functions: 1757
+  Symbols:   2647
+  CStrings:  2483
 
Symbols:
+ _SecCertificateCreateWithData
+ _kTemporaryUserAccountName
+ _objc_retain_x5
CStrings:
+ "%s uid = %{public}d, tokenId = %{public}@, context = %{public}@, sccontext = %{public}@, bcontext = %{public}@ on %@"
+ "-[POAgentAuthenticationProcess faileDevicRegistrationAfterRegistrationWithUserInteraction:]"
+ "-[POExtensionAgentProcess _keyForKeyType:error:]"
+ "-[POExtensionAgentProcess attestKey:pending:clientDataHash:completion:]"
+ "-[POLoginManager attestKey:clientData:completion:]"
+ "-[POLoginManager attestPendingKey:clientData:completion:]"
+ "AllowDeviceIdentifiersInAttestation"
+ "Failed to remove SSO tokens."
+ "Not running registration for the temporary user."
+ "PlatformSSO:"
+ "TB,V_allowDeviceIdentifiersInAttestation"
+ "^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}32@0:8q16^@24"
+ "_allowDeviceIdentifiersInAttestation"
+ "_deleteAllCachedAttestations"
+ "_deleteCachedAttestationForExtensionIdentifier:key:"
+ "_keyForKeyType:error:"
+ "allowDeviceIdentifiersInAttestation"
+ "attestKey:clientData:completion:"
+ "attestKey:pending:clientDataHash:completion:"
+ "attestPendingKey:clientData:completion:"
+ "attestation"
+ "authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:"
+ "createTemporaryUser:passwordContext:completion:"
+ "dsAttrTypeNative:PlatformSSOTemporaryUser"
+ "faileDevicRegistrationAfterRegistrationWithUserInteraction:"
+ "failed to create data vault: %{public}@"
+ "isTemporaryAccountUserName:"
+ "pending attestation"
+ "removeTokensFromKeychainWithService:username:system:"
+ "resetTemporaryAccount:"
+ "retrieveTokensFromKeychainForService:username:system:returningTokens:metaData:"
+ "setAllowDeviceIdentifiersInAttestation:"
+ "updateTemporaryAccountName:altSecurityIdentity:completion:"
+ "updateWithProfile:"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "v44@0:8q16B24@\"NSData\"28@?<v@?@\"NSArray\"@\"NSError\">36"
+ "v44@0:8q16B24@28@?36"
- "%s uid = %{public}d, context = %{public}@, sccontext = %{public}@, bcontext = %{public}@ on %@"
- "-[POExtensionAgentProcess attestKey:clientDataHash:completion:]"
- "-[POExtensionAgentProcess copyDeviceAttestationCertificateWithCompletion:]"
- "-[POLoginManager attestKey:clientDataHash:completion:]"
- "-[POLoginManager copyDeviceAttestationCertificate]"
- "attestKey:clientDataHash:completion:"
- "copyDeviceAttestationCertificate"
- "copyDeviceAttestationCertificateWithCompletion:"
- "removeTokensFromKeychainWithService:username:"
- "retrieveTokensFromKeychainForService:username:returningTokens:metaData:"
- "v24@0:8@?<v@?^{__SecCertificate=}@\"NSError\">16"
- "v24@?0^{__SecCertificate=}8@\"NSError\"16"
- "v40@0:8q16@\"NSData\"24@?<v@?@\"NSData\"@\"NSError\">32"

```
