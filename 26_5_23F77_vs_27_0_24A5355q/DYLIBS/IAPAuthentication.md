## IAPAuthentication

> `/System/Library/PrivateFrameworks/IAPAuthentication.framework/IAPAuthentication`

```diff

-2176.100.2.0.0
-  __TEXT.__text: 0x3080
-  __TEXT.__auth_stubs: 0x3d0
+2181.0.3.0.0
+  __TEXT.__text: 0x30cc
   __TEXT.__const: 0x53999
-  __TEXT.__cstring: 0x1087
+  __TEXT.__cstring: 0x10ca
   __TEXT.__unwind_info: 0x110
-  __DATA_CONST.__got: 0x68
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x7b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0x1e8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x120
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
-  UUID: 9EF185D6-0241-3DFB-BAF2-9B8472C83B31
+  - /usr/lib/libobjc.A.dylib
+  UUID: 7B93F083-2FF3-3B53-8E83-E932BABBD095
   Functions: 54
   Symbols:   267
-  CStrings:  108
+  CStrings:  109
 
Symbols:
+ ___block_descriptor_tmp.64
+ ___block_descriptor_tmp.70
+ ___block_descriptor_tmp.72
+ ___block_literal_global.74
- ___block_descriptor_tmp.62
- ___block_descriptor_tmp.68
- ___block_descriptor_tmp.71
- ___block_literal_global.73
Functions:
~ _IapAuthChallengeVerify : 1844 -> 1888
~ _IapAuthCertVerifyAuthVersion : 1280 -> 1308
~ _MFiVerifyCertificateSerialNumber : 720 -> 724
CStrings:
+ "%s ERROR: SecTrustSetAnchorCertificates returned status rcOS:%02X\n"

```
