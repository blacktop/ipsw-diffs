## SCEP

> `/System/Library/PrivateFrameworks/SCEP.framework/Versions/A/SCEP`

```diff

 140.0.3.0.0
-  __TEXT.__text: 0x8198
+  __TEXT.__text: 0x8230
   __TEXT.__auth_stubs: 0xf90
   __TEXT.__const: 0x78
   __TEXT.__cstring: 0x470
   __TEXT.__oslogstring: 0xde5
-  __TEXT.__unwind_info: 0x160
+  __TEXT.__unwind_info: 0x180
   __TEXT.__objc_methname: 0x45
   __TEXT.__objc_stubs: 0x40
   __DATA_CONST.__got: 0xc8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 13274637-29F4-31D1-B825-634183A5FC4C
-  Functions: 129
-  Symbols:   449
+  UUID: 29084C12-7124-3337-8AF4-BCF40075A988
+  Functions: 138
+  Symbols:   466
   CStrings:  195
 
Symbols:
+ AddCertToCRL.cold.1
+ BypassValidityChecks.cold.1
+ BypassValidityChecks.cold.2
+ CreateSignedAttrsForSecFW.cold.2
+ DecryptSCEPResponsePayload.cold.3
+ DecryptSCEPResponsePayload.cold.4
+ DecryptSCEPResponsePayload.cold.5
+ DecryptSCEPResponsePayload.cold.6
+ MaybeUpdateCRL.cold.1
+ MyOpenSSLLogger.cold.2
+ ProcessRequestCertSignatureResponse.cold.1
+ ProcessRequestCertSignatureResponse.cold.10
+ ProcessRequestCertSignatureResponse.cold.11
+ ProcessRequestCertSignatureResponse.cold.2
+ ProcessRequestCertSignatureResponse.cold.3
+ ProcessRequestCertSignatureResponse.cold.4
+ ProcessRequestCertSignatureResponse.cold.5
+ ProcessRequestCertSignatureResponse.cold.6
+ ProcessRequestCertSignatureResponse.cold.7
+ ProcessRequestCertSignatureResponse.cold.8
+ ProcessRequestCertSignatureResponse.cold.9
+ SCEPGetCACert.cold.18
+ SCEPLog.cold.1
+ UseOSSL.cold.1
+ _EncodeCFDataToBase64.cold.2
+ _GetKeyAndCert
+ _PackageAndSendMessage
+ _ProcessRequestCertSignatureResponse
- SCEPRequestCertSignatureWithCSR.cold.1
- SCEPRequestCertSignatureWithCSR.cold.10
- SCEPRequestCertSignatureWithCSR.cold.11
- SCEPRequestCertSignatureWithCSR.cold.2
- SCEPRequestCertSignatureWithCSR.cold.3
- SCEPRequestCertSignatureWithCSR.cold.4
- SCEPRequestCertSignatureWithCSR.cold.5
- SCEPRequestCertSignatureWithCSR.cold.6
- SCEPRequestCertSignatureWithCSR.cold.7
- SCEPRequestCertSignatureWithCSR.cold.8
- SCEPRequestCertSignatureWithCSR.cold.9

```
