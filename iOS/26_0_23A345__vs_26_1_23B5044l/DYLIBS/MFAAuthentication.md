## MFAAuthentication

> `/System/Library/PrivateFrameworks/MFAAuthentication.framework/MFAAuthentication`

```diff

-1124.2.1.0.0
-  __TEXT.__text: 0x3c734
-  __TEXT.__auth_stubs: 0xec0
+1139.40.1.0.0
+  __TEXT.__text: 0x3c6b4
+  __TEXT.__auth_stubs: 0xee0
   __TEXT.__objc_methlist: 0x444
   __TEXT.__const: 0x62b98
-  __TEXT.__cstring: 0x1930
+  __TEXT.__cstring: 0x193b
   __TEXT.__gcc_except_tab: 0x2bc
-  __TEXT.__oslogstring: 0x4a1d
+  __TEXT.__oslogstring: 0x4a9f
   __TEXT.__ustring: 0xa
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__unwind_info: 0x788

   __TEXT.__objc_methtype: 0x3dc
   __TEXT.__objc_stubs: 0xfe0
   __DATA_CONST.__got: 0x210
-  __DATA_CONST.__const: 0x4fa0
+  __DATA_CONST.__const: 0x4f40
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x770
-  __AUTH_CONST.__const: 0x16d0
-  __AUTH_CONST.__cfstring: 0x1a40
+  __AUTH_CONST.__auth_got: 0x780
+  __AUTH_CONST.__const: 0x16b0
+  __AUTH_CONST.__cfstring: 0x1a80
   __AUTH_CONST.__objc_const: 0x608
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0xb8
   __DATA.__objc_ivar: 0x10
-  __DATA.__data: 0x60
+  __DATA.__data: 0xa0
   __DATA.__bss: 0xf8
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0x48
-  __DATA_DIRTY.__bss: 0x1c8
+  __DATA_DIRTY.__bss: 0x1c0
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 24C99BC2-3365-3235-9BCB-E2E4A1024F8F
-  Functions: 791
-  Symbols:   3034
-  CStrings:  1088
+  UUID: 9013D4AB-DBAE-3514-AA90-0D2A33C66956
+  Functions: 789
+  Symbols:   3031
+  CStrings:  1094
 
Symbols:
+ _ACCUserDefaultsKey_Disable1WayNFCForInductive
+ _ACCUserDefaultsKey_DisableT56Support
+ _MFAADeviceIdentityCreateSignature.cold.3
+ _____initMFAADeviceIdentity_block_invoke.14
+ ___block_descriptor_tmp.11
+ ___block_descriptor_tmp.12
+ ___block_literal_global.301
+ ___block_literal_global.303
+ __fetchCertificate
+ _gCertificateStateLock
+ _kCFACCUserDefaultsKey_Disable1WayNFCForInductive
+ _kCFACCUserDefaultsKey_DisableT56Support
+ _pthread_mutex_lock
+ _pthread_mutex_unlock
- ___MFAADeviceIdentityCertsExist_block_invoke
- ___MFAADeviceIdentityCopyCertificate_block_invoke.cold.1
- ___MFAADeviceIdentityCopyCertificate_block_invoke.cold.2
- ___MFAADeviceIdentityCreateSignature_block_invoke
- ___MFAADeviceIdentityCreateSignature_block_invoke.cold.1
- ___MFAADeviceIdentityInitCertStates_block_invoke
- _____initMFAADeviceIdentity_block_invoke.19
- ___block_descriptor_tmp.10
- ___block_descriptor_tmp.14
- ___block_descriptor_tmp.2
- ___block_descriptor_tmp.20
- ___block_literal_global.22
- ___block_literal_global.295
- ___block_literal_global.297
- _gCertificateIndex
- _gCertificateRefreshPolicy
- _gCertificateRefreshState
CStrings:
+ "%s: %@, gCertificateIndex %d, EXIT success %d"
+ "%s: %@, startIndex %d (%d), ENTER"
+ "%s: index %d, call _copyCertificateForIndex %@"
+ "%s:%d %@, index %d, EXIT success %d"
+ "Disable1WayNFCForInductive"
+ "DisableT56Support"
+ "MFAADeviceIdentity: %s: gCertificateIndex: %d\n"
+ "MFAADeviceIdentityCopyCertificate:%d: _copyCertificateForIndex: error %d\n"
+ "MFAADeviceIdentityFetchAll"
+ "MFAADeviceIdentityInitCertStates"
+ "_fetchCertificate"
- "%s: %@, ENTER"
- "%s: i %d, call _copyCertificateForIndex %@"
- "%s:%d %@, EXIT success %d"
- "MFAADeviceIdentity"
- "MFAADeviceIdentityCopyCertificate:%d: _copyCertificateForIndex: error\n"
- "MFAADeviceIdentityCopyCertificate_block_invoke"
- "MFAADeviceIdentityInitCertStates_block_invoke"

```
