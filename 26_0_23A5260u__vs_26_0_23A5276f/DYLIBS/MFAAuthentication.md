## MFAAuthentication

> `/System/Library/PrivateFrameworks/MFAAuthentication.framework/MFAAuthentication`

```diff

-1110.0.0.0.1
-  __TEXT.__text: 0x3c318
+1116.0.0.0.0
+  __TEXT.__text: 0x3c4ec
   __TEXT.__auth_stubs: 0xea0
-  __TEXT.__objc_methlist: 0x43c
+  __TEXT.__objc_methlist: 0x444
   __TEXT.__const: 0x62b90
-  __TEXT.__cstring: 0x18ea
+  __TEXT.__cstring: 0x1917
   __TEXT.__gcc_except_tab: 0x2bc
-  __TEXT.__oslogstring: 0x4a01
+  __TEXT.__oslogstring: 0x4a1d
   __TEXT.__ustring: 0xa
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x738
+  __TEXT.__unwind_info: 0x740
   __TEXT.__eh_frame: 0x4c
   __TEXT.__objc_classname: 0x6e
-  __TEXT.__objc_methname: 0x1038
+  __TEXT.__objc_methname: 0x105f
   __TEXT.__objc_methtype: 0x3dc
-  __TEXT.__objc_stubs: 0xfa0
+  __TEXT.__objc_stubs: 0xfe0
   __DATA_CONST.__got: 0x210
-  __DATA_CONST.__const: 0x4f70
+  __DATA_CONST.__const: 0x4f90
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x490
+  __DATA_CONST.__objc_selrefs: 0x4a0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x60
   __AUTH_CONST.__auth_got: 0x760
   __AUTH_CONST.__const: 0x16d0
-  __AUTH_CONST.__cfstring: 0x19e0
+  __AUTH_CONST.__cfstring: 0x1a20
   __AUTH_CONST.__objc_const: 0x608
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2C466ED7-D9FE-319E-82D1-107562E190A9
-  Functions: 782
-  Symbols:   3008
-  CStrings:  1079
+  UUID: E0D6C056-02F1-3EBC-AD66-E553876C90CA
+  Functions: 786
+  Symbols:   3023
+  CStrings:  1086
 
Symbols:
+ +[MFAACertificateManager determineCertificateType:]
+ +[MFAACertificateManager determineCertificateType:].cold.1
+ _ACCUserDefaultsKey_DisableMFi4CertSupport
+ _ACCUserDefaultsKey_MFi4AuthTimeoutValueS
+ _MFAADeviceIdentityCertsExist.cold.1
+ _MFAADeviceIdentityCreateSignature.cold.2
+ ___block_literal_global.209
+ ___block_literal_global.211
+ ___block_literal_global.213
+ ___block_literal_global.215
+ ___block_literal_global.217
+ ___block_literal_global.219
+ ___block_literal_global.221
+ ___block_literal_global.292
+ ___block_literal_global.294
+ _kCFACCUserDefaultsKey_DisableMFi4CertSupport
+ _kCFACCUserDefaultsKey_MFi4AuthTimeoutValueS
+ _mfaa_certificateManager_determineCertificateType
+ _objc_msgSend$determineCertificateType:
+ _objc_msgSend$valueForKey:
- ___block_literal_global.208
- ___block_literal_global.210
- ___block_literal_global.212
- ___block_literal_global.214
- ___block_literal_global.216
- ___block_literal_global.218
- ___block_literal_global.220
- ___block_literal_global.286
- ___block_literal_global.288
Functions:
+ +[MFAACertificateManager determineCertificateType:]
~ _MFAADeviceIdentityCertsExist : 172 -> 200
~ _MFAADeviceIdentityCreateSignature : 244 -> 268
+ +[MFAACertificateManager determineCertificateType:].cold.1
+ _MFAADeviceIdentityCreateSignature.cold.1
+ _mfaa_certificateManager_determineCertificateType
CStrings:
+ "DisableMFi4CertSupport"
+ "Failed parsing certificate!"
+ "MFi4AuthTimeoutValueS"
+ "determineCertificateType:"
+ "valueForKey:"

```
