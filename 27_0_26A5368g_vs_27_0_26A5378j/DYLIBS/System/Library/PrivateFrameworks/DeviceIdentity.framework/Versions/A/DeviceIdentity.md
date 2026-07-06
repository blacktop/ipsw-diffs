## DeviceIdentity

> `/System/Library/PrivateFrameworks/DeviceIdentity.framework/Versions/A/DeviceIdentity`

```diff

-  __TEXT.__text: 0x1f684
+  __TEXT.__text: 0x20de0
   __TEXT.__objc_methlist: 0x444
-  __TEXT.__cstring: 0x4284
+  __TEXT.__cstring: 0x45a4
+  __TEXT.__gcc_except_tab: 0xe90
   __TEXT.__const: 0xe20a
   __TEXT.__ustring: 0x4
   __TEXT.__oslogstring: 0x5ba
-  __TEXT.__gcc_except_tab: 0xd84
   __TEXT.__dlopen_cstrs: 0x11f
-  __TEXT.__unwind_info: 0x430
+  __TEXT.__unwind_info: 0x480
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3b50
+  __DATA_CONST.__const: 0x3ba8
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x628
+  __DATA_CONST.__objc_selrefs: 0x638
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x5f8
-  __DATA_CONST.__got: 0x0
+  __DATA_CONST.__got: 0x278
   __AUTH_CONST.__const: 0x2b0
-  __AUTH_CONST.__cfstring: 0x45a0
+  __AUTH_CONST.__cfstring: 0x4860
   __AUTH_CONST.__objc_const: 0x730
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x1f8
-  __AUTH_CONST.__auth_got: 0x458
-  __AUTH.__data: 0x20
+  __AUTH_CONST.__auth_got: 0x460
+  __AUTH.__data: 0x10
   __DATA.__objc_ivar: 0x54
   __DATA.__data: 0xf8
   __DATA.__bss: 0xa8
   __DATA_DIRTY.__objc_data: 0xa0
+  __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CryptoTokenKit.framework/Versions/A/CryptoTokenKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbootpolicy.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 344
-  Symbols:   1234
-  CStrings:  1236
+  Functions: 360
+  Symbols:   1267
+  CStrings:  1291
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ GCC_except_table11
+ GCC_except_table13
+ GCC_except_table18
+ GCC_except_table31
+ _DeviceIdentityCreateClientCertificateRequestWithBody
+ _DeviceIdentityRequestRKPropertiesCreateData
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_48
+ ___assert_rtn
+ ___destructor_8_s0_s8_s16_s24
+ ___destructor_8_s0_s8_s16_s24_s32_s40_s48_s56_s64_s72_s80_s88_s96_s104_s112_s120_s128_s136_s144_s152_s160_s168_s176_s184_s192_s200_s208_s216_s224_s232_s240_s248_s256_s264_s272
+ _baa_request_body_create_dictionary
+ _baa_request_body_has_required_fields
+ _baa_request_create_with_body
+ _baa_rkproperties_create_data
+ _baa_rkproperties_from_data
+ _baa_rkproperties_has_required_fields
+ _kMAOptionsBAABoardId
+ _kMAOptionsBAAChipID
+ _kMAOptionsBAADeviceLocalPolicyCertificate
+ _kMAOptionsBAARequestVersion
+ _kMAOptionsBAASCRT
+ _kMAOptionsBAASecurityDomain
+ _kMAOptionsBAASerialNumber
+ _kMAOptionsBAAUCRT
+ _kMAOptionsBAAUniqueChipID
+ _kMAOptionsBAAUseIM4C
+ _kMAOptionsBAAVMIdentityAttestation
+ _objc_msgSend$dictionaryWithDictionary:
+ _objc_msgSend$unsignedLongLongValue
+ _udid_from_chipid_and_ecid
+ _udid_from_rkproperties_data
+ baa_request_body_create_dictionary
- GCC_except_table17
- GCC_except_table30
- _OUTLINED_FUNCTION_19
- _OUTLINED_FUNCTION_20
- _OUTLINED_FUNCTION_36
- _OUTLINED_FUNCTION_37
- _OUTLINED_FUNCTION_43
- _OUTLINED_FUNCTION_44
CStrings:
+ "%08X-%016llX"
+ "Could not convert data to dictionary."
+ "DeviceLocalPolicyCertificate"
+ "Failed to create RKProperties data."
+ "Failed to create certificate request."
+ "Input data incomplete."
+ "Missing RKCertification."
+ "Missing RKProperties."
+ "Missing RKPropertiesSignature."
+ "Missing boardID."
+ "Missing chipID."
+ "Missing ecid."
+ "Missing required input."
+ "Missing rkCertificationPub."
+ "Missing securityDomain."
+ "Missing sikPub."
+ "RKProperties is nil."
+ "Request body is nil."
+ "RequestVersion"
+ "UseIM4C"
+ "VMIdentityAttestation"
+ "baa_request.m"
+ "baa_request_body_create_dictionary"
+ "baa_request_body_has_required_fields"
+ "baa_request_create_with_body"
+ "baa_rkproperties_create_data"
+ "baa_rkproperties_from_data"
+ "baa_rkproperties_has_required_fields"
+ "macOS Device Activator (MobileActivation-1145.0.1)"
+ "requestBody"
+ "requestBody->rkCertification"
+ "requestBody->rkProperties"
+ "requestBody->rkPropertiesSignature"
+ "scrt"
- "macOS Device Activator (MobileActivation-1144)"

```
