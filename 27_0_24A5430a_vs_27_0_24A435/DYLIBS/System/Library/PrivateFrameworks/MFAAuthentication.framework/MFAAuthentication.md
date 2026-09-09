## MFAAuthentication

> `/System/Library/PrivateFrameworks/MFAAuthentication.framework/MFAAuthentication`

```diff

 1216.2.2.0.0
-  __TEXT.__text: 0x429ac
-  __TEXT.__objc_methlist: 0x494
-  __TEXT.__const: 0x6de03
-  __TEXT.__cstring: 0x1af8
+  __TEXT.__text: 0x42b50
+  __TEXT.__objc_methlist: 0x4a4
+  __TEXT.__const: 0x6de13
+  __TEXT.__cstring: 0x1bba
   __TEXT.__gcc_except_tab: 0x22c
-  __TEXT.__oslogstring: 0x4e24
+  __TEXT.__oslogstring: 0x4e68
   __TEXT.__ustring: 0xa
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x7d8
+  __TEXT.__unwind_info: 0x7e0
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x56f8
+  __DATA_CONST.__const: 0x57a0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4d0
+  __DATA_CONST.__objc_selrefs: 0x4e8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__got: 0x208
   __AUTH_CONST.__const: 0x1c30
-  __AUTH_CONST.__cfstring: 0x1ba0
+  __AUTH_CONST.__cfstring: 0x1c80
   __AUTH_CONST.__objc_const: 0x648
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 853
-  Symbols:   2002
-  CStrings:  724
+  Functions: 855
+  Symbols:   2018
+  CStrings:  733
 
Symbols:
+ -[MFAACertificateManager createVillanovaNonce:IDSN:challenge:]
+ GCC_except_table35
+ GCC_except_table40
+ _ACCUserDefaultsKey_BLEPairingConfigRequestDelayMs
+ _ACCUserDefaultsKey_BLEPairingDisableOOBPPlusFlow
+ _ACCUserDefaultsKey_BLEPairingDontEarlyInfoAsDeviceUID
+ _ACCUserDefaultsKey_BLEPairingIgnoreZeroEarlyInfo
+ _ACCUserDefaultsKey_PlatformIDOverride
+ _ACCUserDefaultsKey_TestCreateBLEPairingOnInductive
+ _createVillanovaNonce:IDSN:challenge:.kAuthPrefix
+ _kCFACCUserDefaultsKey_BLEPairingConfigRequestDelayMs
+ _kCFACCUserDefaultsKey_BLEPairingDisableOOBPPlusFlow
+ _kCFACCUserDefaultsKey_BLEPairingDontEarlyInfoAsDeviceUID
+ _kCFACCUserDefaultsKey_BLEPairingIgnoreZeroEarlyInfo
+ _kCFACCUserDefaultsKey_PlatformIDOverride
+ _kCFACCUserDefaultsKey_TestCreateBLEPairingOnInductive
+ _objc_msgSend$appendBytes:length:
+ _objc_msgSend$dataWithCapacity:
- GCC_except_table34
- GCC_except_table39
Functions:
~ -[MFAACertificateManager verifyModuleCertificate:forModule:forAuthFlags:] : 1096 -> 1136
+ -[MFAACertificateManager createVillanovaNonce:IDSN:challenge:]
~ _OUTLINED_FUNCTION_13 : 20 -> 12
~ _OUTLINED_FUNCTION_14 : 12 -> 20
+ _OUTLINED_FUNCTION_1
~ _cpGetInternalComponents : 1048 -> 1032
CStrings:
+ "BLEPairingConfigRequestDelayMs"
+ "BLEPairingDisableOOBPPlusFlow"
+ "BLEPairingDontEarlyInfoAsDeviceUID"
+ "BLEPairingIgnoreZeroEarlyInfo"
+ "PlatformIDOverride"
+ "RCAM"
+ "TestCreateBLEPairingOnInductive"
+ "createVillanovaNonce: nonce=%@ idsn=%@ challenge=%@ -> msg=%@ -> %@"
+ "iPhone RCAM"
```
