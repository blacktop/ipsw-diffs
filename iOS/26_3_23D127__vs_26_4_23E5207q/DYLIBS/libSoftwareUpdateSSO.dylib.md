## libSoftwareUpdateSSO.dylib

> `/usr/lib/libSoftwareUpdateSSO.dylib`

```diff

-1837.80.27.0.1
-  __TEXT.__text: 0x2e64
-  __TEXT.__auth_stubs: 0x3d0
+1837.100.235.0.0
+  __TEXT.__text: 0x3164
+  __TEXT.__auth_stubs: 0x380
   __TEXT.__objc_methlist: 0x3b8
   __TEXT.__const: 0x88
   __TEXT.__cstring: 0x2df
   __TEXT.__oslogstring: 0x7b9
-  __TEXT.__unwind_info: 0xd8
+  __TEXT.__unwind_info: 0xf8
   __TEXT.__objc_classname: 0x9d
   __TEXT.__objc_methname: 0xb17
   __TEXT.__objc_methtype: 0x2e8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x388
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1f0
+  __AUTH_CONST.__auth_got: 0x1c8
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x500
   __AUTH_CONST.__objc_const: 0x640

   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 63C94FD8-2B3A-3A1A-BEB9-2908B5B801B4
+  UUID: DAEC51BB-1FE0-32D1-98D4-A2452E9D1F36
   Functions: 62
-  Symbols:   362
+  Symbols:   358
   CStrings:  312
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x21
+ _objc_retain_x23
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x22
- _objc_retain_x24
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ __MAClientLog : 168 -> 180
~ ____MAClientLog_block_invoke : 644 -> 652
~ -[SoftwareUpdateExtensibleSSOAuthenticator copyQueryItemsWithParameters:] : 204 -> 208
~ -[SoftwareUpdateExtensibleSSOAuthenticator authenticate] : 1368 -> 1468
~ -[SoftwareUpdateExtensibleSSOAuthenticator authenticationSupported] : 212 -> 224
~ -[SoftwareUpdateExtensibleSSOAuthenticator authorizationController:didCompleteWithAuthorization:] : 304 -> 328
~ -[SoftwareUpdateExtensibleSSOAuthenticator authorizationController:didCompleteWithError:] : 224 -> 232
~ -[SoftwareUpdateExtensibleSSOAuthenticator setAppIdentifier:] : 12 -> 64
~ -[SoftwareUpdateExtensibleSSOAuthenticator setEnvIdentifier:] : 12 -> 64
~ -[SoftwareUpdateExtensibleSSOAuthenticator setUsername:] : 12 -> 64
~ -[SoftwareUpdateExtensibleSSOAuthenticator setInteractivity:] : 12 -> 64
~ -[SoftwareUpdateExtensibleSSOAuthenticator setOtherParameters:] : 12 -> 64
~ -[SoftwareUpdateSSO initWithOptions:] : 764 -> 804
~ -[SoftwareUpdateSSO invalidate] : 80 -> 84
~ -[SoftwareUpdateSSO setupAuthenticator] : 212 -> 232
~ -[SoftwareUpdateSSO copyTokenFromAuthenticatorResponse:error:] : 1176 -> 1252
~ ___62-[SoftwareUpdateSSO copyTokenFromAuthenticatorResponse:error:]_block_invoke : 132 -> 144
~ -[SoftwareUpdateSSO callerHasRequiredEntitlements] : 256 -> 260
~ -[SoftwareUpdateSSO _completionDeadline] : 104 -> 108
~ ___33-[SoftwareUpdateSSO copyUserInfo]_block_invoke : 300 -> 316
~ -[SoftwareUpdateSSO getDawToken] : 140 -> 160
~ ___32-[SoftwareUpdateSSO getDawToken]_block_invoke : 468 -> 496
~ -[SoftwareUpdateSSO ssoIsSupported] : 176 -> 188
~ -[SoftwareUpdateSSO authenticator:didCompleteWithResult:] : 152 -> 156
~ -[SoftwareUpdateSSO authenticator:didCompleteWithError:] : 264 -> 276
~ _copyPersonID : 1200 -> 1236
~ _MSUSSOIsAvailable : 376 -> 384
~ _copyPersonalizationSSOToken : 900 -> 924
~ _copyDawTokenAndUsername : 824 -> 844

```
