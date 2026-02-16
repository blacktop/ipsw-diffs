## CertUI

> `/System/Library/PrivateFrameworks/CertUI.framework/CertUI`

```diff

-2052.80.1.0.0
-  __TEXT.__text: 0x4578
-  __TEXT.__auth_stubs: 0x4d0
+2052.100.1.0.0
+  __TEXT.__text: 0x46b4
+  __TEXT.__auth_stubs: 0x490
   __TEXT.__objc_methlist: 0x378
   __TEXT.__const: 0x38
   __TEXT.__oslogstring: 0x4ed
   __TEXT.__cstring: 0x49f
   __TEXT.__gcc_except_tab: 0x10
-  __TEXT.__unwind_info: 0x168
+  __TEXT.__unwind_info: 0x180
   __TEXT.__objc_classname: 0x76
   __TEXT.__objc_methname: 0xa41
   __TEXT.__objc_methtype: 0x2b9

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x338
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x278
+  __AUTH_CONST.__auth_got: 0x258
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x7c0
   __AUTH_CONST.__objc_const: 0x3f8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E3740026-B23B-3815-82F4-6E6017FD2D29
+  UUID: 51A362D5-767B-33AC-B813-83F803E35204
   Functions: 86
-  Symbols:   461
+  Symbols:   457
   CStrings:  317
 
Symbols:
+ _objc_retain_x25
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ +[CertUIUtilities localizedAppTitleForBundleID:] : 580 -> 608
~ +[CertUIUtilities _certUIBundle] : 160 -> 176
~ ___32+[CertUIUtilities _certUIBundle]_block_invoke : 72 -> 76
~ +[CertUIConnectionDelegate defaultServiceForProtocol:] : 308 -> 312
~ -[CertUIConnectionDelegate _continueConnectionWithResponse:challenge:service:] : 572 -> 600
~ -[CertUIConnectionDelegate connection:didReceiveAuthenticationChallenge:] : 908 -> 960
~ +[CertUITrustManager defaultTrustManager] : 68 -> 84
~ -[CertUITrustManager _getExceptionsForSSLTrust:hostname:service:] : 432 -> 428
~ __CopyVersion2QueryDictionaryForDigestHostService : 540 -> 512
~ __CopyExceptionsForMutableQuery : 636 -> 620
~ -[CertUITrustManager addSSLTrust:hostname:service:] : 392 -> 388
~ __SaveExceptionsForMutableQuery : 768 -> 752
~ -[CertUITrustManager addSMIMETrust:sender:] : 356 -> 364
~ -[CertUITrustManager removeSSLTrust:hostname:service:] : 352 -> 348
~ __DeleteExceptionsForQuery : 496 -> 484
~ -[CertUITrustManager(SMIMEExtensions) _hasExceptionsForSMIMETrust:sender:] : 840 -> 816
~ +[CertUIPrompt(Private) stringForResponse:] : 196 -> 192
~ -[CertUIPrompt description] : 128 -> 136
~ -[CertUIPrompt connectionDisplayName] : 176 -> 188
~ +[CertUIPrompt promptQueue] : 68 -> 84
~ -[CertUIPrompt _sendablePropertyFromProperty:] : 336 -> 368
~ -[CertUIPrompt _sendablePropertiesFromProperties:] : 336 -> 348
~ -[CertUIPrompt _sendablePropertiesFromTrust:] : 336 -> 344
~ -[CertUIPrompt _propertyNamed:ofType:inProperties:] : 456 -> 472
~ -[CertUIPrompt _purposeFromTrustProperties:] : 208 -> 224
~ -[CertUIPrompt _newUserInfoWithHostname:trust:options:] : 884 -> 920
~ -[CertUIPrompt _responseFromReplyDict:] : 332 -> 344
~ -[CertUIPrompt _sendRemoteMessageWithPromptOptions:] : 308 -> 312
~ -[CertUIPrompt showPromptWithOptions:responseBlock:] : 220 -> 212
~ -[CertUIPrompt showAndWaitForResponse] : 224 -> 228
~ -[CertUIPrompt setHost:] : 12 -> 64
~ -[CertUIPrompt setService:] : 12 -> 64

```
