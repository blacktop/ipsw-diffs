## DeviceIdentity

> `/System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity`

```diff

-  __TEXT.__text: 0x1c524
+  __TEXT.__text: 0x1d9c8
   __TEXT.__objc_methlist: 0x504
-  __TEXT.__cstring: 0x3f78
+  __TEXT.__cstring: 0x429d
+  __TEXT.__gcc_except_tab: 0xaa0
   __TEXT.__const: 0xe1ba
   __TEXT.__ustring: 0x4
   __TEXT.__oslogstring: 0x676
-  __TEXT.__gcc_except_tab: 0x950
   __TEXT.__dlopen_cstrs: 0x134
-  __TEXT.__unwind_info: 0x3f0
+  __TEXT.__unwind_info: 0x438
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3c48
+  __DATA_CONST.__const: 0x3ca0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6a0
+  __DATA_CONST.__objc_selrefs: 0x6b0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x5f8
-  __DATA_CONST.__got: 0x0
+  __DATA_CONST.__got: 0x248
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x4580
+  __AUTH_CONST.__cfstring: 0x4860
   __AUTH_CONST.__objc_const: 0x7b0
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x1f8
-  __AUTH_CONST.__auth_got: 0x488
-  __AUTH.__data: 0x10
+  __AUTH_CONST.__auth_got: 0x4a0
   __DATA.__objc_ivar: 0x54
   __DATA.__data: 0xd4
   __DATA.__bss: 0x90
   __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__data: 0x10
+  __DATA_DIRTY.__data: 0x20
   __DATA_DIRTY.__bss: 0x58
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 272
-  Symbols:   1404
-  CStrings:  1216
+  Functions: 288
+  Symbols:   1453
+  CStrings:  1273
 
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
+ GCC_except_table12
+ GCC_except_table19
+ GCC_except_table7
+ GCC_except_table9
+ _DeviceIdentityCreateClientCertificateRequestWithBody
+ _DeviceIdentityRequestRKPropertiesCreateData
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
+ _objc_retain_x24
+ _objc_retain_x25
+ _udid_from_chipid_and_ecid
+ _udid_from_rkproperties_data
- GCC_except_table11
- GCC_except_table18
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
+ "iOS Device Activator (MobileActivation-1145.0.1)"
+ "requestBody"
+ "requestBody->rkCertification"
+ "requestBody->rkProperties"
+ "requestBody->rkPropertiesSignature"
+ "scrt"
+ "ucrt"
- "iOS Device Activator (MobileActivation-1144)"

```
